---
name: structure-feature
description: "Create feature branch and package structure from design artifacts"
---

# Structure Feature

Available knowledge: [[software-craft/source-stubs#concepts]], [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: read all before starting work.

1. Sync local main with remote: `git fetch origin && git checkout main && git merge --ff-only origin/main`. Create feature branch per [[software-craft/git-conventions#content]]: `feat/<stem>` from updated main. `out: git_branch` is a Runtime artifact — the output of this step IS the branch creation, not a file on disk.
2. Create package structure per [[software-craft/source-stubs#concepts]] and [[architecture/technical-design#key-takeaways]].
