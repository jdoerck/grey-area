# Marain Alphabet

Phoneme inventory and letter names for Marain M1.

**Source:** [Marain Tools](https://marain-tools.netlify.app/) — compiled by the Marain Tools project.  
**Raw data:** [`../raw/marain-alpha.js`](../raw/marain-alpha.js)  
**Machine-readable:** [`alphabet.tsv`](alphabet.tsv)

---

## Notes on the table

- **Key** — the romanization key used by Marain Tools (case-sensitive: uppercase letters are distinct phonemes from their lowercase counterparts)
- **Phoneme** — romanized transcription as used in Marain Tools
- **Letter name** — the Marain word for this letter (used when spelling out)
- **IPA** — International Phonetic Alphabet transcription
- **Type** — V = vowel · C = consonant

---

## Vowels

Table ordered by Marain lexical order (`u a i o A E j O e`).

| Key | Name | Phoneme | Letter name | IPA | Type |
|-----|------|---------|-------------|-----|------|
| `u` | uh | uh | uh | ʌ | V |
| `a` | ah | a | a | a | V |
| `i` | ih | ih | ihk | ɪ | V |
| `o` | oh | o | ot | o | V |
| `A` | ay | ay | ayyuhm | aɪ | V |
| `E` | ee | i | iye | i | V |
| `j` | je | ye | ye | jɛ | V |
| `O` | oo | u | uf | u | V |
| `e` | eh | e | ep | ɛ | V |

---

## Consonants

Table ordered by Marain lexical order (`w m h d p s t l C k b H f v L n g G z S y r T`).

| Key | Name | Phoneme | Letter name | IPA | Type |
|-----|------|---------|-------------|-----|------|
| `w` | w | w | wa | w | C |
| `m` | m | m | ma | m | C |
| `h` | h | h | hek | h | C |
| `d` | d | d | de | d | C |
| `p` | p | p | pika | p | C |
| `s` | s | s | seth | s | C |
| `t` | t | t | tawa | t | C |
| `l` | l | l | le | l | C |
| `C` | tch | tch | tchey | t͡x | C |
| `k` | k | k | keluh | k | C |
| `b` | b | b | bat | b | C |
| `H` | ch | ch | chem | x | C |
| `f` | f | f | ihf | f | C |
| `v` | v | v | vash | v | C |
| `L` | ll | ll | llewu | ɬ | C |
| `n` | n | n | nek | n | C |
| `g` | g | g | gu | g | C |
| `G` | ng | ng | eng | ŋ | C |
| `z` | z | z | zau | z | C |
| `S` | sh | sh | shihk | ʃ | C |
| `y` | y | y | yoter | j | C |
| `r` | r | r | rek | r | C |
| `T` | th | th | tham | θ | C |

---

## Lexical order

The full Marain lexical sort order (digits → letters → punctuation):

```
0 1 2 3 4 5 6 7 w u m h d a p s t i l C k o b H f A v L n E g G z e j S y O r T , " .
```

Digits precede all letters. Uppercase letters (`C H A L E G S O T`) are distinct from lowercase and sort separately within the order above.

---

## Open questions

- This inventory reflects the community/Marain Tools interpretation. It does not yet incorporate Banks' phoneme assignments or the marainkit encoding decisions. See [`../../encoding/docs/roadmap.md`](../../encoding/docs/roadmap.md) for the open phoneme strategy decision.
- The `j` phoneme is classified as a vowel here (type `v`) — it is the palatal approximant /jɛ/, functioning as a semivowel. This may need reconciliation with the abjad structure being designed in the marainkit encoding layer.
