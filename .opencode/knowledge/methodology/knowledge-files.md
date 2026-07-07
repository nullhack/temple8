---
domain: methodology
tags: [knowledge, wikilinks, diataxis, progressive-disclosure, depth, research]
last-updated: 2026-07-01
---

# Knowledge Files

## Key Takeaways

- Knowledge holds reference and explanation only — the what and why; procedure lives in skills, identity in agents, routing in the flow (see [[methodology/separation-of-concerns#concepts]]).
- Every knowledge file uses four ordered sections — Key Takeaways, Concepts, Content, Related — with strict correspondence: bullet N maps to paragraph N maps to subsection N.
- Depth deepens across the sections: Key Takeaways state the principle, Concepts give the reasoning, Content teaches the topic to a competent reader — Content is never thinner than Concepts.
- Cite knowledge with `[[domain/concept]]` or `[[domain/concept#section]]`; the fragment selects how much to extract, saving up to ~80% of the tokens.
- One concept per file, ~150 lines maximum; split rather than grow.
- Knowledge is grounded in real sources — research the topic (the canonical book or framework, academic work, Wikipedia) and cite it inline; inaccurate knowledge is worse than none.
- The knowledge graph is just the wikilinks in each file's Related section — no separate edge store.

## Concepts

**Reference and explanation only.** Knowledge answers what and why: definitions, criteria, the reasoning behind a rule. It never answers how (that is a skill) or who (that is an agent). Mixing procedure into knowledge splits the procedure across two load points and the model cannot tell which is authoritative.

**Correspondence.** The four sections are ordered by depth, and the depth is also structure: bullet N in Key Takeaways expands to paragraph N in Concepts and to subsection N in Content. A reader who jumps from a takeaway to its detail must land on the matching concept. Breaking correspondence strands the reader at the wrong depth.

**Depth deepens progressively.** Each tier does a different job. Key Takeaways is austere reference — the firm principle, scannable, consulted rather than read (Diátaxis, Procida). Concepts is explanation — the reasoning that turns a rule into understanding. Content is the learning tier — it teaches the topic, expanding each concept with the source's actual mechanism and using tables, criteria, and examples so a reader can recognise an instance and tell it from its neighbours. Content that merely restates Concepts in more words has failed: it must be deeper, never thinner. Across all tiers, scrub AI language markers — the prose form of the same parsimony — per [[writing/ai-language-markers]].

**Wikilink routing.** Skills are the authority on when to load knowledge; the wikilink is the address. A fragment selects the cut: `#key-takeaways` loads frontmatter and Key Takeaways; `#concepts` loads through Concepts; no fragment loads the whole file. Extraction is cumulative and cuts from the top.

**Size and attention.** Files past ~150 lines lose attention to their middles. Split a long file into siblings under the same domain and cross-link them. A small file whose rule fits in bullets and concepts omits Content entirely.

**Grounding and accuracy.** Agents load knowledge on demand and treat it as authoritative, so a plausible-sounding error misleads every downstream step — arc42 (Starke) states the stakes plainly: wrong documentation is often worse than none, because it misleads with confidence. Author knowledge by researching the topic first — the canonical book or framework, academic papers, Wikipedia — and cite sources inline. Prefer primary sources (the book, the paper, the framework's own site) over secondary restatements, and cross-check a load-bearing claim against a second source when the stakes are high.

**The graph is emergent.** Each file's Related section lists its neighbours. The graph is the union of those links — no separate edge file. To validate, extract every `[[...]]` and confirm the target file exists and any fragment names a real section.

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

### Depth across the four sections

Each tier serves a different reader need, and the depth must actually increase — a reader who descends from Key Takeaways to Content must receive more, not less.

| Tier | Job | Reader state | Form |
|---|---|---|---|
| Key Takeaways | state the principle | recalls it in passing | austere bullets, one per concept, imperative |
| Concepts | explain the reasoning | understands without detail | one paragraph per bullet, the why |
| Content | teach the topic | applies it, spots violations | each concept expanded with the source's mechanism; tables, criteria, examples |

Key Takeaways is austere reference, after Diátaxis (Procida): "one hardly reads reference material; one consults it." Keep it to the firm principle a reader can stand on — no padding, no hedging. Microsoft's style guide echoes the same: reference must be consistent and unambiguous because developers rely on it as a firm platform. Concepts turns the principle into understanding: the reasoning, the why, the edge that makes the rule non-obvious. Content is the learning tier — where a competent reader who does not yet know this topic comes to grasp it. Expand each concept with the source's actual mechanism (not a paraphrase of it), and reach for a table, a criterion, or a worked example wherever it helps the reader recognise an instance or separate look-alikes. Williams's guidance for reference holds here: include examples everywhere — terse and direct, illustrating the thing itself.

The failure mode is Content thinner than Concepts. If the deepest tier restates the middle tier in more words, the reader descends and learns nothing — expand the Content, or the concept does not deserve its own file. The guardrail runs the other way too: set a manageable scope (Williams — prioritise breadth over depth, with in-depth treatment reserved for the topics that matter) and stop when the concept is grasped. Padding erodes the attention that austere reference earns; arc42's "leave out irrelevant facts" is an explicit decision, not a default.

### Grounding and research

Agents load knowledge on demand and treat it as authoritative — there is no human in the loop to catch a plausible error before it steers a build step. arc42 (Starke) states the stakes plainly: wrong documentation is often worse than none, because it misleads with confidence. Author knowledge by researching the topic first, not by writing what seems right.

1. **Start at the canonical source** — the book or framework the topic sits inside (Evans 2003 for domain-driven design; Diátaxis for documentation structure; the paper that introduced the technique). The canonical source is where the terms, mechanisms, and boundaries were fixed; secondary restatements quietly drop precision. As Divio's reference guide puts it, the only job is to describe "as clearly and completely as possible", and completeness is measured against the machinery, not against intuition.
2. **Corroborate and broaden** — academic or practitioner papers, and Wikipedia for a neutral overview and its cross-references. Wikipedia is strongest for breadth and for surfacing adjacent concepts and the history of an idea; treat it as a map to primary sources, not the destination.
3. **Cite inline (author, year)** at the point of claim, so a reader can verify or go deeper. Prefer the primary citation over a chain of "as cited in".
4. **Cross-check** any load-bearing claim against a second source; if two sources disagree, name the disagreement rather than papering over it.
5. **Reuse the curated research** under `.backup/docs/research/` where it exists — each file records source type, method, verification status, and confidence. Add new research files there for topics not yet covered, so the grounding accumulates rather than evaporating.

A knowledge file is a claim about the world, not a note to self. Grounding it in cited sources is what lets the austere "consult it, don't read it" contract hold.

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
- [[writing/ai-language-markers]]
