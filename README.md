# Marain

> **Work in progress.** This repo is an active design spec, not a finished project.

Iain M. Banks' Culture novels describe a civilization unlike any other in science fiction: post-scarcity, anarchist, governed by superintelligent AI Minds, spread across a galaxy. The Culture's language — Marain — was engineered by those Minds at the very beginning of the civilization, with one explicit purpose: to make its values the cognitive default. Not a rule. A structural fact. The same way a language with a single gender-neutral pronoun makes gender-neutral framing cognitively free, Marain was designed to make egalitarianism, non-hierarchy, and non-dominance the path of least resistance.

Banks was one of the few science fiction authors who actually specified how his invented language works. In a short companion essay — *"A Few Notes on Marain"* — he described the writing system in mathematical terms precise enough to implement.

![Marain Font by TTFTCUTS](notes/assets/marain-TTFTCUTS-font.png)

*© TTFTCUTS — [Marain font](https://fontstruct.com/fontstructions/show/1446008/marain-5)*

---

## The writing system

Each Marain symbol is a **3×3 binary grid** — nine cells, each filled or empty. There are 512 possible states (0–511). This is both the visual form (a glyph you can draw or render) and the transmitted form (a 9-bit number you can send as a bitstream over a tightbeam laser).

Banks gave us a few anchor points: the number 1 is state #1 (one cell filled, top-left corner). The phoneme /w/ — the first letter of the Marain alphabet — is state #121, the binary number `001111001`. The remaining ~480 states are assigned to the rest of the phoneme set, base-8 numerals, punctuation, physical and mathematical constants, chemical elements, and extension space Banks gestures at but does not enumerate.

**[→ Marain Glyph Table](https://marainkit.github.io/marain/)** — every assigned symbol, both reference fonts side by side, with phonetic values, meanings, and binary indices.

Or open [`docs/index.html`](docs/index.html) locally.

---

## Why it's interesting to study

### 1. Language as social engineering

Banks was explicit that the Culture's Minds designed Marain the way an engineer designs a system — not to express what people already think, but to change what they find easy to think. The Sapir-Whorf hypothesis (linguistic relativity) in its weak form has substantial empirical support: the categories your language provides shape what perceptions are fast and cheap versus effortful and slow. Russian speakers discriminate blues faster than English speakers because Russian has two separate basic-level color terms for what English calls "blue." Speakers of languages with absolute spatial frames (cardinal directions instead of left/right) maintain orientation in windowless rooms; English speakers generally can't. Language structure builds cognitive grooves.

Marain was designed with this in mind. The result: a single gender-neutral third-person pronoun (gendered framing isn't available as a default), glyphs readable from any orientation (no privileged reading direction, no implicit hierarchy of position), and a grammar aimed at reducing structural ambiguity. These aren't decorative choices. They are claims about how a civilization would behave if it couldn't easily encode dominance.

### 2. The mathematics of the grid

The 3×3 binary grid has a property Banks probably didn't need to calculate but that falls out of the geometry automatically: **8 of the 512 states are fully invariant under all rotations and mirror reflections**. They look identical from any angle, in any orientation, from any side.

These 8 glyphs — Empty, Point, Diamond, Cross, Corners, Checkerboard, Frame, Full — form two semantic pairs:

```
Empty #0    ↔   Full #511        (nothing ↔ everything)
Point #16   ↔   Frame #495       (one cell ↔ one gap)
Diamond #170 ↔  Checkerboard #341 (sparse ↔ dense alternation)
Cross #186  ↔   Corners #325     (cardinal ↔ diagonal)
```

These glyphs look visually distinct from ordinary text at a glance — the same property that makes hazard symbols stand out from descriptive signs today. A warning vocabulary that works regardless of orientation or rendering medium, not because someone chose those shapes for warnings, but because the geometry selected them.

### 3. Transmission first

Marain's native medium is tightbeam laser: a binary bitstream across interstellar space. The writing system may be better understood not as a script with a corresponding binary encoding, but the other way around — a binary signal, with glyphs as how you render that signal for human eyes. The glyph is what a 9-bit number looks like when you draw its ones and zeros on a 3×3 grid. The written form is a debug view of the transmission.

This inverts the usual relationship between script and encoding. Most writing systems were designed to be seen; their digital encodings (Unicode, UTF-8) were added later as an afterthought. Marain was designed to be transmitted, and the visual form is the afterthought — or rather, one particular rendering among many possible ones. The same glyph can be carved in stone, woven into fabric, drawn on skin, or fired as laser pulses across fifty light-years. The underlying thing is always the same 9-bit number.

---

## The puzzle

Banks gave us the mathematical foundation and a partial alphabet. He did not give us:

- The full phoneme-to-glyph assignments (we have approximate image reconstructions, and two values confirmed in the essay text: #1 for "1", #121 for /w/)
- The complete numeral, punctuation, unit, and constant assignments
- The grammar and tonal system
- How glyphs are arranged spatially when you write a sentence or paragraph

The community has been working on this for decades. There are multiple independent reconstructions — the most developed being zakalwe2040's tonal extension, which adds a 24-character consonant inventory, five emotional tones, and a 4×5 lattice that extends the core 3×3 slate. These reconstructions are largely incompatible with each other and only partially consistent with Banks' original. The scholarly problem — reconstructing a language from a small number of anchor points — is real.

This project studies the system, reconciles what can be reconciled, and builds working implementations where the spec is solid enough to build on.

---

## Three branches of study

### Language `language/`

The linguistic layer: phoneme set, grammar, tonal encoding, vocabulary. We have a 430-word community vocabulary seeded from Marain Tools, a 32-letter phoneme inventory, and example sentences with glosses. The full grammar and tonal spec remain open research questions. This branch also examines what non-Western linguistic structures — Sanskrit, Mandarin, Arabic — contribute to what Marain should look like, consistent with Banks' explicit anti-Eurocentrism.

Key docs: [`language/phonemes/alphabet.md`](language/phonemes/alphabet.md) · [`language/vocabulary.tsv`](language/vocabulary.tsv) · [`language/translations/sentences.md`](language/translations/sentences.md)

### Encoding `encoding/`

The glyph layer: what are all 512 symbols, how do they pack into packets for transmission, what are the invariant glyphs and what do they mean. The packet structure wraps each 9-bit glyph (the "slate") in six context bits (the "rails") and one frame bit (the "herald"), giving a 16-bit self-contained unit. The 6 rail bits are currently reserved — they are the mechanism for future extensions without breaking the core glyph encoding.

Key docs: [`encoding/docs/glyphs.md`](encoding/docs/glyphs.md) · [`encoding/docs/channels.md`](encoding/docs/channels.md) · [`encoding/docs/invariant-glyphs.md`](encoding/docs/invariant-glyphs.md)

### Display `display/`

How Marain should render in actual use. The display system is context-adaptive: the same glyph stream reads differently in a document, a heads-up display, a status alert, and under different lighting conditions. This branch defines the token layer — the CSS variables and typography rules that govern how any renderer should behave — plus a working prototype of the Culture aesthetic.

Key docs: [`display/docs/DESIGN_PHILOSOPHY.md`](display/docs/DESIGN_PHILOSOPHY.md) · [`display/fonts/font-spec.md`](display/fonts/font-spec.md)

---

## Prior art and community

| Project | Notes |
|---------|-------|
| [tomdionysus/marain-font](https://github.com/tomdionysus/marain-font) | TrueType font built from Banks' alphabet image. Author sent it to Banks via his publishers. |
| [zakalwe2040/marain](https://github.com/zakalwe2040/marain) | Tonal Marain: 5 tones, 24-character abjad, 4×5 dot lattice extending the core slate. Most developed community extension. |
| [marain-tools.netlify.app](https://marain-tools.netlify.app/) | Live tool: romanized Marain → glyphs + English gloss. Three input modes including nine-bit binary. |
| Reddit conlang (u/comradelenin456) | Synthetic grammar built on Banks' alphabet: flexible word order, no tenses, six cases, fourth-person pronouns. |

**Canonical source:** Banks' essay *["A Few Notes on Marain"](./notes/source/a-few-notes-on-marain.md)* — the primary source for everything this project treats as settled.

---

## Go deeper

**The foundation:** Start with [`notes/layers.md`](notes/layers.md) for the four-layer model that frames everything — transmission → encoding → language → visual script.

**The design theory:** Read [`notes/sapir-whorf.md`](notes/sapir-whorf.md) for the linguistic relativity evidence that Banks was using, and how it changes what engineered defaults mean. Then [`notes/rationale.md`](notes/rationale.md) for why the project exists and what it's trying to demonstrate.

**Will this survive?** [`notes/esperanto-and-hangul.md`](notes/esperanto-and-hangul.md) examines two designed languages — one that stalled, one that survived 450 years — and what marainkit should take from both.

**The technical puzzle:** [`encoding/docs/glyph-decisions.md`](encoding/docs/glyph-decisions.md) shows where different reconstructions of Marain agree and where they conflict — for readers who want to understand the open questions in detail.
