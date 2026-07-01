---
name: confirm-red-failure
description: "Confirm the target contract's tests fail for the right reason before implementing — new work or rework, never a test defect."
---

# Confirm Red Failure

1. Load [[software-craft/tdd]] — red/green discipline and the right-reason rule.
2. Remove the pending marker from all the target contract's tests for this cycle — the only test edit allowed in build. Do not author tests; they already exist with full bodies.
3. Run the tests. Confirm the failure is ours: IF the source .py is absent and the deferred in-body import raises `ImportError` THEN new work; IF the source .py exists but is stale against the changed contract and an assertion fails THEN rework. Either is the right reason per [[software-craft/tdd]].
4. IF the red fails for the wrong reason (a typo, a bad fixture, a contract the tests themselves violate) THEN reject it — do not patch the test.
5. Read the target contract's .pyi first, not the whole tree.
