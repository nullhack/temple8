---
domain: skill-design
tags: [skills, on-demand-loading, context-budget, diataxis]
last-updated: 2026-04-29
---

# Skill Design Principles

## Key Takeaways

- Skills are procedure only (HOW); the flow defines routing (WHEN), artifacts (WHAT), and transitions (WHERE TO NEXT).
- Skills load into context only when invoked; keep them lean. Target under 150 lines.
- Skills reference knowledge via wikilinks and never inline knowledge content.
- Embed IF-THEN triggers (Gollwitzer, 1999) at the decision point within steps, not in a separate section.
- Skills are how-to guides (Diátaxis, Procida, 2021): step-by-step instructions for achieving a specific outcome.

## Concepts

**Skill = Procedure Only**: The flow YAML is the single source of truth for owner, skills, input_artifacts, output_artifacts, and next transitions. The skill contains only the procedure for doing the work. Do not duplicate artifact paths, routing decisions, or "when to use" sections; those come from the flow.

**On-Demand Loading**: Skills load into context only when invoked. Bloated always-loaded files cause LLMs to ignore critical instructions (Liu et al., 2023). Every token in an unconditionally-loaded file competes for attention. Skills must be self-contained when loaded but must not duplicate content in `AGENTS.md` or other skills.

**Skill as How-To Guide (Diátaxis, Procida, 2021)**: In the Diátaxis framework, skills serve as how-to guides: task-oriented, step-by-step instructions. Tutorials (learning a role) belong in agent files. Reference and explanation belong in knowledge files.

**Reference Knowledge, Never Inline**: When a skill needs domain knowledge (e.g., INVEST criteria, Gherkin format), it must reference the knowledge file via wikilink rather than embedding the content. This prevents duplication and guarantees the knowledge file remains the single source of truth.

**Prospective Memory Cues** (Gollwitzer, 1999; McDaniel & Einstein, 2000): Memory for intended actions is better when cues are embedded at the decision point. Include the IF-THEN trigger and the knowledge reference at the point of decision, not in a separate reference document.

**Lean Skill Design**: Target lengths: under 150 lines for focused skills, under 250 lines for complex multi-phase skills. Cut without hesitation: exhaustive examples (one is enough), reference documentation (use wikilinks), boilerplate configuration (belongs in project files), knowledge content (extract to knowledge files).

**Imperative Language Standard**: Write skills in imperative style. Verb-first. No articles ("the", "a", "an"). No pronouns ("it", "they", "you"). Fragments OK. Drop filler words. Every sentence starts with an action verb. Examples: "Run `beehave check`" not "You should run beehave check". "Write test body" not "The next step is to write the test body". "No skip" not "You must not skip this step". This style reduces token count, eliminates ambiguity about who acts, and forces procedural clarity.

## Content

### Skill = Procedure Only (No Duplication)

The flow YAML defines everything the agent needs to know about context:

| Concern | Source | What the skill does |
|---|---|---|
| Which agent? | Flow `owner` | Agent identifies itself |
| Which skill? | Flow `skills` | Agent loads it via `flowr status` |
| Which transitions? | Flow `next` | Agent checks via `flowr status` |
| Which artifacts? | Flow `input/edited/output_artifacts` | Skill says "write to output artifacts" |
| How to do the work? | Skill steps + knowledge | Skill loads knowledge via wikilinks |

The skill never hardcodes artifact paths, transition names, or "when to use" conditions.

### Skill Body Structure

```markdown
---
name: <skill-name>
description: "<one-line description of what this skill does>"
---

# <Skill Title>

Available knowledge: [[domain/concept]]. `in` artifacts: read all before starting work.

1. <verb-first procedural step>
2. <step referencing knowledge per [[domain/concept]]>  ← Link at point of use
3. ...remaining procedural steps
```

**When to include available knowledge:**
- Include when the skill references knowledge files or document artifacts
- Omit if the skill has no knowledge references (e.g., pure mechanical procedures)

**When to reference knowledge in steps:**
- Reference knowledge when applying a technique: "Apply pre-mortem per [[requirements/pre-mortem]]"
- Reference knowledge when using criteria: "Validate each Rule per [[requirements/invest]]"
- Do NOT inline knowledge content: Wrong: "split if >8 examples", Right: "per [[requirements/decomposition]]"

**What NOT to include:**
- Lists of specific artifact names (these come from flow)
- "Review input artifacts" as step 1 (flow already defines inputs)
- Routing logic or transition conditions (flow owns this)
- "Write results to output artifacts" (orchestrator's todo handles output items)
- "Advance the flow" or "Check flow transitions" (orchestrator's anchor handles state exit)
- Knowledge content (reference via wikilinks only)

### On-Demand Loading

Skills load into context only when invoked. Skills must be self-contained when loaded but must not duplicate content that already exists in `AGENTS.md` or other skills.

### Prospective Memory Cues

Include the IF-THEN trigger and the knowledge reference at the decision point:

```
If a class has more than one reason to change, read [[software-craft/tdd#concepts]]
and apply the Single Responsibility Principle.
```

Not just "Apply SOLID principles" (no cue for when) or just "See [[software-craft/tdd#concepts]]" (no cue for when to load).

### De-Duplication

When two skills need the same knowledge, both should reference the same knowledge file rather than each embedding a copy. Each piece of knowledge belongs in exactly one canonical location.

### Input Handling

Verify input artifacts per AGENTS.md Session Protocol.

## Related

- [[knowledge-design/principles]]
- [[agent-design/principles]]
- [[workflow/flowr-spec]]