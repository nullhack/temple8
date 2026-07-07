---
domain: methodology
tags: [skills, procedure, on-demand-loading, context-budget]
last-updated: 2026-07-01
---

# Skill Files

## Key Takeaways

- A skill is procedure only — the HOW; the flow owns the when, what, and where-to-next, and knowledge owns the why (see [[methodology/separation-of-concerns#concepts]]).
- Keep skills lean: under ~150 lines for a focused skill, ~250 for a multi-phase one — every line competes for attention the model could spend on the work.
- Write skills as how-to guides: imperative, verb-first, no articles or pronouns.
- Cue knowledge at the decision point with an IF-THEN trigger and a wikilink together; a bare link has no trigger, a bare rule has no address.
- Never duplicate the flow in a skill — no artifact paths, transition names, gate conditions, or "advance the flow".
- One skill per state — never share a skill across states. If two states share a procedure, factor the shared part into knowledge and give each state its own skill that loads it; a shared skill lets a dispatched agent skip or merge the distinct steps.

## Concepts

**Procedure only.** The skill contributes the one thing the flow cannot: the step-by-step method. `dispatch_to` says who, `skills` says which procedure, `input artifacts` / `output artifacts` say what is read and written, `next` says where to go, `conditions` says what unlocks the gate (see [[methodology/separation-of-concerns#what-the-flow-owns]]). A skill that restates these builds a second source that drifts.

**On-demand, therefore lean.** A skill enters context only when its state dispatches it, and that budget is the whole task. Cut exhaustively: one example is enough, reference material belongs in knowledge, boilerplate belongs in project config, and any fact the flow already states is deleted on sight.

**How-to guide.** In Diátaxis terms a skill is a how-to: task-oriented, step-by-step, aimed at a concrete outcome. It is not a tutorial (that is identity), not reference (that is knowledge), not explanation (also knowledge).

**Cue knowledge at the decision point.** A bare "see [[domain/concept]]" is a link with no trigger; a bare "apply SOLID" is a trigger with no link. Combine them — state the IF-THEN condition and attach the wikilink at the point where the agent meets the decision. Prospective memory fires when cue and action sit together at the moment of need.

**Imperative standard.** Verb-first. Drop articles ("the", "a") and pronouns ("you", "it"). Fragments are fine. "Run `flowr next`" — not "You should now run the flowr next command." This compresses tokens, removes ambiguity about who acts, and forces each step open with an action.

## Content

### Skill file format

```markdown
---
name: <skill-name>
description: "<one-line outcome this skill produces>"
---

# <Skill Title>

1. Load the cited knowledge before any other step: resolve [[domain/concept]] (and every wikilink named below). If a linked file is not yet authored, the inline IF-THEN triggers below carry enough to act; the link deepens once it exists.
2. <verb-first step>
3. IF <condition at the decision point> THEN <action> per [[domain/concept]]
4. <remaining steps>
```

The citation form is always `IF <condition> THEN <action> per [[domain/concept]]` — inline trigger plus link together at the point of need. The trigger states the condition and the action (enough to act now); the wikilink adds depth and resolves when the knowledge file is authored. A bare `per [[X]]` or a bare `Available knowledge: [[X]]` list is the antipattern (see Concepts above) — a link with no trigger.

Begin with the Load step only when the skill cites knowledge; omit it for pure mechanical procedures.

### What never goes in a skill

- Specific artifact paths — they come from the flow's `input artifacts` / `output artifacts`.
- Transition names, gate conditions, or "advance the flow" — the orchestrator owns state exit.
- Knowledge content (criteria, definitions, more than one illustrating example) — reference it via wikilink.
- Anything the flow already states — see [[methodology/separation-of-concerns#what-the-flow-owns]].

### De-duplication

When two skills need the same criterion, both cite the same knowledge file. A fact lives in exactly one place; every consumer links rather than copying.

## Related

- [[methodology/separation-of-concerns]]
- [[methodology/agent-files]]
- [[methodology/knowledge-files]]
