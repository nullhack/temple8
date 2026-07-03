---
name: consolidate-interview
description: "End of session — replace running notes with the full synthesis across all three funnel levels and author the glossary of ubiquitous language."
---

# Consolidate Interview

1. Load [[requirements/ubiquitous-language]] — term extraction for the glossary. This level synthesises (Active Listening L3, applied in step 3); it does not probe.
2. Read the running interview-notes across all three levels.
3. Apply Active Listening L3: replace the running notes with the full synthesis across all three funnel levels and present it to the stakeholder for approval. The summary reflects what the stakeholder said — no new framing or topic labels.
4. Render `docs/glossary.md` from `.templates/docs/glossary.md.template` (substitute `<project-name>`): one `## Context: <bounded-context>` section per context, one `### <Term>` entry per term in the template's format (`A <category> that <distinguishing characteristic>.` + `*Aliases: … · Source: …*`), from the stakeholder's own terms, so it leads all subsequent naming per [[requirements/ubiquitous-language]].
5. Exit interview-ready when the stakeholder approves; re-enter the funnel at general whenever plan or build finds the elicitation itself was insufficient.
