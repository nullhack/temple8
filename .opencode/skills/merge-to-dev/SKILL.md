---
name: merge-to-dev
description: "Squash-merge the feature commits into dev and verify the whole suite plus whole-suite stubtest are clean."
---

# Merge To Dev

1. Load [[software-craft/git-conventions]] — squash-merge form.
2. Switch to dev and squash-merge the feature commits per [[software-craft/git-conventions]]; the green-suite and whole-suite stubtest gate is verified on dev after the merge.
3. Verify the full suite is green on dev after the merge: no pending markers remain (every source .pyi has its sibling .py, so every test runs) and every test passes.
4. Verify whole-suite stubtest is clean across both source and tests: every source .pyi and every test .pyi agrees with its sibling .py — no drift smuggled in by the batch.
