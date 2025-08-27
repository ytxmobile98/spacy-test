import argparse
import pathlib
import spacy

CURDIR = pathlib.Path(__file__).resolve().parent
doc_path = CURDIR / "docs" / "text-sample.txt"

# Trained pipelines for Chinese:
# https://spacy.io/models/zh
PIPELINES = set([
    "zh_core_web_sm",
    "zh_core_web_md",
    "zh_core_web_lg",
])


def tokenize(pipeline: str, text: str):
    nlp = spacy.load(pipeline)
    doc = nlp(text)
    return doc


def parse_args():
    parser = argparse.ArgumentParser(description="SpaCy Tokenization")
    parser.add_argument(
        "-p", "--pipeline", choices=PIPELINES, required=True,
        help="SpaCy pipeline to use")
    return parser.parse_args()


def main(args: argparse.Namespace):
    text = doc_path.read_text()
    doc = tokenize(args.pipeline, text)
    for token in doc:
        print(token.text, token.idx)


if __name__ == "__main__":
    main(parse_args())
