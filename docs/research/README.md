# Research

A human-reference library of the sources cited (author, year) across the
`.opencode/knowledge/` files. Each entry is a short card with the full
citation, a URL where one exists, and a summary of the source's contribution.

## Purpose

This folder is for **human reference only**. No flow step and no skill loads
it. It is consulted during knowledge authoring, when an author writing or
revising a knowledge file needs to confirm what a `Author, Year` citation
refers to, or to recover the source's mechanism before deepening Content.

## Taxonomy

Mirrors the source disciplines, with only the sub-domains that hold cited
sources kept:

- `psychology/{social,cognitive}/` — the interview and review techniques.
- `software-engineering/{quality,process,requirements}/` — the craft sources.
- `information-science/{domain-modeling,documentation}/` — the modelling and
  documentation sources.

## Card template

- Skeleton: `.templates/docs/research/card.md.template` (copy, name `<author>_<year>.md`, file under the matching discipline).
- Authoring standard: `.opencode/knowledge/methodology/research-files.md` — the card's purpose, the verify-never-recall rule, and the no-fabrication rule.

Each file follows:

`# Title (Author, Year)` / `## Citation` (full bibliographic + `URL:`) /
`## Method` / `## Confidence` / `## Key Insight` / `## Core Findings` /
`## Mechanism` / `## Relevance` / `## Related Research`.

A source without an offline copy carries a stub card with whatever is known
and an explicit "unverified" note; it is never fabricated.
