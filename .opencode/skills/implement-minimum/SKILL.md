---
name: implement-minimum
description: "Write the minimum production code needed to make the failing test pass"
---

# Implement Minimum

Available knowledge: [[software-craft/tdd]], [[software-craft/test-design]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]]. `in` artifacts: read all before starting work.

1. Write the minimum code to make the failing test pass AND satisfy reviewer checks per [[software-craft/tdd#key-takeaways]]. Add docstrings, type hints, and lint compliance only when reviewers require them, not proactively. Fix any existing test failures or beehave violations in files you touch. Never use `noqa` — find and fix the root cause. Never change `pyproject.toml`.
2. IF a spec gap or inconsistency is discovered during implementation → do NOT modify specification documents (domain_spec.md, glossary.md, product_definition.md, ADRs, feature files). These are owned by other flow states. Flag the gap in output notes. The SE may ONLY modify production code and test code.
3. Run `task test-fast` to confirm the test passes (GREEN).
