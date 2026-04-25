# Mixed-Script Systems, CJK Fonts, and the Marain Problem

> **Track:** Encoding system — research into mixed-script typographic systems (Japanese/Chinese/Korean) and their relevance to the Marain font design problem. This is original analysis in support of marainkit design decisions. Evidence labels are not applied per-claim. See [`../../notes/tracks.md`](../../notes/tracks.md).

> **Purpose:** Deep research into writing systems that combine logographic and phonetic scripts — principally Japanese (kanji + kana), Chinese (hanzi + pinyin/bopomofo), and Korean (hanja + hangul) — and the fonts designed to render them. This document connects the typographic challenges of CJK to the Marain font design problem, building on the research in [`research.md`](research.md) and [`font-spec.md`](font-spec.md).
>
> **Why this matters for Marain:** Banks' Marain is, by design, a script that encodes *both* semantic density (like logographs) and phonetic composability (like an abjad) within a single 3×3 grid. It is not purely logographic, not purely phonetic, but a hybrid — much like the systems that serve a quarter of the world's population. The fonts that render CJK scripts have solved (or failed to solve) many of the same problems Marain faces.

---

## Part 1: The Writing Systems

### 1.1 Japanese: Three Scripts in One Sentence

Japanese is arguably the most typographically complex living writing system. A single sentence routinely intermixes three scripts:[^wiki-jws]

- **Kanji** (漢字): Logographic characters inherited from Chinese. Each represents a morpheme — a unit of meaning. There are approximately 2,136 in the official *jōyō kanji* list for everyday use, but educated readers recognise many more.[^wiki-kanji] Kanji carry the semantic load: nouns, verb stems, adjective roots.

- **Hiragana** (平仮名): A syllabary of 46 base characters. Cursive, flowing forms derived from simplified whole kanji during the Heian period (794–1185), originally by court women who were denied access to Chinese literary education.[^wiki-jws] Hiragana handles grammatical glue: verb inflections, particles, conjunctions, and words with no standard kanji.

- **Katakana** (片仮名): A parallel syllabary of 46 base characters. Angular, fragmentary forms derived from *parts* of kanji, originally by Buddhist monks for annotating texts.[^wiki-kanji] Katakana handles foreign loanwords, onomatopoeia, scientific terms, and emphasis — functioning somewhat like italics in Latin script.

The critical insight for Marain: **these three scripts are not alternatives but complements.** Kanji provides density and disambiguation; kana provides inflection and phonetic transparency. Japanese written without kanji (all-kana) is harder to read, not easier, because the visual rhythm of alternating dense-logographic and light-phonetic characters *is itself a word-boundary signal*.[^wiki-jws][^japanesepod] In a language written without spaces, the script-switching is the punctuation.

This parallels the Marain Column A / Column B distinction. Column A (arbitrary binary encoding) produces visually undifferentiated glyph streams. Column B (phonemic encoding with curated vocabulary) would produce a more structured visual rhythm. The Japanese precedent suggests that mixing encoding modes might be not just acceptable but actively desirable for readability.

### 1.2 Chinese: Logographic Compression and Compositional Structure

Chinese hanzi are purely logographic — each character encodes meaning, with pronunciation carried as an associated property rather than a structural component. The system contains tens of thousands of characters (the *Kangxi Dictionary* of 1716 indexed 47,035), though practical literacy requires roughly 3,000–4,000.[^grokipedia-ccc]

What makes hanzi relevant to Marain is not the character *count* but the character *structure*. Over 80% of modern Chinese characters are **phono-semantic compounds**: composites of a semantic radical (hinting at meaning) and a phonetic component (hinting at pronunciation).[^grokipedia-ccc] For example, 河 (hé, "river") combines the water radical 氵 with the phonetic component 可 (kě). The character is simultaneously a picture (water-related) and a sound (kě-adjacent).

This dual encoding — semantic *and* phonetic information compressed into a single glyph — is precisely what Marain's Column B aspires to. The zakalwe2040 tonal extension[^readme-prior] already explores encoding tone alongside phoneme identity. The Chinese precedent demonstrates that this kind of dual encoding is not merely possible but has been the dominant encoding strategy for thousands of years.

**The radical system** is also structurally relevant. The 214 Kangxi radicals function as a finite vocabulary of composable sub-glyph units — building blocks from which complex characters are assembled.[^wiki-radicals] Components change shape depending on position: 人 (person) becomes 亻 when used as a left-side radical; 火 (fire) becomes 灬 when placed below.[^saporedicina] This context-dependent deformation of components within a fixed bounding box is analogous to how Marain glyphs might need variant renderings depending on their position within a macro 3×3 layout grid.

### 1.3 Korean Hangul: The Featural Alphabet in a Grid

Hangul is the writing system most structurally analogous to Marain, and it is not a coincidence that Banks — with his anti-Eurocentric design philosophy — would have been aware of it.

Created in 1443–1446 by King Sejong the Great specifically to democratise literacy (the existing Chinese characters were inaccessible to commoners), Hangul is a **featural alphabet**: the shapes of consonant letters encode articulatory features of the sounds they represent.[^wiki-hangul] The letter ㄱ (g/k) resembles the root of the tongue touching the soft palate. Adding strokes increases articulatory force: ㄱ → ㅋ (aspirated k) → ㄲ (tense kk).[^hangul-jamo]

But here's what matters for Marain: Hangul letters are not written linearly. They are **composed into syllable blocks** — square cells containing 2–4 letters (jamo) arranged spatially.[^wiki-hangul-syllables] The syllable block 한 (han) arranges ㅎ (h, top-left), ㅏ (a, right), ㄴ (n, bottom) into a single square glyph. The *same* jamo letter takes different proportions and shapes depending on where it sits within the block:

- A leading consonant (choseong) at the top stretches horizontally.
- A vowel (jungseong) stretches vertically on the right, or horizontally below.
- A trailing consonant (jongseong) at the bottom stretches horizontally and flattens.

This produces **11,172 possible syllable blocks** from just 24 base letters (19 consonants × 21 vowels × 28 trailing consonants including null).[^hangul-syllables-grok] The blocks look superficially like Chinese characters — dense, square, space-filling — but they are fully decomposable into phonetic atoms.

**The Marain parallel is direct.** Marain's 3×3 binary grid is a spatial composition system where the "meaning" of each cell depends on its position within the grid. Hangul demonstrates that spatial composition of phonetic units into square blocks is not merely workable but can produce one of the most efficient and learnable writing systems ever designed — one that UNESCO recognised for its scientific structure.[^hangul-syllables-grok]

### 1.4 Mixed Scripts: The General Principle

Beyond CJK, several other writing systems mix logographic and phonetic elements:

- **Ancient Egyptian**: hieroglyphs functioned simultaneously as logograms, phonograms, and determinatives (semantic classifiers), often within the same inscription.
- **Akkadian cuneiform**: inherited Sumerian logograms while adding syllabic signs for the unrelated Akkadian language.
- **Modern Japanese**: as described, the world's most complex living mixed system.

The recurring pattern: **when a writing system serves a complex civilisation over long periods, it tends toward mixed modes.** Pure logography becomes unsustainable as vocabulary grows (you can't make a new picture for every new concept). Pure phonography loses semantic density (homophones become visually indistinguishable). The hybrid survives because it exploits both recognition pathways — visual memory for frequent, semantically heavy units, and phonetic decoding for everything else.[^pubmed-kana-kanji]

Research on Japanese literacy confirms this dual-pathway model: kana reading is predicted by phonological processing skills (auditory-linguistic), while kanji reading is predicted by visual long-term memory (pattern recognition).[^pubmed-kana-kanji] A writing system that engages both pathways simultaneously has a higher effective bandwidth than one that relies on only one.

---

## Part 2: Fonts for Mixed-Script Systems

### 2.1 The Scale Problem

The first and most obvious challenge of CJK font design is sheer scale. A Latin font needs ~200–300 glyphs. A comprehensive Chinese font needs 20,000+. A Pan-CJK font (covering Chinese, Japanese, and Korean) needs 65,535 glyphs per weight — the maximum that a single OpenType font can contain.[^source-han-sans] At seven weights, that's nearly half a million designed glyphs per family.[^adobe-serif]

This has practical consequences: a single CJK font file can exceed 15–20MB uncompressed,[^cjk-optimization] versus 15–50KB for a Latin WOFF2. Web performance, storage, and rendering all become engineering problems at this scale.

Marain, by contrast, has a *tiny* glyph space: 512 states. But the Marain font must solve a problem CJK fonts don't face: **every one of those 512 states must be visually distinct from every other.** CJK fonts can tolerate similar-looking characters because context (surrounding characters, grammar, known vocabulary) disambiguates them. Marain Column A has no such context — any binary state can appear at any position.

### 2.2 Source Han Sans / Noto Sans CJK: The Benchmark

The most significant CJK font project of the past decade is Source Han Sans (Adobe's name) / Noto Sans CJK (Google's name) — the same font released simultaneously under both brands in 2014.[^noto-wiki][^google-dev-blog]

**Design principles:**

The project was led by Ryoko Nishizuka at Adobe's Tokyo office, coordinating with Sandoll Communications (Korea) and Changzhou SinoType (China). The foundational design challenge was: how do you make characters from four different writing traditions (Simplified Chinese, Traditional Chinese, Japanese, Korean) look like they belong in the same font, while respecting each tradition's distinct stroke conventions?[^google-dev-blog]

The answer: **shared skeleton, regional flesh.** The underlying geometric proportions (stroke angles, counter sizes, weight distribution) are consistent across regions. But the specific stroke forms — how a horizontal stroke terminates, whether a dot curves left or right, the exact bend of a particular radical — vary by region.[^typotheque-variants] The same Unicode code point (e.g., 骨, "bone") renders with subtly different stroke forms in the JP, SC, TC, and KR versions of the font.[^google-dev-blog]

This is achieved through OpenType `locl` (localised forms) features: the font detects the language tag on a text run and swaps in the appropriate regional glyph variant. One font binary, multiple visual outputs depending on declared context.

**Relevance to Marain:** This is exactly the context model described in the Marain display spec — `(type, viewing, status)` → rendering output.[^readme-context] Source Han Sans proves that a single font architecture can produce contextually appropriate renderings from the same underlying character set. The Marain font can learn from this: one glyph renderer, multiple output modes driven by declared context.

### 2.3 The Em-Square Problem

CJK characters are designed to fill a square bounding box — the **em square**. Every character, from the simplest (一, a single horizontal stroke) to the most complex (鬱, 29 strokes), occupies the same square footprint.[^typotheque-typesetting] This makes CJK text inherently monospaced in the character dimension, even though Latin text paired with it is proportional.

This creates the **optical weight mismatch**: at the same point size, CJK characters appear larger and heavier than Latin letters, because they fill their em-square almost entirely, while Latin letters leave substantial space above (for ascenders) and below (for descenders).[^shorai-sans][^kanji-blog] Well-designed multi-script fonts address this by either slightly reducing the CJK character size or scaling up the Latin component.

**Relevance to Marain:** Marain glyphs are inherently square (3×3 grid). They face the same coexistence challenge with surrounding Latin text that kanji does. The `font_spec.md` addresses this in §8 (Coexistence with Reference Fonts), but the CJK precedent provides concrete solutions: align glyph vertical centre with x-height midpoint; match optical weight to the surrounding Latin Regular weight; use approximately 0.25em spacing to match word-spacing rhythm.

### 2.4 Stroke Weight Consistency Across Complexity

One of the hardest problems in CJK font design is maintaining consistent *perceived* weight across characters of wildly different complexity.[^typotheque-typesetting] The character 一 (one) has a single stroke. The character 鬱 (depression) has 29. At the same point size in the same weight, the simple character's single stroke should appear roughly the same weight as the average stroke in the complex character — but if you make all strokes literally the same width, the complex character looks darker (more ink per square unit) and the simple character looks lighter.

The solution: **optical compensation.** Strokes in complex characters are slightly thinner than strokes in simple characters. Counters (enclosed white space) in complex characters are carefully opened to prevent visual clogging. This is not automated — it requires character-by-character design judgment across thousands of glyphs.[^source-han-serif]

**Relevance to Marain:** The 512-state Marain glyph space has exactly this problem. Glyph #511 (all cells filled) has maximum visual weight. Glyph #16 (one cell filled) has minimum visual weight. In a text stream, these will appear next to each other. The font spec should consider optical compensation: perhaps slightly reducing cell size for high-fill glyphs, or slightly increasing cell padding, to maintain consistent perceived density across the glyph stream.

### 2.5 Kana/Kanji Coexistence in Japanese Fonts

In Japanese fonts, kanji and kana must visually harmonise despite fundamental structural differences. Kanji fill the em-square densely. Hiragana is cursive and flowing, with organic curves that leave substantial white space. Katakana is angular and fragmentary, even sparser than hiragana.

Good Japanese fonts achieve harmony not by making kana look like kanji (that would destroy their readability) but by carefully calibrating:

- **Size**: kana characters are typically set slightly smaller than kanji within the same em-square, leaving more surrounding white space — which preserves the alternating-density rhythm that signals word boundaries.[^kanji-blog]
- **Weight**: kana strokes are often slightly lighter than kanji strokes at the same nominal weight, compensating for their lower overall density.
- **Vertical alignment**: both occupy the same em-square, but kana sit slightly higher on the ideographic baseline, creating a subtle vertical rhythm.

**Relevance to Marain:** If Marain ever implements a mixed-mode display (e.g., Column A binary glyphs interspersed with Column B phonemic glyphs, or Marain glyphs interspersed with Latin annotation), the Japanese kana/kanji precedent provides the playbook: don't force visual uniformity across modes; instead, calibrate size, weight, and rhythm to create a legible alternating texture.

### 2.6 Hangul Font Design: Composing 11,172 Blocks from 24 Letters

Hangul font design is the CJK discipline closest to Marain's actual problem. Because Hangul blocks are *composed* from jamo, a Hangul font designer has two options:[^hangul-font-gen]

1. **Design all 11,172 blocks individually.** This is what high-quality commercial fonts do. It takes one to two years of manual work per font weight. Each block is hand-tuned so that the jamo components are proportionally balanced, strokes don't collide, and white space is distributed evenly.

2. **Design variant forms of each jamo and compose them algorithmically.** Each consonant and vowel has multiple variant glyphs — a "wide" form for when it's the only leading consonant, a "narrow" form for when it shares space with a trailing consonant, a "short" form for when the vowel is tall, etc. OpenType features (particularly `ccmp`, `ljmo`, `vjmo`, `tjmo`) handle the composition.[^opentype-hangul]

The second approach is directly analogous to what the Marain font spec proposes for macro 3×3 layout: cells within a glyph that adapt their rendering based on the rendering context. The Hangul precedent demonstrates that this works at industrial scale — but also that the quality gap between hand-tuned and algorithmically composed blocks is noticeable to native readers.

### 2.7 Notable CJK Fonts and What They Teach

Typotheque maintains a curated survey of new original CJK fonts that provides a useful cross-section of contemporary approaches — from geometric sans-serifs to revival serifs — across Chinese, Japanese, and Korean.[^typotheque-cjk-collection]

| Font | Designer/Foundry | Key Innovation | Lesson for Marain |
|------|-----------------|----------------|-------------------|
| **Source Han Sans / Noto Sans CJK** | Adobe + Google, led by Ryoko Nishizuka | First comprehensive Pan-CJK font; regional glyph variants via OpenType `locl`[^google-dev-blog] | Context-driven rendering from a single font binary |
| **Source Han Serif / Noto Serif CJK** | Adobe + Google | Serif companion; coordinated Latin (Source Serif) designed to match CJK weight[^adobe-serif] | Multi-script optical weight matching |
| **Shorai Sans** | Monotype (Akira Kobayashi, Ryota Doi) | Geometric sans optimised for Latin-Japanese harmony; kana with "subtle curves" matching Avenir[^shorai-sans] | Geometric grid aesthetics can be warmed with micro-curves |
| **PingFang** | Apple (DynaComware) | System font optimised for screen rendering across iOS/macOS; San Francisco companion | Screen-first CJK design at system scale |
| **Hiragino** | Screen (字游工房) | Pioneering Mac Japanese font; exceptionally clear kana at small sizes | Small-size legibility for dense scripts |
| **M PLUS 1p / 2p** | Coji Morishita (open source) | Variable-width (proportional) Japanese font — breaking the monospaced CJK convention | Not all CJK must be monospaced; proportional CJK is viable |
| **Sandoll fonts** (various) | Sandoll Communications | Leading Korean foundry; Hangul-specific optical adjustments for jamo composition | Expertise in compositional glyph design |

---

## Part 3: Synthesis — What CJK Teaches Marain

### 3.1 Mixed Encoding Is a Feature, Not a Bug

Japanese demonstrates that readers *benefit* from visual heterogeneity in the glyph stream. The alternation between dense kanji and light kana creates a rhythm that aids parsing. Marain should not aim for visual uniformity across its glyph stream. If Column A (arbitrary binary) and Column B (phonemic) produce visually distinct textures, that distinction is *information*, not noise.

### 3.2 The Grid Is Not a Prison

Hangul proves that a grid-based composition system can be both scientifically rigorous and aesthetically beautiful. The key is that components adapt their shape to the grid context — they don't just sit rigidly in fixed positions. Marain's 3×3 grid cells are currently defined as binary (filled/empty), which is more rigid than Hangul's flexible jamo. But the *rendering* of those cells (shape, size, gap, colour) can vary with context, just as Hangul jamo vary within their syllable blocks.

### 3.3 Regional Variants Are a Solved Problem

Source Han Sans demonstrates that a single font architecture can serve multiple regional rendering conventions through OpenType features and language tagging. Marain's context model `(type, viewing, status)` maps directly onto this pattern. The font doesn't need separate binaries for `document/daylight/normal` vs `hud/low-light/warn` — it needs a single rendering engine with context-responsive parameters, exactly as Noto Sans CJK uses `locl` to swap regional glyph variants.

### 3.4 Semantic + Phonetic Dual Encoding Is Ancient and Robust

Chinese phono-semantic compounds have been the dominant character formation strategy for over two thousand years. The principle — embed a semantic hint *and* a phonetic hint in the same visual unit — is exactly what Column B's tonal encoding aspires to. The Chinese radical system (214 composable semantic units) suggests that Marain's 8 invariant glyphs could function as a "radical vocabulary" — semantic classifiers that provide structural context for the non-invariant phonemic glyphs around them.

### 3.5 Scale Drives Architecture

CJK fonts handle 20,000+ glyphs through modular architectures: shared master outlines with regional overrides, algorithmically composed syllable blocks, subsetting for web delivery. Marain's 512-state space is tiny by comparison, but the principle still applies: the rendering architecture should separate the *glyph definition* (the 9-bit binary state) from the *rendering parameters* (context-driven tokens) from the *output format* (SVG, Canvas, CSS Grid). This separation is what allows CJK fonts to serve half the world from a single codebase.

### 3.6 The Democratisation Parallel

Every script system discussed here has a democratisation story:

- **Kana** was created because kanji was inaccessible to women and commoners.[^wiki-jws]
- **Simplified Chinese** was introduced in the 1950s to reduce barriers to mass literacy.[^grokipedia-ccc]
- **Hangul** was explicitly commissioned to make literacy achievable for the general population.[^wiki-hangul]
- **Atkinson Hyperlegible** was designed to democratise reading for the low-vision community.[^notes-ah]
- **Intel One Mono** was designed to democratise code reading for visually impaired developers.[^notes-iom]

Marain, in the Culture novels, serves the same function: a language *engineered* by Minds to be maximally accessible, egalitarian, and non-hierarchical. The marainkit project inherits this commitment. Every design decision in the Marain font spec should be evaluated against the question: **does this make the glyph system more or less accessible to more or fewer people?**

---

## Part 4: Specific Design Recommendations

Based on the CJK research, the following additions or modifications to `font_spec.md` are recommended:

### 4.1 Optical Weight Normalisation

**Add to §3:** Like CJK fonts that compensate for stroke-count density variation, the Marain renderer should optically normalise glyph weight. Proposed mechanism: a subtle scaling factor applied to cell size based on fill count. Glyphs with 7–9 filled cells render cells at 95% of nominal size; glyphs with 1–3 filled cells render at 105%. The adjustment should be imperceptible in isolation but produce a more even texture in continuous streams.

### 4.2 Mixed-Mode Visual Rhythm

**Add to §5 or as new §:** When Column A and Column B glyphs appear in the same stream (e.g., a Column B phonemic word followed by Column A binary data), the transition should be visually marked — not by an explicit delimiter, but by a subtle rendering parameter shift, analogous to the kanji→kana weight/size shift in Japanese. Column B glyphs could render with slightly more inter-glyph padding, or with the `dot` cell variant, creating a lighter texture that signals "this is phonemic content" to a reader trained on the system.

### 4.3 Macro Layout as Syllable Block

**Strengthen the macro 3×3 grid proposal:** The recommended Approach 2 layout (a 3×3 grid of glyphs, each glyph being a 3×3 grid of cells) maps directly onto the Hangul syllable block principle: sub-units composed within a square container. The Hangul precedent validates this as readable by human cognition. The specific recommendation: treat each macro 3×3 group as a "word" or "morpheme" equivalent, with tighter intra-group spacing and looser inter-group spacing, mimicking the density rhythm of Japanese kanji + kana alternation.

### 4.4 Invariant Glyphs as Radicals

**Extend §3.5:** The 8 invariant glyphs should be formally designated as a "radical vocabulary" in the Chinese sense — structural classifiers that appear alongside content glyphs to provide categorical context. In Column B, an invariant glyph preceding a phonemic sequence could indicate the semantic domain (warning, structural, metadata), functioning exactly as the water radical 氵 indicates "this character is water-related" in Chinese.

### 4.5 Furigana-Style Annotation

**New proposal:** Japanese furigana (small kana printed above kanji to indicate pronunciation) provides a model for how Marain could handle annotation. When a Marain glyph stream needs to be readable by someone unfamiliar with the encoding, small Latin or phonetic annotations could appear above or beside the glyph blocks — a "furigana layer" that provides phonetic transparency without disrupting the visual structure of the glyph stream. This would be a rendering option, not a fundamental change to the encoding.

---

## Footnotes

[^wiki-jws]: Wikipedia. "Japanese writing system." Accessed March 2026.
[^wiki-kanji]: Wikipedia. "Kanji." Accessed March 2026.
[^japanesepod]: JapanesePod101. "Katakana vs Hiragana vs Kanji." December 2025.
[^grokipedia-ccc]: Grokipedia. "Chinese character components." January 2026.
[^wiki-radicals]: Wikipedia. "Chinese character radicals." Accessed March 2026.
[^saporedicina]: Saporedicina. "Chinese Radicals — 汉字偏旁部首." May 2022.
[^wiki-hangul]: Wikipedia. "Hangul." Accessed March 2026.
[^hangul-jamo]: Grokipedia. "Hangul Jamo (Unicode block)." January 2026.
[^wiki-hangul-syllables]: Wikipedia. "Hangul Syllables." Accessed March 2026.
[^hangul-syllables-grok]: Grokipedia. "Hangul Syllables." January 2026.
[^pubmed-kana-kanji]: Wydell, T.N. & Butterworth, B. "Logographic Kanji versus phonographic Kana in literacy acquisition." PubMed, 2008. Finding: kana literacy predicted by auditory processing; kanji literacy predicted by visual long-term memory.
[^noto-wiki]: Wikipedia. "Noto fonts." Accessed March 2026.
[^google-dev-blog]: Google Developers Blog. "Noto: A CJK Font That is Complete, Beautiful and Right." July 2014.
[^source-han-sans]: Jenxi.com. "Source Han Sans." Overview and analysis. Accessed March 2026.
[^adobe-serif]: Adobe Type. "Source Han Serif — An open source Pan-CJK typeface." source.typekit.com.
[^cjk-optimization]: Font-Converters.com. "CJK Font Optimization Guide." February 2026. A standard Chinese font contains over 20,000 glyphs; a single unoptimised CJK font file weighs 5–20MB.
[^typotheque-cjk-collection]: Typotheque. "Collection of new original CJK fonts." https://www.typotheque.com/blog/collection-of-new-original-cjk-fonts
[^typotheque-variants]: Typotheque (Eric Q. Liu). "Understanding CJK regional character variants." May 2025.
[^typotheque-typesetting]: Typotheque. "Typesetting principles of Chinese, Japanese, and Korean (CJK) text." May 2025.
[^shorai-sans]: Creative Boom. "Shorai Sans: new Monotype font creates harmony between Latin and Japanese letterforms." November 2022. Akira Kobayashi notes CJK characters fill the em-square while Latin characters do not.
[^kanji-blog]: Kanji Blog. "The ultimate guide to Japanese typography." October 2022. Japanese characters have no ascenders or descenders; all occupy uniform-height square frames.
[^hangul-font-gen]: MDPI Electronics. "Positional Component-Guided Hangul Font Image Generation." July 2025. A complete Hangul font set from 11,172 characters can take one to two years of manual design.
[^opentype-hangul]: OpenType Shaping Documents (n8willis/GitHub). "opentype-shaping-hangul.md." Technical spec for Hangul jamo composition via OpenType features.
[^source-han-serif]: Adobe Type. "Source Han Serif" release notes. Dr. Ken Lunde as project architect; Ryoko Nishizuka as lead designer; nearly half a million glyphs managed.
[^readme-prior]: marainkit/marain README.md §Prior Art. zakalwe2040/marain: 5 tones, 24-character abjad, 4×5 dot lattice.
[^readme-context]: marainkit/marain README.md §Display Layer — Context Model. Three axes: type, viewing, status.
[^notes-ah]: See [`research.md`](research.md) §1 — Atkinson Hyperlegible analysis.
[^notes-iom]: See [`research.md`](research.md) §2 — Intel One Mono analysis.
[^asian-absolute]: Asian Absolute. "CJK Typesetting in 2025." July 2025.
[^outlier]: Outlier Linguistics. "Chinese Character Radicals. Don't Do It." Blog post on the distinction between dictionary-indexing radicals and functional semantic/phonetic components.
