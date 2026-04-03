#!/usr/bin/env python3
"""
Split the Culture complete-works omnibus EPUB into individual book files.

Usage:  python3 direction/scripts/split-epub.py
Output: books/  (at repo root, alongside Fonts/)

Run from the repo root.
"""

import zipfile
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
SOURCE = ROOT / "Iain M Banks - The Culture complete works.epub"
OUT_DIR = ROOT / "books"

# Map: directory number → (output title, path to OPF within that directory)
BOOKS = {
    "1":  ("Consider Phlebas",          "content.opf"),
    "2":  ("The Player of Games",        "OEBPS/PlayerofGames_opf.opf"),
    "3":  ("Use of Weapons",             "content.opf"),
    "4":  ("The State of the Art",       "content.opf"),
    "5":  ("Excession",                  "OEBPS/content.opf"),
    "6":  ("Inversions",                 "content.opf"),
    "7":  ("Look to Windward",           "content.opf"),
    "8":  ("Matter",                     "content.opf"),
    "9":  ("Surface Detail",             "OEBPS/package.opf"),
    "10": ("The Hydrogen Sonata",        "OEBPS/package.opf"),
    "11": ("A Few Notes on the Culture", "OEBPS/content.opf"),
    "12": ("A Few Notes on Marain",      "content.opf"),
}

CONTAINER_XML = """\
<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="{opf_path}" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

MIMETYPE = "application/epub+zip"


def make_epub(src_zip: zipfile.ZipFile, book_dir: str, title: str, opf_path: str) -> Path:
    prefix = f"{book_dir}/"
    book_files = [n for n in src_zip.namelist() if n.startswith(prefix) and not n.endswith("/")]

    safe = title.replace(":", "").replace("/", "-")
    out_path = OUT_DIR / f"Iain M Banks - {safe}.epub"

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as out:
        # EPUB spec: mimetype must be first entry, stored uncompressed
        mime_info = zipfile.ZipInfo("mimetype")
        mime_info.compress_type = zipfile.ZIP_STORED
        out.writestr(mime_info, MIMETYPE)

        # Container manifest pointing to this book's OPF
        out.writestr("META-INF/container.xml", CONTAINER_XML.format(opf_path=opf_path))

        # Copy all book files, stripping the leading directory prefix
        for name in book_files:
            rel = name[len(prefix):]
            if not rel:
                continue
            data = src_zip.read(name)
            info = zipfile.ZipInfo(rel)
            info.compress_type = zipfile.ZIP_DEFLATED
            out.writestr(info, data)

    return out_path


def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Source EPUB not found: {SOURCE}")

    OUT_DIR.mkdir(exist_ok=True)

    with zipfile.ZipFile(SOURCE, "r") as src:
        for book_dir, (title, opf_path) in BOOKS.items():
            out = make_epub(src, book_dir, title, opf_path)
            size_kb = out.stat().st_size // 1024
            print(f"  {out.name}  ({size_kb} KB)")

    print(f"\nDone. {len(BOOKS)} files written to {OUT_DIR}/")


if __name__ == "__main__":
    main()
