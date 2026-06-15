"""
Shared scraping helpers for the Africa MT builder.

Used by both the local-text scraper (youversion_parallel_text_builder.py) and
the pivot-cache builder (build_pivot_caches.py) so the chapter-fetch / parse /
clean logic lives in exactly one place.
"""

import re
import time
from queue import Queue

import requests
from bs4 import BeautifulSoup


# ─────────────────────────────────────────────
# CONFIG (shared)
# ─────────────────────────────────────────────

NUM_WORKERS     = 16
REQUEST_DELAY   = 2      # seconds between requests per worker
REQUEST_TIMEOUT = 20
MAX_RETRIES     = 3
RETRY_WAIT      = 5

CHAPTER_API = "https://nodejs.bible.com/api/bible/chapter/3.1"

REQUEST_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept":          "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
}

ALL_BOOK_CODES = [
    "GEN","EXO","LEV","NUM","DEU","JOS","JDG","RUT","1SA","2SA",
    "1KI","2KI","1CH","2CH","EZR","NEH","EST","JOB","PSA","PRO",
    "ECC","SNG","ISA","JER","LAM","EZK","DAN","HOS","JOL","AMO",
    "OBA","JON","MIC","NAM","HAB","ZEP","HAG","ZEC","MAL",
    "MAT","MRK","LUK","JHN","ACT","ROM","1CO","2CO","GAL","EPH",
    "PHP","COL","1TH","2TH","1TI","2TI","TIT","PHM","HEB","JAS",
    "1PE","2PE","1JN","2JN","3JN","JUD","REV",
]

BOOK_CHAPTERS = {
    "GEN":50,"EXO":40,"LEV":27,"NUM":36,"DEU":34,"JOS":24,"JDG":21,
    "RUT":4,"1SA":31,"2SA":24,"1KI":22,"2KI":25,"1CH":29,"2CH":36,
    "EZR":10,"NEH":13,"EST":10,"JOB":42,"PSA":150,"PRO":31,"ECC":12,
    "SNG":8,"ISA":66,"JER":52,"LAM":5,"EZK":48,"DAN":12,"HOS":14,
    "JOL":3,"AMO":9,"OBA":1,"JON":4,"MIC":7,"NAM":3,"HAB":3,"ZEP":3,
    "HAG":2,"ZEC":14,"MAL":4,
    "MAT":28,"MRK":16,"LUK":24,"JHN":21,"ACT":28,"ROM":16,"1CO":16,
    "2CO":13,"GAL":6,"EPH":6,"PHP":4,"COL":4,"1TH":5,"2TH":3,"1TI":6,
    "2TI":4,"TIT":3,"PHM":1,"HEB":13,"JAS":5,"1PE":5,"2PE":3,"1JN":5,
    "2JN":1,"3JN":1,"JUD":1,"REV":22,
}


# ─────────────────────────────────────────────
# TEXT CLEANING
# ─────────────────────────────────────────────

def clean_text(text: str) -> str:
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\d+', '', text)
    lines = text.splitlines()
    processed = []
    for line in lines:
        line = line.strip()
        if line:
            if line[-1] not in ['.', '!', '?', ':', ';']:
                line += '.'
            processed.append(line)
    text = ' '.join(processed)
    text = re.sub(r'[\"“”‘’\(\)\[\]\{\}]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[,.]{2,}', '.', text)
    text = re.sub(r'([,.!?;:])\.', '.', text)
    if text and not text.endswith('.'):
        text += '.'
    return text


# ─────────────────────────────────────────────
# CHAPTER-LEVEL FETCHING  (YouVersion JSON API)
# ─────────────────────────────────────────────

def parse_chapter_content(content_html: str, book: str, chapter: int) -> dict:
    """Return {verse_num: raw_text} from a chapter API `content` HTML blob."""
    soup = BeautifulSoup(content_html, "lxml")
    prefix = f"{book}.{chapter}."
    parts: dict = {}

    for span in soup.find_all("span", attrs={"data-usfm": True}):
        usfm = span["data-usfm"]
        if not usfm.startswith(prefix):
            continue
        tail = usfm[len(prefix):]
        try:
            verse_num = int(re.split(r"[-+]", tail)[0])
        except ValueError:
            continue
        content_spans = span.select("span.content")
        if content_spans:
            text = " ".join(c.get_text(" ", strip=True) for c in content_spans)
        else:
            text = span.get_text(" ", strip=True)
        text = text.strip()
        if text:
            parts.setdefault(verse_num, []).append(text)

    return {n: " ".join(chunks) for n, chunks in parts.items()}


def get_chapter_verses(session: requests.Session, version_num: int, book: str,
                       chapter: int) -> dict:
    """
    Fetch one chapter via the JSON API and return {verse_num: raw_text}.
    Returns None if the chapter cannot be fetched or has no parseable verses.
    """
    params = {"id": version_num, "reference": f"{book}.{chapter}"}
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            time.sleep(REQUEST_DELAY)
            resp = session.get(CHAPTER_API, params=params,
                               headers=REQUEST_HEADERS, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 404:
                return None
            resp.raise_for_status()
            data = resp.json()
            content = data.get("content", "")
            if not content:
                return None
            verses = parse_chapter_content(content, book, chapter)
            return verses if verses else None
        except Exception:
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_WAIT)
            else:
                return None
    return None


# ─────────────────────────────────────────────
# SESSION POOL
# ─────────────────────────────────────────────

def build_session_pool(n: int) -> Queue:
    q = Queue()
    for _ in range(n):
        s = requests.Session()
        s.headers.update(REQUEST_HEADERS)
        q.put(s)
    print(f"  {n} HTTP sessions ready")
    return q
