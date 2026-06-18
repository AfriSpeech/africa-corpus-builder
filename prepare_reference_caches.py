"""
prepare_reference_caches.py  —  convert pivot caches to the corpus format
=========================================================================
Reads the pivot Bible caches in `pivots/` (built by build_pivot_caches.py)
and writes them into `african_bible_parallel_text_datasets/` in the format
that `africa_corpus.py` expects:

  english_cache.csv                     verse_key, eng
  reference_caches/French_fr_v93.csv    verse_key, version_id, lang_code, text
  reference_caches/Arabic_ar_v13.csv
  reference_caches/Chinese_zh_v48.csv
  reference_caches/Portuguese_pt_v1608.csv

Run this once before push_to_hf.py.

    python prepare_reference_caches.py
"""

import csv
import os

PIVOT_DIR = "./pivots"
OUT_ROOT  = "./african_bible_parallel_text_datasets"
REF_DIR   = os.path.join(OUT_ROOT, "reference_caches")

csv.field_size_limit(10_000_000)

# Pivot metadata: lang_code -> (version_id, display_name, abbr)
PIVOTS = {
    "en": (37,   "English",    "CEB"),
    "fr": (93,   "French",     "LSG"),
    "ar": (13,   "Arabic",     "AVD"),
    "zh": (48,   "Chinese",    "CUNPSS"),
    "pt": (1608, "Portuguese", "ARA"),
}


def convert_english():
    src = os.path.join(PIVOT_DIR, "en.csv")
    dst = os.path.join(OUT_ROOT, "english_cache.csv")
    if not os.path.exists(src):
        print(f"  skip en (no pivots/en.csv)")
        return
    os.makedirs(OUT_ROOT, exist_ok=True)
    rows = 0
    with open(src, newline="", encoding="utf-8") as fin, \
         open(dst, "w", newline="", encoding="utf-8") as fout:
        w = csv.DictWriter(fout, fieldnames=["verse_key", "eng"])
        w.writeheader()
        for row in csv.DictReader(fin):
            if row.get("text"):
                w.writerow({"verse_key": row["verse_key"], "eng": row["text"]})
                rows += 1
    print(f"  english_cache.csv  {rows:,} verses")


def convert_reference(lang_code):
    vid, name, abbr = PIVOTS[lang_code]
    src = os.path.join(PIVOT_DIR, f"{lang_code}.csv")
    fname = f"{name}_{lang_code}_v{vid}.csv"
    dst = os.path.join(REF_DIR, fname)
    if not os.path.exists(src):
        print(f"  skip {lang_code} (no pivots/{lang_code}.csv)")
        return
    os.makedirs(REF_DIR, exist_ok=True)
    rows = 0
    with open(src, newline="", encoding="utf-8") as fin, \
         open(dst, "w", newline="", encoding="utf-8") as fout:
        w = csv.DictWriter(fout, fieldnames=["verse_key", "version_id", "lang_code", "text"])
        w.writeheader()
        for row in csv.DictReader(fin):
            if row.get("text"):
                w.writerow({
                    "verse_key":  row["verse_key"],
                    "version_id": vid,
                    "lang_code":  lang_code,
                    "text":       row["text"],
                })
                rows += 1
    print(f"  reference_caches/{fname}  {rows:,} verses")


def main():
    print("Preparing reference caches ...")
    convert_english()
    for code in ["fr", "ar", "zh", "pt"]:
        convert_reference(code)
    print("Done.")


if __name__ == "__main__":
    main()
