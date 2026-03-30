# Glyph Decisions — Comparison Tables and Design Discussion

Working document for resolving open encoding decisions. Captures all known glyph assignments across Banks, zakalwe2040, and marainkit for the three contested layers: phonemes, numerals, and operators.

For actionable decisions and priority order see [`roadmap.md`](roadmap.md).
For the full glyph catalogue see [`glyphs.md`](glyphs.md).
For the current assigned-values index see [`glyph-index.md`](glyph-index.md).

---

## Phonemes

Banks published 32 phonemes as a glyph-table image[^1] — most values are approximate visual reads at low resolution and flagged `†`. Only *w* (#121) is confirmed explicitly in the essay text. zakalwe2040 published a 24-consonant abjad with values extracted from `docs/abjad.svg`. The two sets were compared programmatically; only *ma* and *la* match.

`†` = Banks approximate (image read, unverified)
`‡` = zakalwe2040 (SVG-extracted)
`✓` = cross-system match · `✗` = conflict · `—` = no assignment in that system
`[I]` = conflicts with a marainkit invariant

| Phoneme | Banks # | Banks Pattern | Z # | Z Pattern | Status |
|---------|---------|---------------|-----|-----------|--------|
| m / *ma* | 457 † | `█░░/█░░/███` | 457 ‡ | `█░░/█░░/███` | ✓ |
| w / *wa* | **121** | `█░░/███/█░░` | 511 ‡ | `███/███/███` | ✗ Z uses marainkit Full [I] |
| p / *pa* | 459 † | `██░/█░░/███` | 79 ‡ | `███/█░░/█░░` | ✗ |
| b / *ba* | 432 † | `░░░/░██/░██` | 295 ‡ | `███/░░█/░░█` | ✗ Z's ba = Banks' *n* value |
| f / *fa* | 56 † | `░░░/███/░░░` | 173 ‡ | `█░█/█░█/░█░` | ✗ |
| v / *va* | **367 †** | `███/█░█/█░█` | 362 ‡ | `░█░/█░█/█░█` | ✗ Banks *v* = Z *sa* (#367) |
| th / *tha* | 186 † | `░█░/███/░█░` | 133 ‡ | `█░█/░░░/░█░` | ✗ Banks' *th* = marainkit Cross [I] |
| — / *dtha* | — | — | 319 ‡ | `███/███/░░█` | — |
| tch / *cha* | 60 † | `░░█/███/░░░` | 127 ‡ | `███/███/█░░` | ✗ |
| ch | **174 †** | `░██/█░█/░█░` | 127 ‡ | `███/███/█░░` | ✗ (ch ≠ cha — different phonemes) |
| — / *dja* | — | — | 465 ‡ | `█░░/░█░/███` | — |
| t / *ta* | 168 † | `░░░/█░█/░█░` | 307 ‡ | `██░/░██/░░█` | ✗ |
| n / *na* | 295 † | `███/░░█/░░█` | 493 ‡ | `█░█/█░█/███` | ✗ Z's *na* = Banks' *h* value |
| s / *sa* | 214 † | `░██/░█░/██░` | 367 ‡ | `███/█░█/█░█` | ✗ |
| d / *da* | 480 † | `░░░/░░█/███` | 87 ‡ | `███/░█░/█░░` | ✗ |
| l / *la* | 484 † | `░░█/░░█/███` | 484 ‡ | `░░█/░░█/███` | ✓ |
| z / *za* | 384 † | `░░░/░░░/░██` | 469 ‡ | `█░█/░█░/███` | ✗ |
| r / *ra* | 292 † | `░░█/░░█/░░█` | 189 ‡ | `█░█/███/░█░` | ✗ |
| sh / *sha* | 57 † | `█░░/███/░░░` | 383 ‡ | `███/███/█░█` | ✗ |
| y / *ya* | 184 † | `░░░/███/░█░` | 468 ‡ | `░░█/░█░/███` | ✗ |
| g / *ga* | 120 † | `░░░/███/█░░` | 502 ‡ | `░██/░██/███` | ✗ |
| k / *ka* | 312 † | `░░░/███/░░█` | 500 ‡ | `░░█/░██/███` | ✗ |
| ng / *nga* | 16 | `░░░/░█░/░░░` | 509 ‡ | `█░█/███/███` | ✗ Banks' *ng* = marainkit Point [I] |
| ah / *aa* | 456 † | `░░░/█░░/███` | 322 ‡ | `░█░/░░░/█░█` | ✗ |
| h / *ha* | 493 † | `█░█/█░█/███` | 487 ‡ | `███/░░█/███` | ✗ Z's *ha* ≠ Z's *na* (#493) |
| *ay* | 2 † | `░█░/░░░/░░░` | — | — | Banks only |
| *eh* | 32 † | `░░░/░░█/░░░` | — | — | Banks only |
| *ee* | 50 † | `░█░/░██/░░░` | — | — | Banks only |
| *ih* | 84 † | `░░█/░█░/█░░` | — | — | Banks only |
| *uh* | 273 † | `█░░/░█░/░░█` | — | — | Banks only |
| *oh* | **118 †** | `░██/░██/█░░` | — | — | Banks only — previously misread as #170 |
| *ch* | **174 †** | `░██/█░█/░█░` | — | — | Banks only — no Z equivalent |
| *v* | **367 †** | `███/█░█/█░█` | — | — | Banks *v* value = Z *sa* (#367) — cross-system conflict |
| *ll* | **469 †** | `█░█/░█░/███` | — | — | Banks only — no Z equivalent; = Z *za* value (#469) |
| *je* | **431 †** | `███/█░█/░██` | — | — | Banks only — no Z equivalent |

**Summary:** 2 of 24 cross-system matches (*ma*, *la*). 1 confirmed canonical Banks value (*w* = #121). 2 Banks phonemes land on marainkit invariants (#16/*ng*, #186/*th*). *oh* and *oo* were previously misread as #170 (Diamond) — both resolved to non-invariant values (#118, #371). Diamond is now unambiguously marainkit-only.

---

## Numerals

Banks states Marain uses **base 8 (octal)** — 8 digits, none with published values. zakalwe2040 uses **base 10 (decimal)**, digit names from Mandarin Chinese.

| Digit | Banks # | zakalwe2040 # | Z Pattern | Conflicts |
|-------|---------|---------------|-----------|-----------|
| 0 | unpublished | 341 ‡ | `█░█/░█░/█░█` | Z = marainkit Checkerboard [I]; marainkit assigns #0 (Empty) to zero/null |
| 1 | 1 (implied †) | 471 ‡ | `███/░█░/███` | Banks implies #1 = "the number one" |
| 2 | unpublished | 466 ‡ | `░█░/░█░/███` | — |
| 3 | unpublished | **121** ‡ | `█░░/███/█░░` | **Z = Banks' canonical *w*** |
| 4 | unpublished | 243 ‡ | `██░/░██/██░` | — |
| 5 | unpublished | 95 ‡ | `███/██░/█░░` | — |
| 6 | unpublished | 373 ‡ | `█░█/░██/█░█` | — |
| 7 | unpublished | 125 ‡ | `█░█/███/█░░` | — |
| 8 | N/A (base-8) | 317 ‡ | `█░█/███/░░█` | — |
| 9 | N/A (base-8) | 381 ‡ | `█░█/███/█░█` | — |

**Key tension:** Base-8 vs base-10 is an architectural choice, not a glyph choice. Choosing base-8 (Banks) eliminates the digit-3/#121 conflict entirely — digits 8 and 9 simply don't exist, and all 8 digit values would need to be freshly assigned.

---

## Operators and Notation

Banks defines no operator values. All assignments below are zakalwe2040. Column "Conflicts" notes collisions with marainkit invariants or Banks phonemes.

### Arithmetic

| Symbol | Meaning | # | Pattern | Conflicts |
|--------|---------|---|---------|-----------|
| `+` | addition | 170 ‡ | `░█░/█░█/░█░` | marainkit Diamond (danger/hazard); Banks *oh* [I] |
| `×` | multiplication | 495 ‡ | `███/█░█/███` | marainkit Frame (container) [I] |
| `−` | subtraction | 300 ‡ | `░░█/█░█/░░█` | — |
| `÷` | division | 364 ‡ | `░░█/█░█/█░█` | — |
| `mod` | modulo | 301 ‡ | `█░█/█░█/░░█` | — |

### Logic

| Symbol | Marain name | # | Pattern | Conflicts |
|--------|------------|---|---------|-----------|
| `&` | *wa* (and) | 284 ‡ | `░░█/██░/░░█` | — |
| `\|` | *ow* (or) | 113 ‡ | `█░░/░██/█░░` | — |
| `!` | *ma* (not) | 343 ‡ | `███/░█░/█░█` | — |

### Equality and copula

| Symbol | Marain name | # | Pattern | Conflicts |
|--------|------------|---|---------|-----------|
| `=` | *heeya* (equality) | 63 ‡ | `███/███/░░░` | — |
| `:=` | *kun* (define/assign) | 191 ‡ | `███/███/░█░` | — |
| `iz` | *iz* (copula — to be) | 186 ‡ | `░█░/███/░█░` | marainkit Cross (alert/stop); Banks *th* [I] |

### Punctuation

| Symbol | Marain name | # | Pattern | Conflicts |
|--------|------------|---|---------|-----------|
| `?` | *mahu* (question / λ) | 342 ‡ | `░██/░█░/█░█` | — |
| `.` | period / decimal point | **16** ‡ | `░░░/░█░/░░░` | **✓ Agrees with marainkit Point and Banks decimal point** |
| `,` | comma | 128 ‡ | `░░░/░░░/░█░` | — |
| `;` | semicolon | 144 ‡ | `░░░/░█░/░█░` | — |

### Brackets and delimiters

No conflicts with marainkit invariants or Banks phonemes in this entire set. Open/close pairs are bit-mirror images of each other — visually coherent.

| Symbol | # | Pattern | Mirror of |
|--------|---|---------|-----------|
| `>` | 81 ‡ | `█░░/░█░/█░░` | `<` #276 |
| `<` | 276 ‡ | `░░█/░█░/░░█` | `>` #81 |
| `]` | 211 ‡ | `██░/░█░/██░` | `[` #406 |
| `[` | 406 ‡ | `░██/░█░/░██` | `]` #211 |
| `)` | 251 ‡ | `██░/███/██░` | `(` #446 |
| `(` | 446 ‡ | `░██/███/░██` | `)` #251 |
| `}` | 479 ‡ | `███/██░/███` | `{` #503 |
| `{` | 503 ‡ | `███/░██/███` | `}` #479 |

---

## Discussion

*Recorded from design sessions — not resolved decisions. See [`roadmap.md`](roadmap.md) for the actionable backlog.*

### On the phoneme layer

The two systems (Banks and zakalwe2040) are effectively independent designs. Both use the M1 3×3 binary grid, but made almost entirely different phoneme-to-value choices — only *ma* (#457) and *la* (#484) agree. This is not surprising: Banks never published his mapping rationale, and zakalwe2040 started fresh with an explicit design principle (place of articulation + homoiconicity).

The confidence levels are asymmetric. Banks is canonical but mostly unverifiable — 30 of 32 phoneme values are approximate image reads from a low-resolution photograph, and any one of them could be wrong. zakalwe2040's values are precisely extracted from SVG source but non-canonical. The single strongest data point in the entire system is Banks explicitly writing "*w* = #121" in prose. Everything else is provisional.

A "hybrid" approach — accepting only *ma* and *la* as confirmed cross-system values and leaving the rest open — is honest about uncertainty but doesn't produce a usable phoneme layer. A decision is eventually required: follow Banks' approximate values, follow zakalwe2040's designed abjad, or define a fresh marainkit assignment.

### On the abjad architecture

zakalwe2040's abjad is organized by place of articulation (bilabial → glottal), then frequency — explicitly designed for high-frequency speech optimization. Banks' system has no documented organizing principle beyond "glyphs can be rotated without confusion." For a practical implementation, zakalwe2040's structure is more learnable and internally consistent.

However, adopting it means accepting *wa* = #511, which permanently assigns the all-filled glyph (our "maximum/critical/full stop") to the most common bilabial approximant in the language. That's a real cost.

### On the buffer bit and long vowels

Banks defines a 10th "buffer bit" after each 9-bit glyph in transmission. It is currently unassigned. zakalwe2040 handles vowel length through diacritic channels in the 4×5 lattice. Both are solving the same problem — distinguishing short from long vowels — through different mechanisms.

Using the 10th bit as a long-vowel marker is appealing because: it costs nothing (the bit already exists), it's compatible with both the M1 3×3 grid and the 4×5 lattice, and it parallels the Hebrew/Arabic distinction between consonant-only text and vowel-pointed text. The buffer bit would effectively make every glyph optionally pointed. Worth exploring seriously before committing to a phoneme layer.

### On the numeral base

Banks is unambiguous: base 8. It's a reasonable choice — the Culture uses base-9 encoding (3×3 = 9 cells), and base-8 is the natural integer subdivision of that (2³). Octal aligns with the binary structure of each glyph in a way decimal does not.

Choosing base-8 eliminates the worst single conflict in the system (digit-3 = #121 = Banks' *w*) without needing to reassign anything. The 8 digit values would need to be freshly specified — none are published — but that's a creative choice, not a conflict.

zakalwe2040's decimal system has the practical advantage of direct correspondence to everyday arithmetic, and the Mandarin digit names give it cultural specificity. But it contradicts the source and produces two invariant collisions (#341 for digit-0, and indirectly displacing marainkit's #0 = zero).

### On the Diamond/plus conflict

`+` = #170 (Diamond) is the most defensible zakalwe2040 operator assignment. A rotated plus sign is a diamond. The homoiconic logic holds. However, marainkit's use of Diamond as a warning/hazard glyph also has strong visual logic — a diamond shape is a universal danger marker (road signs, chemical hazard labels, playing cards for risk). Both readings are natural.

Two possible resolutions:
1. **Accept dual meaning, distinguish by context.** Mathematical context → `+`; display/status context → danger. Relies on the surrounding text to disambiguate.
2. **Reassign `+` to a non-invariant value.** Preserves Diamond as unambiguously hazard. Requires a new `+` value that doesn't conflict with anything else.

Option 1 is how natural languages work — the same symbol means different things in different registers. Option 2 is cleaner for a machine-readable encoding. The Culture used Minds, who would prefer 2; Culture citizens writing by hand might accept 1.

### On brackets

The 8 bracket/delimiter values (81, 276, 211, 406, 251, 446, 479, 503) have no conflicts with any invariant or Banks phoneme. Open/close pairs are constructed as bit-mirrors of each other, which is elegant and consistent with Marain's rotation-invariance philosophy. This entire set could be adopted wholesale. It is the lowest-friction zakalwe2040 contribution.

### On M2 and the 4×5 lattice

The 4×5 lattice is a proper superset of M1. The 3×3 slate is exactly an M1 glyph; the diacritic and tonal channels are additional rows/columns that extend the encoding. This means any M1 glyph is valid in the lattice's slate position — M1 is forward-compatible with M2 by design.

If marainkit ever defines an extended encoding layer, zakalwe2040's geometry is the natural starting point. The phoneme assignments in that layer would be a separate question — the geometry could be adopted while the values are redesigned.

---

[^1]: Iain M. Banks, *"A Few Notes on Marain"* (date unknown). Glyph table image: [`docs/assets/marain-example-banks.png`](../../docs/assets/marain-example-banks.png).
