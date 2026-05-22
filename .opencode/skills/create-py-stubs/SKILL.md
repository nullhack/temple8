---
name: create-py-stubs
description: "Create minimum typed source stubs as domain spec breadcrumbs, generate test stubs via pytest-beehave, then verify all planning artifacts are complete for baseline"
---

# Create Python Stubs

Available knowledge: [[architecture/technical-design]], [[software-craft/source-stubs]], [[software-craft/test-stubs]], [[software-craft/tdd]], [[requirements/decomposition#key-takeaways]]. `in` artifacts: read all before starting work.

1. Read the feature file and identify the domain entities, value objects, and use cases referenced by the Examples and Scenario Outlines.
2. For each referenced entity/value object/use case not yet implemented, create a minimal typed stub per [[software-craft/source-stubs#concepts]]: Protocol method signatures with `raise NotImplementedError` bodies, no docstrings, no type hints beyond the contract. These stubs are breadcrumbs from the domain spec. The SE can add, remove, or modify them during implementation.
3. Run `beehave generate <feature_title>` to generate test stubs from the feature file per [[software-craft/test-stubs#concepts]]:
   - Plain Examples → bare function stubs with `...` body
   - Scenario Outlines → `@given` decorated stubs with inferred Hypothesis strategies + `@example` decorators for each Examples table row
   - Placeholder names become function parameters; strategy is inferred from Examples table column types
4. Run `beehave check` and resolve violations per [[software-craft/test-stubs#concepts]].
5. Verify decomposition per [[requirements/decomposition#key-takeaways]]: no Rule spans >1 bounded context, no Rule has >8 Must behaviors after MoSCoW triage and Scenario Outline collapse.
6. Verify all planning artifacts are present and consistent: feature file, product definition, domain spec, glossary.
7. Commit all changes to the feature branch per [[software-craft/git-conventions#content]].
