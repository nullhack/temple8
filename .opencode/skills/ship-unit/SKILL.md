---
name: ship-unit
description: "Commit the built unit as one logical change with a descriptive imperative message."
---

# Ship Unit

1. Load [[software-craft/git-conventions]] — imperative message form and the one-logical-change rule.
2. Commit the unit as one logical change: the implemented source .py plus any structural artifacts (migrations, fixtures, cassettes) it required.
3. Write a descriptive imperative message per [[software-craft/git-conventions]].
4. Keep the .pyi unchanged from plan — contracts are fixed during build.
