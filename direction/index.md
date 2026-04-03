# Contributor Knowledge Base — Index

This directory captures key insights, decisions, and utility scripts for anyone working on the Marain project — human contributors and AI tools alike. It records *why* things are the way they are, not just *what* they are.

Check this index before starting work on code or architecture.

---

## Notes

| File | Summary |
|------|---------|
| [encoding-density-and-packets.md](encoding-density-and-packets.md) | Density calculation (9-bit glyphs ≈ 3.6 bits/letter vs ASCII's 8); reframing of the 16-bit word as `[glyph: 9] + [context: 7]` — the non-slate bits as an embedded context packet |

---

## Scripts

| File | Purpose | Language |
|------|---------|----------|
| [dict-to-tsv.py](scripts/dict-to-tsv.py) | Convert `language/raw/marain-*.js` source files to TSV for database import | Python 3 |
| [split-epub.py](scripts/split-epub.py) | Split the Culture complete-works omnibus EPUB into 12 individual book files → `books/` | Python 3 |
| [rag-extract.py](scripts/rag-extract.py) | Extract Marain references (passages, ship names, vocabulary, character names) from each novel → `docs/source/culture-marain/` | Python 3 |

---

## Conventions

- Notes go in `direction/` as `.md` files; add a row to the Notes table above.
- Scripts go in `direction/scripts/`; add a row to the Scripts table above.
- Update files in place when they improve — do not create duplicates.
- Capture the *why*, not just the *what* — decisions without rationale decay fast.
- If a note matures into something formal, promote it to `docs/`.
