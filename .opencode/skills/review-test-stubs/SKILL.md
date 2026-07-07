---
name: review-test-stubs
description: "Review the test stubs for coverage, scope, vacuous-assertion freedom, finding-grounded scope, and happy-path completeness against the interview and the modeled schema — not for code quality."
---

# Review Test Stubs

1. Load [[software-craft/code-review]], [[requirements/domain-decomposition]], [[software-craft/test-design]], [[methodology/simplicity-discipline]] — review method, gap analysis, the vacuous-assertion smells, and the scope-minimal rule.
2. Treat this review as coverage and scope against requirements, not code quality — quality is gated later on the bodies.
3. Check consistency: every stub maps to an interview requirement and uses the glossary's ubiquitous language; external-layer stubs match the captured cassettes; persistence-adjacent stubs reference the modeled schema in `.cache/<session_id>/data-model.md`, not invented shapes.
4. Check scope: integration and E2E only; IF a unit test leaked in THEN reject it.
5. Check happy-path completeness: the stub set, once implemented, would exercise the full happy paths of every identified building block. IF a building block or quality attribute maps to no stub THEN flag the gap per [[requirements/domain-decomposition]].
6. Vacuous-assertion check: for every assertion in every stubbed test, confirm it would **fail under a trivial implementation** (constant return, empty collection, identity function, `return value`). A test that cannot fail under a trivial impl tests nothing — route to `needs-stubs-rework` citing the specific test and the smell. The named smells, per [[software-craft/test-design]]:
   - `hasattr`-only — asserts an attribute exists, nothing about its value;
   - no-op helper — `_to_jsonable(value: object) -> object: return value` passes as "JSON-serialisable"; `return True`, `assert True`;
   - lower-bound-only — `assert x >= 0` against an empty fixture (trivially true);
   - constant-satisfiable — a renderer/format test that a constant-string output would pass;
   - tautology — the assertion derives the expected value from the computation under test.
   IF any assertion matches a smell THEN reject the stub set with the test and the smell cited; do not defer to `simulate-contracts`. The gate evidence key `vacuous-assertion-free` is `true` only when no stub in the set carries any named smell.
7. Scope-minimal check (the inverted-traceability mirror of step 5): every test traces to a consolidated finding; any test expressing structure beyond its finding is flagged for rework citing the speculative element. Step 5 asks "is every finding tested?"; this step asks "is every test finding-grounded?". A test that introduces an abstraction, a seam, a configurability, or a building block not grounded in a cited finding is speculative per [[methodology/simplicity-discipline]] — route to `needs-stubs-rework` with the speculative element named. The gate evidence key `scope-minimal` is `true` only when no stub in the set expresses speculative structure.
