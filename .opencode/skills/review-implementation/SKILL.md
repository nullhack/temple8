---
name: review-implementation
description: "Gate the implementation against its contract for correctness, quality, drift, and green tests."
---

# Review Implementation

1. Load [[software-craft/code-review]], [[software-craft/solid]], [[software-craft/smell-catalogue]], [[software-craft/design-patterns]] — review method, quality criteria, smell taxonomy, and the pattern catalog.
2. Review the implemented source against its contract per [[software-craft/code-review]].
3. Check impl-matches-contract: the .py satisfies its .pyi and the requirement, without excess.
4. Check source-quality-clean: IF SOLID, DRY, KISS, YAGNI, Object Calisthenics are violated OR a smell is present THEN reject per [[software-craft/solid]], [[software-craft/smell-catalogue]].
5. Check stubtest-clean: the source .py and its sibling .pyi agree, AND the target's test .py and its sibling .pyi agree — no drift on either pair.
6. Check tests-green: the target's tests pass and no previously-green test regressed.
7. Read the target's .pyi first; open the .py only for the spots under review.
8. IF review reveals the contract itself is the problem — not the implementation — THEN append the finding to `.cache/<session_id>/journal.md` (contract, the gap, the evidence) and fire `reveals-gap`. This routes back to plan, not changes-needed.
