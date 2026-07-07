---
domain: architecture
tags: [quality-attributes, non-functional-requirements, atam, trade-offs, ilities]
last-updated: 2026-07-02
---

# Quality Attributes

## Key Takeaways

- Quality attributes (the `-ilities`) are the architectural drivers — distinct from functional requirements. They are what the system *must be* (fast, available, secure, modifiable), not what it *does* (Bass, Clements & Kazman, 2021).
- Canonical set: Availability, Deployability, Interoperability, Modifiability, Performance, Security, Testability, Usability. Each has a **tactics catalog** (design moves that directly address it) and is made operational as a **scenario** (stimulus → environment → response).
- Attributes **conflict** — Performance vs Modifiability; Security vs Performance; Availability vs cost — and the architect resolves it by explicit prioritisation, not by optimising everything.
- Elicited in `interview-cross-cutting` as a cross-cutting concern; coverage-checked in `interview-building-blocks` (every quality attribute → ≥1 building block, the gap analysis of [[requirements/domain-decomposition]]).
- Load-bearing trade-offs between attributes are **architecturally significant decisions** — recorded as ADRs via the `record-decision` skill, not left implicit.
- The full ATAM ceremony (stakeholder utility-tree ranking) is trimmed for this flow: elicit the attributes that matter, surface the conflicts, record the trade-offs. Most quality attributes are qualitative at test-time; the tests assert behaviour, the ADR records the quality-attribute reasoning behind it.

## Concepts

**Architectural drivers, not functional requirements.** A quality attribute is a measurable property of the runtime or development-time system — how fast it responds, how available it stays, how easy it is to change — as opposed to a functional requirement, which describes behaviour. The architect's leverage is over the attributes: choosing an architecture is, largely, choosing which attributes to optimise and which to sacrifice. Treating them as an afterthought is how systems end up fast-but-unmaintainable, or secure-but-unusable (Bass, Clements & Kazman, 2021).

**Scenarios make an `-ility` operational.** "The system must be performant" is unactionable; "a read request arrives at peak load; the system responds within 200 ms, 99th percentile" is a scenario that can be designed toward and tested against. The scenario form (stimulus, environment, response) is the bridge between a fuzzy `-ility` and a concrete design move — and it is what the interview elicits, not the bare word.

**The tactics catalog.** Each attribute has known design moves: Performance uses caching, concurrency, resource arbitration; Availability uses redundancy, fault-detection, recovery; Modifiability uses encapsulation, substitution, binding-time deferral; Security uses authentication, authorisation, audit. Tactics are the building blocks the architect combines; architectural styles (layered, hexagonal, event-driven) are pre-combined tactic bundles optimised for different attributes (Bass, Clements & Kazman, 2021).

**Conflicts force explicit trade-offs.** Performance (fewer indirections) fights Modifiability (more abstraction layers); Security (encryption, validation) costs Performance; Availability (redundancy) costs resources. The architect cannot satisfy all of them — the decision is *which matter most for this system*, and that decision is exactly what an ADR exists to record when it is load-bearing.

**Where this lives in the flow.** Quality attributes surface at `interview-cross-cutting` (funnel level 2) alongside bounded contexts, integration points, and lifecycle events — the cross-cutting concerns the interview must capture. `interview-building-blocks` then runs the gap analysis: every quality attribute must map to ≥1 building block whose tactics address it (per [[requirements/domain-decomposition]]), or the gap is flagged. The system-architect at `derive-source-stubs` honours them implicitly (the type surface and adapter choices carry the tactics); the explicit record of any hard trade-off is an ADR.

**Qualitative at test-time.** Most quality attributes are not directly asserted by the contract tests, which verify behaviour. Performance, availability, security posture are carried in the design (the tactics chosen) and the ADR (the reasoning), not in a `@pytest.mark.pending` test. The tests are the source of truth for *behaviour*; the ADR is the source of truth for the *quality-attribute reasoning* behind the architecture that produces that behaviour.

## Content

### The canonical set and a tactic each

| Attribute | Concern | A representative tactic |
|---|---|---|
| Availability | uptime under fault | redundancy + failover + health checks |
| Deployability | ease + safety of release | environment parity + staged rollout |
| Interoperability | speaking to other systems | a published contract + an anti-corruption layer |
| Modifiability | ease of change without side effects | encapsulation + binding-time deferral |
| Performance | response time + throughput under load | caching + concurrency + resource arbitration |
| Security | resistance to unauthorised access | authentication + authorisation + audit |
| Testability | ease of verifying behaviour | observability + dependency injection + deterministic state |
| Usability | ease of correct use | consistent interface + clear error paths |

### Conflicts and their trade-off

| Conflict | The trade-off |
|---|---|
| Performance ↔ Modifiability | indirection costs cycles; abstraction eases change |
| Security ↔ Performance | encryption + validation add overhead |
| Availability ↔ cost | redundancy needs more resources |
| Interoperability ↔ model purity | a published contract invites external models in (use an ACL, per [[architecture/context-mapping]]) |

A trade-off that ripples across contracts is architecturally significant — record it as an ADR (`record-decision` skill); a trade-off local to one module is BAU and is not recorded.

### Eliciting in the interview

`interview-cross-cutting` captures, per quality attribute the stakeholders care about, a one-line scenario (stimulus → response), not the bare word. "Performant" → "geocode + forecast under 500 ms at 10 req/s." "Available" → "the history write succeeds even if the external weather API is down." The scenario is what `interview-building-blocks` can map to a building block and its tactics.

## Related

- [[requirements/domain-decomposition]] — the gap analysis that maps every quality attribute → ≥1 building block
- [[architecture/context-mapping]] — interoperability and model-purity tactics across context boundaries
- [[requirements/ubiquitous-language]] — the glossary is where each attribute's project-specific name is registered
