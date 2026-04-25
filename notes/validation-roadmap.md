# Validation Roadmap

> **Track:** Encoding system (primary) + Philosophical argument — this document lists testable claims in the marainkit spec, their current evidence status, and proposed experiments. Moving from elegant reasoning to evidence-grounded design. See [`tracks.md`](tracks.md).

> **Evidence labels used in this document:**
> `[canonical]` — directly from Banks source text ·
> `[inference]` — consistent with canon, not explicitly stated ·
> `[project decision]` — deliberate choice where canon is silent ·
> `[speculative]` — interesting hypothesis, not yet tested
>
> *See [evidence-labels.md](evidence-labels.md) for full definitions.*

---

## Purpose

Several claims in this repo are currently supported only by reasoning. They are testable. Until tested, they remain hypotheses — and framing them as conclusions weakens the project's credibility.

Experiments do not need to be formal studies. Structured informal tests with documented results are sufficient to upgrade a `[speculative]` claim to `[project decision]` or `[inference]`. The goal is not academic rigour — it is *evidence over assertion*.

This document is the tracking list. Each entry has a claim, its current evidence status, a proposed experiment, and the prerequisites for running it.

---

## Status legend

| Status | Meaning |
|--------|---------|
| 🔴 Blocked | Cannot test until a prerequisite exists |
| 🟡 Ready | Prerequisites met — test is runnable now |
| 🟢 Done | Tested — results documented |

---

## Priority claims

### 1. Invariant glyphs are perceptually distinctive at a glance

**Claim:** Users can distinguish invariant glyphs from ordinary Marain glyphs faster and more reliably than chance — without having learned the system.

**Current evidence:** `[inference]` — derived from their geometric properties (maximum contrast between filled/empty, rotational symmetry, resemblance to existing hazard symbols). The distinctiveness argument is structurally sound but untested at actual rendering sizes and exposure durations.

**Why it matters:** The entire safety vocabulary relies on this being true. If invariant glyphs do not pop out at a glance, the "safety system emerges from geometry" claim fails.

**Proposed experiment:**
- Render 20 glyphs at 24px in the target cell style (square or dot)
- Mix: 4 invariants, 16 randomly selected ordinary glyphs
- Brief-exposure display: 150ms per glyph (too fast to decode, fast enough to register shape)
- Task: participant marks each as "distinctive / warning-like" or "ordinary"
- Measure: hit rate for invariants, false-positive rate for ordinary glyphs
- Target threshold: ≥ 80% hit rate, ≤ 20% false-positive rate

**Prerequisites:** Rendered glyph set at target size. Minimum viable: a static image grid. No software build required.

**Status:** 🟡 Ready

---

### 2. Macro 3×3 layout improves grouping and recall over linear

**Claim:** Arranging glyphs in macro 3×3 blocks (one glyph per cell, 9 glyphs per macro-block) improves short-term recall and parsing speed compared to the current linear stream.

**Current evidence:** `[speculative]` — supported by analogy to Korean Hangul (syllable blocks processed as morpheme units before decomposing into phonetic components) and by general Gestalt grouping theory. No Marain-specific evidence exists.

**Why it matters:** Macro 3×3 layout is the recommended upgrade from the current linear renderer (see `encoding/docs/layout.md`). If the grouping benefit doesn't hold for Marain glyphs, the rationale for the layout change weakens.

**Proposed experiment:**
- Generate 10 short "phrases" (5–9 glyphs each) in both linear and macro 3×3 formats
- Show each format for 3 seconds, then blank
- Task: reproduce the sequence by selecting glyphs from an unlabelled grid
- Within-participant design: same phrases shown in both formats, counterbalanced order
- Measure: reproduction accuracy, time to first response
- Compare linear vs macro 3×3 on both measures

**Prerequisites:** Macro 3×3 layout renderer must exist. This is MVP deliverable 5 — see [`../direction/mvp.md`](../direction/mvp.md).

**Status:** 🔴 Blocked — requires macro layout renderer

---

### 3. Render variant legibility at minimum supported size

**Claim:** Different cell rendering styles (square, rounded, dot, pixel) have meaningfully different legibility profiles at small sizes. One variant should be designated the minimum-size default.

**Current evidence:** `[project decision]` — `font-spec.md §7.1` defines four variants and notes that square has highest fidelity while dot is more visually distinctive and braille-resonant. No comparative test at actual minimum sizes has been run. The choice of default is unresolved.

**Why it matters:** The minimum rendering size gates the range of practical applications. A variant that is illegible at 10px cannot be used in dense HUD displays or inline code contexts. The wrong default will be quietly incorrect in a lot of implementations.

**Proposed experiment:**
- Render all 4 variants (square, rounded, dot, pixel) at 4 sizes: 24px, 14px, 10px, 8px
- Select 20 test glyphs: 8 invariants + 12 representative ordinary glyphs (high, medium, and low cell density)
- Task: identify whether a specified cell (e.g. "top-right") is filled or empty
- Measure: accuracy and response time per variant per size
- Report: the size at which each variant drops below 90% accuracy — that is its minimum supported size

**Prerequisites:** Rendered test panels. Can be generated as static images from the existing grey-area renderer.

**Status:** 🟡 Ready

---

### 4. Channel marks (rails) remain subordinate without becoming invisible

**Claim:** When rails are rendered, they remain visually subordinate to the slate — participants identify slate content correctly at the same rate with and without rails present.

**Current evidence:** `[speculative]` — `font-spec.md` specifies that rail rendering must be visually subordinate (smaller, lighter, or recessed), but the constraint has not been tested. There is a real risk that rails either disappear entirely (too subtle to be useful) or compete with the slate (too prominent to be subordinate).

**Why it matters:** Rail semantics are not yet assigned, but when they are, the rendering constraint must be validated. A rail that is invisible provides no information. A rail that competes with the slate degrades glyph readability.

**Proposed experiment:**
- Render 20 packets: slate only vs slate + upper rail vs slate + both rails
- Use a rail rendering at 60% of slate cell size, 50% opacity (starting point — adjust as needed)
- Task: identify the slate glyph (ignore rails)
- Measure: slate identification accuracy across all three conditions
- Secondary measure: can participants accurately read the rail state when asked?
- Target: slate accuracy ≥ 95% in all conditions; rail readability ≥ 70% when specifically attended to

**Prerequisites:** A font that renders rails. This is a post-MVP capability — rails require semantic assignment first. See `encoding/docs/channels.md`.

**Status:** 🔴 Blocked — requires rail renderer and rail semantic assignment

---

### 5. Binary state recovery from rendered glyphs

**Claim:** A user who understands the 3×3 binary grid can recover the exact binary state of a rendered glyph with acceptable error rates at practical rendering sizes.

**Current evidence:** `[inference]` — the design ensures each cell is either filled or empty with no ambiguity by spec. Whether rendering artefacts (anti-aliasing, subpixel rendering, compression) introduce enough ambiguity to cause errors at small sizes is unknown.

**Why it matters:** The archival and transmission use cases depend on this being true at the sizes used in practice. If a user cannot reliably read a 10px glyph, the "carve it in stone, read it in 500 years" claim is a thought experiment, not a property of the system.

**Proposed experiment:**
- Render 30 glyphs at 4 sizes: 24px, 14px, 10px, 8px (square variant — highest fidelity baseline)
- Include: 8 invariants, 12 high-density ordinary glyphs, 10 low-density ordinary glyphs
- Task: participant fills in a blank 3×3 grid (filled/empty per cell) for each rendered glyph
- Measure: per-cell accuracy, whole-glyph accuracy, error rate by cell position and glyph density
- Report: the size at which whole-glyph accuracy drops below 95% — that is the practical minimum for binary-exact use cases

**Prerequisites:** Rendered test panels at each size. The square variant is already specifiable from `font-spec.md §7.1`. Can be generated from grey-area.

**Status:** 🟡 Ready

---

## Running the experiments

### What "documented results" means

For each experiment run, create a file in `direction/` named `validation-<claim-number>-results.md` containing:
- Date, participant count, method (in-person, remote, self-administered)
- Raw summary statistics (accuracy rates, response times)
- Whether the target threshold was met
- Any anomalies or confounds noticed
- Updated evidence label for the claim

### What changes when a test passes

- The claim's evidence label upgrades: `[speculative]` → `[project decision]` (if the design choice holds) or `[inference]` (if the result is better explained as structural than decided)
- The relevant spec document is updated to note the evidence
- This roadmap entry is marked 🟢 Done with a link to the results file

### What changes when a test fails

- The claim remains `[speculative]`
- The design decision that depends on it is flagged for revision
- The experiment result and its implications are recorded in `direction/`

---

## Deferred claims

The following claims appear in the repo but are not near-term testable — they depend on infrastructure or user populations that do not yet exist.

| Claim | Why deferred |
|-------|-------------|
| Gender-neutral pronoun reduces hierarchical framing in practice | Requires Column B vocabulary, implemented tonal register, and a population of Marain speakers. Decades away. |
| Fixed specification largely solves long-term meaning drift | Requires a timescale of decades minimum. Not testable in this project's lifetime. |
| Marain reduces ambiguity surface for AI systems | Requires working AI integrations with a Marain encoder. Post-MVP. |
| Substrate-independence (carved glyphs legible after 500 years) | Physical archival test. Worth a small informal experiment — carve or stamp a few glyphs and photograph — but not a priority. |

These remain `[speculative]` indefinitely unless circumstances change. They are worth noting because they are the *motivating* claims for the project — but they should not be treated as near-term engineering requirements.

---

*See also:* [`../direction/mvp.md`](../direction/mvp.md) — narrow MVP definition; experiments 1, 3, and 5 above are MVP deliverables. [`tracks.md`](tracks.md) — track definitions. [`evidence-labels.md`](evidence-labels.md) — label definitions.