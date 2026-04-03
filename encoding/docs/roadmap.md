# Encoding Roadmap and Decision Backlog

Decisions required before the encoding layer can be built. Grouped by layer. Each item has a status, the options under consideration, and a lean (current best guess) where one exists.

For the full analysis behind these items see [`glyph-decisions.md`](glyph-decisions.md).

---

## Status legend

| Status | Meaning |
|--------|---------|
| 🔴 Blocked | Cannot build without this |
| 🟡 Open | Needs a decision but not immediately blocking |
| 🟢 Decided | Resolved — see note |
| 🔵 Deferred | Consciously punted; revisit at M2 |

---

## Layer 0 — Foundations

### [🟢] Invariant glyphs are reserved

The 8 rotation/mirror-invariant values (#0, #16, #170, #186, #325, #341, #495, #511) are treated as structurally reserved. Any phoneme, numeral, or operator assignment that collides with them is a conflict requiring explicit resolution. This is decided — it is a mathematical property of the grid, not a preference.

---

## Layer 1 — Phonemes

### [🟢] Choose a number base

**Decision:** Base-8 (octal). Closed 2026-04-03.

Canonical (Banks), consistent with binary glyph structure (3×3 = 9 bits, 8 = 2³), eliminates the digit-3 = #121 / *w* conflict. zakalwe2040's base-10 was rejected as non-canonical and conflicting with marainkit invariants.

---

### [🟢] Choose a phoneme assignment strategy  *(issue #5)*

**Decision:** Banks corrected. Closed 2026-04-03.

All 32 Banks phonemes adopted as the canonical assignment, with two corrections where Banks' image reads landed on marainkit invariant glyphs: /ng/ corrected from #16 → #286, /th/ corrected from #186 → #447. Three hybrid anchors confirmed as cross-system agreement: #121 = *w*, #484 = *m*, #187 = *l*. Full assignment captured in `encoding/docs/glyph-table.tsv`.

~~**Why it's blocking:** phoneme values determine the alphabet layer. All downstream decisions (how to render spoken Marain, how to disambiguate rotations, what a "word" looks like) depend on this.~~

~~**Lean:** hybrid, anchoring on #121, #457, #484. Banks' image-read values are too low-confidence to commit to wholesale; zakalwe2040's abjad is too incompatible at *wa*/#511 to adopt directly.~~

~~**Blocked by:** number base decision~~ — resolved 2026-04-03. Base-8 leaves 504 non-digit, non-invariant glyph slots for phoneme assignment (512 − 8 digits − 8 invariants = 496, minus punctuation/operators).

---

### [🟡] Resolve the *wa* / #511 conflict

zakalwe2040 assigns *wa* = #511 (all-filled). marainkit reserves #511 as "Full stop / maximum / critical." Banks gives *w* = #121.

**Options:**
- Keep Banks' #121 for *w/wa*. #511 remains a structural/warning glyph. (Recommended.)
- Accept zakalwe2040's *wa* = #511, reassign marainkit "Full" to a different invariant. Loses the elegant invariant pairing.

**Lean:** keep #121 = *w/wa*.

---

### [🟡] Resolve Banks phonemes that land on marainkit invariants

Banks' approximate image reads assign:
- *ng* → #16 (Point) — Banks also cites this as a decimal point. The two meanings coexist naturally.
- *oh* → #170 (Diamond) — "danger" and "phoneme" share a value. Needs disambiguation.
- *th* → #186 (Cross) — "alert/stop" and "phoneme" share a value. Needs disambiguation.

**Options:**
- Accept dual meanings, distinguished by context (speech vs. display register).
- Reassign the phonemes to non-invariant values, freeing the invariants for structural use only.
- Treat Banks' image reads for these three as incorrect and let marainkit meanings stand.

**Note:** *ng* = #16 as decimal point / period is **accepted** — triple agreement across Banks, marainkit, and zakalwe2040. The phoneme and punctuation registers don't collide. The *oh*/#170 and *th*/#186 collisions are harder to justify and remain open.

---

### [🟡] Buffer bit as long-vowel marker

Banks defines a 10th "buffer bit" appended to each 9-bit glyph in transmission. Currently unassigned. zakalwe2040 handles vowel length via diacritic channels in the 4×5 lattice.

**Options:**
- Assign the buffer bit as a **long-vowel flag** (0 = short/default, 1 = long). No M1 index space consumed; every glyph gains a paired long-vowel form. Compatible with the 4×5 lattice (the diacritic channels and buffer bit are parallel solutions to the same problem at different encoding layers).
- Leave the buffer bit undefined.
- Use the buffer bit for something else (e.g., uppercase marker, stress marker).

**Lean:** long-vowel flag. Elegant, zero-cost, maps cleanly onto the vowel-pointing model used by zakalwe2040 and Semitic scripts generally.

---

## Layer 2 — Numerals

### [🔴] Assign base-8 digit values

**Blocked by:** number base decision above.

Once base-8 is confirmed, 8 digit values (#0–#7 in Banks' system) need to be assigned. No published values exist anywhere. Options:

- Derive geometrically (e.g., segment-count / segment-shape analogues to seven-segment displays).
- Use a visually progressive sequence (each digit adds one filled cell from #0 = empty).
- Assign freely, prioritising avoiding all invariants and confirmed phoneme values.

**Note:** marainkit already treats #0 (Empty, *nuul*) as zero/null. This should anchor the digit-0 assignment: #0 = 0. Conflicts with zakalwe2040's digit-0 = #341 (Checkerboard) — accepting base-8 means zakalwe2040's numeral-0 is simply not adopted.

---

## Layer 3 — Operators and Notation

### [🟡] Resolve `+` = #170 (Diamond) conflict

zakalwe2040 assigns addition to #170 (Diamond), which is visually homoiconic (diamond = rotated plus) but conflicts with marainkit's warning/hazard meaning.

**Options:**
- Accept dual meaning: `+` in arithmetic context, warning in display context.
- Reassign `+` to a non-invariant value; keep Diamond for hazard only.

**Lean:** undecided. The homoiconic argument for `+` = Diamond is genuinely strong. This may be a case where context-disambiguation is the right answer.

---

### [🟡] Resolve `iz` (copula) = #186 (Cross) conflict

zakalwe2040 assigns the copula verb *iz* (to be) to #186 (Cross = alert/stop). No homoiconic justification. Appears to be an arbitrary collision.

**Options:**
- Reassign *iz* to a non-invariant, non-phoneme value.
- Accept dual meaning (unlikely to be useful — "to be" and "stop" don't complement each other).

**Lean:** reassign *iz*.

---

### [🟢] Adopt brackets wholesale

zakalwe2040's 8 bracket/delimiter values (#81, #276, #211, #406, #251, #446, #479, #503) have no conflicts with invariants or Banks phonemes. Open/close pairs are constructed as bit-mirrors. Adopt unless a specific value is later needed for something else.

---

### [🟢] Adopt logic and equality operators (minus *iz*)

`&` (#284), `|` (#113), `!` (#343), `=` (#63), `:=` (#191) have no conflicts. Adopt. *iz* (#186) remains open pending resolution above.

---

## Font and rendering

### [🟡] Resolve cell shape default — square vs. dot

`font-spec.md §7.1` defines four variants (`square`, `rounded`, `dot`, `pixel`). The default must be chosen before any implementation work. Square has highest fidelity; dot is more visually distinctive and braille-resonant. Decision gates the build pipeline.

---

### [🟡] Validate centre-cell salience hypothesis

`font-spec.md §4.3` proposes that the centre cell (position 4) has lowest perceptual salience. If validated, glyphs differing only in their centre cell should not be adjacent in the vocabulary. Needs empirical testing — brief-exposure identification trials at 14px rendering.

---

### [🟡] Column B vocabulary selection

Once phoneme strategy is decided (see Layer 1 above), select the active vocabulary from the 512-state space. Must satisfy: D₄ equivalence class constraint (no two glyphs from same rotation/reflection class), minimum Hamming distance ≥ 2, high salience scores, no invariant glyphs. See `font-spec.md §5.3`.

---

## Architecture

### [🔵] M2 — 4×5 lattice as extended encoding layer

zakalwe2040's 4×5 lattice (slate + upper/lower diacritic channels + tonal channel) is architecturally a superset of M1. Any M1 glyph is valid in the 3×3 slate position. If marainkit defines M2, this geometry is the reference design.

The phoneme *assignments* in zakalwe2040's M2 lattice would not necessarily carry over — the geometry could be adopted independently of the values. Deferred until M1 is stable.

---

### [🔵] M3 — Radial / fractal layout

See [`layout.md`](layout.md). How a Mind would write. Not practical for current tooling or human readers. Deferred indefinitely.

---

## Beyond encoding — project rationale

### [🟡] Develop rationale document

[`docs/rationale.md`](../../docs/rationale.md) is a stub capturing the philosophical and practical motivations for marainkit: semantic specificity, equality of access, universalism, AI alignment, hardware efficiency, substrate-independent archival, resilience, accessibility, and longevity of meaning. Needs expansion through discussion.

---

### [🟡] Dictionary — implement concept-ID model

Architecture decided (see [`docs/rationale.md`](../../docs/rationale.md) — Dictionary architecture section). Key decisions remaining:

- Choose primary concept ID scheme: Wikidata Q-IDs, OMW synset IDs, or both
- Define TSV schema (column order, required vs optional fields, versioning)
- Decide snapshot strategy for offline/air-gapped translation
- Build TSV → SQLite generation script

**Principle:** dictionary maps Marain → concept ID. Translations are derived at query time, not stored. Canonical format is plain TSV; SQLite is a generated index.

---

## Decision log

*Record decisions here when made, with date and rationale.*

| Date | Item | Decision | Rationale |
|------|------|----------|-----------|
| 2026-03-31 | `#16` = point / period / decimal | Accepted | Triple agreement: Banks, marainkit, zakalwe2040. Phoneme *ng* coexists — registers don't collide. |
| 2026-03-31 | Numerals | Base-8 (octal), sequential-fill rule, Mandarin names from zakalwe2040 | Consistent with Banks; eliminates #121 conflict; count-the-dots readable; *líng*–*qī* for 0–7. |
| 2026-03-31 | *nuul* | Name for glyph #0 concept | Distinct from digit name *líng*; drawn-out vowel suits the held-silence meaning; exercises buffer-bit vowel system. |
| 2026-04-03 | Number base | **Base-8 (octal)** | Canonical (Banks); consistent with 3×3 = 9 bits, 8 = 2³; eliminates digit-3/#121 conflict. Issue #4 closed. |
| 2026-04-03 | Phoneme strategy | **Banks corrected** | All 32 Banks phonemes adopted. /ng/ #16→#286, /th/ #186→#447 (invariant conflicts resolved by correction). Hybrid anchors #121=*w*, #484=*m*, #187=*l* confirmed. Full table in `glyph-table.tsv`. Issue #5 closed. |
