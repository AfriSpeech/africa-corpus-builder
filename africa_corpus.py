"""
africa_corpus.py  —  African parallel & monolingual corpus retrieval
====================================================================
A small library (and CLI) for pulling ready-made corpora from the verse
collections in `african_bible_parallel_text_datasets/`.

Everything in that directory is aligned on a shared `verse_key`
(BOOK.chapter.verse), so any two languages can be turned into a parallel
corpus with a single join — nothing is scraped at retrieval time.

What you can retrieve
---------------------
  • Parallel  African ↔ English           (English is the default target)
  • Parallel  African ↔ African           (e.g. Twi ↔ Swahili, Amharic ↔ Zulu)
  • Parallel  African ↔ other language    (French, Arabic, Chinese, Portuguese)
  • Monolingual corpus for any language

Library usage
-------------
    import africa_corpus as ac

    ac.list_languages()                        # what's available
    rows = ac.parallel("twi", "swh")           # [(verse_key, twi, swh), ...]
    rows = ac.parallel("twi")                  # twi ↔ English (default)
    sents = ac.monolingual("twi")              # ["...", "...", ...]
    ac.write_parallel_csv("twi", "swh", "twi_swh.csv")
    ac.write_monolingual_csv("twi", "twi.csv")

CLI usage
---------
    python africa_corpus.py --list
    python africa_corpus.py --source twi --target swh --out twi_swh.csv
    python africa_corpus.py --source twi                       # twi ↔ English
    python africa_corpus.py --monolingual twi --out twi.csv
    python africa_corpus.py --source all --out-dir corpora/    # all languages
    python africa_corpus.py                                    # interactive

Source: verse text comes from public Bible translations via YouVersion.
"""

import argparse
import csv
import os
import random
import re
import sys

csv.field_size_limit(10_000_000)

# ─────────────────────────────────────────────
# PATHS & CONSTANTS
# ─────────────────────────────────────────────

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.join(REPO_ROOT, "african_bible_parallel_text_datasets")

HF_REPO_ID   = os.environ.get("AFRICA_CORPUS_REPO", "michsethowusu/africa-corpus")
HF_REPO_TYPE = "dataset"

_NON_LANG_FILES = {"english_cache.csv", "progress.json",
                   "progress.json.tmp", "testament_status.json"}

_BOOK_ORDER = [
    "GEN","EXO","LEV","NUM","DEU","JOS","JDG","RUT","1SA","2SA",
    "1KI","2KI","1CH","2CH","EZR","NEH","EST","JOB","PSA","PRO",
    "ECC","SNG","ISA","JER","LAM","EZK","DAN","HOS","JOL","AMO",
    "OBA","JON","MIC","NAM","HAB","ZEP","HAG","ZEC","MAL",
    "MAT","MRK","LUK","JHN","ACT","ROM","1CO","2CO","GAL","EPH",
    "PHP","COL","1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAS",
    "1PE","2PE","1JN","2JN","3JN","JUD","REV",
]
_BOOK_INDEX = {b: i for i, b in enumerate(_BOOK_ORDER)}

_LANG_FILE_RE = re.compile(r"^(?P<name>.+)_(?P<code>[a-z]{2,8})_v(?P<vid>\d+)\.csv$")


def _verse_sort_key(verse_key: str):
    try:
        book, ch, vs = verse_key.split(".")
        return (_BOOK_INDEX.get(book, 999), int(ch), int(vs))
    except (ValueError, KeyError):
        return (999, 0, 0)


# ─────────────────────────────────────────────
# DATA ACCESS  (local cache + HuggingFace download)
# ─────────────────────────────────────────────

_FILE_LIST: list | None = None


def _local_csvs() -> list:
    if not os.path.isdir(DATA_ROOT):
        return []
    out = []
    for root, _dirs, files in os.walk(DATA_ROOT):
        for name in files:
            full = os.path.join(root, name)
            if name.endswith(".csv") and os.path.getsize(full) >= 64:
                rel = os.path.relpath(full, DATA_ROOT)
                out.append(rel.replace(os.sep, "/"))
    return out


def dataset_files() -> list:
    """Repo-relative paths of every data CSV (local copy if present, else HF)."""
    global _FILE_LIST
    if _FILE_LIST is None:
        local = _local_csvs()
        if local:
            _FILE_LIST = local
        else:
            try:
                from huggingface_hub import HfApi
            except ImportError:
                raise RuntimeError(
                    "No local data found and huggingface_hub is not installed.\n"
                    "Install it with:  pip install huggingface_hub")
            files = HfApi().list_repo_files(HF_REPO_ID, repo_type=HF_REPO_TYPE)
            _FILE_LIST = [f for f in files if f.endswith(".csv")]
    return _FILE_LIST


def data_path(rel: str) -> str:
    """Resolve a repo-relative CSV to a local path, downloading from HF if needed."""
    local = os.path.join(DATA_ROOT, rel)
    if os.path.exists(local):
        return local
    try:
        from huggingface_hub import hf_hub_download
    except ImportError:
        raise RuntimeError(
            f"'{rel}' is not present locally and huggingface_hub is not installed.\n"
            f"Install it with:  pip install huggingface_hub")
    return hf_hub_download(HF_REPO_ID, rel, repo_type=HF_REPO_TYPE)


# ─────────────────────────────────────────────
# LANGUAGE REGISTRY
# ─────────────────────────────────────────────

class Language:
    def __init__(self, code, name, kind, files=None, text_column="text"):
        self.code        = code
        self.name        = name
        self.kind        = kind          # "african" | "reference"
        self.files       = files or []
        self.text_column = text_column

    def __repr__(self):
        return f"<Language {self.code} '{self.name}' ({self.kind})>"


def _group_by_filename(rels, kind, text_column) -> dict:
    langs: dict = {}
    for rel in sorted(rels):
        fname = rel.split("/")[-1]
        m = _LANG_FILE_RE.match(fname)
        if not m:
            continue
        code = m.group("code")
        name = m.group("name").replace("_", " ")
        if code not in langs:
            langs[code] = Language(code, name, kind, files=[], text_column=text_column)
        if name not in langs[code].name:
            langs[code].name += f" / {name}"
        langs[code].files.append(rel)
    return langs


def _discover_african() -> dict:
    """African datasets: top-level `{Name}_{code}_v{id}.csv` files."""
    rels = [r for r in dataset_files()
            if "/" not in r and r.split("/")[-1] not in _NON_LANG_FILES]
    return _group_by_filename(rels, "african", "local")


def _discover_reference() -> dict:
    """Reference languages from `reference_caches/` + English from `english_cache.csv`."""
    files = dataset_files()
    rels  = [r for r in files if r.startswith("reference_caches/")]
    langs = _group_by_filename(rels, "reference", "text")
    if "english_cache.csv" in files:
        langs["en"] = Language("en", "English", "reference",
                               files=["english_cache.csv"], text_column="eng")
    return langs


_REGISTRY: dict | None = None


def registry() -> dict:
    global _REGISTRY
    if _REGISTRY is None:
        reg = _discover_african()
        reg.update(_discover_reference())
        _REGISTRY = reg
    return _REGISTRY


def refresh():
    """Forget the cached file list and registry (useful in long-running processes)."""
    global _FILE_LIST, _REGISTRY
    _FILE_LIST = None
    _REGISTRY  = None


def resolve(token: str) -> Language:
    """Look a language up by exact code or exact (case-insensitive) name."""
    reg   = registry()
    token = token.strip()
    if token in reg:
        return reg[token]
    low = token.lower()
    for lang in reg.values():
        if lang.code.lower() == low:
            return lang
        name_parts = [p.strip().lower() for p in lang.name.split("/")]
        if low in name_parts:
            return lang
    raise KeyError(f"Unknown language '{token}'. Run with --list to see available codes.")


# ─────────────────────────────────────────────
# VERSE LOADING
# ─────────────────────────────────────────────

def _load_verses(lang: Language) -> dict:
    """Return {verse_key: {distinct texts}} for a language."""
    verses: dict = {}
    for rel in lang.files:
        path = data_path(rel)
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            col = lang.text_column if lang.text_column in (reader.fieldnames or []) else None
            if col is None:
                col = "local" if lang.kind == "african" else "text"
            for row in reader:
                key  = row.get("verse_key")
                text = (row.get(col) or "").strip()
                if key and text:
                    verses.setdefault(key, set()).add(text)
    return verses


# ─────────────────────────────────────────────
# PUBLIC API
# ─────────────────────────────────────────────

def list_languages():
    """Return (african, reference) lists of Language objects."""
    reg       = registry()
    african   = sorted((l for l in reg.values() if l.kind == "african"),   key=lambda l: l.name)
    reference = sorted((l for l in reg.values() if l.kind == "reference"), key=lambda l: l.name)
    return african, reference


def _apply_limit(rows: list, limit, sample: bool, seed: int) -> list:
    if limit is None or limit >= len(rows):
        return rows
    if not sample:
        return rows[:limit]
    idx = sorted(random.Random(seed).sample(range(len(rows)), limit))
    return [rows[i] for i in idx]


def parallel(source: str, target: str = "en", limit=None,
             sample: bool = False, seed: int = 0) -> list:
    """Aligned (verse_key, source_text, target_text) rows for two languages."""
    a = resolve(source)
    b = resolve(target)
    if a.code == b.code:
        raise ValueError("Source and target languages must differ.")

    va = _load_verses(a)
    vb = _load_verses(b)
    shared = set(va) & set(vb)

    rows: list = []
    seen: set  = set()
    for key in sorted(shared, key=_verse_sort_key):
        for ta in va[key]:
            for tb in vb[key]:
                pair = (ta, tb)
                if pair in seen:
                    continue
                seen.add(pair)
                rows.append((key, ta, tb))
    return _apply_limit(rows, limit, sample, seed)


def monolingual(language: str, limit=None, sample: bool = False,
                seed: int = 0) -> list:
    """Return the deduplicated list of sentences for one language."""
    lang   = resolve(language)
    verses = _load_verses(lang)
    seen: set = set()
    out:  list = []
    for key in sorted(verses, key=_verse_sort_key):
        for text in sorted(verses[key]):
            if text not in seen:
                seen.add(text)
                out.append(text)
    return _apply_limit(out, limit, sample, seed)


def write_parallel_csv(source: str, target: str, out_path: str,
                       limit=None, sample: bool = False, seed: int = 0) -> int:
    a    = resolve(source)
    b    = resolve(target)
    rows = parallel(source, target, limit=limit, sample=sample, seed=seed)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["verse_key", a.code, b.code])
        w.writerows(rows)
    return len(rows)


def write_monolingual_csv(language: str, out_path: str, limit=None,
                          sample: bool = False, seed: int = 0) -> int:
    lang  = resolve(language)
    sents = monolingual(language, limit=limit, sample=sample, seed=seed)
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow([lang.code])
        for s in sents:
            w.writerow([s])
    return len(sents)


def all_african_codes() -> list:
    """Codes of every available African language, in display-name order."""
    african, _ = list_languages()
    return [l.code for l in african]


def build_batch(sources: list, target: str = "en",
                monolingual_mode: bool = False, limit=None,
                sample: bool = False, seed: int = 0,
                out_dir: str = ".") -> list:
    """Write one corpus file per source language. Returns [(code, path, row_count)]."""
    os.makedirs(out_dir, exist_ok=True)
    results: list = []
    for src in sources:
        code = resolve(src).code
        try:
            if monolingual_mode:
                out_path = os.path.join(out_dir, f"{code}_monolingual.csv")
                n = write_monolingual_csv(src, out_path, limit, sample, seed)
            else:
                tcode = resolve(target).code
                if tcode == code:
                    print(f"  skip {code}: same as target")
                    continue
                out_path = os.path.join(out_dir, f"{code}_{tcode}_parallel.csv")
                n = write_parallel_csv(src, target, out_path, limit, sample, seed)
            results.append((code, out_path, n))
            print(f"  {code}: {n:,} rows -> {out_path}")
        except (KeyError, ValueError) as e:
            print(f"  skip {src}: {e}")
    return results


# ─────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────

def _print_languages():
    african, reference = list_languages()
    print(f"\nAfrican languages ({len(african)}):")
    for l in african:
        print(f"  {l.code:8s}  {l.name}")
    print("\nReference languages (usable as parallel target):")
    for l in reference:
        print(f"  {l.code:8s}  {l.name}")
    print()


def _default_out_name(source: str, target) -> str:
    a = resolve(source).code
    if target is None:
        return f"{a}_monolingual.csv"
    b = resolve(target).code
    return f"{a}_{b}_parallel.csv"


def _parse_sources(spec: str) -> list:
    if spec.strip().lower() == "all":
        return all_african_codes()
    return [s.strip() for s in spec.split(",") if s.strip()]


def _interactive():
    _print_languages()
    mode = input("Build [p]arallel or [m]onolingual corpus? [p]: ").strip().lower()
    mono = mode.startswith("m")

    prompt = ("Language(s) — code, comma-separated list, or 'all' "
              if mono else
              "Source language(s) — code, comma-separated list, or 'all' ")
    sources = _parse_sources(input(prompt + ": ").strip() or "all")

    target = None
    if not mono:
        target = input("Target language code [en]: ").strip() or "en"

    lim = input("Number of samples per language [all]: ").strip()
    limit  = int(lim) if lim.isdigit() else None
    sample = False
    if limit:
        sample = input("Random sample? [y/N]: ").strip().lower().startswith("y")

    if len(sources) == 1:
        out = _default_out_name(sources[0], target)
        if mono:
            n = write_monolingual_csv(sources[0], out, limit, sample)
        else:
            n = write_parallel_csv(sources[0], target, out, limit, sample)
        print(f"\nWrote {n:,} rows to {out}")
    else:
        out_dir = input("Output directory [corpora]: ").strip() or "corpora"
        build_batch(sources, target, mono, limit, sample, out_dir=out_dir)
        print(f"\nDone — files written to {out_dir}/")


def main():
    ap = argparse.ArgumentParser(
        description="Retrieve parallel or monolingual corpora for African languages.")
    ap.add_argument("--list", action="store_true", help="list available languages")
    ap.add_argument("-s", "--source",
                    help="source language(s): a code, comma-separated list, or 'all'")
    ap.add_argument("-t", "--target", default="en",
                    help="target language code for parallel corpora (default: en)")
    ap.add_argument("-m", "--monolingual", action="store_true",
                    help="build monolingual corpora instead of parallel")
    ap.add_argument("-n", "--limit", type=int,
                    help="max samples per language (default: all)")
    ap.add_argument("--sample", action="store_true",
                    help="randomly sample --limit rows instead of taking the first N")
    ap.add_argument("--seed", type=int, default=0,
                    help="random seed for --sample (default: 0)")
    ap.add_argument("--out", help="output CSV path (single language)")
    ap.add_argument("--out-dir", default="corpora",
                    help="output directory when building for multiple languages")
    args = ap.parse_args()

    if args.list:
        _print_languages()
        return

    if not args.source:
        try:
            _interactive()
        except (KeyError, ValueError) as e:
            sys.exit(f"Error: {e}")
        return

    sources = _parse_sources(args.source)
    target  = None if args.monolingual else args.target

    try:
        if len(sources) == 1:
            out = args.out or _default_out_name(sources[0], target)
            if args.monolingual:
                n = write_monolingual_csv(sources[0], out, args.limit,
                                          args.sample, args.seed)
            else:
                n = write_parallel_csv(sources[0], target, out, args.limit,
                                       args.sample, args.seed)
            print(f"Wrote {n:,} rows to {out}")
        else:
            build_batch(sources, target, args.monolingual, args.limit,
                        args.sample, args.seed, out_dir=args.out_dir)
            print(f"Done — files written to {args.out_dir}/")
    except (KeyError, ValueError) as e:
        sys.exit(f"Error: {e}")


if __name__ == "__main__":
    main()
