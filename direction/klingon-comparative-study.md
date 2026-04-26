# Klingon and Marain: A Comparative Study

> Research note. What can the development history of Klingon — the most thoroughly expanded canonical sci-fi conlang — tell us about marainkit's project?

---

## TL;DR

Klingon and Marain are two of the most thoroughly worked-out canonical sci-fi conlangs, but they invert each other on almost every axis. Klingon was created **bottom-up from sound** (Doohan's improvised grunts → Okrand's phonological system → grammar → vocabulary → script as decoration). Marain is being approached **top-down from data** (tightbeam bitstream → encoding standard → conlang → glyphs as renderer). Klingon's expansion is gatekept by a single linguist; Marain's is necessarily distributed because Banks is dead.

The most useful insight Klingon offers is **not** about how to design the language — it's about how a community successfully expanded a fragmentary canon into a working system without breaking the source's spirit. The mechanisms they used (single canonical authority, explicit non-canon tier, lexical-cultural correlation as a design principle, accepting that script and language are separable) are directly applicable to marainkit's "open space" specification approach.

---

## 1. Origin stories — opposite directions

### Klingon: bottom-up from phonology

Klingon's order of construction:

1. **1979** — actor James Doohan and producer Jon Povill improvised guttural sounds for *Star Trek: The Motion Picture*. No grammar, no system. Just noises.
2. **1984** — Marc Okrand, a working linguist (PhD from Berkeley on Mutsun, an extinct Ohlone language), was hired for *Star Trek III* and told to retroactively make those noises into a real language. Doohan's dozen improvised words became the seed.
3. Okrand built **phonology first** — 21 consonants, 5 vowels, deliberately odd sound system designed to be alien but pronounceable.
4. Then **grammar** — he chose OVS (object-verb-subject) word order specifically because it's the rarest of the six possible permutations (about 1% of natural languages, mostly in the Amazon basin). Agglutinative morphology with up to 9 verb suffix slots.
5. Then **vocabulary** — heavily weighted toward warfare, honor, weapons. *The Klingon Dictionary* published 1985.
6. **Script came last and was always decorative.** The pIqaD glyphs were designed by Astra Image Corporation in 1979 based on Klingon battlecruiser hull markings (Matt Jeffries) and Tibetan writing (chosen for the sharp angles, an allusion to Klingons' love of bladed weapons). They were always meant as set decoration. Okuda explicitly refused to map them to phonemes: "if you do that, then eventually it begins to look like English."

### Marain: top-down from data

Compare to marainkit's four-layer model. The order is inverted:

1. **Layer 4 — transmission protocol** (tightbeam bitstream) is canonical and primary.
2. **Layer 3 — data encoding** (9-bit units, base-9, 512 states) is structurally derived from Banks' "3×3 matrix, three states each."
3. **Layer 2 — the conlang itself** is the *least* specified layer in canon. Phonemes, grammar, and tonal encoding remain open spec.
4. **Layer 1 — glyphs** are explicitly framed as *a renderer of the bitstream*, not a primary writing system.

Klingon's pIqaD is a decorative afterthought stapled onto a fully designed spoken language. Marain's glyph system is a structural consequence of the binary substrate and arguably the *most* developed layer. The two projects are mirror images of each other in what they treat as primary.

**Implication for marainkit:** the spec is justified in inverting the conventional conlang priority order. Banks established the data encoding as canonical and the visual script as derivative. That's not a quirk to be apologised for — it's the architectural feature that distinguishes Marain from every other sci-fi conlang.

---

## 2. Cultural-linguistic correlation — Klingon's strongest design principle

The single most-cited "design principle" of Klingon is **lexical-cultural correlation**: the vocabulary deliberately encodes the culture's values through what is and isn't lexicalised. From Wikipedia's summary of Okrand's approach:

- Multiple distinct verbs for "to fight" / "to clash against," each at a different intensity
- Abundant vocabulary for warfare, weaponry, honor
- "Cursing is considered a fine art" — extensive lexicon of insults
- **No native word for "hello"** — the closest equivalent is *nuqneH*, which means "what do you want?"
- **No native word for "please"** — Klingons are direct; politeness markers don't exist as discrete lexemes
- Word order itself (OVS) emphasises the *target* of action, fitting a warrior worldview where what you act on matters more than who's acting

This is straightforward Sapir-Whorf design: shape vocabulary to shape thought. Okrand knew exactly what he was doing — his linguistics PhD was explicitly on a language with unusual typological features (Mutsun), and he drew on knowledge of Native American languages and Southeast Asian languages to create something that sounded genuinely alien rather than European-with-a-twist.

### Where Klingon and Marain converge

The marainkit Sanskrit research note already arrived at the analogous principle for Marain: **forced legibility, not omission**. Where Klingon encodes warrior values by *having* warrior vocabulary, Marain encodes Culture values by *decomposing* hierarchical concepts into morphemes that reveal mechanism rather than concealing it. *Varṇa* (caste) doesn't enter the dictionary as an atomic lexeme; it enters as a compound whose components expose what it actually does.

Both languages use vocabulary structure as ideology, but with **opposite mechanisms**:

| | Klingon | Marain |
|---|---------|--------|
| Strategy | What you have | What you decompose |
| Cultural value | Encoded by abundance | Encoded by transparency |
| "Politeness" | Absent (direct culture) | Explicit register markers (egalitarian culture) |
| Honorifics | Suffix slot 8 | Architecturally rejected (no privileged direction = no privileged person) |
| Word for "hello" | None — directness | Open question; likely tonal context, not lexeme |

**Implication for marainkit:** Klingon validates the design move of treating absence and presence in the lexicon as semantically loaded. The "no case system needed" decision in marainkit's existing decision log is the same kind of move Klingon makes in reverse: a deliberate gap that reflects what the language is for.

---

## 3. The fragmentary-canon problem

Both Klingon and Marain started life as **incomplete sketches** in source media:

- Klingon: a few names, hull markings, Doohan's improvised grunts, vague cultural notes.
- Marain: Banks' essay *A Few Notes on Marain*, scattered references in the novels, the 3×3 base-9 description, the canonical tightbeam medium, the gender-neutral pronoun.

Both required **expansion to be usable**. The question for marainkit is: what does Klingon's expansion model teach about doing this without breaking source spirit?

### Klingon's mechanism: single canonical authority + explicit non-canon tier

The KLI's solution is brutal and clear:

> "Only words and grammatical forms introduced by Marc Okrand are considered canonical Klingon by the KLI and most Klingonists." (Wikipedia)

New vocabulary requires Okrand's explicit approval. He releases batches at qep'a' conventions — 99 words in 2019, 81 in 2024. As of April 2025, the official lexicon is around 4,850 words. Everything else is non-canon, and the line is policed.

This works because Banks, frankly, was a worse fit for the role than Okrand. Okrand is a trained linguist who can adjudicate consistency. Banks was a novelist who used Marain as world-building texture. He's also dead.

Marainkit cannot have a single canonical authority. So the question becomes: **what plays the role of Okrand?**

The marainkit answer, implicit in the existing approach, is **the spec itself plays that role**. Decisions are committed as markdown. Open questions are documented as gaps. Design principles (forced legibility, distinction over uniformity, accessibility-first) are written down and used to adjudicate proposals. The repo *is* the canonical authority, and proposals are evaluated against the documented principles rather than against an individual's judgement.

This is structurally different from Klingon's model but performs the same function. **The spec is the Okrand.**

### Klingon's explicit-tier design

Klingon also has a useful tier structure: canon (Okrand-approved), KLI-curated additions (community-vetted, not canon), and non-canon (everything else). The KLI maintains lists. Different fonts, different proposed scripts, different syntactic experiments all coexist with clear labels.

Marainkit's existing approach already does this, but could probably do it more explicitly. The current repo has:

- Banks-canonical (the essay, novel references) — should be tagged
- marainkit-decided (Frame glyph as logo, Intel One Mono, base-9 status index) — currently in `decisions.md`
- Open questions (Layer 2 phonemes, Column B, tonal encoding) — currently in roadmap

A possible improvement: an explicit `docs/canon-tiers.md` that names these layers, since the project will accumulate decisions that some users will want to adopt and others reject. The decision-log pattern is good; making the *tier* of each decision explicit would be better.

---

## 4. Script vs. language — Klingon's accidental clarity

The most useful piece of Klingon history for marainkit might be the pIqaD story, because it accidentally proved a structural point that marainkit is asserting deliberately:

**A language and its visual script are separable systems.**

Klingon's situation:

- Spoken Klingon is a fully developed language with grammar, phonology, and ~5,000 words.
- pIqaD is "merely decorative graphic elements, designed to simulate real writing" (Wikipedia). Paramount has never officially mapped pIqaD glyphs to Klingon phonemes. Okuda explicitly refused to do so.
- The KLI created an unofficial mapping (the "KLI pIqaD") that some Klingonists use, but **the vast majority of fluent Klingon speakers use the Latin romanization Okrand designed**.
- The Unicode Technical Committee rejected pIqaD for inclusion in 2001 specifically because "research showed almost no use of the script for communication, and the vast majority of the people who did use Klingon employed the Latin alphabet by preference."

So the actual working Klingon community uses a **functional transcription system** for daily use, and treats the visual script as a decorative/ceremonial overlay.

This maps directly onto marainkit's Layer separation:

- **Layer 2 (conlang)** is functional: phonemes, grammar, what you would actually use to compose meaning.
- **Layer 1 (glyphs)** is the rendered visualisation of the encoded bitstream.
- **Layer 3 (encoding)** is what makes the two equivalent.

What Klingon teaches: **don't expect glyphs to be the primary daily medium even for enthusiasts**. The spec should accept that most users will operate via romanization or direct binary input, with glyphs as visualisation. That's not a failure of the system — it's how Klingon actually works in practice, and it's how Chinese works in practice (most digital Chinese input is via pinyin transliteration).

The implication for Column B: when phoneme/tonal composition mode is built, the input method probably looks more like a romanization-style picker than a glyph-grid picker, with glyphs rendered as output. Klingon's evolution suggests this is what people actually use.

---

## 5. Where Klingon is *not* a useful guide

Some aspects of Klingon are genuinely unhelpful as models:

### Narrative-driven evolution

Klingon expanded primarily to serve **plot needs** in subsequent Star Trek productions. New words were added because *Discovery* needed dialogue, or because someone wanted to translate Hamlet. The evolution is reactive and narrative-led.

Marain has no equivalent forcing function. Banks isn't writing more Culture novels. There is no production schedule demanding new vocabulary. This is both a freedom and a problem: Klingon's vocabulary grew because it had to; Marain's will only grow if marainkit makes it grow, and the spec needs to be intentional about *what* should grow rather than waiting for external demand.

### Actor-driven phonological drift

Multiple sources note that Okrand frequently amended Klingon to match actors' mispronunciations. The language was retroactively shaped by what was easier to say on a film set. This is a *bug* of Klingon's origin that became a feature of its character but is not a model marainkit should emulate. Marain's phonology, when it's specified, should be designed against principles (Banks' essay, accessibility, the four-layer model) — not retrofitted to fit accidents.

### Rare-typology-as-alienness

Okrand chose OVS because it's rare. The aesthetic logic is "alien = rare." This reads, in 2026, as slightly orientalist — "alien" defined as "not-English, not-European." Marainkit's existing instinct to draw on Sanskrit, CJK script research, and Hangul-style syllable blocks is healthier: it draws on *human* linguistic traditions Banks himself would have respected, rather than treating "rare" as automatically "alien."

The Marain claim is stronger than Klingon's: Marain is alien because it's *engineered*, not because it's *unusual-among-natural-languages*. Klingon plays at being alien; Marain claims a different design lineage entirely.

### The gatekeeper problem

Klingon's single-authority model produces consistency but also brittleness. Okrand will not be alive forever. The KLI has no clear succession plan for who adjudicates canon after him. Klingon may face a fragmentation crisis within the next 20 years.

Marain has already passed through the equivalent crisis (Banks died in 2013) and the community fragmented — see the prior-art entries in the README. The marainkit response is to make the *spec* the authority rather than any person, which is more durable but also less decisive.

---

## 6. Specific findings worth pulling forward

Things from Klingon's history that are directly applicable as marainkit decisions or open questions:

1. **Mutsun as Okrand's foundation is worth examining.** Okrand's PhD was on Mutsun, an extinct Ohlone language. He has explicitly said this shaped Klingon's grammar more than any other influence. The lesson: a deeply-known minor language as the structural template can produce a more coherent conlang than a magpie approach. Marainkit's Sanskrit research note already plays this role; the question is whether to formally elevate Sanskrit (or another single language) to "structural template" status, or to keep the magpie approach intentionally.

2. **The HolQeD model.** The KLI publishes a quarterly journal of Klingon linguistic research. Marainkit is currently producing equivalent material in `docs/`, but it might be worth deciding whether these notes accumulate into something publishable — a journal, a periodically-versioned spec document, or a living reference. The Klingon precedent suggests the journal-of-research model creates a stable scholarly community around a fictional language in a way that ad-hoc documentation does not.

3. **Wordplay as a cultural marker.** The KLI runs wordplay contests — palindromes, pangrams, spoonerisms in Klingon. This isn't frivolous: it's how a community demonstrates and tests genuine fluency. When marainkit's Layer 2 is mature enough, the analogous test is "can you compose Marain that does something a Mind would consider elegant?" The answer to that question will reveal whether the language is actually usable or just visually impressive.

4. **The dialect question.** Okrand introduced multiple Klingon dialects to absorb the actor-mispronunciation problem. Marain canonically has encryption tiers (M1, M8–M16, M32), which serve a different purpose but create a similar layered structure. The marainkit spec already operates entirely at M1; this is good and should stay explicit. **Tier discipline is a useful inheritance from Klingon's accidental dialect system.**

5. **Translation as the proof of life.** The Klingon community proved the language was real by translating Shakespeare, the Tao Te Ching, and Gilgamesh. The proof-of-life translation for Marain probably isn't Shakespeare (Banks was deeply suspicious of canonical Western texts as scaffolding). A more Banks-coherent target might be a passage from *Consider Phlebas* itself, translated *back* into Marain — a recursive demonstration that the language can carry the meaning Banks already wrote in English. This is left as an open question.

---

## 7. The deeper insight

Klingon and Marain are doing fundamentally different things, and that's the most important finding:

**Klingon is a language designed to make a fictional culture feel real.**

**Marain is a language designed to demonstrate what a hyperintelligent civilisation would do if it engineered a language from scratch.**

Klingon's design constraint is "alien-but-pronounceable-by-actors-on-a-film-set." Marain's design constraint is "what would Minds actually build?" These produce different priorities at every layer:

- Klingon optimises for *performance* (sounding alien on screen). Marain optimises for *transmission* (binary across light-years).
- Klingon's script is decorative. Marain's script is a debug view of structured data.
- Klingon's culture-language correlation is encoded by *vocabulary abundance*. Marain's is encoded by *architectural transparency*.
- Klingon expands by canonical decree. Marain expands by spec'd principle.

What Klingon offers marainkit is mostly **negative space**: a clear example of what marainkit is *not* trying to do, which sharpens the project's own goals.

What it offers positively:

- **Validation that fragmentary canon can sustain a real linguistic community** if the right scaffolding (a journal, tier discipline, an authority structure) is built around it.
- **Validation that script and language are separable** — most Klingon speakers use romanization, and that's fine.
- **Validation of lexical-cultural correlation** as a legitimate design principle, even if marainkit's mechanism (forced legibility) is the inverse of Klingon's (vocabulary abundance).
- **A warning about gatekeeper fragility** — the spec-as-authority model marainkit uses is more durable than Klingon's single-person model, which will face a crisis when Okrand is no longer available.

---

## Open questions raised by this comparison

- Should marainkit adopt explicit canon-tier markers (Banks-canonical / marainkit-decided / community-proposed / experimental) in its decision log?
- Should Sanskrit be formally elevated to structural-template status (analogous to Mutsun for Klingon), or is the multi-source magpie approach intentional?
- Is there a Marain equivalent of *HolQeD* — a periodic publication that consolidates research — worth instituting, even informally?
- What is the proof-of-life translation target for Marain? (Shakespeare is wrong. *Consider Phlebas* is interesting but recursive. The Tao Te Ching might actually be the right target on cultural-philosophical grounds.)
- Is Column B's input method going to be a romanization-picker rather than a glyph-picker, by analogy with how Klingon is actually written daily?

---

## Sources

- Marc Okrand, *The Klingon Dictionary* (1985, rev. 1992)
- Klingon Language Institute (kli.org) — particularly the development history and writing history pages
- Arika Okrent, *In the Land of Invented Languages* (2009)
- Wikipedia: Klingon language; Klingon scripts; Marc Okrand; Object–verb–subject word order
- Klingonska Akademien (klingonska.org) — particularly the pIqaD documentation
- Nick Nicholas, "pIqaD" (opoudjis.net) — on the canonicity question and Unicode rejection
- Interviews with Okrand collected by the National Museum of Language and the Philosophical Society of Washington
- Banks, *A Few Notes on Marain* (in `/docs/`)
