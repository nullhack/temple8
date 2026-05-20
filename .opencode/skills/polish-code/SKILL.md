---
name: polish-code
description: "Apply full project conventions — naming, docstrings, formatting, type annotations — after feature acceptance"
---

# Polish Code

Available knowledge: [[software-craft/tdd#key-takeaways]], [[writing/ai-language-markers#key-takeaways]]. `in` artifacts: read all before starting work.

1. Run `task conventions` to see all convention violations (naming, docstrings, formatting, import sorting, etc.).
2. Fix **all** violations codebase-wide, not just those introduced in the current feature. Resolve each at its source; do not suppress with `noqa`. Do NOT use `--fix` (it can break code).
3. Run `ruff format .` to apply consistent formatting.
4. Add Google-style docstrings to all public classes and methods where missing.
5. Add type annotations to all public signatures where missing.
6. Run `task static-check` and fix any pyright errors.
7. Run `task test` to verify nothing broke.
8. IF `task test` shows coverage failure → run `task test-build` to see missing lines, then add coverage tests in `tests/unit/`.
9. Scan docstrings, comments, and user-facing strings for AI language markers per [[writing/ai-language-markers#key-takeaways]]. Rewrite any flagged text in natural, direct style.
10. Commit to the feature branch per [[software-craft/git-conventions#content]].
