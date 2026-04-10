# Project Tracks

This project pursues three distinct ambitions. They are complementary but they are not the same thing, and they need to speak in different voices. Conflating them makes inference look canonical and philosophy look like engineering requirement.

---

## Track 1 — Banks-faithful reconstruction

**What it is:** Careful reading of the canonical source material. What does Banks actually say? What can be directly quoted? What is explicitly stated vs. implied?

**Voice:** Scholarly and conservative. Claims are grounded in specific passages. Uncertainty is acknowledged.

**Primary documents:**
- [`notes/source/a-few-notes-on-marain.md`](source/a-few-notes-on-marain.md) — the Banks essay
- [`notes/source/culture-marain/`](source/culture-marain/) — novel references
- [`notes/glossary.md`](glossary.md) — canonical terminology definitions

**How to recognise it:** Passages are cited. Claims are labelled `[canonical]`. When the source is silent, that silence is noted.

---

## Track 2 — Encoding and rendering system

**What it is:** An original technical project *inspired by* Banks. The encoding spec, glyph system, display layer, font build pipeline, dictionary architecture — these are marainkit's inventions, not Banks'. Banks provided the premise; we built the system.

**Voice:** Engineering and design. Decisions are recorded with rationale. Open questions are tracked. Technical claims are specific enough to be tested or built.

**Primary documents:**
- [`encoding/docs/`](../encoding/docs/) — glyph spec, layout, channels, roadmap
- [`display/`](../display/) — adaptive display system, token model
- [`notes/layers.md`](layers.md) — four-layer architecture
- [`notes/glossary.md`](glossary.md) — encoding terminology

**How to recognise it:** Claims are labelled `[project decision]`. Decisions have rationale. There are open issues and blockers. Implementation status is noted.

---

## Track 3 — Philosophical argument

**What it is:** Claims about language, cognition, equality, and archival resilience — the *why* behind the design choices. Why does this project matter? What could a system like this achieve?

**Voice:** Exploratory and aspirational. Claims are clearly marked as hypotheses. The distinction between "we designed it to do X" and "it does X" is maintained.

**Primary documents:**
- [`notes/rationale.md`](rationale.md) — motivations and design hypotheses
- [`notes/sapir-whorf.md`](sapir-whorf.md) — linguistic relativity as a design framework

**How to recognise it:** Claims are labelled `[speculative]`. Language like "this project explores whether..." rather than "this system does...". Evidence citations where evidence exists; honest acknowledgement of what hasn't been tested.

---

## Why the distinction matters

When these tracks share a voice, three bad things happen:

1. **Inference looks canonical.** A reader can't tell whether a claim is directly from Banks or is our interpretation of Banks.
2. **Philosophy looks like engineering requirement.** A speculative design goal ("this could reduce ambiguity at scale") sounds like a specified property of the system.
3. **The technical work is harder to evaluate.** A reader who wants to assess the encoding spec has to filter out the philosophical claims to know what's actually been decided.

Each track is worth pursuing. The problem is not having all three — it is when they blur.

---

## Document track labels

Each document carries a short note near the top identifying its primary track. Documents that span tracks note the dominant one and indicate where the secondary track appears.

Format:

> **Track:** [track name] — [one sentence on what this document is doing in that track]

---

*See also:* [`evidence-labels.md`](evidence-labels.md) — labels for individual claim epistemic status within a document.
