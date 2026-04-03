#!/usr/bin/env python3
"""
Convert Marain Tools JS source files to TSV for database import.

Source: https://marain-tools.netlify.app/
Usage:  python3 direction/scripts/dict-to-tsv.py
Output: language/vocabulary.tsv, language/phonemes/alphabet.tsv

Run from the repo root.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent


def strip_js_var(text: str, varname: str) -> str:
    """Strip 'var name = ' prefix and trailing ';', fix trailing comma."""
    text = re.sub(rf"^\s*var {varname}\s*=\s*", "", text.strip())
    text = text.rstrip().rstrip(";").rstrip()
    # Remove trailing comma before closing brace/bracket (invalid JSON)
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def parse_dict():
    path = ROOT / "language" / "raw" / "marain-dict.js"
    text = path.read_text(encoding="utf-8")
    text = strip_js_var(text, "dict")
    return json.loads(text)


def parse_alpha():
    path = ROOT / "language" / "raw" / "marain-alpha.js"
    text = path.read_text(encoding="utf-8")
    # File contains two var declarations; extract just the dict object
    match = re.search(r"var alpha\s*=\s*(\{.*?\})\s*var lexorder", text, re.DOTALL)
    if not match:
        sys.exit("Could not parse marain-alpha.js")
    obj_text = re.sub(r",(\s*\})", r"\1", match.group(1))
    return json.loads(obj_text)


def write_vocabulary_tsv(data: dict):
    out = ROOT / "language" / "vocabulary.tsv"
    with out.open("w", encoding="utf-8") as f:
        f.write("word\tgloss\tdefinition\tpos\n")
        for word, entry in data.items():
            gloss = entry.get("gloss", "").strip()
            definition = entry.get("def", "").strip()
            pos = entry.get("pos", "").strip()
            # Escape any tabs in values
            row = "\t".join([word, gloss, definition, pos])
            f.write(row + "\n")
    print(f"Written: {out} ({len(data)} entries)")


def write_alphabet_tsv(data: dict):
    out = ROOT / "language" / "phonemes" / "alphabet.tsv"
    with out.open("w", encoding="utf-8") as f:
        f.write("key\tname\tphoneme\tletter_name\tipa\ttype\n")
        for key, vals in data.items():
            row = "\t".join([key] + vals)
            f.write(row + "\n")
    print(f"Written: {out} ({len(data)} entries)")


if __name__ == "__main__":
    write_vocabulary_tsv(parse_dict())
    write_alphabet_tsv(parse_alpha())
