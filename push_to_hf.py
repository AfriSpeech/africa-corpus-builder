"""
push_to_hf.py  —  maintainer tool (incremental sync)
=====================================================
Keeps the HuggingFace dataset that `africa_corpus.py` reads from in sync
with your local `african_bible_parallel_text_datasets/` directory.

By default it APPENDS: it lists what is already on HuggingFace, compares
against your local CSVs, and uploads only the files not yet there.

Users never run this; they only read the data — `africa_corpus.py`
automatically picks up anything new on HuggingFace the next time it runs.

What gets uploaded
------------------
  • every African language CSV   ({Name}_{code}_v{id}.csv)
  • english_cache.csv
  • reference_caches/*.csv

Run `prepare_reference_caches.py` first to build the english_cache and
reference_caches from the pivot files.

Auth
----
Uses your cached HuggingFace login, or set HF_TOKEN in the environment:
    export HF_TOKEN=hf_your_token

Usage
-----
    python push_to_hf.py                       # append new files only
    python push_to_hf.py --dry-run             # show what would upload
    python push_to_hf.py --sync                # re-upload all (HF skips unchanged)
    python push_to_hf.py --repo michsethowusu/africa-corpus
"""

import os
import sys

from huggingface_hub import HfApi
from huggingface_hub.utils import RepositoryNotFoundError

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.join(REPO_ROOT, "african_bible_parallel_text_datasets")

HF_REPO_ID   = os.environ.get("AFRICA_CORPUS_REPO", "michsethowusu/africa-corpus")
HF_REPO_TYPE = "dataset"

SKIP      = {"progress.json", "progress.json.tmp", "testament_status.json"}
MIN_BYTES = 64


def collect_local() -> list:
    rels = []
    for root, _dirs, files in os.walk(DATA_ROOT):
        for name in files:
            if name in SKIP or not name.endswith(".csv"):
                continue
            local = os.path.join(root, name)
            if os.path.getsize(local) < MIN_BYTES:
                continue
            rel = os.path.relpath(local, DATA_ROOT).replace(os.sep, "/")
            rels.append(rel)
    return sorted(rels)


def remote_files(api: HfApi, repo_id: str) -> set:
    try:
        return set(api.list_repo_files(repo_id, repo_type=HF_REPO_TYPE))
    except RepositoryNotFoundError:
        return set()


def main():
    argv    = sys.argv[1:]
    dry_run = "--dry-run" in argv
    sync    = "--sync"    in argv
    repo_id = HF_REPO_ID
    for i, a in enumerate(argv):
        if a == "--repo" and i + 1 < len(argv):
            repo_id = argv[i + 1]

    token = os.environ.get("HF_TOKEN")
    api   = HfApi(token=token)

    local = collect_local()
    if not local:
        sys.exit(
            f"No data files found under {DATA_ROOT}\n"
            f"Run prepare_reference_caches.py first, then re-run this script."
        )

    remote  = remote_files(api, repo_id)
    new      = [r for r in local if r not in remote]
    existing = [r for r in local if r in remote]

    print(f"Local data files  : {len(local)}")
    print(f"Already on HF     : {len(existing)}")
    print(f"New (not on HF)   : {len(new)}")
    for r in new:
        print(f"   + {r}")

    to_upload = local if sync else new
    if not to_upload:
        print("\nHuggingFace is already up to date.")
        return

    if dry_run:
        print(f"\n[dry-run] would upload {len(to_upload)} file(s); nothing sent.")
        return

    print(f"\nEnsuring dataset repo {repo_id} ...")
    api.create_repo(repo_id=repo_id, repo_type=HF_REPO_TYPE,
                    exist_ok=True, private=False)

    print(f"Uploading {len(to_upload)} file(s) ...")
    api.upload_folder(
        repo_id=repo_id,
        repo_type=HF_REPO_TYPE,
        folder_path=DATA_ROOT,
        allow_patterns=to_upload,
        commit_message=("Sync Africa corpus data" if sync
                        else f"Add {len(to_upload)} new corpus file(s)"),
    )
    print(f"\nDone: https://huggingface.co/datasets/{repo_id}")


if __name__ == "__main__":
    main()
