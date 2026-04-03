# Marain Vocabulary

Community vocabulary list compiled from Marain Tools.

**Source:** [Marain Tools](https://marain-tools.netlify.app/) — compiled by the Marain Tools project.  
**Entries:** 430  
**Raw data:** [`raw/marain-dict.js`](raw/marain-dict.js)  
**Canonical format:** [`vocabulary.tsv`](vocabulary.tsv)

---

## Format — vocabulary.tsv

Tab-separated, UTF-8, with header row:

| Column | Description |
|--------|-------------|
| `word` | Marain word in romanized form (case-sensitive) |
| `gloss` | Short English gloss (interlinear label) |
| `definition` | Full English definition |
| `pos` | Part of speech — largely unpopulated in source data; `pos` is a placeholder |

The TSV is the canonical format for this data. It can be imported directly into SQLite or any relational database. See [`../../docs/rationale.md`](../docs/rationale.md) for the planned dictionary architecture (Marain → concept ID mapping).

---

## Conversion script

[`direction/scripts/dict-to-tsv.py`](../../direction/scripts/dict-to-tsv.py) — converts `language/raw/marain-dict.js` and `language/raw/marain-alpha.js` to TSV. Run from the repo root:

```bash
python3 direction/scripts/dict-to-tsv.py
```

---

## Notes on the source data

- Part-of-speech tagging is largely absent — the `pos` field reads `"pos"` for almost all entries (a placeholder). One entry has `"det"` (`aka`), one has `"noun"` (`ak`).
- Several multi-word entries exist (e.g. `"des sAk"` = to close, `"fAyont dam pAwAkA"` = rhyme scheme). These are lexicalised phrases, not phrases to be parsed compositionally.
- Spelling uses case-sensitive romanization matching the alphabet in [`phonemes/alphabet.md`](phonemes/alphabet.md).

---

## Relationship to marainkit encoding

This vocabulary is community-derived (via Marain Tools / Reddit conlang) and is not yet reconciled with Banks' canonical phoneme assignments or the marainkit glyph encoding. Before using this vocabulary in Column B encoding work, consult [`../encoding/docs/roadmap.md`](../encoding/docs/roadmap.md) for the open decisions on phoneme strategy and number base.
