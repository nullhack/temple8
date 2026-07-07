---
name: consolidate-interview
description: "End of session — replace running notes with the full synthesis across all three funnel levels and author the glossary of ubiquitous language."
---

# Consolidate Interview

1. Load [[requirements/ubiquitous-language]], [[methodology/simplicity-discipline]] — term extraction for the glossary and the simplicity discipline that enforces the drop at consolidation. This level synthesises (Active Listening L3, applied in step 3); it does not probe.
2. Read the running interview-notes across all three levels.
3. Apply Active Listening L3: replace the running notes with the full synthesis across all three funnel levels and present it to the stakeholder for approval. The summary reflects what the stakeholder said — no new framing or topic labels.
4. Drop speculative items per [[methodology/simplicity-discipline]]: every behaviour group, building block, quality attribute, and field surfaced at any funnel level is either grounded in a cited stakeholder need (a CIT incident, a laddered constraint, a named access pattern) or removed from the synthesis before approval. An item with no cited grounding does not reach the contracts — the contracts are the smallest surface that serves the cited needs, neither over- nor under-engineered. Flag each drop in the synthesis so the stakeholder can object; an unchallenged drop is final.
5. Render `docs/glossary.md` from `.templates/docs/glossary.md.template` (substitute `<project-name>`): one `## Context: <bounded-context>` section per context, one `### <Term>` entry per term in the template's format (`A <category> that <distinguishing characteristic>.` + `*Aliases: … · Source: …*`), from the stakeholder's own terms, so it leads all subsequent naming per [[requirements/ubiquitous-language]].
6. Exit interview-ready when the stakeholder approves; re-enter the funnel at general whenever plan or build finds the elicitation itself was insufficient.
