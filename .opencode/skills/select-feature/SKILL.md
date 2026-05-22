---
name: select-feature
description: "Select the next feature to develop by detecting delivery status from disk evidence, deriving priority from dependency count and WSJF"
---

# Select Feature

Available knowledge: [[requirements/wsjf#key-takeaways]], [[software-craft/test-stubs#key-takeaways]]. `in` artifacts: read all before starting work.

1. List available feature files in `docs/features/`.
2. IF no feature files exist → exit via `no-features`; features need discovery first.
3. Run `beehave status --json` for project-wide overview per [[software-craft/test-stubs#concepts]]. For each feature, determine delivery status from its stage:
   - Any stage other than `ok` → feature is incomplete.
   - Stage `ok` → all Examples have implemented tests with no structural violations, but functional correctness must still be verified.
   For features at `ok` stage, run `task test-fast` scoped to that feature's test directory:
   - Any failures → feature is incomplete.
   - All pass → feature is delivered (skip).

4. IF every feature is delivered → exit via `no-features`.
5. Collect all incomplete features. Derive dependency count for each from `domain_spec.md` context map:
   - Count how many other incomplete features this feature depends on (via integration points and entity relationships in the context map).
   - Filter: select features with the **lowest dependency count** first (0 = no dependencies).
6. IF only one feature has the lowest dependency count → select it. Skip to step 8.
7. IF multiple features tie on dependency count → score each tied feature per [[requirements/wsjf#key-takeaways]]:
   - Estimate Value (1-5, mapped to Kano categories) and Effort (1-5, mapped to complexity).
   - Compute WSJF = Value / Effort.
   - Select the highest WSJF score; ties broken by Value.
8. Set the `feature_title` session param to the selected feature's filename stem (without `.feature` extension).
