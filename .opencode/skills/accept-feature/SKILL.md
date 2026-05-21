---
name: accept-feature
description: "Validate business behavior against BDD examples from the end user's perspective"
---

# Accept Feature

Available knowledge: [[requirements/gherkin#key-takeaways]], [[software-craft/test-design#key-takeaways]], [[software-craft/test-stubs#concepts]]. `in` artifacts: read all before starting work.

1. Run `task test-build` to verify all tests pass with coverage.
2. Verify all BDD examples pass from the end user's perspective, not the test harness, per [[software-craft/test-design#key-takeaways]].
3. IF an example passes in the test harness but fails from the user's perspective → flag it as a semantic alignment gap per [[software-craft/test-design#concepts]].
4. Verify structural traceability: run `beehave status --json` for stage overview, then `beehave check` for detailed violations per [[software-craft/test-stubs#concepts]]. Every Example in the feature file must have exactly one corresponding test function, and every test function must trace back to an Example. The feature stage must be `ok` and `beehave check` must produce no output.
5. Verify semantic depth per [[software-craft/test-design#concepts]].
6. Verify quality attributes are met.
7. Verify definition of done criteria are satisfied.
8. Produce a traceability matrix: for each stakeholder Q&A topic from interview notes, map to:
   - **Behavioral Q&A**: a passing test (Example title → test function name).
   - **Technology Q&A**: implementation evidence (import, module structure, config) where the technology named in the Q&A is exercised in code. Technology Q&As are verified by reading the feature file's `# Constraints:` and checking the corresponding implementation — NOT through behavioral tests.
   - **Explicit stakeholder deferral**: with the reason it was deferred.
   Untraced Q&As of either type → incomplete delivery.
