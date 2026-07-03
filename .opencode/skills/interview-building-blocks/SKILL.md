---
name: interview-building-blocks
description: "Funnel level 3 — identify building-block names and rough boundaries only, and run gap analysis."
---

# Interview (Building Blocks)

1. Load [[requirements/domain-decomposition]], [[requirements/aggregate-boundaries]], [[architecture/quality-attributes]] — gap analysis, boundary sizing, and the quality-attribute taxonomy the coverage check runs over. This level is structural decomposition, not CIT/Laddering elicitation (those served levels 1–2).
2. Read the running interview-notes; append the building-block names and boundaries to it.
3. Capture building-block NAMES and rough boundaries ONLY — no detailed spec (rules, examples, criteria come later in planning). The purpose is to know WHAT building blocks exist, not to specify each.
4. Run gap analysis: IF a bounded context from cross-cutting maps to no block THEN flag the gap; IF a quality attribute maps to no block THEN flag the gap. Do not silently fill gaps per [[requirements/domain-decomposition]], [[requirements/aggregate-boundaries]].
