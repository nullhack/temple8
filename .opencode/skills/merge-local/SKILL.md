---
name: merge-local
description: "Squash-merge feature commits into local dev branch, pull remote dev, and resolve conflicts"
---

# Merge Local

Available knowledge: [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: read all before starting work.

1. Sync local main with remote: `git fetch origin && git checkout main && git merge --ff-only origin/main`.
2. Sync local dev with main (handles post-PR divergence): `git checkout dev && git reset --hard origin/main`. IF origin/main does not exist yet (first feature), pull remote dev instead: `git merge --ff-only origin/dev`.
3. Pull latest remote dev for safety: `git merge --ff-only origin/dev`. IF this fails (dev diverged from remote dev), reset to origin/main per step 2 and proceed.
4. IF the feature branch needs updates from dev, rebase the feature branch on dev before squash-merging.
5. Squash all feature commits into a single commit per [[software-craft/git-conventions#concepts]].
6. Merge the squashed commit into local dev.
7. Run feature-type verification per [[software-craft/git-conventions#content]].
8. Run `uv run task test-fast` to verify all tests pass on local dev.
9. Delete the feature branch: `git branch -d <feature-branch>`. IF the branch has unmerged work (check `git log dev..<feature-branch>`), abort and report.
10. IF conflicts arise during rebase or merge:
    - IF the conflict is a straightforward text merge → resolve and continue.
    - IF the conflict requires a design decision → present options to the stakeholder with consequences before resolving.
