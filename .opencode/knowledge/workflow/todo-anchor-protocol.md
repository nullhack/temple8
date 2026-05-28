---
domain: workflow
tags: [todo, anchor, protocol, execution-contract, state-isolation, loop-prevention]
last-updated: 2026-05-28
---

# Todo Anchor Protocol

## Key Takeaways

- Todo list is the execution contract: every item must be `completed` before anchor fires.
- Anchor item is mandatory and always last; prevents state-skipping by requiring `flowr next` → `flowr transition` → todo rewrite.
- One state per todo. Never generate a todo that spans multiple flow states or includes steps from adjacent states.
- Loops (review → fix → re-review) are separate dispatches with separate flowr transitions; the todo must not collapse them.

## Concepts

**Todo as Execution Contract**: The todo list generated at state entry is not a suggestion. It is the procedural checklist. The orchestrator creates it from `flowr check` output, dispatches the owner agent to do the work, then uses the anchor to advance. Every item must be `completed` before the anchor fires.

**One State Per Todo**: A todo covers exactly one flow state. When a flow has multiple states (e.g., design-review → structure-review → conventions-review), each state gets its own todo, its own dispatch, and its own flowr transition. Never generate a todo that includes items from the next state or collapses loop iterations.

**Anchor Item**: The last item in every todo reads: "flowr next → pick transition → flowr transition → rewrite todo from next state." The anchor must:
- Run `uv run python -m flowr next --session default --evidence key=value` to see all transitions with status markers (`"open"` / `"blocked"`)
- For `"blocked"` transitions, check `conditions` dict to understand what evidence is needed
- For chosen transition, run `uv run python -m flowr check --session default <trigger>` to verify conditions
- Conditions NOT met → do NOT transition. Gather evidence or flag user.
- Present options to the stakeholder if multiple `"open"` paths exist
- Show evidence to user for confirmation
- Run `uv run python -m flowr transition <trigger> --session default --evidence key=value`
- Generate a new todo list from the next state's metadata via `uv run python -m flowr check --session default`
- Never be skipped. It is the guardrail that prevents state-skipping

**Loop Prevention**: When a review tier rejects and the flow loops back (e.g., `fail` → `tdd-cycle`), the orchestrator must:
1. Complete the current state's anchor (transition `fail`)
2. Enter the new state (e.g., `tdd-cycle`)
3. Generate a fresh todo from the new state's metadata
4. Dispatch the owner agent with only the new state's skills
5. Never carry items from the review state into the fix state's todo

**State Isolation**: The todo must not include steps from adjacent states. If the work reveals that an artifact outside the `out` contract needs changes, flag it in output notes. Do not add it to the current todo.

## Content

### Todo Generation Rules

At state entry, generate the todo from the state's `flowr check` output. Use opencode's native status fields: `pending`, `in_progress`, `completed`.

1. **Preparation** (`pending`): verify branch matches `attrs.git`, list available `in` artifacts
2. **Dispatch** (`pending`): call the state's owner agent as subagent with skill paths + attrs + in artifacts
3. **Skill-derived items** (`pending`): one per numbered step in the skill, verbatim
4. **Output** (`pending`): one per `out` artifact to create/update
5. **Verification** (`pending`): check constraints, run tests/lint per skill
6. **Anchor** (`pending`, always last): check next state conditions, verify evidence, transition

Only one item should be `in_progress` at a time. Mark `completed` immediately upon completion.

### Anchor Checklist

Before exiting a state, confirm each item:

- **Dispatch completed:** Exactly one agent dispatch happened with exactly the skills listed.
- **Single-state scope:** No work from adjacent states was performed during this dispatch.
- **Flowr next checked:** `uv run python -m flowr next --session default` ran. JSON output parsed. Transitions with `"status": "open"` are available; `"status": "blocked"` transitions show required evidence in `conditions`.
- **Conditions verified:** For chosen transition, conditions checked via `uv run python -m flowr check --session default <trigger>`. All conditions met before proceeding.
- **Loop transition resolved:** IF multiple `open` transitions exist (loop states like tdd-cycle refactor), use subagent's reported exit signal (`"next-example"` vs `"all-examples-pass"`) from `beehave status --json`. IF ambiguous → run `beehave status --json` directly and decide.
- **Review findings relayed:** IF transitioning via `fail` back to a prior state, include reviewer findings verbatim in the re-dispatch prompt as a **Prior Review Findings** section.
- **Transition executed:** `uv run python -m flowr transition <trigger> --session default --evidence key=value` ran successfully.
- **Todo rewritten:** New todo list generated from the next state's metadata via `uv run python -m flowr check --session default`.
- **No state skipped:** Every item above the anchor is `completed`.

### Anti-Patterns

**Collapsing states**: A todo that includes items like "review design" AND "review structure" AND "review conventions" collapses three states into one. Each is a separate state requiring its own todo, dispatch, and transition.

**Pre-generating loop iterations**: A todo that includes "fix issues from review" alongside the review items pre-generates a loop iteration that may not happen. The fix state only gets a todo if the review rejects.

**Carrying state forward**: After transitioning, the old todo is replaced entirely. The new todo is generated fresh from `uv run python -m flowr check --session default` output. Never append to the previous todo.

### Owner Mapping

Owner dispatch mapping per AGENTS.md Session Protocol.

## Related

- [[workflow/flowr-operations]]
- [[skill-design/principles]]
