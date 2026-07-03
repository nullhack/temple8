---
name: record-decision
description: "Author (or amend) an Architecture Decision Record for a load-bearing architectural decision, in place, with a change log."
---

# Record Decision

1. Confirm the decision is ADR-worthy before authoring: it has genuine trade-offs between multiple viable alternatives **and** cross-cutting impact (reversing it would ripple across contracts). IF it has one obvious choice or only local impact THEN it is BAU — do not record it; stop here.
2. Copy `.templates/docs/decisions/YYYY-MM-DD-<kebab-title>.md.template` to `docs/decisions/<today>-<slug>.md`, replacing the date placeholder with today's ISO date and the slug with a short kebab title for the decision.
3. Fill the sections from the decision itself, not from memory of the alternatives: `Context` (the forces — link the interview, glossary, existing ADRs, cassettes, and the contract set; do not restate them), `Decision` (one imperative sentence), `Alternatives considered` (each alternative + why it was rejected), `Consequences` (+ / − / neutral, with mitigations for the negatives). Apply the prose bar per [[writing/ai-language-markers]] — scrub AI markers (`delve`, `tapestry`, `plays a crucial role`, `rather than`); the ADR's authority comes from the decision's forces, not formal-sounding prose.
4. In `Traceability`, link the artefacts the decision touches — tests, source `.pyi`, migrations, cassettes, glossary terms, related ADRs — by path. Points only; never restate the artefact's content (tests are the source of truth).
5. Seed the `Change log` with one row: `<today> | Created | <one-line reason>`.
6. IF the decision supersedes an existing ADR THEN edit that ADR in place — amend its `Status`, `Decision`, `Alternatives considered`, and `Consequences` to the current decision — and append a `Change log` row (`<today> | Amended | <what changed and why>`). Do not create a new file; the body always reflects the current decision and the log carries the history.
7. Verify every path in `Traceability` resolves to a real artefact before finishing.
