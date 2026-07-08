---
name: merge-to-dev
description: "Squash-merge the feature commits into dev, regenerate docstrings, and verify the whole suite plus whole-suite stubtest are clean."
---

# Merge To Dev

1. Load [[software-craft/git-conventions]], [[software-craft/docstring-lifecycle]] — squash-merge form and the docstring lifecycle.
2. Switch to dev and squash-merge the feature branch (`feature/<session_id>`) per [[software-craft/git-conventions]]; the green-suite and whole-suite stubtest gate is verified on dev after the merge. Delete the merged branch (`git branch -d feature/<session_id>`) — no dangling branches.
3. Verify the full suite is green on dev after the merge: no pending markers remain (every source .pyi has its sibling .py, so every test runs) and every test passes.
4. Verify whole-suite stubtest is clean across both source and tests: every source .pyi and every test .pyi agrees with its sibling .py — no drift smuggled in by the batch.
5. Regenerate docstrings for the public surface of every contract shipped this cycle (modules, classes, public functions and methods) — faithful prose from the stable code, never a mechanical restatement of the signature; the *why* of an architectural decision lives in an ADR, not a docstring. Per [[software-craft/docstring-lifecycle]].
6. Run `task lint-merge` — adds `SIM` and `RUF` to the dev select and runs `ruff format .` — so restructure and format land on dev exactly once per merge, never during build.
7. Commit the regenerated docstrings and the format pass on dev as `docs(<scope>): regenerate docstrings + format`.
