---
name: refactor-green
description: "Improve the source structure under green tests, with the .pyi fixed and the tests untouched."
---

# Refactor Green

1. Load [[software-craft/refactoring-techniques]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]] — the refactoring moves, smell taxonomy, and quality criteria.
2. Improve the source structure while tests stay green. The source .py is fluid; the .pyi is fixed; tests are fixed contracts — do not edit them.
3. IF a smell is present THEN remove it using the catalogue and a matching technique per [[software-craft/smell-catalogue]], [[software-craft/refactoring-techniques]]. Apply SOLID, DRY, KISS, YAGNI, Object Calisthenics per [[software-craft/solid]], [[software-craft/object-calisthenics]].
4. Keep the .py consistent with its sibling .pyi so stubtest stays clean. IF a change requires editing the .pyi THEN stop — a contract change is escalated at review.
5. Read the target's .pyi first; touch the .py only where the stub omits needed detail. Loop until the structure is clean.
