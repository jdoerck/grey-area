# Evidence Labels

This project mixes Banks source material, interpretation, original design decisions, and speculative ideas. To make the distinction visible, key claims throughout the documentation are tagged with one of four evidence labels.

---

## The four labels

### `[canonical]`
Directly supported by Banks source text (*A Few Notes on Marain*, the Culture novels, or explicit authorial statements). The claim can be traced to a specific passage.

**Example:** Marain has a single gender-neutral third-person pronoun. Banks states this explicitly.

---

### `[inference]`
Consistent with canonical source material, but not explicitly stated. The claim follows logically from what Banks wrote, but Banks did not write it in so many words.

**Example:** Marain was designed primarily for transmission rather than inscription. The source supports binary efficiency and tightbeam transmission, but does not explicitly call the written form a "debug view."

---

### `[project decision]`
A deliberate design choice made by marainkit where the canonical source is silent or ambiguous. The decision is ours to make; we have made it; it is documented.

**Example:** The 8 invariant glyphs are reserved for structural and warning vocabulary. Banks defines their geometry; the reservation policy is our decision.

---

### `[speculative]`
An interesting idea or design hypothesis that is not yet grounded in evidence, testing, or implementation. Worth pursuing, but should not be treated as a proven property of the system.

**Example:** The claim that a fixed specification "largely solves" long-term meaning drift. Plausible, but untested.

---

## How labels are used

Labels appear inline in documents, in bold brackets, attached to a specific claim or section heading:

```
**[canonical]** Banks states that Marain has a gender-neutral third-person pronoun.

**[inference]** The written script is downstream of the binary signal.

**[project decision]** Invariant glyphs are reserved for structural and warning use.

**[speculative]** A fixed specification largely solves long-term meaning drift.
```

Where an entire section carries a single evidence level, the label appears in the section heading:

```
### Longevity of meaning `[speculative]`
```

Where a section contains claims of mixed status, individual sentences are labelled.

---

## Why this matters

The repo has real technical substance. Muddling its epistemic levels — treating inference as canon, or speculation as engineering requirement — undermines the credibility of the parts that *are* solid. Labels make the distinction visible without removing the ideas.

A reader encountering a `[speculative]` label should understand: *this is an interesting hypothesis worth testing, not a property the system has already demonstrated.*

---

*See also:* [`rationale.md`](rationale.md), [`sapir-whorf.md`](sapir-whorf.md), [`layers.md`](layers.md) — documents where labels are applied.
