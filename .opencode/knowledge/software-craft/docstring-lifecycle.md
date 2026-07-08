---
domain: software-craft
tags: [docstrings, lint, lifecycle]
last-updated: 2026-07-08
---

# Docstring and Lint Lifecycle

## Key Takeaways

- Source `.py` is kept **docstring-free** during dev; docstrings are **generated** at merge from stable code, then stripped. Source only — never tests (the body is the spec) or stubs (`PYI021`).
- Lint splits: **bug-catchers run throughout** — the dev `ruff` select is `A ASYNC B C9 DTZ ERA F G LOG PYI S`; restructure (`SIM`, `RUF`) and `ruff format` run at merge via `task lint-merge`.
- ruff cannot ban a docstring's *presence* in `.py` (no rule flags it; `PYI021` is `.pyi`-only); `scripts/strip_docstrings.py` is the mechanical substitute.

## Related

- [[software-craft/tdd]] — the cycle runs on docstring-free code
- [[software-craft/git-conventions]] — the merge at which docstrings regenerate
