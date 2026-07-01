---
domain: methodology
tags: [knowledge, wikilinks, diataxis, progressive-disclosure]
last-updated: 2026-07-01
---

# Knowledge Files

## Key Takeaways

- Knowledge holds reference and explanation only — the what and why; procedure lives in skills, identity in agents, routing in the flow (see [[methodology/separation-of-concerns#concepts]]).
- Every knowledge file uses four ordered sections — Key Takeaways, Concepts, Content, Related — with strict correspondence: bullet N maps to paragraph N maps to subsection N.
- Cite knowledge with `[[domain/concept]]` or `[[domain/concept#section]]`; the fragment selects how much to extract, saving up to ~80% of the tokens.
- One concept per file, ~150 lines maximum; small focused files may omit Content.
- The knowledge graph is just the wikilinks in each file's Related section — no separate edge store.

## Concepts

**Reference and explanation only.** Knowledge answers what and why: definitions, criteria, the reasoning behind a rule. It never answers how (that is a skill) or who (that is an agent). Mixing procedure into knowledge splits the procedure across two load points and the model cannot tell which is authoritative.

**Progressive disclosure.** A reader rarely needs a whole file. The four sections are ordered by depth, so a wikilink fragment can stop early: Key Takeaways for a one-line reminder, through Concepts for understanding, to Content for the full reference. Each tier is self-sufficient at its depth.

**Correspondence.** Bullet N in Key Takeaways expands to paragraph N in Concepts and to subsection N in Content. A reader who jumps from a takeaway to its detail must land on the matching concept. Breaking correspondence strands the reader at the wrong depth.

**Wikilink routing.** Skills are the authority on when to load knowledge; the wikilink is the address. A fragment selects the cut: `#key-takeaways` loads frontmatter and Key Takeaways; `#concepts` loads through Concepts; no fragment loads the whole file. Extraction is cumulative and cuts from the top.

**Size and attention.** Files past ~150 lines lose attention to their middles. Split a long file into siblings under the same domain and cross-link them. A small file whose rule fits in bullets and concepts omits Content entirely.

**Domains organise concepts.** `.opencode/knowledge/` is grouped by domain (`methodology/`, and later `requirements/`, `software-craft/`, `workflow/`, …). A domain is a topic area that holds one or more concept files; one concept per file lets a wikilink load exactly that concept. Deep topic areas may nest subdirectories.

## Content

### Knowledge file format

```markdown
---
domain: <domain-name>
tags: [<tag>, <tag>]
last-updated: <YYYY-MM-DD>
---

# <Title>

## Key Takeaways

- <one bullet per concept; imperative mood>

## Concepts

<one paragraph per bullet, same order and grouping>

## Content

<Reference and explanation only. Self-contained — readable without the linked
files. Subsections correspond 1:1 (or N:1) to the Key Takeaway bullets. Omit
this section entirely when bullets and concepts are enough.>

## Related

- [[domain/other-concept]]
```

### Format rules

1. One concept per file.
2. ~150 lines maximum; split rather than grow.
3. Self-contained — understandable without reading the linked files.
4. Key Takeaways first; one bullet per concept, imperative mood, scannable.
5. Concepts expand the bullets one-for-one, same order.
6. Correspondence: bullet N ↔ paragraph N ↔ Content subsection N.
7. No procedure — how-to belongs in skills.
8. Frontmatter carries `domain`, `tags`, `last-updated` for search and filtering.

### Wikilink convention

`[[domain/concept]]` resolves to `.opencode/knowledge/{domain}/{concept}.md`. A `#section` fragment (lowercase, hyphenated) selects cumulative extraction from the top:

| Fragment | Loads | Use |
|---|---|---|
| `#key-takeaways` | frontmatter + Key Takeaways | recall a principle |
| `#concepts` | through Concepts | understand without detail |
| (none) | the whole file | apply criteria, find violations |

Wikilinks appear in skills, knowledge, and agents. They do not appear in the always-loaded `AGENTS.md` except to document the convention itself.

A wikilink may be a **forward reference** during staged authoring — a skill can cite knowledge not yet written. A dangling link is debt to resolve (track it), not an error; it resolves the moment the cited file is authored.

### The graph is emergent

Each file's Related section lists its neighbours. The graph is the union of those links — no separate edge file. To validate, extract every `[[...]]` and confirm the target file exists and any fragment names a real section.

## Related

- [[methodology/separation-of-concerns]]
- [[methodology/agent-files]]
- [[methodology/skill-files]]
