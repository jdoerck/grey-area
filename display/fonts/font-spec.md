# Font Specification: Marain Display Font

> **Version:** 0.1 (draft)
> **Status:** Early spec — principles and constraints defined; glyph design not yet begun.
> **Companion document:** [`research.md`](research.md) — full research notes on reference fonts and legibility research.

---

## 1. Purpose

This document specifies the design principles, constraints, and technical requirements for the flagship Marain display font — the typeface that renders 3×3 binary glyphs in the marainkit ecosystem.

The font's job is to make Marain's 512-state glyph space legible, distinctive, and beautiful across the full range of display contexts defined in the Marain context model.[^context-model]

This is not a Latin typeface. It is a **glyph rendering system** for a binary grid script. Many conventions of Latin type design do not apply. Where they do apply (as principles rather than techniques), this spec explains the transfer.

---

## 2. Reference Fonts

Two typefaces anchor the Marain display layer and inform this spec:

| Role | Font | Designer | Key property |
|------|------|----------|-------------|
| UI / content | Atkinson Hyperlegible Next | Elliott Scott / Applied Design Works | Letterform distinction over harmony[^dezeen] |
| Code / tokens | Intel One Mono | Fred Shallcrass / Frere-Jones Type | Character exaggeration for developer legibility[^fastco-ibd-2024] |

These fonts are **companions to** the Marain glyph font, not templates for it. The Marain font must coexist with both in the same interface without visual conflict. See §8 for coexistence requirements.

---

## 3. Design Principles

Six principles, derived from analysis of both reference fonts and the legibility research they draw on.[^notes]

### 3.1 Distinction Is Structure

> *"Reinforcing the identity of any shape is not just amplifying what is unique about that letter, but also making it clearly not some other letter."* — Tobias Frere-Jones[^fastco-2023]

Every glyph in the active Marain vocabulary must be perceptually distinguishable from every other glyph at the minimum supported rendering size (see §6). This is the foundational constraint. Aesthetic preferences, geometric regularity, and rendering efficiency are all subordinate to it.

In practice this means:

- **No two glyphs in the active vocabulary may share a rotation/reflection equivalence class** unless both are invariant (i.e., from the set of 8 invariant glyphs).[^invariant-glyphs]
- **Minimum Hamming distance:** Glyphs assigned to adjacent semantic positions (e.g., consecutive phonemes in Column B) should differ by at least 2 cells, not 1. A single-cell difference is too easily lost at small sizes or under blur.
- **Perceptual testing required:** Distinction must be verified empirically at target rendering sizes, not assumed from grid geometry. A 2-cell Hamming distance may still be perceptually ambiguous if the differing cells are in low-salience positions (e.g., centre vs. edge).

**Rationale:** Both reference fonts break typographic harmony rules to achieve per-character distinctiveness. Atkinson Hyperlegible gives serifs to I but not T.[^wiki-ah] Intel One Mono flares M's verticals to distinguish it from N.[^fastco-2023] The Marain equivalent is glyph selection policy: choosing which 512-states to assign to active vocabulary slots, with distinction as the primary selection criterion.

### 3.2 Degradation Reveals, Not Conceals

Under degraded viewing conditions — small size, low contrast, blur, peripheral vision, motion — the remaining visible features of a glyph must still carry enough information to identify it. This is the "pirate eye patch" principle:[^pirate] design for capability preservation across environmental transitions.

**Techniques:**

- **Favour distributed fill patterns.** A glyph with cells scattered across the grid retains more recognisable structure under blur than one with cells clustered in a corner. Cluster patterns degrade into amorphous blobs; distributed patterns degrade into recognisable textures.[^counter-principle]
- **Avoid mirror-image pairs in the active vocabulary.** Under sufficient degradation, left-right or top-bottom reflection becomes hard to detect. Glyphs that are reflections of each other should not both appear in the active set.
- **Weight invariant glyphs toward high-salience roles.** The 8 invariant glyphs[^invariant-glyphs] are, by definition, immune to rotational ambiguity. They are the Marain equivalent of Atkinson Hyperlegible's most carefully distinguished characters — the {I, l, 1, i} set — and should be reserved for functions where misidentification has the highest cost: warnings, structural delimiters, and state escalation markers.

### 3.3 Context Drives Rendering, Not Content

The same glyph bitstream renders differently depending on the declared display context `(type, viewing, status)`.[^context-model] The font must support this without changing glyphs — **the glyph set is constant; the rendering parameters adapt.**

Rendering parameters under font control:

| Parameter | Varies by | Range |
|-----------|-----------|-------|
| Cell size (px) | `type`, `viewing` | 2–12px per cell |
| Cell gap (px) | `viewing` | 0–2px |
| Fill colour | `status`, `viewing` | Token-driven; see display spec |
| Background colour | `status`, `viewing` | Token-driven |
| Glyph padding | `type` | 0–4px per glyph |
| Group spacing | `type` | Linear vs. macro grid |

**Rationale:** Atkinson Hyperlegible maintains typographic stability across all modes — no font swapping per context. Intel One Mono uses a single font with contextual OpenType features (raised colon, ligature sets) that adapt to context without changing the fundamental character shapes.[^github-iom] The Marain font follows the same principle: one glyph set, many rendering contexts.

### 3.4 Grid Cells Are Atoms, Not Pixels

The 3×3 grid defines 9 cells, each binary (filled or empty). The font treats these cells as atomic units — they are rendered, not interpolated. At no rendering size does a cell become "partially filled" or anti-aliased across a cell boundary.

This constraint exists to maintain the bijective relationship between bitstream and visual output. A glyph must be unambiguously decodable back to its 9-bit binary state from its rendered image.[^encoding-layer]

**Implementation:**

- Each cell renders as a filled or empty square (or circle, per style variant — see §7).
- At sizes below the minimum threshold where cells cannot be individually resolved, the font should refuse to render rather than produce an ambiguous output. A fallback indicator (e.g., a single "too small" symbol) replaces the glyph.
- Anti-aliasing applies to the cell boundary against the background, never across cell boundaries within a glyph.

### 3.5 Invariant Glyphs Are Sacred

The 8 glyphs that are unchanged under all rotations and reflections have special status:[^invariant-glyphs]

| Category | Glyphs | Binary values |
|----------|--------|---------------|
| **Warning vocabulary** | Diamond, Cross, Corners, Checkerboard | #170, #186, #325, #341 |
| **Structural vocabulary** | Empty, Point, Frame, Full | #0, #16, #495, #511 |

These glyphs must:

- Be visually distinct from all non-invariant glyphs at every supported size.
- Be renderable with a distinct visual treatment (e.g., colour, border, animation) when the `status` axis is at `warn` or `critical`, mapping naturally onto the base-9 status escalation scale.[^context-model]
- Never be reassigned to arbitrary content encoding. Their geometric uniqueness gives them semantic privilege.

**Rationale:** Atkinson Hyperlegible's circular motifs reference braille dots — a visual link to the font's institutional origin that also serves a functional purpose (increasing dot salience).[^braille-inst] The Marain invariant glyphs serve an analogous dual role: they are structurally unique *and* carry the highest-stakes meaning in the system.

### 3.6 Generous Space Is a Feature

Both reference fonts use generous spacing as a deliberate legibility strategy. Intel One Mono's line-height and letter-spacing are wider than most monospace fonts, allowing text to breathe during hours of reading.[^pimpmytype] Atkinson Hyperlegible's careful kerning creates even rhythm without crowding.[^wiki-ah]

The Marain font applies this principle at two levels:

- **Inter-cell gap:** The gap between cells within a glyph. A nonzero gap at sufficient rendering sizes dramatically improves individual cell identification. At minimum sizes, the gap collapses to zero.
- **Inter-glyph gap:** The space between adjacent glyphs. In linear layout, this is straightforward. In macro 3×3 grid layout, it is the gap between glyph positions in the outer grid.

Spacing must be **token-driven** — defined as CSS custom properties / Style Dictionary tokens, not hardcoded values — to support the context model's rendering adaptation.[^cross-cutting]

---

## 4. Glyph Space Inventory

### 4.1 Complete Space

512 possible 3×3 binary states. Each state is uniquely identified by a 9-bit integer (0–511), read row-by-row, left-to-right, top-to-bottom.

### 4.2 Equivalence Classes Under Rotation

Under 4-fold rotation (0°, 90°, 180°, 270°), the 512 states collapse into equivalence classes. Two states in the same class are rotations of each other.

Under the full dihedral group D₄ (4 rotations × 2 reflections = 8 symmetries), the classes collapse further. The 8 invariant glyphs are the singleton classes — each is its own equivalence class.

**Spec requirement:** The vocabulary assignment algorithm (§5) must compute these equivalence classes and enforce the constraint that no two glyphs from the same D₄ class appear in the active vocabulary.

### 4.3 Cell Salience Map

Not all cells in the 3×3 grid contribute equally to glyph recognition. Based on the principle that human visual scanning is horizontally biased and that central features attract fixation:[^notes]

```
Salience estimate (relative, not empirically validated):

  ┌───┬───┬───┐
  │ 2 │ 3 │ 2 │   Edge cells: moderate salience
  ├───┼───┼───┤
  │ 3 │ 1 │ 3 │   Centre cell: lowest salience (ambiguous under blur)
  ├───┼───┼───┤
  │ 2 │ 3 │ 2 │   Middle-edge cells: highest salience
  └───┴───┴───┘

  1 = lowest    3 = highest
```

**Caution:** This is a theoretical estimate. The centre cell's low salience is hypothesised from the principle that features surrounded by other features on all sides are harder to isolate — analogous to the closed-counter problem in Latin type.[^counter-principle] Empirical testing is required (see §9).

If validated, this salience map implies that glyphs differing only in their centre cell should not be assigned to adjacent vocabulary positions.

---

## 5. Vocabulary Assignment

### 5.1 Tier 1: Reserved (Invariant Glyphs)

The 8 invariant glyphs are pre-assigned:

| Function | Glyph | Value | Visual description |
|----------|-------|-------|--------------------|
| Delimiter: empty | ☐ | #0 | All cells empty |
| Delimiter: point | ◉ | #16 | Centre only |
| Warning: diamond | ◇ | #170 | Diamond pattern |
| Warning: cross | ✕ | #186 | Plus/cross pattern |
| Warning: corners | ⊞ | #325 | Four corners |
| Warning: checker | ▦ | #341 | Checkerboard |
| Delimiter: frame | ☐ | #495 | Border only (centre empty) |
| Delimiter: full | ■ | #511 | All cells filled |

### 5.2 Tier 2: Active Vocabulary (Column A)

Column A encodes arbitrary UTF-8 text as binary, rendered glyph-by-glyph.[^grey-area] The active vocabulary is the full 512-state space (every binary state maps to a glyph). Vocabulary *assignment* is the identity function — the binary value *is* the glyph.

For Column A, the font spec governs rendering quality, not glyph selection. The legibility challenge is: can a reader decode any arbitrary 9-bit pattern back to its binary state from the rendered image?

### 5.3 Tier 3: Active Vocabulary (Column B)

Column B encodes Marain phonemes — a curated subset of the 512-state space where each glyph maps to a linguistic unit.[^column-b] Vocabulary selection here is a design problem:

- Select N glyphs (where N = phoneme count, likely 24–36 based on abjad structure) from the 512-state space.
- Maximise pairwise perceptual distinctiveness.
- Respect D₄ equivalence class constraints (§3.1).
- Favour glyphs with high minimum salience (§4.3).
- Reserve invariant glyphs for non-phonemic functions.

This is a constrained optimisation problem. The spec does not solve it here but defines the constraints the solution must satisfy.

---

## 6. Rendering Requirements

### 6.1 Minimum Rendering Size

Each cell must resolve to at least **3×3 CSS pixels** (device pixels may vary) to be individually identifiable. With a 1px inter-cell gap, this gives a minimum glyph size of:

```
Minimum glyph: (3 × 3) + (2 × 1) = 11 CSS px per side
```

Below this threshold, the font must display a fallback indicator rather than an ambiguous rendering.

### 6.2 Recommended Rendering Sizes

| Context | Cell size | Gap | Glyph size | Notes |
|---------|-----------|-----|------------|-------|
| `code / indoor / normal` | 4px | 1px | 14px | Default for token display |
| `document / indoor / normal` | 6px | 1px | 20px | Comfortable reading size |
| `hud / low-light / normal` | 8px | 2px | 28px | High salience, generous spacing |
| `alert-surface / * / warn` | 10px | 2px | 34px | Warning states enlarge |
| `alert-surface / * / critical` | 12px | 2px | 40px | Critical states maximise |

### 6.3 Rendering Modes

**Filled-square mode (default):** Each cell is a square with sharp corners. Gap between cells is background-coloured. This is the highest-fidelity mode and the canonical rendering.

**Filled-circle mode (variant):** Each filled cell renders as a circle inscribed in the cell's bounding square. Empty cells are empty. This mode evokes the braille-dot motif from Atkinson Hyperlegible[^braille-inst] and may be more comfortable at large sizes where the square grid becomes visually harsh.

**Minimal mode:** At sizes near the minimum threshold, gaps collapse to zero and cells render as a contiguous grid. This sacrifices some cell-level legibility for overall glyph recognisability — the glyph becomes a "texture" rather than a readable grid.

---

## 7. Style Variants

### 7.1 Cell Shape

| Variant | Cell shape | Gap behaviour | Use case |
|---------|-----------|---------------|----------|
| `square` | Square with square corners | Constant gap | Default; highest information density |
| `rounded` | Square with rounded corners | Constant gap | Softer appearance for document contexts |
| `dot` | Circle inscribed in cell | Constant gap | Braille-evocative; display and decorative |
| `pixel` | Square, zero gap | No gap | Retro/minimal; small sizes only |

All variants render the same 9-bit binary state. The variant is a rendering parameter, not a glyph change.

### 7.2 Colour and Fill

Cell fill and background colours are controlled by the display token system, not the font spec. The font spec requires only:

- Sufficient contrast between filled and empty cells. Minimum contrast ratio: **APCA Lc 60** for normal content, **Lc 75** for warning/critical states.[^apca]
- Fill colour is uniform within a cell (no gradients, no partial fills).
- The 8 invariant glyphs may optionally render with a distinct fill treatment (e.g., a secondary colour, a border, or a subtle background tint) when `status ≥ warn`.

---

## 8. Coexistence with Reference Fonts

The Marain glyph font will appear alongside Atkinson Hyperlegible (for surrounding UI text) and Intel One Mono (for code and token displays). Visual coexistence requires:

### 8.1 Vertical Alignment

When a Marain glyph appears inline with Latin text (e.g., a glyph embedded in a sentence), the glyph's vertical centre should align with the x-height midpoint of the surrounding text. The glyph should not exceed the cap height of the surrounding font.

### 8.2 Optical Weight Matching

The visual "weight" of a Marain glyph (the proportion of filled area to total area) must not make surrounding text look lighter or heavier by contrast. For the average glyph (approximately 4.5 of 9 cells filled — the statistical mean of random binary states), the perceived weight should approximate the Regular weight of Atkinson Hyperlegible Next.

### 8.3 Spacing Rhythm

Inter-glyph spacing in linear layout should produce a reading rhythm compatible with the word-spacing of the surrounding font. This is approximately **0.25em of the surrounding font's em square** as a starting point, subject to testing.

---

## 9. Testing Requirements

### 9.1 Perceptual Distinctiveness Testing

For any active vocabulary (particularly Column B), every glyph pair must be tested for confusability at the minimum rendering size. Method: brief exposure (100–200ms) of single glyphs, forced-choice identification from the full vocabulary. Accuracy must exceed **95% per glyph at 14px rendering** (the default code context size).

### 9.2 Degradation Testing

Render each glyph at minimum size with simulated degradation:

- Gaussian blur (σ = 1px, 2px)
- Low contrast (APCA Lc 45, Lc 30)
- Background noise (random cell-sized speckle)

Identification accuracy must exceed **85% under any single degradation** and **70% under combined degradation.**

### 9.3 Context Testing

Render test strings of 9+ glyphs in each display context defined in the context model. Measure reading speed and error rate. Compare against a control condition using the existing Grey Area linear renderer.[^grey-area]

---

## 10. Implementation Notes

### 10.1 Not a Traditional Font File

The Marain glyph font is not a .otf/.ttf font. It is a **rendering function** that takes a 9-bit value and a rendering context and produces SVG, Canvas, or CSS output. The "font" is a module in the Grey Area encoder or a standalone rendering library.

This is consistent with the project's existing architecture: Grey Area already produces SVG/GIF output from binary input.[^grey-area] The font spec defines the rendering rules that this output must follow.

### 10.2 Token Integration

All rendering parameters (cell size, gap, fill colour, background, padding) must be expressed as Style Dictionary tokens.[^style-dictionary] The font rendering module consumes these tokens at runtime. No magic numbers in the rendering code.

### 10.3 Format Outputs

| Output format | Use case | Notes |
|---------------|----------|-------|
| Inline SVG | Web display | Primary output; scalable |
| Canvas | Animation / HUD | Performance-critical contexts |
| CSS Grid | Pure-CSS rendering | No JS dependency; progressive enhancement |
| Static raster (PNG/GIF) | Export / archival | Fixed size; metadata preserves binary values |

---

## 11. Open Questions

- **Cell salience map:** Is the hypothesised salience gradient (§4.3) empirically valid? Does centre-cell ambiguity hold at all rendering sizes?
- **Dot vs. square default:** Should the default variant be square (highest fidelity) or dot (most visually distinctive and braille-resonant)?
- **Macro 3×3 layout spacing:** When glyphs are arranged in a 3×3-of-3×3 macro grid, what inter-glyph and inter-group spacing produces optimal reading speed?
- **Column B vocabulary optimisation:** What algorithm best selects N glyphs from 512 to maximise pairwise perceptual distance under the D₄ constraint?
- **Animation:** Should glyph state transitions (e.g., status escalation) animate? If so, what easing and duration maintain the "states scale, don't shout" principle?[^cross-cutting]
- **Variable font exploration:** Could a variable font axis control cell shape (square ↔ circle) or gap width, enabling smooth transitions across viewing contexts?

---

## Footnotes

[^context-model]: marainkit/marain README.md §Display Layer — Context Model. Three axes: type, viewing, status.
[^cross-cutting]: marainkit/marain README.md §Cross-cutting Principles. "Token-driven only," "States scale, don't shout," "Structure carries meaning."
[^invariant-glyphs]: marainkit/marain README.md §Encoding Layer — Invariant Glyphs. 8 of 512 states invariant under D₄.
[^encoding-layer]: marainkit/marain README.md §Encoding Layer. "Binary encoding is canonical. Glyphs are a debug view."
[^grey-area]: marainkit/grey-area — working encoder (text → UTF-8 binary → SVG/GIF). Currently Layer 1, Column A.
[^column-b]: marainkit/marain README.md §Open Questions — Language. Column B: phoneme picker UI.
[^style-dictionary]: Style Dictionary — confirmed design token backbone for the Culture design system.
[^pirate]: "Pirate eye patch" analogy — design for capability preservation across environmental transitions.
[^apca]: APCA (Advanced Perceptual Contrast Algorithm) — recommended contrast model for the Culture design system.
[^notes]: See companion document `notes.md` for full research analysis.
[^dezeen]: Crook, Lizzie. "Atkinson Hyperlegible typeface is designed for visually impaired readers." Dezeen, 11 September 2020.
[^fastco-2023]: M. Elissaveta Brandon. "Intel's Intel One Mono is a font designed for low-vision developers." Fast Company, 20 June 2023.
[^fastco-ibd-2024]: Fast Company. "Innovation by Design 2024: Intel One Mono." 22 July 2024.
[^wiki-ah]: Wikipedia. "Atkinson Hyperlegible." Accessed March 2026.
[^braille-inst]: Braille Institute of America. "Read Easier With Our Family of Hyperlegible® Fonts." brailleinstitute.org/freefont (2025).
[^github-iom]: Intel Corporation. "intel/intel-one-mono" GitHub repository. README.md.
[^pimpmytype]: Schöndorfer, Oliver. "Intel One Mono (free font)." Pimp My Type, September 2023.
[^counter-principle]: Derived from counter-space research; see notes.md §4.2.
[^readability-matters]: Readability Matters. "How important is x-height for font legibility?" May 2025.
[^dw-2021]: Design Week. "Designing a typeface for the visually impaired." August 2021.
