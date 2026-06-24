---
license: other
pretty_name: Africa Corpus
configs:
  - config_name: african_languages
    default: true
    data_files:
      - split: train
        path: "*_v*.csv"
  - config_name: english
    data_files:
      - split: train
        path: english_cache.csv
  - config_name: reference_caches
    data_files:
      - split: train
        path: reference_caches/*.csv
language:
  - af
  - am
  - ar
  - en
  - fr
  - ha
  - ig
  - lg
  - ln
  - mg
  - ny
  - om
  - pt
  - rw
  - sg
  - so
  - sn
  - st
  - sw
  - ti
  - tn
  - ts
  - tw
  - wo
  - xh
  - yo
  - zh
  - zu
task_categories:
  - translation
  - text-generation
tags:
  - africa
  - african-languages
  - low-resource
  - parallel-corpus
  - machine-translation
  - bible
multilinguality:
  - multilingual
  - translation
---

# Africa Corpus

Verse-aligned text for **693 African languages**, plus several world languages,
for building **parallel** and **monolingual** corpora. Every language is aligned
on a shared verse key, so any two languages can be joined into a parallel corpus:

- African ↔ English (English is the default pair)
- African ↔ African (e.g. Twi ↔ Yoruba, Hausa ↔ Amharic)
- African ↔ other language (French, Arabic, Chinese, Portuguese)
- Monolingual corpus for any single language

## How to use

This dataset is meant to be used through the **Africa Corpus Builder** library,
which downloads only the files you need and joins them for you:

👉 **https://github.com/michsethowusu/africa-corpus-builder**

```bash
pip install huggingface_hub
git clone https://github.com/michsethowusu/africa-corpus-builder.git
cd africa-corpus-builder

# Swahili ↔ English
python africa_corpus.py --source swc

# Twi ↔ Yoruba, a random 5,000-pair sample
python africa_corpus.py --source twi --target yor --limit 5000 --sample

# Monolingual Hausa
python africa_corpus.py --source hau --monolingual

# List every available language
python africa_corpus.py --list
```

You can also load the raw CSVs directly:

```python
from huggingface_hub import hf_hub_download
import pandas as pd

path = hf_hub_download("michsethowusu/africa-corpus",
                       "Swahili_swc_v74.csv", repo_type="dataset")
df = pd.read_csv(path)
```

## Layout

The dataset is split into three viewer configs because the file groups have
different columns:

| Config | File pattern | Columns |
|---|---|---|
| `african_languages` | `{Language}_{code}_v{id}.csv` | `verse_key, version_id, local` |
| `english` | `english_cache.csv` | `verse_key, eng` |
| `reference_caches` | `reference_caches/{Language}_{code}_v{id}.csv` | `verse_key, version_id, lang_code, text` |

All files share the `verse_key` column (e.g. `JHN.3.16`), which is how any two
languages are aligned. The filename itself encodes the language name, code, and
Bible version id, so each file is self-describing.

## Coverage

693 African languages, covering all major African
language families: Niger-Congo, Afro-Asiatic, Nilo-Saharan, Khoisan, and
Austronesian (Madagascar). Total verse records: ~16 million.

Reference languages available as parallel targets: English (CEB), French (LSG),
Arabic (AVD), Chinese (CUNPSS), Portuguese (ARA).

## Source & license

Text is derived from public **Bible translations** retrieved from
[YouVersion](https://www.bible.com). Please review YouVersion's terms of service
before redistributing derived data. The accompanying code is released under the
MIT License (see the GitHub repository).

## Acknowledgements

Inspired by [ghana-corpus-builder](https://github.com/GhanaNLP/ghana-corpus-builder)
by the [Ghana NLP Community](https://ghananlp.org). Language–macroarea mapping
from [Glottolog](https://glottolog.org). If you use this data in research,
please cite the underlying Bible-translation sources.
