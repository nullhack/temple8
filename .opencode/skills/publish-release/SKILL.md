---
name: publish-release
description: "Publish the delivered batch as release notes, a PR to main, or a tagged release."
---

# Publish Release

1. Load [[software-craft/versioning]], [[software-craft/git-conventions]] — release/tag policy and git form.
2. This step fires only on stakeholder approval (the `approved` transition from merge); if publication is declined, deliver skips straight to refresh. Publish the batch per the project's release policy: release notes, a PR to main, or a tagged release per [[software-craft/versioning]], [[software-craft/git-conventions]].
