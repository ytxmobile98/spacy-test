# spaCy test

## Setup

```bash
uv sync
```

## Running

```bash
# Tokenization test
python3 main.py --pipeline <pipeline> --input-file <input-file>
```

Supported pipelines:

* zh_core_web_sm
* zh_core_web_md
* zh_core_web_lg

> See: <https://spacy.io/models/zh>
>
> (The first three pipelines on this page are supported, for local CPU inference)