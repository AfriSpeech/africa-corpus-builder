"""
Build & push the African Bible datasets to Hugging Face
=======================================================
Consumes:
    african_bible_parallel_text_datasets/{Lang}_{code}_v{id}.csv   (verse_key, version_id, local)
    pivots/{en,fr,ar,zh,pt}.csv                                    (verse_key, text)

Produces two Hugging Face datasets, each with ONE config (subset) per language:

  1. PARALLEL  ({namespace}/african-bible-parallel)
       columns: verse_key, lang_code, local, en, fr, ar, zh, pt

  2. MONOLINGUAL  ({namespace}/african-bible-monolingual)
       One config per African language (local text only) + an `eng` config.

Strategy to avoid HF rate limits (128 commits/hour):
  Phase 1 — build all parquet files locally (no API calls, resumable)
  Phase 2 — upload each repo in ONE bulk commit via upload_large_folder

Usage:
    python build_and_push_hf.py --build-only      # phase 1: build parquets locally
    python build_and_push_hf.py --push-only        # phase 2: upload (needs HF login)
    python build_and_push_hf.py                    # both phases
    python build_and_push_hf.py --namespace michsethowusu
    python build_and_push_hf.py --langs twi ewe    # only these languages
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
import json
import os

import pandas as pd

LOCAL_ROOT    = "./african_bible_parallel_text_datasets"
PIVOT_DIR     = "./pivots"
VERSIONS_CSV  = "youversion_africa_versions.csv"
BUILD_DIR     = "./hf_build"
BUILD_PROGRESS = "./build_progress.json"
PIVOT_LANGS   = ["en", "fr", "ar", "zh", "pt"]

csv.field_size_limit(10**7)


# ─────────────────────────────────────────────
# BUILD PROGRESS  (resume phase 1)
# ─────────────────────────────────────────────

def load_build_progress():
    if os.path.exists(BUILD_PROGRESS):
        return json.load(open(BUILD_PROGRESS))
    return {"parallel": [], "monolingual": []}

def save_build_progress(prog):
    tmp = BUILD_PROGRESS + ".tmp"
    json.dump(prog, open(tmp, "w"))
    os.replace(tmp, BUILD_PROGRESS)


# ─────────────────────────────────────────────
# METADATA & PIVOTS
# ─────────────────────────────────────────────

def load_versions_meta(path):
    by_lang = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vid = (row.get("version_id") or "").strip()
            if not vid.isdigit():
                continue
            code = (row["lang_code"] or "").strip()
            name = (row["lang_name"] or "").strip()
            by_lang.setdefault(code, []).append((int(vid), name))
    return by_lang


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
        print(f"  pivot {lang}: {len(d):,} verses")
    return pivots


# ─────────────────────────────────────────────
# PER-LANGUAGE BUILD
# ─────────────────────────────────────────────

def load_local_for_lang(lang_code, versions):
    rows = []
    for vid, lname in versions:
        path = os.path.join(LOCAL_ROOT, lang_csv_name(lname, lang_code, vid))
        if not os.path.exists(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                local = (r.get("local") or "").strip()
                if local:
                    rows.append((r["verse_key"], local))
    return rows


def build_parallel_df(lang_code, pairs, pivots):
    en = pivots["en"]
    seen, recs = set(), []
    for vk, local in pairs:
        if (vk, local) in seen:
            continue
        seen.add((vk, local))
        if vk not in en:
            continue
        recs.append({
            "verse_key": vk, "lang_code": lang_code, "local": local,
            "en": en.get(vk, ""), "fr": pivots["fr"].get(vk, ""),
            "ar": pivots["ar"].get(vk, ""), "zh": pivots["zh"].get(vk, ""),
            "pt": pivots["pt"].get(vk, ""),
        })
    return pd.DataFrame.from_records(recs) if recs else None


def build_mono_df(pairs):
    seen, recs = set(), []
    for vk, local in pairs:
        if local in seen:
            continue
        seen.add(local)
        recs.append({"verse_key": vk, "text": local})
    return pd.DataFrame.from_records(recs) if recs else None


# ─────────────────────────────────────────────
# PARQUET PATH HELPERS
# HF datasets expects: data/{config_name}/train-*.parquet
# ─────────────────────────────────────────────

def parquet_path(dataset, config):
    return os.path.join(BUILD_DIR, dataset, "data", config, "train-00000-of-00001.parquet")

def parquet_exists(dataset, config):
    return os.path.exists(parquet_path(dataset, config))

def write_parquet(df, dataset, config):
    path = parquet_path(dataset, config)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_parquet(path, index=False)


# ─────────────────────────────────────────────
# DATASET CARD
# ─────────────────────────────────────────────

def write_dataset_card(dataset_dir, repo_id, configs, description):
    configs_yaml = "\n".join(
        f"  - config_name: {c}\n    data_files:\n      - split: train\n        path: data/{c}/train-*.parquet"
        for c in sorted(configs)
    )
    card = f"""---
configs:
{configs_yaml}
---

# {repo_id.split('/')[-1]}

{description}

**Configs (subsets):** {len(configs)} languages/variants.

Built with [africa-mt-builder](https://github.com/AfriSpeech/africa-mt-builder).
"""
    with open(os.path.join(dataset_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(card)


# ─────────────────────────────────────────────
# PHASE 1 — BUILD PARQUETS LOCALLY
# ─────────────────────────────────────────────

def phase_build(by_lang, pivots, langs_filter, prog):
    all_langs = sorted(by_lang.keys())
    if langs_filter:
        all_langs = [l for l in all_langs if l in langs_filter]
    total = len(all_langs)

    # English monolingual
    if "eng" not in prog["monolingual"]:
        en = pivots["en"]
        if en:
            df = pd.DataFrame([{"verse_key": k, "text": v} for k, v in en.items() if v])
            write_parquet(df, "monolingual", "eng")
            print(f"  built monolingual::eng  ({len(df):,} rows)")
            del df
        prog["monolingual"].append("eng")
        save_build_progress(prog)

    for idx, code in enumerate(all_langs, 1):
        versions = by_lang[code]
        par_done  = code in prog["parallel"]
        mono_done = code in prog["monolingual"]
        if par_done and mono_done:
            continue

        pairs = load_local_for_lang(code, versions)
        if not pairs:
            if not par_done:
                prog["parallel"].append(code)
            if not mono_done:
                prog["monolingual"].append(code)
            save_build_progress(prog)
            continue

        if not par_done:
            df = build_parallel_df(code, pairs, pivots)
            if df is not None:
                write_parquet(df, "parallel", code)
                print(f"  [{idx}/{total}] parallel::{code}  {len(df):,} rows")
                del df
            prog["parallel"].append(code)
            save_build_progress(prog)

        if not mono_done:
            df = build_mono_df(pairs)
            if df is not None:
                write_parquet(df, "monolingual", code)
                print(f"  [{idx}/{total}] monolingual::{code}  {len(df):,} rows")
                del df
            prog["monolingual"].append(code)
            save_build_progress(prog)

        del pairs

    print(f"\nPhase 1 done — parquets in {os.path.abspath(BUILD_DIR)}")


# ─────────────────────────────────────────────
# PHASE 2 — BULK UPLOAD
# ─────────────────────────────────────────────

def phase_push(namespace, par_name, mono_name, private, token):
    from huggingface_hub import HfApi
    api = HfApi()

    for dataset, name in [("parallel", par_name), ("monolingual", mono_name)]:
        repo_id  = f"{namespace}/{name}"
        data_dir = os.path.join(BUILD_DIR, dataset)
        if not os.path.exists(data_dir):
            print(f"  {dataset}: no build dir found, skipping")
            continue

        configs = [
            d for d in os.listdir(os.path.join(data_dir, "data"))
            if os.path.isdir(os.path.join(data_dir, "data", d))
        ] if os.path.exists(os.path.join(data_dir, "data")) else []

        desc = (
            "African-language Bible verses paired with English, French, Arabic, "
            "Chinese, and Portuguese translations."
            if dataset == "parallel" else
            "African-language Bible verses — monolingual text per language, "
            "plus an English (CEB) subset."
        )
        write_dataset_card(data_dir, repo_id, configs, desc)

        print(f"\nPushing {repo_id}  ({len(configs)} configs) ...")
        api.create_repo(repo_id, repo_type="dataset", private=private,
                        exist_ok=True, token=token)
        api.upload_large_folder(
            folder_path=data_dir,
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
        )
        print(f"  Done -> https://huggingface.co/datasets/{repo_id}")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--namespace", default="michsethowusu")
    ap.add_argument("--parallel-name",  default="african-bible-parallel")
    ap.add_argument("--mono-name",      default="african-bible-monolingual")
    ap.add_argument("--langs", nargs="*", default=None)
    ap.add_argument("--build-only", action="store_true", help="Phase 1 only")
    ap.add_argument("--push-only",  action="store_true", help="Phase 2 only (parquets must exist)")
    ap.add_argument("--private", action="store_true")
    args = ap.parse_args()

    token = os.environ.get("HF_TOKEN")
    langs_filter = set(args.langs) if args.langs else None

    if not args.push_only:
        print("=== Phase 1: Building parquets locally ===")
        print("Loading version metadata ...")
        by_lang = load_versions_meta(VERSIONS_CSV)
        print("Loading pivot caches ...")
        pivots = load_pivots()
        prog = load_build_progress()
        phase_build(by_lang, pivots, langs_filter, prog)

    if not args.build_only:
        print("\n=== Phase 2: Bulk upload to HuggingFace ===")
        phase_push(args.namespace, args.parallel_name, args.mono_name,
                   args.private, token)

    print("\nAll done!")


if __name__ == "__main__":
    main()
