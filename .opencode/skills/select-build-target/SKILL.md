---
name: select-build-target
description: "Pull the next source contract to build from the pending backlog, respecting outside-in dependency order."
---

# Select Build Target

1. Load [[software-craft/tdd]], [[software-craft/docstring-lifecycle]] — the cycle and the naked-source rule.
2. Discover the backlog: collect tests carrying the pending marker (`uv run pytest --collect-only -m pending -q`). Map each pending test to the source module it exercises.
3. Pick the lowest-layer contract that still has pending tests — layer order is dependency order, so a module is built only after the modules it imports are built.
4. IF a shared or foundation module (shared data types with no dedicated external-boundary test of its own) is needed THEN pull it in and build it alongside the first contract that depends on it; record both.
5. Treat the pending marker — not the presence of the source .py — as what makes a contract selectable: a reworked contract re-enters the queue even when its .py already exists. IF no pending tests remain anywhere THEN the system is built.
6. Strip the target source .py at cycle entry: IF the target module's .py already exists (rework) THEN run `uv run python scripts/strip_docstrings.py <package>/<module>.py` to remove the docstrings carried over from the last merge — source .py stays naked across red/green/refactor/review/ship per [[software-craft/docstring-lifecycle]]. Skip if the .py is absent (new contract).
7. Skim the target's .pyi and its tests for context, not the whole project.
