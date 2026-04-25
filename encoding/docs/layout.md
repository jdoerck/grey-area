# Layout and Directionality

> **Track:** Encoding system (primary) + Philosophical argument (directionality analysis) — the three layout approaches are marainkit design options; the directionality and cultural-chauvinism analysis draws on Track 3 reasoning about Culture values. Evidence labels are not applied per-claim. See [`../../notes/tracks.md`](../../notes/tracks.md).

Covers the directionality model and layout approaches for rendering Marain glyphs.

---

## The Directionality Question

Marain glyphs are rotation-invariant by design. This has real consequences for layout:

- **Within a glyph:** horizontal scanning is neurological, not cultural — consistent across all human cultures
- **Between glyphs:** no gravitational anchor for a civilisation operating in zero-g with rotation-invariant symbols
- **Line stacking:** top-to-bottom survives document rotation (becomes bottom-to-top, still readable)

**Likely M1 convention:** a *recommended* default direction (left-to-right, top-to-bottom) rather than a *mandatory* one. The tool should expose direction as a user setting.

### Is a linear layout culturally chauvinistic?

Partly — but defensibly so:

- **Chauvinistic part:** Assuming "human-readable" implies linear and paginated. Not universal even on Earth — Aztec codices radiate from centres; Chinese classical texts use columnar right-to-left layout.
- **Defensible part:** M1 is the tier for ordinary Culture citizens, not AI Minds. Ordinary Culture citizens still have two forward-facing eyes and a brain hemisphere that strongly prefers sequential processing. Linearity at M1 is *mammal* chauvinism, not Western chauvinism.
- **Banks' concession:** He wrote the Culture novels in English, in linear prose, for human readers. M1 being somewhat book-like is the same pragmatic concession.

### Ceremonial vs. density-optimised

Aztec codices and illuminated manuscripts optimise for **impact**, not density. Size and position encode significance. A civilisation of Minds would consider spatial extravagance a bug — if tone and semantic weight are inside the 9-bit glyph, you don't need theatrical staging. Every cell carries equal weight. This is a **deeply egalitarian property**.

> The book format is correct for M1: practical, dense, unpretentious. Very Culture.

---

## Three Layout Approaches

```
APPROACH 1: Linear (current)
┌───┬───┬───┬───┬───┬───┐
│ G │ G │ G │ G │ G │ G │ → left to right
└───┴───┴───┴───┴───┴───┘
Inherited from UTF-8. Works. Un-Culture-like.

APPROACH 2: Macro 3×3 Grid (recommended upgrade)
┌───┬───┬───┐
│ G │ G │ G │  Each cell = one 3×3 glyph
├───┼───┼───┤  Readable from any edge
│ G │ G │ G │  Maps cleanly onto 3×3 macro structure
├───┼───┼───┤
│ G │ G │ G │
└───┴───┴───┘

APPROACH 3: Radial / Fractal (Mind-level ideal)
        G
      G   G
    G   G   G    Radiates from centre
      G   G      No start, no end
        G         How a Mind would write it
```

**Practical sweet spot for this project: Approach 2.**

Approach 2 maps onto the 3×3 macro structure naturally, is readable from any edge, and does not require a UI change to the glyph renderer — just a change to how glyphs are arranged in the output grid.

**The Hangul precedent:** Korean Hangul composes 2–4 phonetic letters (jamo) into square syllable blocks — the same principle as Approach 2, and it has been the dominant writing system of a major civilisation for six centuries. A reader processes the block as a unit (recognising the morpheme) before decomposing it into its constituent phonetic parts. A macro 3×3 group of Marain glyphs could function identically: the group is a "word" or morpheme unit, with tighter intra-group spacing and looser inter-group spacing creating the same density rhythm. See [`display/fonts/cjk-mixed-scripts.md §3.3`](../../display/fonts/cjk-mixed-scripts.md) for the full analysis.

Approach 3 is intellectually correct but not practical for human readers or current tooling. Defer indefinitely.

---

## Open Questions

- Should directionality be a render setting in GCU Grey Area?
- Implement macro 3×3 layout mode as an option alongside current linear stream?
