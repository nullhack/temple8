---
name: interview-features
description: "Funnel level 3 — identify feature names and rough boundaries only, and run gap analysis."
---

# Interview (Features)

1. Load [[requirements/feature-discovery]], [[requirements/feature-boundaries]] — gap analysis and boundary sizing. This level is structural decomposition, not CIT/Laddering elicitation (those served levels 1–2).
2. Read the running interview-notes; append the feature names and boundaries to it.
3. Capture feature NAMES and rough boundaries ONLY — no detailed spec (rules, examples, criteria come later in planning). The purpose is to know WHAT features exist, not to specify each.
4. Run gap analysis: IF a bounded context from cross-cutting maps to no feature THEN flag the gap; IF a quality attribute maps to no feature THEN flag the gap. Do not silently fill gaps per [[requirements/feature-discovery]], [[requirements/feature-boundaries]].
5. Continue Active Listening L2 between features.
