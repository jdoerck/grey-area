# Why Marain — Rationale and Goals

*Stub. This document captures the motivations behind marainkit. To be expanded in future sessions.*

---

## The core argument

A constructed language with a deterministic, binary-encoded writing system offers properties that no natural language and no existing script can fully provide. The reasons to build this are not aesthetic — they are practical, ethical, and civilisational.

---

## Benefits — stub list

### Semantic specificity
Natural languages are ambiguous by design — context, tone, and shared culture fill the gaps. A constructed language can define meanings precisely and permanently, eliminating the classes of misunderstanding that cause harm at scale: legal ambiguity, medical miscommunication, diplomatic misreading.

### Equality of access to knowledge
A script that is learned rather than inherited does not belong to any culture, nation, or economic class. A child in any location, with any native language, encounters it on equal terms. Knowledge encoded in Marain is not gated by which language you were born into.

### Universalism
No natural writing system is neutral. Every existing script carries the history and power structures of the civilisation that produced it. A constructed system, designed openly and transparently, can be genuinely universal — owned by no one, available to everyone.

### Alignment with AI systems
Binary-encoded, deterministic, semantically precise language is the natural interface layer between human meaning and machine processing. A Marain encoding layer eliminates the lossy translation step between human intent and machine representation. As AI systems become more embedded in daily life, a shared formal language reduces the surface area for misinterpretation.

### Hardware efficiency
A 9-bit grid with 512 states maps cleanly onto binary memory structures. Marain text is compact, self-describing, and does not require complex Unicode normalisation, bidirectional rendering, or font fallback chains. It is maximally efficient on constrained hardware — embedded systems, low-power devices, transmission over degraded channels.

### Deep history encoding — substrate independence
Information encoded in Marain does not require functioning software, a power grid, or institutional continuity to be read. The encoding is geometric and binary — it can be carved, stamped, woven, printed, or transmitted as radio pulses. A civilisation that loses its infrastructure can still read Marain from a physical surface. This is not true of any digital-native format.

### Resilience and redundancy
The 8 rotation/mirror-invariant glyphs provide orientation markers that survive physical degradation, partial destruction, and arbitrary rotation. A fragment of Marain text can be identified and oriented without context. No natural script has this property.

### Inclusion across ability
A system designed from first principles can accommodate non-standard interaction: tactile (raised dots), auditory (tonal encoding), visual (high-contrast binary glyphs). Accessibility is architectural, not retrofitted.

### Longevity of meaning
Natural language drift makes texts opaque within centuries. A constructed language with a fixed, published specification does not drift unless intentionally updated. Meanings encoded today remain legible to a reader in 500 years who has access only to the specification.

---

---

## Dictionary architecture

*Technical stub — to be expanded. Recorded here because the choice flows directly from the project's core values.*

### The model

The dictionary maps **Marain → concept**, not **Marain → English word**. Translations are derived at query time from an external concept graph, not stored locally. This keeps the dictionary lean, substrate-independent, and language-neutral by default.

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
