---
domain: methodology
tags: [simplicity, kiss, yagni, scope-discipline, anti-patterns, traced-requirement]
last-updated: 2026-07-07
---

# Simplicity Discipline

## Key Takeaways

- Simplicity is a **traced requirement, not an aspiration**. Every abstraction, seam, configurability, and building block in the contracts is either grounded in a cited stakeholder need or removed at consolidation. "Might need it later" is not a need.
- **Neither over- nor under-engineer.** Over-engineering is structure beyond the finding (a speculative abstraction); under-engineering is a missing structure the cited need requires (a gap that will surface as a hop break or a build-implied gap at `simulate-contracts`). The discipline cuts both ways: every cited need gets exactly the structure it requires, no more, no less.
- **YAGNI is the default; KISS is the shape.** You build the thing the spec requires and you build it in the simplest shape that serves the cited access pattern. A speculative abstraction is rejected; a missing abstraction the workload demands is a gap.
- The simplicity check is **applied at every gate that authors structure**: the three interview funnels (drop speculative items before they reach the contracts), `consolidate-interview` (grounded in a cited need or removed), `author-test-stubs` (no test expresses structure beyond its finding), `review-test-stubs` (the scope-minimal, inverted-traceability check), `model-data-schema` (the smallest schema that serves the cited access patterns), and `simulate-contracts` (build-implied gaps include under-determined behaviour from speculative or missing structure).
- The anti-pattern catalogue names the smells: **premature abstraction, speculative configurability, duplicate concept, seam-without-a-reason, speculative field, speculative building block**. Each is grounded-or-dropped at the earliest gate that sees it.

## Concepts

**Traced requirement, not aspiration.** A requirement is traced when it cites a stakeholder need recorded in `interview-notes.md` — a concrete incident (CIT), a writable constraint (Laddering), a named access pattern. A structure is justified when removing it would leave a cited need unmet; it is speculative when no cited need requires it. The rule is symmetric: a structure the cited need does not require is over-engineering (drop it); a structure the cited need does require but the contracts omit is under-engineering (a gap, not simplicity). The discipline is not "build less" — it is "build exactly what the cited need requires, in the simplest shape that serves it."

**Why YAGNI is the default.** A speculative abstraction — a seam, a configurability, a building block — is paid for twice: once when authored into the contracts (test surface, source stub, schema, glossary term), and again when implemented and maintained. The future it was bought against rarely arrives in the shape predicted, so the abstraction either fights the real requirement or is silently bypassed. The cost is not only the code; it is the surface area the gate trio (`review-test-stubs`, `simulate-contracts`) must police, and the ambiguity a speculative seam introduces into the simulation (two impls, one matching the spec and one matching the seam, both passing). Dropping the speculative structure at the interview shrinks the contract surface before the gates run.

**Why KISS is the shape, not the ceiling.** "Build the simplest thing" is misread as "build the dumbest thing" — a licence to omit structure the cited need genuinely requires. The simplest shape that serves a cited access pattern is the goal; if the access pattern requires an abstraction (a value object, a protocol, a denormalised projection), the abstraction is the simplest shape and omitting it is under-engineering. The test is the cited need, not the line count.

**Where the discipline runs.** The interview funnels ask the simplicity question at each level (L1: smallest surface that meets the need; L2: speculative vs grounded behaviour groups; L3: load-bearing vs collapsible building blocks). `consolidate-interview` drops speculative items before they reach the contracts. `author-test-stubs` expresses only the structure the findings require. `review-test-stubs` runs the scope-minimal check — the inverted-traceability mirror of coverage: not "is every finding tested?" but "is every test finding-grounded?". `model-data-schema` models the smallest schema that serves the cited access patterns. `simulate-contracts` catches the residue as build-implied gaps (an effect asserted without pinning how; two impls both passing). The discipline is applied at the earliest gate, not deferred to the latest.

## Content

### The anti-pattern catalogue

Each anti-pattern is a structure beyond the cited need. Each is named at the gate that first sees it and dropped (or routed to rework) with the speculative element cited.

| Anti-pattern | Signal | Where caught | Action |
|---|---|---|---|
| Premature abstraction | a class, protocol, or hierarchy with no cited need requiring it | interview L3, `review-test-stubs`, `simulate-contracts` | collapse into the caller; drop the abstraction; cite the missing need or remove |
| Speculative configurability | a parameter, option, or strategy hook no cited access pattern exercises | interview L2, `review-test-stubs` | inline the one variant the spec requires; drop the hook |
| Duplicate concept | two names for one cited need (a value object and a primitive both carrying the same domain value) | interview L3, `consolidate-interview`, `simulate-contracts` | unify behind one canonical form per the data-shape rule in [[software-craft/source-stubs]] |
| Seam-without-a-reason | an interface or boundary with a single implementation and no cited integration or anti-corruption need | interview L3, `review-test-stubs`, `derive-source-stubs` | inline the implementation; introduce the seam only when a second implementation or a cited context boundary requires it |
| Speculative field | a column in `data-model.md` with no consumer in any cited access pattern | `model-data-schema` | drop the field; route to `needs-capture` if a future capture might ground it |
| Speculative building block | a bounded context or module with no quality attribute and no behaviour group grounding it | interview L3, `consolidate-interview` | drop the block at consolidation; flag if a later finding requires it |

### The simplicity question at each funnel level

| Level | Question | What it catches |
|---|---|---|
| L1 (general) | "What's the smallest surface that meets the need?" | scope inflation at the big-picture level — the stakeholder's answer names the minimum, the contracts honour it |
| L2 (cross-cutting) | "Which of these behaviour groups are speculative — not grounded in a cited stakeholder need?" | behaviour groups the stakeholder did not name in a CIT incident or a laddered constraint |
| L3 (building-blocks) | "Is this building block load-bearing, or could it collapse into a neighbour?" | modules that have no unique responsibility a cited need requires |

A speculative item surfaced at any level is either grounded (cite the need) or dropped (remove from the notes). `consolidate-interview` enforces the drop: a speculative item with no cited grounding does not reach the contracts.

### Scope-minimal — the inverted-traceability mirror

`review-test-stubs` runs two complementary checks:

| Check | Direction | Question | Failure |
|---|---|---|---|
| traceability (existing) | finding → test | "Is every finding tested?" | a finding with no test is a coverage gap |
| scope-minimal (the mirror) | test → finding | "Is every test finding-grounded?" | a test expressing structure beyond its finding is speculative |

A test that introduces an abstraction, a seam, a configurability, or a building block not grounded in a cited finding is speculative — routed to `needs-stubs-rework` with the speculative element named. The gate evidence key `scope-minimal` is `true` only when no stub in the set expresses speculative structure.

### The clean non-speculative model

The simplicity discipline applies to the schema as much as to the test and source contracts. `model-data-schema` models the smallest schema that serves the cited access patterns: a table with no query that reads it, a column with no consumer, a normalisation level beyond what the workload needs, an index without a named query — each is speculative structure, dropped at `model-data-schema`, not deferred to build. The model is clean (non-speculative) when every element traces to a cited access pattern or finding; the contracts downstream reference a clean model, and `simulate-contracts` rejects a contract whose persistence shapes disagree with it.

## Related

- [[requirements/interview-techniques]] — CIT and Laddering are how a need becomes "cited"; a need that is not cited is not a requirement
- [[requirements/domain-decomposition]] — the gap analysis the simplicity question at L3 feeds into
- [[architecture/data-modeling]] — the schema-as-contract rule and the speculative-field anti-pattern, applied at `model-data-schema`
- [[software-craft/source-stubs]] — the data-shape rule that resolves a duplicate concept
- [[software-craft/test-design]] — the vacuous-assertion smells (a vacuous test often hides a speculative structure that the test does not pin)
- [[requirements/spec-simulation]] — the build-implied-gap sweep catches residue the earlier gates missed
