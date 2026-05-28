# PM_20260501_missing-feature-test-template: Missing feature test stub template

## Failed At

project-structuring. SA: "SA generated test stubs without a template to follow, using `...` ellipsis bodies and carrying MoSCoW tags into docstrings"

## Root Cause

The `.templates/` directory had no template for feature BDD test stubs. The `structure-project` skill referenced design artifacts and `@id` traceability but provided no concrete stub format, so the agent fell back to `...` bodies and imported MoSCoW classification into docstrings.

## Missed Gate

The `stubs_traceable` condition checks that all `@id` tags have corresponding test stubs, but doesn't validate stub format (skip decorator, docstring content, naming convention).

## Fix

1. Added test stub template at `.templates/tests/features/<rule_slug>_test.py.template` with `@pytest.mark.skip(reason="not yet implemented")`, `test_<feature_stem>_<id>` naming, and Gherkin-step docstrings.
2. Updated `stub-design.md` knowledge file with explicit stub format requirements: skip decorator (never `...`), naming convention, no MoSCoW tags in docstrings.
3. Updated `structure-project` SKILL.md step 4 to reference the template and prohibit MoSCoW tags and `...` bodies.
4. Updated `feature.feature.template` to note that `@id` tags are for traceability only, not priority classification.
5. Updated `moscow.md` and `write-bdd-features` SKILL.md to clarify MoSCoW is internal triage only: must NOT appear as Gherkin tags or in .feature files.

## Restart Check

SA verifies that all test stubs use `@pytest.mark.skip(reason="not yet implemented")`, have no MoSCoW tags in docstrings, and follow the `test_<feature_stem>_<id>` naming convention.