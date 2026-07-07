---
domain: methodology
tags: [research, citations, accuracy, grounding, reference-library]
last-updated: 2026-07-02
---

# Research Files

## Key Takeaways

- A research card is the full citation and the source's load-bearing idea — the reference a knowledge author consults to confirm what an inline `(Author, Year)` citation refers to.
- Cards are human reference only; no flow step or skill loads them. They are consulted during knowledge authoring, and the knowledge files are what the flow loads.
- Verify every field against the source — authorship, year, ISBN, DOI, URL — never author from memory, and never fabricate; an unverified source carries an explicit note until researched.
- Capture the source's mechanism, not a paraphrase of it — the machinery a reader applies to decide whether the citation supports the claim.
- The `Key Insight` and `Relevance` fields are what make an inline citation auditable — the insight is the load-bearing idea, the relevance names the knowledge file the citation grounds.
- One card per source under `docs/research/`, grouped by source discipline; the skeleton is `.templates/docs/research/card.md.template`.

## Concepts

**A reference library, not a second knowledge layer.** A card holds the bibliographic fact and the source's central contribution at a glance — the thing a knowledge author needs when they meet `(Author, Year)` in a file and ask "which book, and what does it actually say?". It is not a second statement of the knowledge; the knowledge file carries the claim, the card carries the source.

**Human reference only.** Cards sit under `docs/research/` outside the `.opencode/` graph; no flow state names them as an artifact, no skill loads them, no wikilink resolves to them. They are read by a human (or an authoring agent) during the grounding step of writing knowledge — the step [[methodology/knowledge-files#grounding-and-research]] already names — and never during the build lifecycle.

**Verify, never recall.** Authorship, ISBNs, DOIs, and exact titles drift in recall; a card authored from memory is a plausible error waiting to mislead, and arc42 (Starke) states the stakes plainly — wrong reference material is often worse than none, because it misleads with confidence. Every field is checked against the source's publisher page, the canonical site, or a neutral reference (Wikipedia) before the card is committed. A source whose provenance cannot be confirmed carries an explicit "URL unverified" note rather than an invented detail; the note is debt to clear, not a licence to fabricate.

**Mechanism over paraphrase.** A card that restates the source's title in different words teaches nothing; the `Mechanism` field carries how the idea actually works — the machinery a reader needs to recognise an instance and separate the citation from its neighbours. This is the same depth contract Knowledge Files sets between its Concepts and Content tiers: the deepest layer carries the source's actual mechanism, and a layer that only paraphrases has failed.

**Auditable citations.** An inline `(Author, Year)` in a knowledge file is a promise that the source supports the claim. The card's `Key Insight` states the load-bearing idea in one sentence, and `Relevance` names the knowledge file(s) the citation grounds — together they let a reader trace a claim from knowledge to source without re-reading the source. A citation whose card's `Key Insight` does not support the claim is a defect to fix in the knowledge, not the card.

**One card per source, by discipline.** A source appears once, under the sub-domain that matches its discipline (`psychology/`, `software-engineering/`, `information-science/`), and every knowledge file that cites it links to the same card by author-year. The card is the single home of the source's bibliographic fact; copying that fact into each citing knowledge file would build the drift the methodology already forbids.

## Content

### The card is a reference, not knowledge

The `.opencode/knowledge/` graph carries the claims a build depends on; the `docs/research/` library carries the sources behind those claims. The split keeps the load surface (what an agent ingests mid-build) small while letting a human author dig deeper when grounding a claim. A card never restates the knowledge — it records the source so the knowledge's citation can be verified. This mirrors Diátaxis's separation of reference from explanation (Procida): the card is consulted, not read, and a reader lands on it to confirm a fact and leaves.

### Why nothing in the flow loads a card

A flow state's `input artifacts` and `output artifacts` point at the build's working files; a skill's `Load` step resolves wikilinks under `.opencode/knowledge/` only. Cards live outside both — under `docs/research/`, addressed by filesystem path, not wikilink — so the build lifecycle is indifferent to them. The README at `docs/research/README.md` says as much: the folder is for human reference, consulted during knowledge authoring for author-year lookups. Grounding is an authoring-time activity, not a build-time one.

### Verify every field — the failure mode is recall, not malice

The load-bearing lesson of this project's research folder: authorship and bibliographic data authored from memory were wrong in three of seven fresh-captured cards, even when the source itself was real and well-known. A card for *Extreme Programming Installed* named Kent Beck as an author — he wrote the foreword; the authors are Ron Jeffries, Ann Anderson, and Chet Hendrickson. A card for *User Story Mapping* carried a fabricated ISBN. A card for *Software and Systems Traceability* omitted a third editor. The ISBNs and the Beck authorship would have propagated into every knowledge file that cited them. The rule that follows is absolute: a card's authorship, year, title, ISBN, DOI, and URL are checked against the source's publisher page, its Wikipedia entry, or the canonical site before commit, every time, regardless of how well-known the source seems. A web article is fetched in full and its key claim quoted; a book's title, authors, ISBN, and page count are confirmed against the publisher or Wikipedia.

### No fabrication — unverified is a note, not a guess

When a source is cited in knowledge but its exact provenance cannot be confirmed at capture time, the card carries an explicit `URL: unverified` (or equivalent) note in its Citation section and a `Confidence: Low` line that says why. The note is tracked as debt to clear by a later research pass. What never happens is inventing an ISBN, a URL, a page count, or a co-author to make the card look complete. arc42's warning runs both ways: a missing field a reader knows to verify is honest debt; a confident wrong field is silent corruption. The two unverified-then-confirmed web articles in this folder (Moskvin 2025, Turmyshev 2026) passed through the note-carrying state before their URLs were researched and their cards rewritten from the actual articles.

### Capture the mechanism

The `Mechanism` field is where the card earns its depth. A paraphrase of the title — "this book is about refactoring" — leaves a reader unable to tell whether the citation supports a specific claim about extract method versus one about code smells. The field carries the source's actual machinery: for Moskvin 2025, that vcrpy records verbatim and does not scrub, that the generic Presidio-based scrubber is over-engineered at 670 MB, and that the author lands on JSON-Pointer field redaction via `before_record_response`; for Turmyshev 2026, that external is defined as "any dependency that introduces network latency, rate limits, or data you don't control" and that internal services and repositories are never stubbed. A reader of the card can then decide whether the citation supports the claim the knowledge makes. Apply the prose bar per [[writing/ai-language-markers]] — scrub AI markers (`delve`, `tapestry`, `plays a crucial role`, `rather than`) from the card's prose; the Mechanism field earns its depth through the source's machinery, not formal-sounding padding.

### Auditable inline citations

An inline `(Author, Year)` in a knowledge file resolves to exactly one card. The card's `Key Insight` carries the one-sentence load-bearing idea, and `Relevance` names the knowledge file(s) — and, ideally, the claim — the citation grounds. A reader checking a claim follows the citation string to the card, reads the Key Insight, and either confirms the claim is supported or finds a defect. The defect is fixed where it lives: if the citation does not support the claim, the knowledge file's claim or citation changes, not the card. This is what keeps the knowledge graph honest as it grows — every `(Author, Year)` has a single auditable home.

### Location, taxonomy, and the template

Cards live under `docs/research/` in a taxonomy that mirrors source disciplines, with only the sub-domains that hold cited sources kept:

```
docs/research/
  psychology/{social,cognitive}/
  software-engineering/{architecture,quality,process,requirements}/
  information-science/{domain-modeling,documentation,writing}/
  README.md
```

A new card is copied from `.templates/docs/research/card.md.template` (the `.templates/` → destination convention: strip the `.templates/` prefix and `.template` suffix), placed under the matching discipline, and named `<author>_<year>.md` (lowercase, underscore-separated, matching the folder's existing files). Multiple authors use the form `firstauthor_secondauthor_year`. The eight sections — Citation, Method, Confidence, Key Insight, Core Findings, Mechanism, Relevance, Related Research — are the card's fixed shape; the template carries the skeleton and the verify-never-recall reminder.

## Related

- [[methodology/knowledge-files]]
- [[methodology/separation-of-concerns]]
- [[writing/ai-language-markers]]
