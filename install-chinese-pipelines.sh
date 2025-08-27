#!/usr/bin/env bash

# Install Chinese pipelines for spaCy.
# Reference: https://spacy.io/models/zh
# We only install the first three pipelines optimized for CPU.

# Here we use the `uv` command to install these pipelines:
uv add \
    'https://github.com/explosion/spacy-models/releases/download/zh_core_web_lg-3.8.0/zh_core_web_lg-3.8.0-py3-none-any.whl' \
    'https://github.com/explosion/spacy-models/releases/download/zh_core_web_md-3.8.0/zh_core_web_md-3.8.0-py3-none-any.whl' \
    'https://github.com/explosion/spacy-models/releases/download/zh_core_web_sm-3.8.0/zh_core_web_sm-3.8.0-py3-none-any.whl'