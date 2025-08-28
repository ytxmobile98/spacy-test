import argparse
from pathlib import Path
import spacy

# Trained pipelines for Chinese:
# https://spacy.io/models/zh
PIPELINES = set([
    "zh_core_web_sm",
    "zh_core_web_md",
    "zh_core_web_lg",
])


def parse_args():
    parser = argparse.ArgumentParser(description="SpaCy Tokenization")

    parser.add_argument(
        "-f", "--input-file", type=str, required=True,
        help="Path to the text document to tokenize")
    parser.add_argument(
        "-p", "--pipeline", choices=PIPELINES, required=True,
        help="SpaCy pipeline to use")
    return parser.parse_args()


def main(args: argparse.Namespace):
    text = Path(args.input_file).read_text()
    nlp = spacy.load(args.pipeline)
    doc = nlp(text)
    for token in doc:
        print(token.text, token.idx)


if __name__ == "__main__":
    main(parse_args())
