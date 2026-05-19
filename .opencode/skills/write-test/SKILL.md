---
name: write-test
description: "Write a failing test body for one BDD example"
---

# Write Test

Available knowledge: [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/test-stubs]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]]. `in` artifacts: read all before starting work.

1. Pick the next test function with an `...` (Ellipsis) body from the auto-generated test stubs: prefer tests within the same Rule file before moving to the next Rule, and order by fewest dependencies first per [[software-craft/tdd#concepts]]. pytest-beehave creates stubs with `test_<example_title_slug>` naming and `...` bodies (auto-skipped during collection). IF the Example belongs to a structural (invariant) Rule → also generate a Hypothesis property test in `tests/unit/` per [[software-craft/test-design#concepts]], using the counterexamples surfaced by the behavior pre-mortem per [[requirements/pre-mortem#concepts]].
2. **External fixture gate**: IF the Example/Scenario Outline references an external adapter or API (check domain spec External Contracts section), verify the real fixture exists in `tests/fixtures/<service_name>/` per [[software-craft/external-fixtures#key-takeaways]]. IF the fixture is missing → flag as a blocker. Do NOT write the test against imagined data. Request fixture capture before proceeding.
3. Write a failing test that specifies the expected behavior per [[software-craft/tdd#key-takeaways]]. Replace the `...` body with the test implementation. The test function name (derived from the Example title) is immutable — it is the traceability link maintained by pytest-beehave. For Scenario Outline stubs with `@given`/`@example` decorators, use the placeholder parameters in the test body:
    - All placeholders and literals from the spec steps must appear in the test body per Spec Value Fidelity ([[software-craft/test-design#concepts]]) — `beehave check` verifies their presence. Use each value in a way that reflects its domain purpose: identifiers identify, boundaries bound, configurations configure. Never add noise code to satisfy traceability.
4. IF a spec gap or inconsistency is discovered → do NOT modify specification documents (domain_spec.md, glossary.md, product_definition.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
5. Run `task test-fast` to confirm the test fails for the right reason (RED) per [[software-craft/tdd#key-takeaways]].
