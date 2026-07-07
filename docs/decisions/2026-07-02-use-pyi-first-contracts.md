# Use `.pyi`-first staged contracts as the development chain

> A record of a load-bearing architectural decision — the *why* behind a choice
> that multiple viable alternatives competed for. Authored only by the
> system-architect, only when a decision has genuine trade-offs **and**
> cross-cutting impact (reversing it would ripple across contracts); BAU
> decisions are not recorded. Supersession is edit-in-place: amend the body to
> the current decision and append a Change log row — do **not** create a new
> file. Tests are the source of truth for behaviour; the Traceability section
> points at affected artefacts and never restates them.

## Status

Accepted

## Decider + Date

- **Decider:** system-architect (clean-slate rebuild)
- **Date:** 2026-07-02

## Context

The clean-slate rebuild removed the previous spec-driven orchestration layer (the
`beehave`/BDD layer, `.feature` files, generated stubs). The workflow retains its
core principle — tests are the source of truth for behaviour — but needs a
contract chain that lets the surface be authored and simulated *before any source
is implemented*, and a way to detect drift between a signature view and the body
that pyright structurally cannot see (pyright prefers the `.pyi` and hides
`.py`/`.pyi` disagreement at runtime). The chain also has to be cheap to read
mid-build, so an agent re-entering a contract does not ingest every full body to
understand the surface.

## Decision

Adopt a staged `.pyi`-first contract chain as the sole development path: plan
authors test `.pyi` (signatures expressing the domain), then test `.py` bodies
marked `@pytest.mark.pending` (the body is the spec), then derives source `.pyi`
from what the tests reference, then simulates the set before build; build
implements each source `.py` from its fixed `.pyi` one contract per cycle.
`mypy.stubtest` is the drift detector for both source and test `.pyi`, gated at
simulate (tests), green/review (scoped source + test pair), and merge
(whole-suite).

## Alternatives considered

- **Beehave/BDD with `.feature` files and generated stubs:** rejected — the
  dropped layer. Generation drifts from the source of truth, the Gherkin
  ceremony is heavy for a Python workflow, and the `.feature` file becomes a
  second spec that disagrees with the tests.
- **Inline annotations only (signatures-with-`...` in the `.py`, no `.pyi`):**
  rejected — there is no drift detector. pyright reads the `.py` directly and
  cannot flag a body that has drifted from its declared surface, so the "cheap
  signature view" goal dissolves into reading full bodies; the staged-authoring
  goal (simulate the *surface* before implementation) has no separate artefact
  to simulate.
- **No upfront contracts (write tests at build time, classical TDD):** rejected —
  loses the staged contract surface and the pre-build simulation. Build would
  author tests + implementation together, collapsing the plan/build separation
  and removing the moment where the whole set is checked for coherence before any
  code is written.

## Consequences

- **(+)** Contracts are authored and simulated as a complete set before any
  source is implemented; coherence gaps surface at plan, not at build.
- **(+)** `mypy.stubtest` catches `.pyi`/`.py` drift at every gate; pyright's
  blind spot is covered.
- **(+)** Reads mid-build are cheap — the `.pyi` is the signature view; a full
  `.py` body is opened only for the detail the stub omits.
- **(−)** A test `.pyi` carries no domain types (its parameters are fixtures and
  `self`), so its domain value is near-zero and it is maintained solely so
  stubtest can check the test pair — a recurring lint-and-sync cost.
- **(−)** The chain adds a `derive-source-stubs` step and a scoped-stubtest
  discipline that inline annotations would not need; `mypy` is required
  alongside `pyright`.
- **(neutral)** Source `.pyi` are fixed during build; a contract gap escalates
  back to plan rather than being edited in place — this is the intended
  discipline, not a cost.

## Traceability

Points at the artefacts this decision touches; never restates their content.

- **Tests:** `tests/integration/**/*_test.pyi`, `tests/e2e/**/*_test.pyi` (the
  staged test surface).
- **Source `.pyi`:** `<package>/**/*.pyi` (the derived source surface).
- **Migrations:** unaffected.
- **Cassettes:** unaffected (the external contract is orthogonal).
- **Glossary:** `docs/glossary.md` — "staged contract surface", "pending mark",
  "stubtest".
- **Related ADRs:** none yet.

## Change log

Appended on any amendment; the body above always reflects the current decision.

| Date | Change | Reason |
|---|---|---|
| 2026-07-02 | Created | Initial clean-slate decision. |
