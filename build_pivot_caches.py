"""
Pivot cache builder
===================
Fetches the pivot reference Bibles ONCE and stores them as flat caches that
build_and_push_hf.py joins onto the local-language text by verse_key.

Pivots (one good full OT+NT Bible per language):
    en  CEB    Common English Bible           (id 37)
    fr  LSG    Bible Segond 1910              (id 93)
    ar  AVD    New Van Dyck                   (id 13)
    zh  CUNPSS Chinese Union Version          (id 48)
    pt  ARA    Almeida Revista e Atualizada   (id 1608)

    python build_pivot_caches.py            # fetch all pivots
    python build_pivot_caches.py en fr      # fetch only some

Output:
    pivots/{lang}.csv          columns: verse_key, text
    pivots/progress.json       resume state
"""

import csv
import json
import os
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

from youversion_common import (
    ALL_BOOK_CODES, BOOK_CHAPTERS, NUM_WORKERS,
    get_chapter_verses, clean_text, build_session_pool,
)

# lang -> (version_id, abbreviation)  — edit here to swap a pivot translation.
PIVOTS = {
    "en": (37,   "CEB"),
    "fr": (93,   "LSG"),
    "ar": (13,   "AVD"),
    "zh": (48,   "CUNPSS"),
    "pt": (1608, "ARA"),
}

PIVOT_DIR     = "./pivots"
PROGRESS_FILE = os.path.join(PIVOT_DIR, "progress.json")

PROG_LOCK = threading.Lock()
CSV_LOCKS = {}
CSV_LOCKS_META = threading.Lock()


def csv_lock(path):
    with CSV_LOCKS_META:
        if path not in CSV_LOCKS:
            CSV_LOCKS[path] = threading.Lock()
        return CSV_LOCKS[path]


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress(prog):
    os.makedirs(PIVOT_DIR, exist_ok=True)
    tmp = PROGRESS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(prog, f)
    os.replace(tmp, PROGRESS_FILE)


def append_rows(path, rows):
    if not rows:
        return
    with csv_lock(path):
        write_header = not os.path.exists(path)
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["verse_key", "text"])
            if write_header:
                w.writeheader()
            w.writerows(rows)


def fetch_chapter(lang, version_id, book, chapter, csv_path, prog, done, session_q):
    session = session_q.get()
    try:
        verses = get_chapter_verses(session, version_id, book, chapter)
        rows = []
        if verses:
            for vn in sorted(verses):
                txt = clean_text(verses[vn])
                if txt:
                    rows.append({"verse_key": f"{book}.{chapter}.{vn}", "text": txt})
        append_rows(csv_path, rows)
        with PROG_LOCK:
            done.add(f"{book}.{chapter}")
            prog[lang] = list(done)
            save_progress(prog)
        return len(rows)
    finally:
        session_q.put(session)


def build_one(lang, session_q, prog):
    version_id, abbr = PIVOTS[lang]
    csv_path = os.path.join(PIVOT_DIR, f"{lang}.csv")
    done = set(prog.get(lang, []))
    print(f"\n{'='*60}\n  Pivot {lang} — {abbr} (v{version_id})\n{'='*60}")

    tasks = []
    for book in ALL_BOOK_CODES:
        for ch in range(1, BOOK_CHAPTERS[book] + 1):
            if f"{book}.{ch}" not in done:
                tasks.append((book, ch))
    print(f"  {len(tasks)} chapters to fetch ({len(done)} already done)")

    total = 0
    with ThreadPoolExecutor(max_workers=min(NUM_WORKERS, session_q.qsize())) as pool:
        futs = {pool.submit(fetch_chapter, lang, version_id, b, c, csv_path,
                            prog, done, session_q): (b, c) for b, c in tasks}
        for fut in as_completed(futs):
            try:
                total += fut.result()
            except Exception as e:
                b, c = futs[fut]
                print(f"  {b}.{c} failed: {e}")
    print(f"  {lang}: {total} verses cached -> {csv_path}")


def main():
    langs = [a for a in sys.argv[1:] if a in PIVOTS] or list(PIVOTS)
    print(f"Building pivot caches for: {', '.join(langs)}")
    os.makedirs(PIVOT_DIR, exist_ok=True)
    session_q = build_session_pool(NUM_WORKERS)
    prog = load_progress()
    for lang in langs:
        build_one(lang, session_q, prog)
    print(f"\nAll pivot caches done -> {os.path.abspath(PIVOT_DIR)}")


if __name__ == "__main__":
    main()
