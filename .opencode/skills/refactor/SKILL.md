---
name: refactor
description: "Improve code structure while keeping all tests passing, then cycle to the next example or exit"
---

# Refactor

Available knowledge: [[software-craft/tdd]], [[software-craft/refactoring]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]], [[software-craft/refactoring-techniques]], [[software-craft/solid]], [[software-craft/design-patterns]]. `in` artifacts: read all before starting work. 

1. Review the code for improvement opportunities while keeping all tests passing per [[software-craft/tdd#concepts]].
2. Refactor only if there is a test that would break if the refactoring is wrong per [[software-craft/tdd#key-takeaways]].
3. Apply small steps: one refactoring at a time, tests green after each step, no new functionality per [[software-craft/refactoring#key-takeaways]]. Do not add docstrings to test functions, classes, or helpers. Tests document themselves via function names and AAA structure.
4. Apply design-only transformations per [[software-craft/tdd#concepts]]: YAGNI > KISS > DRY > ObjCal > Smells > SOLID > patterns. Do not apply convention compliance (docstrings, type hints, import ordering, format changes). Those belong in the Conventions Phase.
5. Detect improvement opportunities per the full design principle priority in [[software-craft/tdd#content]]: YAGNI per [[software-craft/tdd#concepts]], KISS per [[software-craft/tdd#concepts]], DRY per [[software-craft/tdd#concepts]], ObjCal per [[software-craft/object-calisthenics#key-takeaways]], smells per [[software-craft/smell-catalogue#key-takeaways]], SOLID per [[software-craft/solid#key-takeaways]], patterns per [[software-craft/design-patterns#key-takeaways]]. Apply the appropriate refactoring technique per [[software-craft/refactoring-techniques#concepts]].
6. IF no improvement is needed → skip refactoring and proceed to the next test.
7. IF a spec gap or inconsistency is discovered during refactoring → do NOT modify specification documents (domain_spec.md, glossary.md, product_definition.md, ADRs, feature files). Flag it in output notes. The SE may ONLY modify production code and test code.
8. Commit refactor changes separately from feature changes per [[software-craft/git-conventions#concepts]].
9. Run `beehave check` per [[software-craft/test-stubs#concepts]] to confirm traceability intact, then `task test-fast` to confirm all tests remain green after refactoring.
10. Run `beehave status --json` per [[software-craft/test-stubs#concepts]]. Report the result in output: IF any scenario has `status: "stub"` → report `"next-example"` (loop continues). IF all scenarios have `status: "implemented"` with no violations → report `"all-examples-pass"` (loop exits). The orchestrator uses this to choose the correct transition.
