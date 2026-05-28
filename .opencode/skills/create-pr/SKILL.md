---
name: create-pr
description: "Push local dev to remote and create an administrative PR for changes already merged"
---

# Create PR

Available knowledge: [[software-craft/git-conventions#key-takeaways]]. `in` artifacts: read all before starting work.

1. Push local dev to remote: `git push origin dev`.
2. Create a pull request (dev → main) with the squashed commit format from [[software-craft/git-conventions#content]], including traceability to Example titles for all acceptance criteria.
3. IF the PR is approved → write results to output artifacts, advance to next state.
4. IF changes are requested → address feedback on a fix branch per [[software-craft/git-conventions#concepts]], then re-push and update the PR.
5. IF the PR is cancelled → write results to output artifacts, route to post-mortem.
6. After PR is merged to main on remote: sync local branches for next cycle.
   - `git fetch origin`
   - `git checkout main && git merge --ff-only origin/main`
   - `git checkout dev && git reset --hard origin/main`
   - This prevents history divergence on the next dev → main PR.
