"""
Build & push the African Bible datasets to Hugging Face
=======================================================
Consumes:
    african_bible_parallel_text_datasets/{Lang}_{code}_v{id}.csv   (verse_key, version_id, local)
    pivots/{en,fr,ar,zh,pt}.csv                                    (verse_key, text)

Produces two Hugging Face datasets, each with ONE config (subset) per language:

  1. PARALLEL  ({namespace}/african-bible-parallel)
       columns: verse_key, lang_code, local, en, fr, ar, zh, pt
       Multiple versions of the same language are combined and deduped on
       (verse_key, local).  A row is kept when it has local text AND at least
       the English pivot (the anchor); fr/ar/zh/pt are filled where available.

  2. MONOLINGUAL  ({namespace}/african-bible-monolingual)
       One config per African language: columns  verse_key, text   (local only),
       deduped on text.  Plus an extra `eng` config with the English pivot text.

Usage:
    python build_and_push_hf.py --dry-run                 # build locally, no upload
    python build_and_push_hf.py                           # build + push (needs HF token)
    python build_and_push_hf.py --namespace afrispeech
    python build_and_push_hf.py --langs twi ewe gaa       # only these languages
    python build_and_push_hf.py --private

Auth: set env HF_TOKEN, or run `huggingface-cli login` first.
"""

import sys
import subprocess

def _ensure(pkgs):
    import importlib
    miss = []
    names = {"huggingface_hub": "huggingface_hub", "datasets": "datasets", "pandas": "pandas"}
    for p in pkgs:
        try:
            importlib.import_module(names.get(p, p))
        except ImportError:
            miss.append(p)
    if miss:
        print(f"Installing: {', '.join(miss)} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--quiet"] + miss)

_ensure(["pandas", "datasets", "huggingface_hub"])

import argparse
import csv
import os
from collections import defaultdict

import pandas as pd

LOCAL_ROOT   = "./african_bible_parallel_text_datasets"
PIVOT_DIR    = "./pivots"
VERSIONS_CSV = "youversion_africa_versions.csv"
BUILD_DIR    = "./hf_build"
PIVOT_LANGS  = ["en", "fr", "ar", "zh", "pt"]

csv.field_size_limit(10**7)


# ─────────────────────────────────────────────
# LOAD
# ─────────────────────────────────────────────

def load_versions_meta(path):
    """version_id -> (lang_code, lang_name);  lang_code -> lang_name."""
    by_id, lang_name = {}, {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vid = (row.get("version_id") or "").strip()
            if not vid.isdigit():
                continue
            code = (row["lang_code"] or "").strip()
            name = (row["lang_name"] or "").strip()
            by_id[int(vid)] = (code, name)
            lang_name.setdefault(code, name)
    return by_id, lang_name


def lang_csv_name(lang_name, lang_code, version_num):
    return f"{lang_name}_{lang_code}_v{version_num}".replace(" ", "_").replace("/", "-") + ".csv"


def load_pivots():
    pivots = {}
    for lang in PIVOT_LANGS:
        path = os.path.join(PIVOT_DIR, f"{lang}.csv")
        d = {}
        if os.path.exists(path):
            with open(path, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    d[r["verse_key"]] = r["text"]
        pivots[lang] = d
        print(f"  pivot {lang}: {len(d)} verses")
    return pivots


def collect_local_rows(by_id, langs_filter):
    """lang_code -> list of (verse_key, local) across all that language's versions."""
    rows = defaultdict(list)
    for vid, (code, name) in by_id.items():
        if langs_filter and code not in langs_filter:
            continue
        path = os.path.join(LOCAL_ROOT, lang_csv_name(name, code, vid))
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                local = (r.get("local") or "").strip()
                if local:
                    rows[code].append((r["verse_key"], local))
    return rows


# ─────────────────────────────────────────────
# BUILD
# ─────────────────────────────────────────────

def build_parallel(local_rows, pivots):
    """lang_code -> DataFrame[verse_key, lang_code, local, en, fr, ar, zh, pt]."""
    out = {}
    en = pivots["en"]
    for code, pairs in local_rows.items():
        seen, recs = set(), []
        for vk, local in pairs:
            if (vk, local) in seen:
                continue
            seen.add((vk, local))
            if vk not in en:                      # anchor: require English
                continue
            recs.append({
                "verse_key": vk, "lang_code": code, "local": local,
                "en": en.get(vk, ""), "fr": pivots["fr"].get(vk, ""),
                "ar": pivots["ar"].get(vk, ""), "zh": pivots["zh"].get(vk, ""),
                "pt": pivots["pt"].get(vk, ""),
            })
        if recs:
            out[code] = pd.DataFrame.from_records(recs)
    return out


def build_monolingual(local_rows, pivots):
    """lang_code -> DataFrame[verse_key, text]  (deduped on text); plus 'eng'."""
    out = {}
    for code, pairs in local_rows.items():
        seen, recs = set(), []
        for vk, local in pairs:
            if local in seen:
                continue
            seen.add(local)
            recs.append({"verse_key": vk, "text": local})
        if recs:
            out[code] = pd.DataFrame.from_records(recs)
    en = pivots["en"]
    if en:
        out["eng"] = pd.DataFrame(
            [{"verse_key": k, "text": v} for k, v in en.items() if v]
        )
    return out


# ─────────────────────────────────────────────
# OUTPUT
# ─────────────────────────────────────────────

def write_local(frames, subdir):
    base = os.path.join(BUILD_DIR, subdir)
    os.makedirs(base, exist_ok=True)
    total = 0
    for cfg, df in frames.items():
        df.to_parquet(os.path.join(base, f"{cfg}.parquet"), index=False)
        total += len(df)
    print(f"  wrote {len(frames)} configs / {total} rows -> {base}")


def push(frames, repo_id, private):
    from datasets import Dataset
    from huggingface_hub import HfApi
    token = os.environ.get("HF_TOKEN")
    HfApi().create_repo(repo_id, repo_type="dataset", private=private,
                        exist_ok=True, token=token)
    for cfg, df in sorted(frames.items()):
        print(f"  push {repo_id} :: {cfg}  ({len(df)} rows)")
        Dataset.from_pandas(df, preserve_index=False).push_to_hub(
            repo_id, config_name=cfg, token=token, private=private)


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--namespace", default="afrispeech")
    ap.add_argument("--parallel-name", default="african-bible-parallel")
    ap.add_argument("--mono-name", default="african-bible-monolingual")
    ap.add_argument("--langs", nargs="*", default=None,
                    help="restrict to these lang_codes")
    ap.add_argument("--dry-run", action="store_true",
                    help="build parquet locally, do not upload")
    ap.add_argument("--private", action="store_true")
    args = ap.parse_args()

    langs_filter = set(args.langs) if args.langs else None

    print("Loading version metadata ...")
    by_id, _ = load_versions_meta(VERSIONS_CSV)
    print("Loading pivot caches ...")
    pivots = load_pivots()
    print("Collecting local verses ...")
    local_rows = collect_local_rows(by_id, langs_filter)
    print(f"  languages with scraped text: {len(local_rows)}")

    print("\nBuilding PARALLEL frames ...")
    par = build_parallel(local_rows, pivots)
    print(f"  parallel configs: {len(par)}")
    print("Building MONOLINGUAL frames ...")
    mono = build_monolingual(local_rows, pivots)
    print(f"  monolingual configs: {len(mono)}")

    if args.dry_run:
        write_local(par, "parallel")
        write_local(mono, "monolingual")
        print("\nDry run complete — nothing uploaded.")
        return

    par_repo  = f"{args.namespace}/{args.parallel_name}"
    mono_repo = f"{args.namespace}/{args.mono_name}"
    print(f"\nPushing parallel -> {par_repo}")
    push(par, par_repo, args.private)
    print(f"Pushing monolingual -> {mono_repo}")
    push(mono, mono_repo, args.private)
    print("\nDone.")


if __name__ == "__main__":
    main()
