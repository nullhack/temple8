---
name: interview-building-blocks
description: "Funnel level 3 — identify building-block names and rough boundaries only, and run gap analysis."
---

# Interview (Building Blocks)

1. Load [[requirements/domain-decomposition]], [[requirements/aggregate-boundaries]], [[architecture/quality-attributes]], [[methodology/simplicity-discipline]] — gap analysis, boundary sizing, the quality-attribute taxonomy the coverage check runs over, and the simplicity discipline. This level is structural decomposition, not CIT/Laddering elicitation (those served levels 1–2).
2. Read the running interview-notes; append the building-block names and boundaries to it.
3. Capture building-block NAMES and rough boundaries ONLY — no detailed spec (rules, examples, criteria come later in planning). The purpose is to know WHAT building blocks exist, not to specify each.
4. Ask the simplicity question for each block: "Is this building block load-bearing, or could it collapse into a neighbour?" A block with no unique responsibility a cited need requires is speculative per [[methodology/simplicity-discipline]] — flag it for collapse into a neighbour or drop at consolidation. A block the cited need requires but no current block covers is a gap, flagged here (not silently filled).
5. Flag rework: IF a finding implies MODIFYING an existing block's behaviour (not adding a new one) THEN mark that block in the decomposition table as `rework — modifies existing <block>` and record the stakeholder's CIT-grounded reason. This is a requirements-level observation only — discovery does not touch tests. Plan reads these flags at `author-test-stubs` and marks the matching existing tests `@pytest.mark.pending` so the build backlog picks them up as rework per [[software-craft/tdd]]. A finding with no such flag is new work.
6. Run gap analysis: IF a bounded context from cross-cutting maps to no block THEN flag the gap; IF a quality attribute maps to no block THEN flag the gap. Do not silently fill gaps per [[requirements/domain-decomposition]], [[requirements/aggregate-boundaries]].
