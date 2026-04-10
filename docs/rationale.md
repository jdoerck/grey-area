# Why Marain — Rationale and Goals

*Stub. This document captures the motivations behind marainkit. To be expanded in future sessions.*

> **Evidence labels used in this document:**
> `[canonical]` — directly from Banks source text ·
> `[inference]` — consistent with canon, not explicitly stated ·
> `[project decision]` — deliberate choice where canon is silent ·
> `[speculative]` — interesting hypothesis, not yet tested
>
> *See [evidence-labels.md](evidence-labels.md) for full definitions.*

---

## The core argument

This project explores whether a constructed language with a deterministic, binary-encoded writing system can offer properties that no natural language and no existing script can fully provide. The motivations for pursuing this are not aesthetic — they are practical, ethical, and civilisational. The hypotheses below describe what we are designing *toward*; they are not claims the system has already demonstrated.

---

## Benefits — stub list

### Semantic specificity `[speculative]`
Natural languages are ambiguous by design — context, tone, and shared culture fill the gaps. A constructed language can define meanings more precisely and permanently than a natural one. **[speculative]** Whether this eliminates the classes of misunderstanding that cause harm at scale — legal ambiguity, medical miscommunication, diplomatic misreading — is a design hypothesis, not a demonstrated property.

### Equality of access to knowledge `[project decision]` `[speculative]`
**[project decision]** A script that is learned rather than inherited is a design goal of marainkit — it should not belong to any culture, nation, or economic class. **[speculative]** Whether a child in any location encounters it on genuinely equal terms depends on adoption, tooling, and pedagogy that do not yet exist. The aspiration is real; the outcome is not yet established.

### Universalism `[speculative]`
No natural writing system is neutral. Every existing script carries the history and power structures of the civilisation that produced it. **[speculative]** Whether a constructed system, designed openly and transparently, can be *genuinely* universal — owned by no one, available to everyone — is a research question, not a proven outcome. The goal is worth pursuing; the claim requires evidence.

### Alignment with AI systems `[speculative]`
**[speculative]** Binary-encoded, deterministic, semantically precise language *may* reduce the surface area for misinterpretation between human intent and machine processing. The claim that it "eliminates the lossy translation step" is a hypothesis. The relationship between Marain's encoding model and AI system design has not been tested.

### Hardware efficiency `[project decision]`
**[project decision]** A 9-bit grid with 512 states maps cleanly onto binary memory structures. Marain text is compact, self-describing, and does not require complex Unicode normalisation, bidirectional rendering, or font fallback chains. These are architectural properties of the design — verifiable in principle, though not yet benchmarked against real targets.

### Deep history encoding — substrate independence `[project decision]` `[speculative]`
**[project decision]** The encoding is geometric and binary — it can be carved, stamped, woven, printed, or transmitted as radio pulses. This substrate independence is a deliberate design property. **[speculative]** The claim that "a civilisation that loses its infrastructure can still read Marain from a physical surface" while no digital-native format survives is a thought experiment, not a tested scenario.

### Resilience and redundancy `[canonical]` `[project decision]`
**[canonical]** The 8 rotation/mirror-invariant glyphs emerge from the geometry of the 3×3 binary grid — they are a mathematical property of the system, not an invention. **[project decision]** The decision to reserve these as orientation markers — to exploit their orientation-invariance for orientation recovery — is marainkit's choice. Banks does not specify this use.

### Inclusion across ability `[project decision]`
**[project decision]** A system designed from first principles can accommodate non-standard interaction: tactile (raised dots), auditory (tonal encoding), visual (high-contrast binary glyphs). This is a design goal, not a property the system has demonstrated. Accessibility is an architectural aspiration; whether it has been achieved requires implementation and testing.

### Longevity of meaning `[speculative]`
**[speculative]** The claim that a fixed, published specification prevents meaning drift is plausible — natural languages do drift and constructed ones with stable specs may drift less — but it is untested at the timescales claimed. A reader in 500 years with access only to the specification is a thought experiment, not a validated scenario.

---

---

## Dictionary architecture

*Technical stub — to be expanded. Recorded here because the choice flows directly from the project's core values.*

### The model

**[project decision]** The dictionary maps **Marain → concept**, not **Marain → English word**. Translations are derived at query time from an external concept graph, not stored locally. This keeps the dictionary lean, substrate-independent, and language-neutral by default.

```
Marain glyph / word  →  concept ID  →  translation in any language (on demand)
```

### Concept ID candidates

- **Wikidata Q-numbers** — every concept has a stable Q-ID. Maps to ~300 languages for free via the Wikidata API or periodic snapshots. No local translation storage required.
- **Open Multilingual Wordnet (OMW) synset IDs** — older, more conservative, stronger semantic structure (hypernyms, hyponyms, meronyms). Better fit for a language focused on semantic precision.
- Both IDs can be carried per entry — they are not mutually exclusive.

### Storage formats

| Format | Role |
|--------|------|
| Plain TSV | Canonical source of truth. One entry per line. Human-readable, diffable, no software dependency. Archivally stable. |
| SQLite | Queryable local index, generated from TSV. Single file, no server. The SQLite team targets 100+ year format stability — used for archival by the US Library of Congress. |
| JSON Lines | Export / interchange. One JSON object per line. Streamable for bulk processing. |
| RDF N-Triples | Semantic web export. One triple per line, minimal syntax. Zero migration cost if the project grows into linked-data infrastructure. |

**Eliminated:** any format with a server dependency (Postgres, MongoDB, Neo4j, Redis). These fail the substrate test.

### Translation without local storage

By anchoring on concept IDs rather than translated strings, mass translation into any language is a query against Wikidata, not a storage problem. A periodic offline snapshot can be bundled for air-gapped use. The dictionary itself stays small enough to be printed, carved, or transmitted over a low-bandwidth channel.

---

## Open threads — for future discussion

- The relationship between a constructed script and political neutrality
- Whether universalism is achievable or whether any design embeds assumptions
- The role of Marain in scientific and mathematical communication
- Interoperability with existing Unicode and encoding standards
- The ethics of proposing a universal language
- Practical adoption pathways — education, tooling, institutions

---

*See [`roadmap.md`](../encoding/docs/roadmap.md) for the technical backlog. This document is the philosophical counterpart.*

*See [`sapir-whorf.md`](sapir-whorf.md) for the theoretical grounding and actionable design implications of linguistic relativity as applied to marainkit.*
