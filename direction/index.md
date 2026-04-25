# Contributor Knowledge Base — Index

This directory captures key insights, decisions, and utility scripts for anyone working on the Marain project — human contributors and AI tools alike. It records *why* things are the way they are, not just *what* they are.

Check this index before starting work on code or architecture.

---

## Notes

| File | Summary |
|------|---------|
| [encoding-density-and-packets.md](encoding-density-and-packets.md) | Density calculation (9-bit glyphs ≈ 3.6 bits/letter vs ASCII's 8); the packet as `[slate: 9] + [rails + herald: 7]` — why 2 bytes, and why the spare 7 bits become embedded context |
| [esperanto-and-hangul.md](esperanto-and-hangul.md) | Case study of two designed languages — Esperanto failed without state backing; Hangul survived 450 years in the cultural basement on Sejong's *imprimatur* and won. Pulls out seven adoption lessons for marain: substrate over content, cheaper-not-just-better, working iconicity, lock-the-foundation/free-the-surface, surviving the wilderness years, additive composition, politics-as-engineering. |
| [glyph-grid-orientation.md](glyph-grid-orientation.md) | Design flaw: original grid rendering was inverted relative to Banks' vision. Fix: 180° rotation in SVG generation. Why it matters: visual representation carries semantic meaning in constructed languages. |
| [glyph-png-assets.md](glyph-png-assets.md) | How to use PNG glyph icons in documentation — location (`docs/assets/glyphs/`), generation, markdown reference syntax, relationship to the interactive glyph table. |
| [mvp.md](mvp.md) | Narrow MVP definition — 6 deliverables (terminology ✅, invariant policy, glyph index confidence, reference renderer, macro layout, legibility tests), explicit out-of-scope list, definition of done |

---

## Scripts

| File | Purpose | Language |
|------|---------|----------|
| [dict-to-tsv.py](scripts/dict-to-tsv.py) | Convert `language/raw/marain-*.js` source files to TSV for database import | Python 3 |
| [split-epub.py](scripts/split-epub.py) | Split the Culture complete-works omnibus EPUB into 12 individual book files → `books/` | Python 3 |
| [rag-extract.py](scripts/rag-extract.py) | Extract Marain references (passages, ship names, vocabulary, character names) from each novel → `notes/source/culture-marain/` | Python 3 |
| [generate-glyph-table.py](scripts/generate-glyph-table.py) | Generate `docs/index.html` from `encoding/docs/glyph-table.tsv` — interactive glyph table for GitHub Pages | Python 3 |
| [generate-glyph-pngs.py](scripts/generate-glyph-pngs.py) | Generate PNG icons (64px default) of all glyphs from TSV → `docs/assets/glyphs/` for use in documentation | Python 3 |

---

## Skills

Claude Code skills live in `skill/`. Run `./skill/install.sh` to symlink them into
`~/.claude/skills/` and invoke with `/marain`, etc.

| Skill | Command | Purpose |
|-------|---------|---------|
| [marain](../skill/marain/marain.md) | `/marain` | Linguistic + encoding rigour for Marain work |

See `skill/direction.md` for conventions on adding new skills.

---

## Conventions

- Notes go in `direction/` as `.md` files; add a row to the Notes table above.
- Scripts go in `direction/scripts/`; add a row to the Scripts table above.
- Update files in place when they improve — do not create duplicates.
- Capture the *why*, not just the *what* — decisions without rationale decay fast.
- If a note matures into something formal, promote it to `notes/`.
