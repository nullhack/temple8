---
domain: methodology
tags: [agents, identity, subagents, navigation]
last-updated: 2026-07-01
---

# Agent Files

## Key Takeaways

- An agent file is a focused identity **portrait** — the role's lens, what it holds, what it alone decides, and what it refuses; everything surrounding the work lives in the flow (see [[methodology/separation-of-concerns#concepts]]).
- Write enough identity to genuinely set the role's headspace — its professional lens and guardrails — but never restate what the flow, a skill, or knowledge already carries; a copy drifts.
- Never put skills, artifacts, transitions, gates, or procedure in an agent file — the flow already owns them, and a copy drifts.
- `/AGENTS.md` (root) is navigation, not identity: it tells a session where things live and how to discover them, never a file inventory.
- Route read-heavy investigation to a subagent with read-only scope; it quarantines token cost and suppresses anchoring bias.

## Concepts

**Identity, rich; duplication, none.** The agent file defines who the role is — its lens on the work, the principles it holds, the decisions it alone may make, and the anti-patterns it refuses. That portrait should be rich enough that, loaded alone, it puts the reader into the professional's headspace. What it must NOT contain is the rest of the work: skills, artifact paths, transitions, gate conditions, domain facts, step-by-step procedure. Those belong to the flow, skills, and knowledge. The day the flow changes and the agent restates it, a stale copy in the agent wins attention and the agent improvises against the wrong contract. Write identity until the role is set; write no further.

**Two "agents" files, different jobs.** `/AGENTS.md` is the project-root navigation file, loaded every session: it says where the methodology layer lives and how to discover it. `.opencode/agents/{role}.md` is an identity file, loaded only when the role is dispatched. The similar names are coincidence — one tells the session where to find things, the other tells the role who it is.

**Discover, do not enumerate.** A file loaded every session must never list what exists — such a list is wrong the moment a file is added. It gives the commands to discover what exists (`ls`, `find`) and the naming conventions to interpret what is found. Discovery is always current; enumeration is always stale.

**Subagents quarantine cost and bias.** A task that reads widely exhausts one context and anchors on whatever it read first. Dispatch it to a subagent with read-only scope and a concrete question; the subagent spends its own budget and returns a compressed result, leaving the orchestrator's context clean.

## Content

### Agent file format

```markdown
---
description: "<Role> — <one-line summary>"
mode: subagent
temperature: <0.3-0.7>
---

# <Role Name>

<One paragraph setting the role's lens — the professional perspective it brings
to the work and where its attention goes first.>

## What you hold
- <2-4 bullets: the principles and concerns this role prioritises — its values.>

## What you decide
<One statement: the decision this role alone settles.>

## What you refuse
- <2-3 bullets: the anti-patterns and guardrails this role pushes back on.>
```

That is the whole file. The portrait sets the role's headspace; no skill list, no artifact table, no transitions, no gate, no knowledge reference, no step-by-step procedure. Consult-only specialists (advisers with no state of their own) may use a lighter form — lens and what they decide — but the same exclusion holds.

### What never goes in an agent file

Anything the flow or a skill already states. For the full ownership table, see [[methodology/separation-of-concerns#who-owns-what]]. Specifically: skill lists, artifact paths, branch, transitions, gate conditions, step-by-step procedure, and domain facts all belong elsewhere.

### AGENTS.md is navigation only

`/AGENTS.md` is loaded every session. It contains only: where the methodology layer lives, how to resolve wikilinks, the session protocol, naming conventions, and discovery commands (`ls .opencode/agents/`, `ls .opencode/skills/`, `find .opencode/knowledge -name '*.md'`). No gates, no procedures, no knowledge content, no file enumerations.

### When to dispatch a subagent

Route read-heavy or open-ended research (auditing a codebase, surveying a decision space) to a subagent. Give it read-only scope, a concrete question, and a request for a compressed result. Keep its output out of the orchestrator's context unless the answer is needed to route.

## Related

- [[methodology/separation-of-concerns]]
- [[methodology/skill-files]]
- [[methodology/knowledge-files]]
