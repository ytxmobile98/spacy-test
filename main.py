import pathlib
import spacy

CURDIR = pathlib.Path(__file__).resolve().parent
doc_path = CURDIR / "docs" / "text-sample.txt"

nlp = spacy.blank("zh")
doc = nlp(doc_path.read_text())
for token in doc:
    print(token.text, token.idx)
