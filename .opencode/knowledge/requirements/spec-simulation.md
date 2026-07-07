---
domain: requirements
tags: [spec-simulation, mental-execution, composition, cross-test-coherence, gate]
last-updated: 2026-07-01
---

# Spec Simulation

## Key Takeaways

- Simulation is a **mental execution of the contract set** — the test `.pyi`, the test `.py`, and the source `.pyi` together — asking whether a correct implementation that passes every test would actually work end-to-end and be complete.
- The e2e-affecting failures live in **composition and cross-test coherence**, where tools are blind: a type imported from a module that does not re-export it, a value whose shape differs between the tests that produce and consume it, a shared module no test drives, a dependency graph with no valid build order. These surface only when a human walks the contracts.
- Simulation is a **compiler, not a ceremony**. It does not validate that the model "works" — the model (`data-model.md`) is already a binding input. It takes the contract set and simulates how the real application would run if a correct implementation made every test pass, the way a compiler walks an AST to prove the program type-checks and links before any code executes. The goal is to **disprove or confirm** the system works, mentally, before any source `.py` is written.
- **Walk the e2e path hop by hop, journal at each hop** — entry point → adapter → domain → persistence. At each hop confirm the type passed, the value carried, and the side effect performed each trace to a backing contract, and **append the observation to `.cache/<session_id>/journal.md` at that hop** — not only the verdict at the end. A broken hop is the simulation's main catch.
- **Trace each domain value across every test that touches it.** If two tests pass the same concept in different shapes, the contract is incoherent; pin one canonical form or split the concept. No tool performs this — it is a reading, not a check.
- **Spec-diff is not traceability.** Traceability counts whether a finding has any test; spec-diff asks whether the test would actually fail if the finding were violated. A finding named in a test but not enforced — a vacuous assertion, a lower-bound-only check, an `assert True`, an effect asserted without pinning how — is a gap, not a pass.
- **Build-implied gaps** are ambiguities a correct implementation would surface: two impls both pass but only one matches spec; an effect asserted without pinning how; a side effect no test observes; a persistence shape the test asserts but the model doesn't declare. The gate question expands from "would passing = working?" to "would passing = working **and unambiguous**?".
- The tool floor is **necessary but not sufficient**: pyright (zero errors, tolerate `reportMissingModuleSource` pre-build), stubtest over the test pairs (drift), no-orphans (every source symbol exercised, every test reference backed), traceability (every interview finding → a test or deferral; every external service → a captured cassette). Each catches a class of defect; none catches composition or ambiguity.
- The output is a **judgment with evidence**: the gate decision — advance, or a named gap — backed by the per-hop walkthroughs, the value traces, the spec-diff, and the build-implied-gap sweep, all recorded in the journal. The simulation's value is the understanding that informs the decision.

## Concepts

**Mental execution of the contract set.** The plan phase produces the contract set: every test written as an executable body, every source symbol recorded as a `.pyi` signature, the schema recorded in `data-model.md`. Simulation is the act of reading that set as if it were already implemented and asking the one question that gates the build: *if a correct implementation made every one of these tests pass, would the resulting system work as intended and be unambiguous?* It is a prediction of the future, made by walking the contracts the future will be built from. Because the contracts are executable, the prediction is answerable: every type, call, and side effect the simulation reasons about is one a test will enforce. Simulation is a compiler, not a ceremony: it does not validate that the model works (the model is a binding input, already authored), it compiles the contract set in the reader's head to disprove — or confirm — that the system runs, before any source `.py` exists.

**Why the tool floor is not enough.** pyright, stubtest, and the traceability counts each police a class of defect the others miss, and together they form a real floor — but every one of them reads files in isolation or checks a structural invariant, and none of them reads *across* the contract set the way a reader does. A type imported from a module that does not re-export it resolves fine for the checker and breaks at the composition. A value carried as a bare filesystem path by one test and as a `sqlite:///` URL by another is typed `str` in both stubs and passes every check, while the contract it implies is incoherent. A shared data module with no external boundary of its own has no test driving it, and no tool notices the gap. These are the failures that ship to build and surface as e2e breakage; simulation is the step that exists to catch them, because nothing else does.

**The e2e hop-by-hop walkthrough.** The most powerful reading centres on the broadest test — the one that exercises the entry point — and walks the implementation it implies one hop at a time. The entry point composes an adapter, the adapter calls into the domain, the domain persists through a boundary; at each hop the walkthrough confirms three things: the *type* handed across matches the type the receiver declares, the *value* carried matches the shape the producer emits, and the *side effect* the hop performs is one a contract actually specifies. A hop where the type comes from the wrong module, or the value arrives in a shape the receiver does not accept, is the simulation's main catch — the kind of defect that only appears when the pieces are imagined together.

**Cross-test value tracing.** Alongside the e2e spine, each domain value is traced across every test that produces or consumes it. The discipline catches the contract that is internally contradicted: the same database URL arrives as a bare path in one test and a URL in another; the same amount is a `float` in the producer and an `int` in the consumer; the same identifier is a string here and a value object there. Two tests disagreeing on a value's shape is not a tolerance the build can paper over — it is an incoherent contract, and the fix is to pin one canonical form (the data-shape rule) or to recognise that two concepts were conflated and split them. A checker sees two well-typed tests; a reader sees the disagreement.

**The tool floor.** Beneath the readings run the mechanical checks, and they are not optional. pyright at zero errors (tolerating `reportMissingModuleSource`, which is expected when source `.pyi` exist but no `.py` yet) confirms the types are internally consistent. stubtest over the test pairs confirms each test `.pyi` agrees with its `.pyi` sibling. The no-orphans check confirms every source symbol a test could reach is exercised and every test reference is backed by a source `.pyi`. Traceability confirms every interview finding maps to a test or an explicit deferral and every external service has a captured cassette its tests replay. Each is a real filter; none is the simulation.

**Judgment with evidence.** The output is the gate decision itself — *the contract set is coherent and complete; a passing implementation will work* — backed by the walkthroughs and traces that justify it, or a named gap that routes back to plan. Where a gap is found it is stated precisely (which hop, which value, which contradiction); where none is found, the understanding lives in the decision to advance. The simulation's value is that understanding, held at the gate.

## Content

### What gets walked

| Artefact | Role in the simulation |
|---|---|
| test `.py` (the bodies) | the specification — every type constructed, method called, relationship asserted |
| test `.pyi` | the declared module surface each body must agree with |
| source `.pyi` | the implementation surface the tests collectively demand |
| `docs/glossary.md` | the names the tests should use consistently |
| `tests/cassettes/**` | the real external shapes the boundary tests must assert against |

A finding that cannot be grounded in one of these artefacts is not a simulation finding.

### The composition failures tools miss

| Failure | What a tool sees | What the walkthrough sees |
|---|---|---|
| a type imported from a module that does not re-export it | a resolved import | a consumer that will break the composition |
| one value in two shapes across tests | two well-typed values | an incoherent contract |
| a shared data module with no test of its own | no violation | a contract with no driver — who builds it, and when? |
| a dependency cycle in the build order | nothing | no valid outside-in sequence to build in |
| an e2e test whose hops do not all trace to a `.pyi` | a passing test on paper | an end-to-end path with a gap in the middle |

These are the e2e-affecting failures; each ships silently to build if simulation does not catch it.

### The build-implied gaps

Ambiguities a correct implementation would surface — the contract under-determines the behaviour, so two impls both pass but only one matches the spec. Each is a gap even when the tool floor is clean.

| Gap | What the tool sees | What the simulation sees |
|---|---|---|
| two impls both pass, only one matches spec | a green test set | an under-determined contract — the test does not pin the behaviour the spec requires |
| an effect asserted without pinning how | a green test set | a test that asserts an outcome but not the mechanism; a constant, a no-op, or a real computation all pass |
| a side effect no test observes | a green test set | a contract that claims a side effect (a write, a publish) but no test observes it; the impl could omit it and pass |
| a persistence shape the test asserts but `data-model.md` doesn't declare (or vice versa) | a green test set | a contract that disagrees with the modeled schema — incoherent, the model is canonical |

The gate question expands from "would passing = working?" to "would passing = working **and unambiguous**?". A contract set with a build-implied gap is not `accepted`; it routes to `needs-test-bodies` (or `needs-source-stubs` if the ambiguity is at the source-stub surface) with the gap cited.

### Spec-diff

For each consolidated interview finding, confirm the test set **enforces** it, not merely names it. This is distinct from traceability (which counts coverage); spec-diff asks whether the test would actually fail if the finding were violated.

| The finding | Traceability says | Spec-diff says |
|---|---|---|
| "the report carries a generated_at timestamp" | a test references `generated_at` | the test asserts a *value* (a real timestamp, its type, its presence under a non-trivial impl) — `hasattr(report, "generated_at")` is naming, not enforcing |
| "the renderer escapes HTML" | a test calls the renderer | the test asserts the *escaped output* against input that would break a constant-string renderer — a constant-satisfiable test is naming, not enforcing |
| "the adapter returns JSON-serialisable values" | a test calls `_to_jsonable` | the test asserts *round-trip through `json.dumps`* — `_to_jsonable(value: object) -> object: return value` is naming, not enforcing |

A finding named in a test but not enforced is a gap, routed to `needs-test-bodies` with the finding and the offending test cited.

### The e2e hop-by-hop walkthrough

Walk the entry-point test as if the system were built, hop by hop:

1. the entry point receives the input the test sends — confirm its type and shape;
2. it composes its first collaborator (an adapter, a service) — confirm the collaborator's `.pyi` exists and accepts what is passed;
3. the collaborator calls inward (domain, persistence) — confirm each call's type and the value's shape at the boundary;
4. any external hop asserts against a captured cassette — confirm the cassette exists and the shape matches;
5. the side effect at the end (a print, a write, a record) — confirm a contract specifies it.

A hop that fails any confirmation is the gap; name it precisely (which hop, which type, which shape) and route back to plan.

### Cross-test value tracing

For each domain value that crosses a boundary, list every test that produces or consumes it and compare the shape:

| the value | produced as | consumed as | verdict |
|---|---|---|---|
| a database URL | `sqlite:///{path}` (config test) | a bare `{path}` (history test) | **incoherent — pin one form** |
| a rate | a `Rate` value object (rates test) | a `Rate` (cli test) | coherent |
| an amount | `float` (one test) | `int` (another) | **incoherent — split or unify** |

Two shapes for one concept is a defect to resolve at plan, not a tolerance for build to absorb.

### The tool floor

| Check | Catches | Does not catch |
|---|---|---|
| pyright (0 errors; tolerate `reportMissingModuleSource`) | internal type inconsistency | cross-file composition |
| stubtest over test pairs | `.pyi`↔`.py` drift | whether the contract is coherent |
| no-orphans | unexercised source symbols, dangling test references | shared-module coverage gaps |
| traceability | an untested finding, an un-cassocked service | whether the tests agree |

### The output

The simulation produces one of two outcomes, and nothing else:

- **coherent, complete, and unambiguous** — the walkthrough reached no broken hop, the value traces found no disagreement, the spec-diff found no named-but-not-enforced finding, the build-implied-gap sweep found no ambiguity, the tool floor is clean; advance to build. The journal holds the per-hop observations that justify the verdict, not only the verdict.
- **a named gap** — which hop broke, which value disagreed, which finding was named but not enforced, which ambiguity a correct impl would surface, which persistence shape disagreed with the model; route back to plan (or explore, or discover) with the specifics.

The understanding is the output, and it lives in the gate decision — recorded in the journal at the hop it was made, not only at the verdict.

## Related

- [[software-craft/test-stubs]] — the `.pyi`/`.py` pairs the tool floor checks
- [[software-craft/test-design]] — what a complete test set looks like (the surface being walked)
- [[software-craft/source-stubs]] — the data-shape rule that resolves an incoherent value
- [[requirements/domain-decomposition]] — the traceability the simulation re-checks
