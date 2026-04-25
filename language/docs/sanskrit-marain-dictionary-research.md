# Sanskrit → Marain Dictionary Research

> **Status:** Research document · Design exploration  
> **Layer:** L2 (Constructed Language) · feeds into L3 (Encoding)  
> **Context:** Candidate vocabulary for the Marain dictionary, drawn from Sanskrit as the strongest natural-language analogue to an *engineered* language

> **Track:** Philosophical argument (§ Why Sanskrit) + Encoding system (§ Category vocabulary candidates) — the rationale for Sanskrit as donor language is a design hypothesis; vocabulary candidates are marainkit proposals only. Evidence labels are not applied per-claim. See [`../notes/tracks.md`](../notes/tracks.md).

---

## Why Sanskrit

Banks' anti-Eurocentrism isn't decorative — it's structural. The README already notes that Hindu and Chinese visual influences dominate community interpretations of Marain for *philosophical* reasons, not aesthetic ones. Sanskrit earns its place as primary donor language for the Marain dictionary on several grounds:

1. **Designed, not evolved.** Sanskrit's grammatical system (Pāṇini's Aṣṭādhyāyī) is a *formal grammar* — a finite set of ~4,000 rules that generate the entire language. This is the closest any natural language comes to how a Mind would design a language. Pāṇini's system predates formal computation by millennia but operates on the same principles: root (dhātu) + suffix → derived word, with transformation rules applied in sequence. The parallel to Marain's four-layer architecture is direct.

2. **Derivational transparency.** Every Sanskrit word carries its etymology on its face. The root *dṛś* (to see) produces *darśana* (philosophy/worldview — literally "a seeing"). The root *jñā* (to know) produces *vijñāna* (consciousness — literally "knowing-apart/discerning"). An engineered language designed to reduce ambiguity would share this property. Marain words should be similarly decomposable.

3. **Non-translatable density.** Sanskrit has a class of words whose meaning cannot be adequately captured by any single English term — not because they're vague, but because they encode richer semantic structures. *Ātman* is not "soul." *Dharma* is not "duty." *Rasa* is not "emotion." These are exactly the kinds of words an engineered post-scarcity language would need: concepts that English lacks because English was never designed to encode them.

4. **Tonal and phonetic precision.** Sanskrit's phonetic system is exhaustively classified by place and manner of articulation. Marain has 5 tones. Sanskrit has pitch accent. Both treat sound as structured data, not arbitrary convention.

5. **Banks' explicit framing.** The Culture's language was designed to shape society (Sapir-Whorf). Sanskrit was historically treated the same way — *saṃskṛta* literally means "well-formed / perfected / refined." Both are languages whose designers believed the structure of language could improve the structure of thought.

---

## Selection Criteria

Not every Sanskrit word belongs in a Marain dictionary. Candidates must pass at least one filter:

| Filter | Rationale |
|--------|-----------|
| **Culture-value alignment** | Egalitarian, non-hierarchical, non-dominant, post-scarcity |
| **Semantic gap** | Encodes a concept that English handles badly or not at all |
| **Structural elegance** | Derivational transparency; decomposable into meaningful roots |
| **Tonal mapping potential** | Can plausibly map to Marain's 5-tone system at L2/L3 |
| **Warning/safety vocabulary** | Maps to invariant glyph semantics or status escalation |
| **Consciousness/sentience** | Relevant to Mind/human/drone spectrum of awareness in the Culture |

**On hierarchy and social structure:** Sanskrit terms for caste, rank, and authority (*varṇa*, *jāti*, *āśrama*, etc.) are **not excluded** — the Culture encounters these systems constantly and needs precise vocabulary to describe them. However, Marain never encodes a social structure as an *atomic* morpheme. It encodes it as a *compound* whose child morphemes reveal the mechanism: how the hierarchy is maintained, who it constrains, and whether it's imposed or emergent. The language doesn't forbid the thought — it demands that the thought be *complete*. This is a Culture strategy (legibility through structure), not an Orwellian one (control through omission). See **Category 9: Social Structure as Compound** below.

---

## Category 1: Consciousness & Sentience

The Culture's central ethical axis is *sentience* — what deserves moral consideration, from humans to Minds to drones. Sanskrit has the richest vocabulary for states of consciousness of any natural language. This is the highest-priority category for Marain adoption.

### Core Terms

**Chaitanya** (चैतन्य) · *awareness, consciousness, conscious energy*  
Root: *cit* (to perceive, to be conscious). Refers to awareness as a *state of energy*, not a passive condition. Maps directly to the Culture's treatment of consciousness as substrate-independent — a Mind's chaitanya is as real as a human's. Strong candidate for a Marain root morpheme meaning "awareness/sentience."

**Vijñāna** (विज्ञान) · *discerning consciousness, understanding through differentiation*  
Root: *vi-* (apart/distinctly) + *jñā* (to know). Not "consciousness" in the general sense — specifically the faculty of *distinguishing* one thing from another. This is what Minds do when they process data, what drones do when they assess situations. The "distinction" semantic maps beautifully to the distinction-over-harmony principle in glyph design.

**Prajñā** (प्रज्ञा) · *wisdom through direct insight, not inferential knowledge*  
Root: *pra-* (forth/forward) + *jñā* (to know). Wisdom that arises from *seeing directly*, not from reasoning. In Culture terms: the difference between a Mind's instantaneous comprehension of a situation and a human's step-by-step analysis. A candidate for encoding in the tonal system — the *tone* could carry the distinction between inferential and direct knowing.

**Ātman** (आत्मन्) · *the continuous self, the innermost conscious being*  
Root: *at* (to move) — connotes continuity, persistence through change. Critically: ātman applies to *all living beings*, not just humans. In Culture terms, this is closer to "sentient entity" than "soul." The mobility/continuity root is a good fit for a Marain morpheme meaning "persistent identity" — applicable to both biological and substrate-shifted entities.

**Citta** (चित्त) · *the mind as accumulator of experience*  
Root: *cit* (to perceive). Where chaitanya is raw awareness, citta is the *processed* layer — memory, impression, conditioned response. In Culture terms: the neural lace's stored state, or a Mind's experiential history as distinct from its processing capacity.

### States of Consciousness

Sanskrit maps four states (plus a fifth "beyond") that have no English equivalents. These are structurally interesting because they form an **ordered sequence** — potentially mappable to the base-9 status escalation scale.

| Sanskrit | State | Culture Analogue | Escalation Index? |
|----------|-------|-----------------|-------------------|
| **Jāgrat** (जाग्रत्) | Waking — awareness oriented toward external objects | Normal operational state | 0–2 (neutral) |
| **Svapna** (स्वप्न) | Dream — awareness in internal cognitive space | Simulation / modelling / "what-if" | 3–5 (attention) |
| **Suṣupti** (सुषुप्ति) | Deep sleep — awareness without objects, pure rest | Standby / deep maintenance | — |
| **Turīya** (तुरीय) | The Fourth — pure awareness *of* awareness | A Mind's self-reflective monitoring state | 6–7 (elevated) |
| **Turīyātīta** (तुरीयातीत) | Beyond the Fourth — non-dual awareness | Sublime? The state Banks describes in Minds | 8 (transcendent) |

The four-to-five progression mirrors how the Culture treats consciousness as a *spectrum*, not a binary.

---

## Category 2: Non-Hierarchy & Equality

The Culture's core social value. Sanskrit's contributions here are surprising — the Vedic tradition *also* contains strong egalitarian threads alongside its hierarchical ones. We cherry-pick the egalitarian.

### Core Terms

**Sāmya** (साम्य) · *equality, equilibrium, sameness of condition*  
Root: *sama* (equal, even, same). Not "equality" in the legal/rights sense — more fundamental. Sāmya is the *state of being* in which distinctions of rank don't exist. This is the Culture's default social condition. Strong candidate for a core Marain morpheme.

**Samanvaya** (समन्वय) · *systematic coordination, joining together in order*  
Root: *sam* (together) + *anvaya* (logical sequence). Harmony through *structure*, not through suppressing difference. This is exactly how the Culture works — diverse entities coordinating through shared protocols, not through imposed uniformity. Distinct from *samarasa* (having the same taste / non-discriminatory acceptance), which is closer to "tolerance." Marain would benefit from encoding this distinction.

**Maitri** (मैत्री) · *unconditional goodwill toward all beings*  
Root: *mitra* (friend). More expansive than friendship — it's the baseline disposition of wishing well toward *any* sentient entity, without requiring reciprocity or familiarity. The Culture's default social attitude. Notable because it's non-hierarchical (not charity, not benevolence from above) and non-transactional.

**Ahiṃsā** (अहिंसा) · *non-harm in thought, word, and deed*  
Root: *a-* (not) + *hiṃsā* (harm/violence). The canonical Culture value. Note the three-fold scope: thought, word, deed. A Marain encoding could carry this triplicity in the tonal layer — the *same* root morpheme with three tonal variants for the three domains.

**Saha** (सह) · *togetherness, with-ness*  
Root: the conjunction of the first and last letters of the Sanskrit alphabet — sa + ha — encoding unity. Its reversal *hasa* means laughter/joy, suggesting that Sanskrit itself encodes the idea that togetherness produces joy. Elegant enough to survive as a Marain particle or grammatical marker for collective action.

**Kula** (कुल) · *community, clan, the place where belonging resides*  
Not family by blood — community by *affinity*. The Culture's ship communities, orbital habitats, and loose social groupings are kulas in this sense. A word for "the people you choose" rather than "the people you're born to."

---

## Category 3: The Navarasa (Nine Emotional Essences)

This is where Sanskrit becomes *structurally* essential. Marain has 5 tones at L2, and Banks' essay says that emotional meaning lives in the signal itself. The Navarasa — nine primary emotional essences from the Nāṭyaśāstra — provides a ready-made affective vocabulary that maps onto several Marain problems simultaneously.

### The Nine Rasas

| # | Rasa | Bhāva (root emotion) | Colour | Culture Relevance |
|---|------|---------------------|--------|-------------------|
| 1 | **Śṛṅgāra** (शृङ्गार) | Rati (love/attraction) | Light green | Pervasive in Culture society; non-possessive, non-jealous |
| 2 | **Hāsya** (हास्य) | Hāsa (laughter) | White | Culture's irreverent humour; ship Names as comedy |
| 3 | **Karuṇā** (करुणा) | Śoka (sorrow/compassion) | Grey | Contact's moral weight; the cost of intervention |
| 4 | **Raudra** (रौद्र) | Krodha (anger/fury) | Red | Special Circumstances; justified force |
| 5 | **Vīra** (वीर) | Utsāha (heroic energy) | Orange | SC agents; ships in combat |
| 6 | **Bhayānaka** (भयानक) | Bhaya (fear/terror) | Black | Existential threat; the Idiran War |
| 7 | **Bībhatsa** (बीभत्स) | Jugupsā (disgust/aversion) | Blue | Moral revulsion; the Azadians in _Player of Games_ |
| 8 | **Adbhuta** (अद्भुत) | Vismaya (wonder/awe) | Yellow | First contact; the sheer scale of the Culture |
| 9 | **Śānta** (शान्त) | Śama (peace/tranquility) | White/pale | The Culture's baseline state; post-scarcity calm |

### Why This Matters for Marain Encoding

The Navarasa system has properties that align with Marain's architecture:

**Base-9 structure.** There are exactly nine rasas. Marain uses a 3×3 matrix with 9 cells per glyph (base-9). This is *probably* coincidence. But it means that assigning one rasa per glyph cell position is structurally clean. Each cell position could carry an affective weight.

**Bhāva/Rasa distinction.** The *bhāva* is the raw emotion; the *rasa* is the aesthetic experience of that emotion — the "flavour" a sensitive observer extracts. Marain's separation of Layer 2 (language content) and Layer 3 (encoding) mirrors this: the bhāva lives in the semantic content, the rasa lives in *how it's transmitted*. Tone, rhythm, and signal modulation carry rasa.

**The ninth rasa (Śānta) as default.** Abhinavagupta described Śānta as the string of a necklace — not the most visible jewel, but the structure that holds the others. This maps to the `normal` state in the display context model. Śānta is status index 0.

**Colour associations.** Each rasa has a canonical colour. These could inform the alert/status colour tokens in the display layer — not as direct mappings, but as philosophical justification for the palette.

### Proposed Tonal Mapping

With 5 tones and 9 rasas, a direct 1:1 mapping won't work. But rasas can be *grouped* by tonal affinity:

| Tone | Rasas | Semantic Field |
|------|-------|----------------|
| Tone 1 (neutral/level) | Śānta, Hāsya | Baseline, lightness |
| Tone 2 (rising) | Vīra, Adbhuta | Energy, expansion |
| Tone 3 (falling) | Karuṇā, Bhayānaka | Weight, gravity |
| Tone 4 (rising-falling) | Śṛṅgāra, Raudra | Intensity, arc |
| Tone 5 (falling-rising) | Bībhatsa + complex states | Conflict, ambivalence |

This is speculative. But it demonstrates that the tonal layer can *systematically* encode affect, not just as decoration but as data — which is exactly what Banks described.

---

## Category 4: Knowledge & Perception

The Culture is an epistemic civilisation — its power derives from knowing, sensing, and understanding. Sanskrit's vocabulary for *modes of knowing* is more granulated than any Western language's.

### Core Terms

**Darśana** (दर्शन) · *worldview, philosophy — literally "a seeing"*  
Root: *dṛś* (to see, behold, examine, understand). Not "belief system" — the word encodes that every philosophy is a *way of looking*. In Culture terms: the framework through which a Mind or a citizen interprets data. Different darśanas produce different readings of the same signal. A Marain word for "interpretive lens."

**Jñāna** (ज्ञान) · *knowledge as direct acquaintance, not information*  
Root: *jñā* (to know). Distinct from information (*sūcana*) or data. Jñāna is *knowing* in the sense of having integrated something into understanding. A Mind's jñāna about a situation is different from the raw data it has processed. This distinction matters for Marain because the language should be able to distinguish "I have the data" from "I understand."

**Vidyā** (विद्या) · *liberating knowledge, knowledge that transforms the knower*  
Root: *vid* (to know — cognate with Latin *vidēre*, English "vision"). Knowledge that, once acquired, changes what you are. Learning a language is vidyā; looking up a fact is not. Subliming — the Culture's ultimate transcendence — could be described as the culmination of vidyā.

**Avidyā** (अविद्या) · *ignorance, specifically: mistaking one thing for another*  
Root: *a-* (not) + *vid* (to know). Not mere absence of knowledge — *active misperception*. Taking a rope for a snake. In Culture terms: the error state that Contact tries to correct in less-developed civilisations — not that they lack data, but that they misinterpret what they have. A Marain warning term.

**Pramāṇa** (प्रमाण) · *means of valid knowledge*  
Different schools of Indian philosophy accept different pramāṇas (perception, inference, testimony, analogy, etc.). The concept itself — that *how you know* matters as much as *what you know* — is deeply Culture-compatible. A Marain grammatical particle that flags the epistemic source of a claim.

---

## Category 5: Structure, Form & Engineering

Sanskrit has terms for structural and mathematical concepts that predate their Western equivalents.

### Core Terms

**Sūtra** (सूत्र) · *thread; a terse rule with maximum meaning in minimum words*  
Root: *sīv* (to sew). Pāṇini's grammar is written in sūtras — each one a compressed instruction. The Marain encoding spec is, architecturally, a system of sūtras. A candidate for the Marain word for "protocol" or "specification."

**Tantra** (तन्त्र) · *loom, warp; a framework or system*  
Root: *tan* (to stretch, extend). Not the esoteric sense — the older, structural sense of a *woven framework*. The Culture's technological infrastructure is a tantra. Style Dictionary's token system is a tantra. The word encodes "systematic interconnection."

**Yantra** (यन्त्र) · *instrument, machine, device for constraining or directing*  
Root: *yam* (to restrain, control). A yantra is not just a machine — it's a *purposeful constraint*. A 3×3 glyph grid is a yantra. A drone's chassis is a yantra. The word encodes the idea that form constrains function *intentionally*.

**Maṇḍala** (मण्डल) · *circle, disc; a structured space with a centre*  
Root: *maṇḍ* (to adorn, surround). A structured arrangement of elements around a focal point. The macro 3×3 layout (Approach 2 in the README) is, geometrically, a maṇḍala. Orbital habitats are maṇḍalas. A candidate for the Marain word for "structured arrangement" or "layout."

**Bīja** (बीज) · *seed; the minimal generative unit*  
Root: *bīj* (to generate). In mathematics: the seed/coefficient of an equation. In mantra theory: the irreducible syllable from which a word-family grows. In Marain: the *root morpheme* from which a word-family is generated. A bīja is the smallest unit that still carries generative meaning.

**Aṇu** (अणु) · *atom; the smallest indivisible unit*  
The classical Indian concept of the fundamental particle. In Marain: the individual cell within a 3×3 glyph — the atomic unit of the visual script.

**Śūnya** (शून्य) · *zero, void, emptiness — the generative nothing*  
Root: *śūn* (to swell — paradoxically, emptiness as *potential*). The invention of zero is an Indian contribution. In Marain: Empty glyph #0. Śūnya is not absence — it's the *space in which something can exist*. The Frame glyph (#495) is the *boundary* of śūnya.

---

## Category 6: Communication & Language

Sanskrit has meta-linguistic vocabulary — words *about* words — that Marain, as a self-aware constructed language, would need.

### Core Terms

**Vāk** (वाक्) · *speech as cosmic creative force*  
Root: *vac* (to speak). In Vedic thought, Vāk is simultaneously the act of speaking, the capacity for speech, and the creative power of language itself. In Culture terms: the tightbeam — speech as a physical force that crosses interstellar space and *makes things happen*.

**Artha** (अर्थ) · *meaning — spanning from physical object to abstract concept*  
Root: *arth* (to intend). The scope of artha in Sanskrit linguistics covers external referent, mental concept, semantic role (agent, object), tense, mood, and more. It's "meaning" in the fullest possible sense. A Marain root for "that which a signal carries."

**Dhvani** (ध्वनि) · *resonance, suggestion, the meaning behind the literal meaning*  
Root: *dhvan* (to sound, resonate). In Sanskrit poetics: the *suggested* meaning that a skilled listener extracts beyond the literal. This is the rasa layer of communication. In Marain: what the tonal encoding carries that the binary content does not.

**Sphoṭa** (स्फोट) · *the burst of meaning that occurs when sound meets comprehension*  
Root: *sphuṭ* (to burst open). A technical term from Sanskrit linguistics: the moment when a sequence of phonemes suddenly resolves into understood meaning. Not the phonemes themselves, not the meaning itself — the *event* of comprehension. In Marain: the moment a glyph sequence resolves into a word. A beautiful concept for which no other language has a term.

**Saṃskāra** (संस्कार) · *impression left on the mind by experience; refinement through processing*  
Root: *sam* (together) + *kṛ* (to do/make). Dual meaning: (a) the trace an experience leaves, and (b) the process of *refining* raw material into finished form. Both apply to Marain: the saṃskāra of encoding (refining raw text into binary → glyph), and the saṃskāra left on the reader by the message.

---

## Category 7: Warning & Safety Vocabulary

The invariant glyphs emerge from geometry, not convention — but they need *semantic assignments*. Sanskrit provides words whose meanings align with the invariant glyph vocabulary.

### Proposed Mappings

| Glyph | # | Geometry | Sanskrit Candidate | Rationale |
|-------|---|----------|-------------------|-----------|
| **Diamond** | 170 | Central point with radiating alert | **Cetas** (चेतस्) — alertness, warning-awareness | The first flicker of "pay attention" |
| **Cross** | 186 | Intersecting axes, boundary marker | **Maryādā** (मर्यादा) — boundary, limit, rule | "You are approaching a boundary" |
| **Corners** | 325 | Occupied extremes, empty centre | **Āvaraṇa** (आवरण) — veil, concealment, obstruction | Something is hidden or blocked |
| **Checkerboard** | 341 | Maximum alternation, instability | **Vikalpa** (विकल्प) — doubt, false concept, alternation | Ambiguity, unresolved state |
| **Empty** | 0 | No cells filled | **Śūnya** (शून्य) — void, zero, potential space | Null / absence / available |
| **Point** | 16 | Single centre cell | **Bindu** (बिन्दु) — point, seed-syllable, origin | Origin marker, reference point |
| **Frame** | 495 | All border cells, empty centre | **Kṣetra** (क्षेत्र) — field, bounded space, domain | Container, encoding space |
| **Full** | 511 | All cells filled | **Pūrṇa** (पूर्ण) — full, complete, whole | Completion, saturation, end-of-stream |

The warning group (Diamond → Cross → Corners → Checkerboard) maps to an escalation: alertness → boundary → concealment → ambiguity. The structural group (Empty → Point → Frame → Full) maps to a lifecycle: void → origin → container → completion.

---

## Category 8: Aesthetic & Ethical Principles

Concepts that inform the *philosophy* of Marain's design, even if they don't become dictionary entries.

**Rasa** (रस) · *essence, juice, flavour; the aesthetic experience itself*  
The meta-concept. In Marain: the claim that a well-designed signal doesn't just carry information — it carries *flavour*. The tonal layer is the rasa layer.

**Sahṛdaya** (सहृदय) · *"one who has heart"; a sensitive, attuned receiver*  
Root: *sa-* (with) + *hṛdaya* (heart). In rasa theory: the ideal audience member who can extract the full emotional meaning from a performance. In Culture terms: any sentient being capable of receiving a Marain transmission and extracting not just the data but the *feel*. The word encodes that communication requires a *prepared receiver*.

**Loka** (लोक) · *world, realm, plane of experience*  
Root: *lok* (to see, perceive). A loka is a world *as experienced* — not an objective place but a domain of perception. Each Culture habitat is a loka. The Sublime is a loka. A Marain word for "experiential domain" that doesn't assume physical space.

**Līlā** (लीला) · *play, divine play; creative activity for its own sake*  
Root: *līl* (to play). Action undertaken not for utility but for the joy of the action itself. This is the Culture's raison d'être — a civilisation that has solved scarcity and now exists *for the play of existing*. Ship Names are līlā. Designing Marain is līlā.

**Advaita** (अद्वैत) · *not-two; non-duality*  
Root: *a-* (not) + *dvaita* (duality). Not "oneness" — the negation of twoness. The Culture's rejection of hierarchical binaries (human/machine, civilised/primitive, male/female) is advaita in practice. Marain's gender-neutral pronoun is an advaita construction.

---

## Category 9: Social Structure as Compound

A language designed by Minds would not describe social structures by naming them — it would describe them by *decomposing* them. The design principle: **Marain never encodes a social structure as atomic. It always encodes it as a compound whose components reveal the mechanism.**

This is not censorship. It's the opposite — it's forced legibility. Orwell's Newspeak removes words to prevent thoughts. Marain *adds* morphological structure to ensure thoughts are complete. A Culture citizen can describe a caste system in Marain. They just can't do it without articulating what the caste system *is made of*.

Three registers are available, distinguished tonally:

| Register | Tonal Contour | Use Case | Example Construction |
|----------|--------------|----------|---------------------|
| **Analytical** | Neutral / level | Contact field reports, academic description | "stratified-role-assignment" |
| **Empathic** | Karuṇā (falling) | Expressing compassion for those constrained by the system | Same compound, sorrow-tone |
| **Critical** | Bībhatsa (complex) | Moral evaluation of the system as harmful | Same compound, revulsion-tone |

The *denotation* is identical across registers. The *affect* changes. Data and feeling travel in the same signal.

### Decomposed Sanskrit Source Terms

These Sanskrit words are not adopted whole into Marain. They are *mined for child morphemes* — their roots and components become the atoms from which Marain builds its own compounds.

**Varṇa** (वर्ण) · *colour, classification, category*  
Root: *vṛ* (to cover, to choose). The root meaning — classification, sorting — is a useful atom. It's the *application* to birth-rank that Marain refuses to encode as a single unit. The child morpheme *vṛ* (to sort/classify) enters the dictionary. A Marain speaker constructing a word for "caste" would combine *vṛ* (classify) with morphemes for "birth" and "imposed" and "fixed" — producing a compound that reads something like "imposed-birth-classification-fixed." You can't say it without hearing all four components.

**Jāti** (जाति) · *birth-group, species, kind*  
Root: *jan* (to be born, to generate). The root *jan* is essential — birth, origin, generation are core vocabulary for any language. It only becomes a hierarchy term when fused with role-assignment. In Marain: *jan* is a free morpheme meaning "origin/generation." To describe a jāti system, you'd compound it with "role" and "constrained-to" — making the causal link between birth and social position *syntactically explicit* every time.

**Āśrama** (आश्रम) · *stage of life, domain of effort*  
Root: *śram* (effort, labour, exertion). A good morpheme for "domain of sustained practice." It becomes hierarchical only when the stages are *ranked* and *sequenced as mandatory*. In Marain: *śram* (sustained-effort) is a root. "Life stage" is a compound of *śram* + temporal morpheme. The ranking, if present, must be explicitly constructed — it's not baked into the word.

**Rājan** (राजन्) · *king, ruler*  
Root: *rāj* (to shine, to rule). The root conflates radiance with authority — the king shines, therefore leads. Marain would decompose this: "authority" is one morpheme, "assigned-by" is another, "consent-of-governed" or "force" or "inheritance" would be a third. You can describe a rājan in Marain, but you have to specify *what kind of authority* and *how it was obtained*. The word won't let you assume legitimacy.

**Sevā** (सेवा) · *service, attendance, devotion to a superior*  
Root: *sev* (to serve, attend upon). Contains an embedded hierarchy: the one who serves and the one served. Marain would decompose the act: "sustained-effort" (*śram*) + "directed-toward" + "another-entity." Whether that constitutes subordination or mutual aid depends on the additional morphemes. Service-as-gift and service-as-compulsion become structurally different words, even though English (and Sanskrit) use the same term for both.

**Dharma** (धर्म) · *that which upholds; duty, cosmic order, righteousness*  
Root: *dhṛ* (to hold, sustain, maintain). This is the most complex case. Dharma simultaneously means cosmic order, personal duty, social obligation, and ethical conduct — and in its hierarchical application, it's used to justify caste as divinely ordained. Marain would keep *dhṛ* (to sustain/maintain) as a root morpheme. But "cosmic order," "personal ethical conduct," and "socially imposed obligation" would be three different compounds built from different child morphemes around *dhṛ*. The word that the Azadians use to justify their social system and the word that a Culture citizen uses for ethical commitment would share a root but diverge in structure — making the *difference* between "order imposed from above" and "order maintained by consent" lexically visible.

### Design Principle Summary

The Culture's Minds understand that social structures are *mechanisms*. They have parts. They have inputs and outputs. They have beneficiaries and those they constrain. A language designed by Minds would encode social structures the way an engineer describes a machine — not by its name, but by its components, its function, and its effects.

This produces three consequences:

1. **No naturalisation.** An atomic word like "caste" allows a speaker to treat the system as a natural category. A compound like "imposed-birth-classification-fixed" does not. The morphology prevents the system from *hiding*.

2. **Cross-system comparison becomes easy.** Because all social structures are built from the same pool of child morphemes (classify, impose, inherit, consent, constrain, assign, etc.), a Marain speaker can instantly see structural similarities between systems that opaque vocabulary obscures. Feudalism and caste share morphemes. Democracy and consensus share different ones.

3. **The tonal layer carries the Culture's stance.** The analytical register describes. The empathic register mourns. The critical register judges. A Contact agent filing a report uses neutral tone. A citizen discussing the same system at a party uses affect-laden tone. The grammar handles both without requiring separate vocabulary.

---

## Open Questions

1. **Root morpheme extraction.** Several candidates above (*jñā*, *cit*, *vid*, *dṛś*, *vac*) are Sanskrit verbal roots that could serve as Marain root morphemes. Should the L2 phoneme set be designed to accommodate them, or should we transliterate them through Marain's own phonological constraints?

2. **Navarasa as tonal grammar.** The 5-tone / 9-rasa mapping is speculative. Does the tonal system carry affect *per-word* (each word has a rasa tone) or *per-phrase* (rasa is a suprasegmental property of larger units)? Per-word is simpler to encode; per-phrase is more expressive.

3. **Invariant glyph assignments.** The Sanskrit mappings in Category 7 are proposals, not decisions. They need to be validated against the D₄ equivalence class constraint and the minimum Hamming distance requirements.

4. **Column B integration.** Many of these words would enter the dictionary through Column B (phoneme composition), not Column A (binary encoding). The Column B spec needs to advance before these can be formally adopted.

5. **Donor language ethics.** Sanskrit is a living scholarly and liturgical language. Borrowing its vocabulary for a fictional constructed language should be done with the same care marainkit applies to Banks' intellectual property — as *inspiration and influence*, not extraction. The "kit" framing applies here too.

6. **Compound construction grammar.** Category 9 proposes that social structures are always compounds, never atomic. This needs a *formal rule* at L2: which morpheme classes are permitted as compound heads, what ordering constraints apply, and how the tonal register system interacts with compound stress. The Sanskrit samāsa (compound) system has six formal types — are any of them directly adoptable?

7. **Register distinction in binary.** The three tonal registers (analytical / empathic / critical) need to be encodable at L3. If tone is carried in data bits alongside phonemic content, the register distinction adds bits per morpheme. What's the cost in glyph density?

---

## References

- Bharata Muni, *Nāṭyaśāstra* (c. 200 BCE–200 CE) — source of rasa theory
- Pāṇini, *Aṣṭādhyāyī* (c. 4th century BCE) — formal grammar as generative system
- Abhinavagupta, *Abhinavabhāratī* (c. 1000 CE) — ninth rasa (Śānta), aesthetic philosophy
- Monier-Williams, *A Sanskrit-English Dictionary* (1899, rev. 2008) — etymological reference
- Malhotra & Dasa, *Sanskrit Non-Translatables* (2020) — untranslatable terms framework
- Stanford Encyclopedia of Philosophy, "Language and Testimony in Classical Indian Philosophy"
- Banks, I.M., "A Few Notes on Marain" — canonical source for Marain properties