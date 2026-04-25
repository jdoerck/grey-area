# Marain M1 — MVP Definition

> **Track:** Encoding system — defines the minimum viable product for marainkit's M1 encoding layer. All scope decisions are marainkit project decisions. Evidence labels are not applied per-claim. See [`../notes/tracks.md`](../notes/tracks.md).

The goal of the MVP is narrow and concrete: demonstrate that the glyph system **works, renders correctly, and is legible** before expanding scope. A technically literate reader who hasn't seen the project before should be able to look at the MVP deliverables and understand what the system is, verify that it functions, and form a confident opinion about whether the design decisions are sound.

This is not a launch. It is a proof of substance.

---

## What the MVP is not

Before listing what's in, it's worth being explicit about what's out.

**Deferred to post-MVP:**
- Column B — phoneme composition, tonal encoding, register semantics. Upstream questions (phoneme inventory authority, glyph assignment policy, tone encoding) are not settled. Column B is a research track. See [`../notes/tracks.md`](../notes/tracks.md) and [`../language/direction.md`](../language/direction.md).
- Rail and herald semantics — the 7 non-slate bits in the packet are reserved. No assignment in M1 until the linguistic layer is stable enough to make the choice with real content.
- Radial / fractal layout (Approach 3) — deferred indefinitely. Not practical for human readers or current tooling.
- Translation dictionary / concept-ID architecture — valuable, not a blocker for demonstrating the glyph system.
- M2 / 4×5 lattice extension — post-M1.
- Formal legibility study — the MVP requires structured informal tests with documented results, not peer-reviewed studies.

---

## MVP deliverables

Six deliverables. The first is already done.

---

### 1. Finalized binary glyph terminology ✅

**Status:** Complete. Closed in issues #21 and #23.

**What was done:** `notes/glossary.md` defines the canonical terms (`slate`, `rails`, `herald`, `lattice`, `packet`, `base-8`, `status scale 0–8`). All documents have been audited and non-conforming usages corrected.

**Acceptance criterion:** No document in the repo uses "ternary cells", "base-9 encoding", or "16-bit word" in an encoding context. ✅

---

### 2. Stable invariant-glyph reservation policy

**Status:** Documented; policy not yet formally closed.

**What exists:** `encoding/docs/invariant-glyphs.md` defines the 8 invariants, their two vocabularies (warning / structural), and the radical vocabulary proposal. `encoding/docs/roadmap.md` records the reservation as decided.

**What remains:** Declare the policy closed — the 8 invariant values (#0, #16, #170, #186, #325, #341, #495, #511) are permanently reserved and will not be assigned to phonemes, operators, or any other vocabulary. Any future Column B assignment that collides with an invariant is a conflict requiring explicit resolution, not a negotiation about whether the invariant is reserved.

**Acceptance criterion:** `invariant-glyphs.md` carries an explicit "policy closed" statement at the top. The roadmap records the closure date.

---

### 3. Clean, complete glyph index

**Status:** `encoding/docs/glyph-index.md` is well-structured but has provisional values.

**What exists:** All 8 invariants assigned. All 8 base-8 numerals assigned (sequential-fill rule). 22 Banks phonemes assigned from image readings. The index clearly marks what is confirmed vs. provisional.

**What remains:** Resolve the provisional Banks phoneme readings. The most reliable path is extracting glyph outlines from `tomdionysus/marain-font` (`Marain.ttf`) using fonttools — this yields precise binary values for all mapped characters without relying on visual reads of a low-resolution image. Footnote [^5] in `glyph-index.md` identifies this as the right approach.

Once extracted:
- Confirm or correct each approximate visual reading
- Mark confirmed values as `[confirmed]` and unresolvable ones as `[provisional — image-read only]`
- Update the "What is missing" section to reflect current state

**Acceptance criterion:** Every entry in `glyph-index.md` is marked with a clear confidence level. The index accurately describes what is known and what is inferred. No value is presented as confirmed unless it is.

---

### 4. One reference renderer

**Status:** `marainkit/grey-area` exists and operates at Layer 1 (Column A). It is not yet aligned with the MVP spec.

**What exists:** A working encoder — UTF-8 text → binary → SVG glyph grid, linear layout.

**What the MVP requires:**

| Requirement | Status |
|-------------|--------|
| Renders all 8 invariant glyphs correctly | Verify |
| Supports square cell variant (§7.1 of `font-spec.md`) | Verify |
| Supports dot cell variant (§7.1 of `font-spec.md`) | Implement if missing |
| Renders at 14px minimum (§6 of `font-spec.md`) | Verify |
| Documented: what it renders, what it doesn't, how to use it | Write |

The renderer does not need to be beautiful. It needs to be **correct and documented**. A reader should be able to clone the repo, run it, and see Marain glyphs without reading any other document first.

**Acceptance criterion:** grey-area renders all assigned glyphs correctly in both square and dot variants. A README exists that describes the input format, output format, and any known limitations. A sentence at the top explicitly states what layer it operates at and what it does not do.

---

### 5. One macro-layout experiment

**Status:** Not implemented. Specified in `encoding/docs/layout.md` (Approach 2).

**What the MVP requires:** Implement macro 3×3 grid layout as an **option** alongside the existing linear mode in grey-area (or as a standalone script if that's easier). A macro 3×3 group of 9 glyphs forms one "word block" — rendered with tighter intra-group spacing and looser inter-group spacing, readable from any edge.

This does not need to be a polished UI feature. It needs to:
- Exist and produce correct output
- Be documented (what it does, how to invoke it)
- Be used in at least one of the legibility tests (#6 below)

**Acceptance criterion:** A user can generate macro 3×3 output from a glyph sequence. The output is visually distinguishable from linear output. The implementation is documented well enough that a new contributor can understand how it works.

---

### 6. Legibility tests — structured informal results

**Status:** Not done. Tests defined in `notes/validation-roadmap.md`.

**What the MVP requires:** At least **three** of the five priority tests from the validation roadmap, each with:
- A documented test setup (what was shown, to how many people, at what size and duration)
- Raw results (even just "8 out of 10 participants identified X correctly")
- A one-sentence conclusion ("The hypothesis is supported / not supported / inconclusive at this sample size")

Tests do not require formal statistical analysis. They require honest, documented observations. A structured informal test with 10 participants is meaningfully more credible than zero tests.

**Priority order for the MVP:**
1. Invariant glyph distinguishability (can be done with current renderer)
2. Render variant legibility at small sizes (can be done with current renderer)
3. Binary state recovery (can be done with current renderer)
4. Macro 3×3 layout recall (requires MVP deliverable #5 first)
5. Rail subordination (requires a rails-capable renderer — post-MVP)

**Acceptance criterion:** Results for at least three tests are documented in `notes/validation-roadmap.md` or linked test-results files. Each result entry follows the format defined in that document.

---

## Definition of done — MVP

The MVP is complete when:

- [ ] Invariant reservation policy is formally closed in `invariant-glyphs.md`
- [ ] All `glyph-index.md` entries have explicit confidence levels; provisional readings are marked as such
- [ ] grey-area renders all assigned glyphs correctly in square and dot variants with a documented README
- [ ] Macro 3×3 layout mode is implemented and documented
- [ ] Results for at least 3 legibility tests are documented in `validation-roadmap.md`
- [ ] A reader with no prior context can look at the repo and come away with an accurate picture of what is working, what is tested, and what remains to be done

---

## After the MVP

Phase 3 issue #29 (`notes/validation-roadmap.md`) tracks all testable claims. Phase 3 issue #28 (this document) defines the delivery scope. Once the MVP is closed, the natural next question is: what does the evidence say, and what does the evidence *not yet* say?

Post-MVP directions (none of these block the MVP):
- Column B: phoneme composition, once upstream language questions are settled
- Macro-layout as default: depends on legibility test results
- M2 architecture: zakalwe2040's 4×5 lattice as a superset of M1
- Translation dictionary: TSV → concept-ID → multilingual

---

*See also:* [`../notes/validation-roadmap.md`](../notes/validation-roadmap.md) — testable claims and proposed experiments · [`../encoding/docs/roadmap.md`](../encoding/docs/roadmap.md) — encoding decision backlog · [`../encoding/docs/glyph-index.md`](../encoding/docs/glyph-index.md) — current glyph assignments