---
domain: architecture
tags: [data-modeling, oltp, olap, schema-as-contract, workload-driven, access-patterns]
last-updated: 2026-07-07
---

# Data Modeling

## Key Takeaways

- The schema is a **binding contract**, authored by the data-architect from captured external shapes and the interview **before** any test stub is written. The build-phase developer implements against the model; they do not invent it. A schema deferred to build is the bug, not the workflow.
- **Access patterns decide schema.** Name the workload (OLTP / OLAP / hybrid) before naming a table — the right shape for one is malpractice for the other, and a "general-purpose" schema optimises for nothing.
- **Workload-driven normalization.** Normalize for OLTP (write integrity, per-row access); denormalize for OLAP only against a measured, named query pattern that pays for it. Normalization is a trade-off against an access pattern, never a virtue.
- **The model is grounded in captures, not guesses.** Every field traces to a captured external shape (cassette / `external-contracts.md`) or an interview finding. A field with no trace is speculative (drop) or a missing capture (route to explore), never a guess.
- **Integrity lives in constraints.** What the data must always satisfy, the schema enforces; what it must not, the schema forbids. An index without the query that justifies it, a constraint the spec does not require — both are rejected.
- The model is **upstream of the test contracts** (`author-test-stubs`, `review-test-stubs`, `write-test-py`, `simulate-contracts` all read `data-model.md` as a binding input); a contract whose persistence shapes disagree with the model is rejected at `simulate-contracts`.

## Concepts

**The schema is a contract, not a deferral.** When the model is left to the build phase, the developer mirrors the code's class shapes into tables — producing schemas optimised for nothing the system actually does. The fix is structural: a state in the plan subflow (`model-data-schema`) dispatches the data-architect to author `data-model.md` from the captured external shapes and the interview, before any test stub exists. The contracts downstream reference the modeled schema; the developer implements against it. The data-architect's standing refusal — "a schema without the queries that justify it, an index without the access pattern that pays for it" (`data-architect.md`) — is the rule this state exists to enforce, at the moment the inputs that satisfy it (captures, interview) are available.

**Access patterns decide schema.** OLTP and OLAP answer different questions. An OLTP workload (ingest-heavy, append-only, point reads) wants normalized tables, write integrity in constraints, and indexes on the keys the per-row reads use. An OLAP workload (read-heavy analytics, aggregations, filters on named dimensions) wants dimensions modeled explicitly and pre-aggregation where a named query pays for the storage cost. A "hybrid" workload is not a fudge — it is two named access paths reconciled by an explicit trade-off (often a normalized write path feeding a denormalized read projection). The data-architect names the workload and the queries before any table is named; the workload is the load-bearing decision, recorded with cited evidence from the interview or the captures.

**Workload-driven normalization.** Third-normal form is the OLTP default because it preserves write integrity and answers point reads cheaply. Denormalization is a trade-off, taken only against a measured, named access pattern: a query that joins several tables at read-time and pays for it at scale, and which a denormalized projection would serve cheaper. A denormalization with no query behind it is premature; a normalization level beyond what the workload needs is structure the system does not require. Either is rejected at `model-data-schema`, not deferred to build.

**Grounded in captures, not guesses.** The captured external shapes (cassettes + `external-contracts.md`) are the truth about what the system must persist and consume; the interview is the truth about why. A field in the model with no trace to either is a guess — and a guess baked into the schema becomes a load-bearing lie the build cannot challenge. A field the model needs but no capture covers is a missing capture, routed back to explore (`needs-capture`), never invented. The rule mirrors the cassette rule for adapter tests ([[software-craft/external-fixtures]]): the capture is the truth; never hand-edit it to make the code pass, and never invent a schema shape to make the code convenient.

**Integrity in constraints.** The data-architect's principle (`data-architect.md`): what the data must always satisfy, the schema enforces; what it must not, the schema forbids. A `NOT NULL` constraint is the contract that the column always carries a value; a `UNIQUE` constraint is the contract that two rows never share it; a `CHECK` is the contract on the value's domain; a `FOREIGN KEY` is the contract that the referenced row exists. Each is a rule the spec requires, recorded as a constraint the schema enforces — not a hope the application code honours. A constraint the spec does not require is over-engineering; a rule the spec requires but the schema does not enforce is a gap.

**Upstream of the test contracts.** The `data-model.md` artifact is an input to `author-test-stubs`, `review-test-stubs`, `write-test-py`, `derive-source-stubs`, and `simulate-contracts` — every state that authors or gates a persistence-adjacent contract reads the model. A test stub whose persistence shapes disagree with the model is incoherent, rejected at `simulate-contracts` with the disagreement cited (which table, which column, which shape the test asserts vs which the model declares). The model is the canonical persistence shape, the way the cassette is the canonical external shape.

## Content

### Workload classification

| Workload | Signal | Schema shape | Normalization |
|---|---|---|---|
| OLTP | ingest-heavy, append-only, per-row point reads/writes | normalized tables, integrity in constraints, indexes on read keys | 3NF default |
| OLAP | read-heavy analytics, aggregations, filters on named dimensions | dimensions modeled explicitly, pre-aggregation where a named query pays | denormalized read projections, fed from a normalized write path |
| Hybrid | both access patterns are cited in the interview | two named paths reconciled by an explicit trade-off (often normalized write + denormalized read projection) | normalization per path, recorded |

A workload classification with no cited evidence is rejected — it is a guess, and the schema shape follows from it.

### Schema-as-contract — what the model declares

`data-model.md` records, per table:

- **purpose** — one line, traced to an interview finding;
- **columns** — name, type, and the constraint that holds (`NOT NULL`, `UNIQUE`, `CHECK`, `FK target`);
- **indexes** — paired with the named query pattern that justifies each;
- **OLTP/OLAP/hybrid verdict** — from the workload classification, with the access patterns the shape optimises for;
- **field traces** — every field traced to a captured external shape or an interview finding.

The build-phase developer implements exactly this model — no tables added, no columns invented, no indexes beyond those the model names. A deviation is a contract break, routed back to plan.

### Anti-patterns

| Anti-pattern | What it looks like | Why it's rejected |
|---|---|---|
| Mirroring a code-class shape into a table | a `User` class with a `profile: Profile` becomes a `users` table with a JSON `profile` blob | the access pattern is the spec for the schema, not the class layout; a blob defeats query integrity and index use |
| Premature denormalization | a `rates` table pre-joined to `currencies` "for performance" with no named query | denormalization is a trade-off against a measured access pattern, never a default |
| An index without a query | `CREATE INDEX idx_x ON t (x)` because "we'll probably query on x" | an index costs writes; only a named query pattern that pays for it justifies it |
| A constraint the spec does not require | `CHECK (status IN ('A','B'))` when the spec names no status enum | over-engineering; integrity is enforced for what the spec requires, not what it might |
| Speculative field | a column with no consumer in any cited access pattern or interview finding | YAGNI; the model serves the cited workload, not a future that may not arrive |
| Invented shape | a column type or constraint that no capture and no finding justifies | the model is grounded in captures and the interview; a guess baked into the schema is a load-bearing lie |

Each is rejected at `model-data-schema` with the offending element cited; the model is the smallest schema that serves the cited access patterns, per [[methodology/simplicity-discipline]].

## Related

- [[software-craft/external-fixtures]] — the captured external shapes the model is grounded in; the cassette is the truth for adapter tests the way the model is the truth for persistence contracts
- [[methodology/simplicity-discipline]] — the smallest schema that serves the cited access patterns; speculative structure is dropped here, not deferred
- [[requirements/spec-simulation]] — `simulate-contracts` rejects a contract set whose persistence shapes disagree with the model
- `.opencode/agents/data-architect.md` — the agent's standing refusals (no schema without queries, no index without an access pattern) are the rule this state enforces
