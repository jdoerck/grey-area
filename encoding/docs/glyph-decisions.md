# Glyph Decisions — Comparison Tables and Design Discussion

Working document. Active conflicts and open decisions lead. Full reference tables and resolved items follow.

For the actionable backlog see [`roadmap.md`](roadmap.md) · full catalogue [`glyphs.md`](glyphs.md) · assigned-values index [`glyph-index.md`](glyph-index.md).

---

## Active conflicts

Items that require a decision before a marainkit encoding layer can be built. Invariant collisions are marked `[I]`.

| # | marainkit / Banks | zakalwe2040 | Conflict |
|---|-------------------|-------------|---------|
| 121 | Banks *w* — only explicitly confirmed canonical value | digit `3` | Z's decimal numeral 3 occupies the single most important confirmed value in the system. Eliminated if base-8 is chosen. |
| 170 | Diamond invariant | `+` (addition) | Z assigns addition to Diamond. Homoiconic (diamond = rotated plus) but burns a warning invariant. `[I]` |
| 186 | Cross invariant · Banks *th* | `iz` (copula — to be) | Two separate sources assign different phonemes to the same invariant. No homoiconic justification for *iz* = Cross. `[I]` |
| 341 | Checkerboard invariant | digit `0` | Z's decimal zero occupies Checkerboard. marainkit already treats #0 (Empty, *nuul*) as zero/null — two competing zeros. `[I]` |
| 495 | Frame invariant | `×` (multiplication) | No strong justification. Frame as "enclosure" is a stretch for multiplication. `[I]` |
| 511 | Full invariant · marainkit "maximum/critical" | *wa* (bilabial approximant) | Z assigns the all-filled glyph to the most common consonant. Directly contradicts Banks #121 for *w*. `[I]` |

---

## Open decisions

These must be made before building any encoder. See [`roadmap.md`](roadmap.md) for full options and current leans.

| Decision | Status | Current lean |
|----------|--------|--------------|
| **Number base** — base-8 (Banks) vs base-10 (Z) | 🟢 Decided | Base-8. Decided 2026-04-03 — see `roadmap.md` decision log. |
| **Phoneme strategy** — follow Banks †, follow Z abjad, or define fresh | 🟢 Decided | Banks corrected. Decided 2026-04-03 — see `roadmap.md` decision log. |
| **wa assignment** — keep Banks #121 or accept Z #511 | 🟡 Open | Keep #121. |
| **Buffer bit** — use Banks' 10th bit as long-vowel marker | 🟡 Open | Yes — zero cost, maps cleanly onto the vowel-pointing model. |
| **`+` vs Diamond** — dual meaning or reassign `+` | 🟡 Open | Undecided. Homoiconic argument for `+`=#170 is genuinely strong. |
| **`iz` reassignment** — copula should not occupy Cross invariant | 🟡 Open | Reassign *iz* to a non-invariant value. |
| **Brackets** — adopt Z bracket set wholesale | 🟢 Decided | Adopt. No conflicts, open/close pairs are bit-mirrors. |
| **Logic + equality** — adopt Z set minus *iz* | 🟢 Decided | Adopt (`&`, `\|`, `!`, `=`, `:=`). *iz* pending above. |

---

## Reference — phoneme comparison

Banks published 32 phonemes as a glyph-table image[^1] — most values are approximate visual reads flagged `†`. Only *w* (#121) is confirmed in essay text. zakalwe2040 published a 24-consonant abjad, extracted from `docs/abjad.svg` (`‡`). Only *ma* and *la* match across systems.

`✓` = cross-system match · `✗` = conflict · `—` = no assignment · `[I]` = invariant collision

| Phoneme | Banks # | Banks Pattern | Z # | Z Pattern | Status |
|---------|---------|---------------|-----|-----------|--------|
| m / *ma* | 457 † | `█░░/█░░/███` | 457 ‡ | `█░░/█░░/███` | ✓ |
| w / *wa* | **121** | `█░░/███/█░░` | 511 ‡ | `███/███/███` | ✗ Z uses marainkit Full [I] |
| p / *pa* | 459 † | `██░/█░░/███` | 79 ‡ | `███/█░░/█░░` | ✗ |
| b / *ba* | 432 † | `░░░/░██/░██` | 295 ‡ | `███/░░█/░░█` | ✗ Z's ba = Banks' *n* value |
| f / *fa* | 56 † | `░░░/███/░░░` | 173 ‡ | `█░█/█░█/░█░` | ✗ |
| v / *va* | 367 † | `███/█░█/█░█` | 362 ‡ | `░█░/█░█/█░█` | ✗ Banks *v* = Z *sa* value |
| th / *tha* | 186 † | `░█░/███/░█░` | 133 ‡ | `█░█/░░░/░█░` | ✗ Banks *th* = Cross [I] |
| — / *dtha* | — | — | 319 ‡ | `███/███/░░█` | — |
| tch / *cha* | 60 † | `░░█/███/░░░` | 127 ‡ | `███/███/█░░` | ✗ |
| ch | 174 † | `░██/█░█/░█░` | — | — | Banks only |
| — / *dja* | — | — | 465 ‡ | `█░░/░█░/███` | — |
| t / *ta* | 168 † | `░░░/█░█/░█░` | 307 ‡ | `██░/░██/░░█` | ✗ |
| n / *na* | 295 † | `███/░░█/░░█` | 493 ‡ | `█░█/█░█/███` | ✗ Z's *na* = Banks' *h* value |
| s / *sa* | 214 † | `░██/░█░/██░` | 367 ‡ | `███/█░█/█░█` | ✗ Z's *sa* = Banks' *v* value |
| d / *da* | 480 † | `░░░/░░█/███` | 87 ‡ | `███/░█░/█░░` | ✗ |
| l / *la* | 484 † | `░░█/░░█/███` | 484 ‡ | `░░█/░░█/███` | ✓ |
| z / *za* | 384 † | `░░░/░░░/░██` | 469 ‡ | `█░█/░█░/███` | ✗ Z's *za* = Banks' *ll* value |
| r / *ra* | 292 † | `░░█/░░█/░░█` | 189 ‡ | `█░█/███/░█░` | ✗ |
| sh / *sha* | 57 † | `█░░/███/░░░` | 383 ‡ | `███/███/█░█` | ✗ |
| y / *ya* | 184 † | `░░░/███/░█░` | 468 ‡ | `░░█/░█░/███` | ✗ |
| g / *ga* | 120 † | `░░░/███/█░░` | 502 ‡ | `░██/░██/███` | ✗ |
| k / *ka* | 312 † | `░░░/███/░░█` | 500 ‡ | `░░█/░██/███` | ✗ |
| ng / *nga* | 16 | `░░░/░█░/░░░` | 509 ‡ | `█░█/███/███` | ✗ Banks *ng* = Point [I] |
| ah / *aa* | 456 † | `░░░/█░░/███` | 322 ‡ | `░█░/░░░/█░█` | ✗ |
| h / *ha* | 493 † | `█░█/█░█/███` | 487 ‡ | `███/░░█/███` | ✗ |
| *ay* | 2 † | `░█░/░░░/░░░` | — | — | Banks only |
| *eh* | 32 † | `░░░/░░█/░░░` | — | — | Banks only |
| *ee* | 50 † | `░█░/░██/░░░` | — | — | Banks only |
| *ih* | 84 † | `░░█/░█░/█░░` | — | — | Banks only |
| *uh* | 273 † | `█░░/░█░/░░█` | — | — | Banks only |
| *oh* | 118 † | `░██/░██/█░░` | — | — | Banks only |
| *ll* | 469 † | `█░█/░█░/███` | — | — | Banks only — = Z *za* value |
| *je* | 431 † | `███/█░█/░██` | — | — | Banks only |
| *oo* | 371 † | `██░/░██/█░█` | — | — | Banks only |

---

## Reference — numerals

| Digit | Banks # | Z # | Z Pattern | Conflicts |
|-------|---------|-----|-----------|-----------|
| 0 | unpublished | 341 ‡ | `█░█/░█░/█░█` | Z = Checkerboard [I]; marainkit treats #0 (Empty) as zero |
| 1 | 1 (implied †) | 471 ‡ | `███/░█░/███` | Banks implies #1 = "the number one" |
| 2 | unpublished | 466 ‡ | `░█░/░█░/███` | — |
| 3 | unpublished | **121** ‡ | `█░░/███/█░░` | **Z = Banks' canonical *w*** — eliminated by choosing base-8 |
| 4 | unpublished | 243 ‡ | `██░/░██/██░` | — |
| 5 | unpublished | 95 ‡ | `███/██░/█░░` | — |
| 6 | unpublished | 373 ‡ | `█░█/░██/█░█` | — |
| 7 | unpublished | 125 ‡ | `█░█/███/█░░` | — |
| 8 | N/A (base-8) | 317 ‡ | `█░█/███/░░█` | — |
| 9 | N/A (base-8) | 381 ‡ | `█░█/███/█░█` | — |

---

## Reference — operators and notation

### Arithmetic

| Symbol | Meaning | # | Pattern | Conflicts |
|--------|---------|---|---------|-----------|
| `+` | addition | 170 ‡ | `░█░/█░█/░█░` | Diamond [I] — see Active conflicts |
| `×` | multiplication | 495 ‡ | `███/█░█/███` | Frame [I] |
| `−` | subtraction | 300 ‡ | `░░█/█░█/░░█` | — |
| `÷` | division | 364 ‡ | `░░█/█░█/█░█` | — |
| `mod` | modulo | 301 ‡ | `█░█/█░█/░░█` | — |

### Logic (adopted)

| Symbol | Marain name | # | Pattern |
|--------|------------|---|---------|
| `&` | *wa* (and) | 284 ‡ | `░░█/██░/░░█` |
| `\|` | *ow* (or) | 113 ‡ | `█░░/░██/█░░` |
| `!` | *ma* (not) | 343 ‡ | `███/░█░/█░█` |

### Equality and copula

| Symbol | Marain name | # | Pattern | Conflicts |
|--------|------------|---|---------|-----------|
| `=` | *heeya* (equality) | 63 ‡ | `███/███/░░░` | — |
| `:=` | *kun* (define/assign) | 191 ‡ | `███/███/░█░` | — |
| `iz` | *iz* (copula — to be) | 186 ‡ | `░█░/███/░█░` | Cross [I] — reassignment pending |

### Punctuation

| Symbol | Marain name | # | Pattern | Notes |
|--------|------------|---|---------|-------|
| `?` | *mahu* (question / λ) | 342 ‡ | `░██/░█░/█░█` | — |
| `.` | decimal point | **16** ‡ | `░░░/░█░/░░░` | ✓ Agrees with marainkit Point |
| `,` | comma | 128 ‡ | `░░░/░░░/░█░` | — |
| `;` | semicolon | 144 ‡ | `░░░/░█░/░█░` | — |

### Brackets (adopted)

Open/close pairs are bit-mirrors. No conflicts.

| Symbol | # | Mirror of |
|--------|---|-----------|
| `>` / `<` | 81 / 276 | each other |
| `]` / `[` | 211 / 406 | each other |
| `)` / `(` | 251 / 446 | each other |
| `}` / `{` | 479 / 503 | each other |

---

## Discussion

*Recorded from design sessions — not resolved decisions.*

### On the phoneme layer

The two systems are effectively independent designs. Both use the M1 3×3 binary grid but made almost entirely different phoneme-to-value choices — only *ma* (#457) and *la* (#484) agree. Banks never published his mapping rationale; zakalwe2040 started fresh with an explicit design principle (place of articulation + homoiconicity).

The confidence levels are asymmetric. Banks is canonical but mostly unverifiable — 31 of 32 phoneme values are approximate image reads, and any could be wrong. zakalwe2040's values are precisely extracted from SVG but non-canonical. The single strongest data point is Banks explicitly writing "*w* = #121" in prose.

A hybrid approach — anchoring on confirmed cross-system values (#121, #457, #484) and assigning the rest fresh — is honest about uncertainty and avoids both the abjad's *wa*/#511 problem and Banks' low-confidence approximations.

### On the abjad architecture

zakalwe2040's abjad is organized by place of articulation (bilabial → glottal), then frequency — explicitly designed for high-frequency speech. Banks' system has no documented organizing principle. For a practical implementation, zakalwe2040's structure is more learnable. The cost of adopting it wholesale is *wa* = #511 (Full invariant) — too high.

### On the buffer bit and long vowels

Banks defines a 10th "buffer bit" after each 9-bit glyph in transmission. Currently unassigned. zakalwe2040 handles vowel length through diacritic channels in the 4×5 lattice. Both solve the same problem differently. Using the buffer bit as a long-vowel flag costs nothing, is compatible with M1 and the 4×5 lattice, and maps cleanly onto the vowel-pointing model used by Semitic scripts. Strongest candidate for a zero-cost extension to M1.

### On the Diamond/plus conflict

`+` = #170 is the most defensible zakalwe2040 operator choice — a diamond is a rotated plus, the homoiconic logic holds. But Diamond as a warning glyph also has universal visual logic (road signs, hazard symbols). Dual meaning distinguished by context is how natural language works; separate values is cleaner for machine encoding. Unresolved.

### On M2 and the 4×5 lattice

The 4×5 lattice is a proper superset of M1 — the 3×3 [slate](../../notes/glossary.md#slate) is exactly an M1 glyph, with diacritic and tonal channels added. M1 is forward-compatible with M2 by design. If marainkit defines an extended encoding layer, zakalwe2040's geometry is the reference starting point. The phoneme *assignments* in that layer are a separate question from the geometry.

---

## Resolved log

Items that were open and are now confirmed. Recorded for reference.

| Item | Resolution | Notes |
|------|-----------|-------|
| *oh* value | **#118** `░██/░██/█░░` | Previously misread as #170 (Diamond). Re-read from source image. |
| *oo* value | **#371** `██░/░██/█░█` | Previously misread as #170, creating false collision with *oh*. |
| *ch* value | **#174** `░██/█░█/░█░` | Previously unreadable at image resolution. Re-read confirmed. |
| *v* value | **#367** `███/█░█/█░█` | Previously unreadable. Note: = zakalwe2040 *sa* value. |
| *ll* value | **#469** `█░█/░█░/███` | Previously unreadable. Note: = zakalwe2040 *za* value. |
| *je* value | **#431** `███/█░█/░██` | Previously unreadable. No Z equivalent, no invariant conflict. |
| Diamond (#170) | **marainkit-only** | Freed from phoneme claims once *oh* and *oo* were correctly read. |
| Brackets | **Adopted** | All 8 values (81, 276, 211, 406, 251, 446, 479, 503). No conflicts. |
| Logic operators | **Adopted** | `&` #284, `\|` #113, `!` #343. *iz* (#186) excluded pending reassignment. |
| Equality | **Adopted** | `=` #63, `:=` #191. *iz* excluded. |
| `.` = #16 | **Accepted** | Triple agreement: Banks decimal point, marainkit Point, zakalwe2040 period. Only cross-system agreement in the entire index. *ng* phoneme shares the value — not a conflict, phoneme and punctuation registers don't collide. |

---

[^1]: Iain M. Banks, *"A Few Notes on Marain"* (date unknown). Glyph table image: [`docs/assets/marain-example-banks.png`](../../notes/assets/marain-example-banks.png).
