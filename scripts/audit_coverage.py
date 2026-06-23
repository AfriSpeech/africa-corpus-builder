"""
audit_coverage.py  —  maintainer tool
=====================================
Finds versions that are missing chapters WITHOUT re-scraping verse text, by
comparing what each version CSV captured against the source's real book/chapter
inventory from the bible.com version metadata endpoint.

Two modes (the dataset has ~900+ files, so the default avoids bulk downloads):

  --risk   (default)  Metadata-only. Flags versions the OLD single-book probe
                      would have mis-skipped: a version that HAS Old Testament
                      books but no Genesis, or HAS New Testament books but no
                      Matthew. Fast, no file downloads.

  --deep              Downloads each language CSV and reports the exact
                      chapters present in the source but absent from our data.
                      Thorough but bandwidth-heavy. Use --only to limit it.

Options
-------
  --hf REPO     dataset repo (default: $AFRICA_CORPUS_REPO or michsethowusu/africa-corpus)
  --only S      restrict --deep to filenames containing substring S

Usage
-----
  python scripts/audit_coverage.py                 # fast risk scan
  python scripts/audit_coverage.py --deep --only Nkonya
"""

import os
import re
import sys
import csv
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from huggingface_hub import HfApi, hf_hub_download

csv.field_size_limit(10_000_000)

HF_REPO_ID = os.environ.get("AFRICA_CORPUS_REPO", "michsethowusu/africa-corpus")
VERSION_API = "https://nodejs.bible.com/api/bible/version/3.1"
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
           "Accept-Language": "en-US,en;q=0.9"}

OT = set("GEN EXO LEV NUM DEU JOS JDG RUT 1SA 2SA 1KI 2KI 1CH 2CH EZR NEH EST "
         "JOB PSA PRO ECC SNG ISA JER LAM EZK DAN HOS JOL AMO OBA JON MIC NAM "
         "HAB ZEP HAG ZEC MAL".split())
NT = set("MAT MRK LUK JHN ACT ROM 1CO 2CO GAL EPH PHP COL 1TH 2TH 1TI 2TI TIT "
         "PHM HEB JAS 1PE 2PE 1JN 2JN 3JN JUD REV".split())
CANON = OT | NT
LANG_RE = re.compile(r"^(.+)_([a-z]{2,4})_v(\d+)\.csv$")


def version_meta(vid):
    """Return the set of book USFM codes the version contains, or None on error."""
    try:
        d = requests.get(VERSION_API, params={"id": vid},
                         headers=HEADERS, timeout=25).json()
        return {b["usfm"] for b in d.get("books", []) if b.get("usfm")}
    except Exception:
        return None


def source_chapters(vid):
    d = requests.get(VERSION_API, params={"id": vid}, headers=HEADERS, timeout=25).json()
    return {(m.group(1), int(m.group(2)))
            for b in d.get("books", []) if b.get("usfm") in CANON
            for c in b.get("chapters", []) if c.get("canonical")
            and (m := re.match(r"^([A-Z0-9]+)\.(\d+)$", c["usfm"]))}


def captured_chapters(fn):
    path = hf_hub_download(HF_REPO_ID, fn, repo_type="dataset")
    s = set()
    for r in csv.DictReader(open(path, encoding="utf-8")):
        try:
            b, c, _ = r["verse_key"].split("."); s.add((b, int(c)))
        except (ValueError, KeyError):
            pass
    return s


def lang_files():
    return sorted(f for f in HfApi().list_repo_files(HF_REPO_ID, repo_type="dataset")
                  if "/" not in f and LANG_RE.match(f))


def risk_scan(files):
    def scan(fn):
        vid = int(LANG_RE.match(fn).group(3))
        bks = version_meta(vid)
        if bks is None:
            return (fn, vid, "ERR")
        flags = []
        if (bks & OT) and "GEN" not in bks:
            flags.append("OT-no-GEN")
        if (bks & NT) and "MAT" not in bks:
            flags.append("NT-no-MAT")
        return (fn, vid, "+".join(flags))
    flagged, errors = [], []
    with ThreadPoolExecutor(max_workers=16) as pool:
        for fn, vid, r in (f.result() for f in as_completed(
                [pool.submit(scan, x) for x in files])):
            if r == "ERR":
                errors.append(fn)
            elif r:
                flagged.append((fn, vid, r))
    flagged.sort()
    print(f"\nAt-risk versions (old probe would mis-skip a testament): {len(flagged)}")
    for fn, vid, r in flagged:
        print(f"  {fn} (v{vid}): {r}")
    if errors:
        print(f"\nmetadata errors ({len(errors)}): {errors[:10]}")
    print("\nRun with --deep --only <name> to see exact missing chapters.")


def deep_scan(files):
    def audit(fn):
        vid = int(LANG_RE.match(fn).group(3))
        try:
            miss = sorted(source_chapters(vid) - captured_chapters(fn))
        except Exception as e:
            return (fn, vid, -1, str(e))
        return (fn, vid, len(miss), dict(Counter(b for b, _ in miss)))
    rows = []
    with ThreadPoolExecutor(max_workers=8) as pool:
        for r in (f.result() for f in as_completed(
                [pool.submit(audit, fn) for fn in files])):
            rows.append(r)
    rows.sort(key=lambda r: -r[2])
    gaps = [r for r in rows if r[2] > 0]
    print(f"\nFiles with missing chapters: {len(gaps)}/{len(files)}")
    for fn, vid, n, bk in gaps:
        print(f"  {fn} (v{vid}): {n} missing — {bk}")


def main():
    argv = sys.argv[1:]
    if "--hf" in argv:
        global HF_REPO_ID
        HF_REPO_ID = argv[argv.index("--hf") + 1]
    only = argv[argv.index("--only") + 1] if "--only" in argv else None

    files = lang_files()
    if only:
        files = [f for f in files if only.lower() in f.lower()]
    print(f"Auditing {len(files)} language file(s) on {HF_REPO_ID}")

    if "--deep" in argv:
        deep_scan(files)
    else:
        risk_scan(files)


if __name__ == "__main__":
    main()
