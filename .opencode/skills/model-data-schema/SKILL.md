---
name: model-data-schema
description: "Author the persistence schema as a binding contract from the captured external shapes and the interview — before any test stub is written."
---

# Model Data Schema

1. Load [[architecture/data-modeling]], [[software-craft/external-fixtures]] — the schema-as-contract rule, OLTP/OLAP selection, workload-driven normalization, and the captured external shapes that bound the model.
2. Bootstrap the journal. IF `.cache/<session_id>/journal.md` does not exist THEN render it from `.templates/cache/journal.md.template` (substitute `<session_id>`). The journal is the carry-over artifact for build-phase escalations, capture gaps, and the simulation walk; empty until those states write to it. Absence on a first pass is expected — never a deliberation point; the first pass IS the empty-journal pass. IF it exists THEN it carries build-phase escalations from the prior build cycle — read them and model the gaps it names first.
3. Read `.cache/<session_id>/external-contracts.md`, `tests/cassettes/**`, `.cache/<session_id>/interview-notes.md`, `docs/glossary.md`.
4. Classify the workload before naming a table. State, with cited evidence from the interview or the captured exchanges, whether the dominant access pattern is:
   - OLTP — ingest-heavy append-only, per-row writes, point reads; normalise; enforce integrity in constraints.
   - OLAP — read-heavy analytics over large sets, aggregations and filters on named dimensions; model the dimensions and pre-aggregate where a named query pays for it.
   - Hybrid — name the OLTP path and the OLAP path separately and the trade-off that reconciles them.
5. Author `.cache/<session_id>/data-model.md` as the schema spec the build-phase developer implements against — NOT a deferral, NOT a sketch. For every table record:
   - its purpose, in one line, traced to a finding in `interview-notes.md`;
   - every column with its type and the constraint that holds on it (NOT NULL, UNIQUE, CHECK, FK target);
   - every index, paired with the named query pattern that justifies it — an index without a cited query is rejected per [[architecture/data-modeling]] and per the agent's own refusal (`data-architect.md`);
   - the OLTP/OLAP/hybrid verdict from step 4 and the access patterns it optimises for.
6. Trace every field to a captured external shape or an interview finding. A field with no trace is either speculative (drop it) or a missing capture (route to `needs-capture`), never an ungrounded guess baked into the model. Anti-patterns to refuse, named in [[architecture/data-modeling]]: mirroring a code-class shape into a table, premature denormalization, an index without a query, a constraint the spec does not require.
7. Apply simplicity discipline per [[methodology/simplicity-discipline]]: model the smallest schema that serves the cited access patterns. A table with no query that reads it, a column with no consumer, a normalisation level beyond what the workload needs — each is speculative structure, dropped here, not deferred to build.
8. IF the model surfaces an important new domain concept THEN add it to the glossary.
9. IF a captured external shape is ambiguous or insufficient to model against THEN append the gap to `.cache/<session_id>/journal.md` (service, the missing case) and fire `needs-capture`. Do NOT invent the shape — the model is grounded in captures, not guesses.
