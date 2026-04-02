# Fonts of Interest

Reference collection of fonts relevant to the display layer — particularly for CJK/multi-script
coverage, glyph design principles, and legibility research. Separate from Marain-specific fonts
(see `resources.md`).

---

## Typotheque CJK Collection

**Source:** https://www.typotheque.com/blog/collection-of-new-original-cjk-fonts  
**Published:** May 2025 | **Development time:** 5 years  
**Awards:** Red Dot "Best of the Best" 2023, Type Directors Club 2023

Specimen images saved in `docs/fonts/cjk-specimens/`.

### Why this collection is relevant

The Typotheque CJK project grapples with the same core problem this project does: designing a
unified glyph system that works across radically different script traditions (Latin, Chinese,
Japanese, Korean) without privileging any one of them. Their `Hanzi-variants-map.png` is
particularly instructive — it shows how the same underlying character resolves differently across
SC/TC/JP/KR regional standards, directly paralleling the glyph disambiguation concerns in the
Marain encoding layer.

The Zed family (Display/Round/Text) is worth studying for legibility in information-dense
contexts — a concern the display layer shares.

### Three base variable CJK fonts

| Font | Coverage |
|------|----------|
| TPTQ Sans CJK | ~50,000 characters, GB 18030-2022 Level 2 |
| TPTQ Serif CJK | Same |
| TPTQ Round CJK | Same |

Each ships in four regional variants: SC (Simplified Chinese), TC (Traditional Chinese),
Japanese, Korean.

### Latin typefaces with matched CJK companions

| Font | Styles | Notes |
|------|--------|-------|
| Fedra Sans | 10 | Humanist sans |
| Fedra Serif | 8 | Optimised for small sizes |
| Greta Sans | 20 | 4 widths; Hangul included |
| Greta Text | 8 | Newspaper-optimised serif |
| Lava | 12 | Magazine serif; Hangul included |
| November | 18 | Accessible sans, orthogonal terminals; Hangul included |
| October | 18 | Geometric sans, rounded terminals; Hangul included |
| Ping | 18 | Geometric fluid sans |
| Ping Round | 18 | Warm geometric sans |
| Zed Display | 27 | Minimalist sans |
| Zed Round | 27 | Soft-appearance, UI-oriented |
| Zed Text | 18 | High-legibility information sans |
| Nocturno | — | Coming later 2025 |

### Downloaded specimens

| File | Description |
|------|-------------|
| `TPTQ-cover-no-text.svg` | Main article cover |
| `November-CJK-type-specimen.svg` | November CJK specimen — accessible humanist sans |
| `Typotheque-CJK-font-collection.svg` | Overview of full collection |
| `Lava-CJK-type-specimen.svg` | Lava CJK specimen — magazine serif |
| `Hanzi-variants-map.png` | Regional Han character variant comparison (SC/TC/JP/KR) — most directly relevant |
| `CJK-awards-2023.jpg` | Award recognition |
| `TPTQ-Round-CJK-type-specimen.svg` | TPTQ Round CJK specimen |

---

## Notes on CJK relevance to Marain

The Marain glyph system is a 3×3 binary grid — not a logographic system. But the display layer
faces analogous challenges:

- **Disambiguation at small sizes** — same problem Typotheque solved for CJK at low PPI
- **Script-agnostic layout** — Marain has no privileged direction; CJK typography regularly
  handles non-Latin text flow
- **Glyph density** — a line of Marain at M1 has similar spatial density to CJK text

The cultural grounding also matters: the Marain community has consistently drawn on Chinese and
Sanskrit visual traditions (see `design-notes.md` §7). Fonts that handle CJK well are natural
references for how to render a constructed script that sits outside the Latin tradition.
