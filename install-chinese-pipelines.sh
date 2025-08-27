#!/usr/bin/env bash

# Install Chinese pipelines for spaCy
# Reference: https://spacy.io/models/zh

# Download these pipelines for CPU inference (local testing)
PIPELINES=(
    zh_core_web_sm
    zh_core_web_md
    zh_core_web_lg
)
for PIPELINE in "${PIPELINES[@]}"; do
    python3 -m spacy download "$PIPELINE"
done