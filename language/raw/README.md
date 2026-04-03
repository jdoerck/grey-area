# language/raw/

Original source files from [Marain Tools](https://marain-tools.netlify.app/). Kept as reference; **not** the canonical format for this project.

| File | Contents |
|------|----------|
| `marain-alpha.js` | Alphabet: 32 letters with phoneme, IPA, and letter-name data |
| `marain-dict.js` | Vocabulary: ~430 words with gloss and definition |
| `marain-sentences.js` | 3 example sentences with word-by-word and idiomatic glosses |

Canonical formats live in the parent directories:
- [`../phonemes/alphabet.md`](../phonemes/alphabet.md) and [`../phonemes/alphabet.tsv`](../phonemes/alphabet.tsv)
- [`../vocabulary.tsv`](../vocabulary.tsv) and [`../vocabulary.md`](../vocabulary.md)
- [`../translations/sentences.md`](../translations/sentences.md)

To regenerate the TSV files from these sources: `python3 direction/scripts/dict-to-tsv.py`
