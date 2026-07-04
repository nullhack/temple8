---
domain: workflow
tags: [flowr, state-machine, session, subflow, evidence, cli, routing]
last-updated: 2026-07-02
---

# flowr Operations

## Key Takeaways

- flowr is a non-deterministic state machine **specification** — a YAML file declares structure (states, transitions, guards), not behaviour; flowr never runs the work, it routes (nullhack/flowr, 2026).
- Drive one state at a time: `check` reads the current state's attrs; the orchestrator dispatches the agent named in `dispatch_to`; that agent asserts evidence; `transition` advances. This is the whole loop.
- A state with `flow:`/`flow-version:` is a **subflow pointer**: entry pushes a stack frame, exit pops it; the parent's `next` key must match the child's exit name; `session init` auto-enters the first subflow.
- Escalations re-enter the target subflow at its **first state** — flowr keeps no position memory — so `build → plan` on a contract gap re-runs plan from `author-test-stubs`, and `plan/explore → discover` re-runs the interview funnel from the top.
- A guarded transition fires only when its condition group is satisfied; the orchestrator asserts evidence with `--evidence key=value` (one per condition key). flowr **collects asserted evidence, it does not run checks** — CI is the enforcement backstop per [[methodology/separation-of-concerns#evidence-vs-enforcement]].
- Sessions persist to `.cache/sessions/<name>.yaml` (filesystem is the source of truth); `state.attrs` is a free-form `dict`, so the key names (`dispatch_to`, `skills`, `input artifacts`, `output artifacts`, `git branch`, `conditions`) are project convention, not enforced by flowr.

## Concepts

**Specification, not engine.** A flow file declares the graph: states with attributes, transitions with optional guards, exits. flowr validates the graph (seven MUST checks at load — every `next` resolves, no ambiguous targets, parent `next` keys match child `exits`, no cross-flow cycles, exits referenced, named conditions resolve, defaulted params supplied), queries it (`check`, `next`), and advances it (`transition`). It has no opinions about retries, timeouts, or error handling, and it never executes the dispatched work — that is the external agent's job (nullhack/flowr, 2026).

**The state-reading loop.** The orchestrator never improvises routing. At each step it runs `check` to read the current state's attrs — `dispatch_to` (the one dispatched agent), `skills` (the procedures), `input artifacts` (what must be on disk), `output artifacts` (what may be written), `git branch`, and `conditions` (any guarded transitions). It verifies the inputs exist, dispatches that agent with the skill paths and inputs, then asserts that agent's evidence to fire the next `transition`. One state, one dispatch.

**Subflows and the call stack.** A state carrying `flow:` is a pointer into a child flow; entering it pushes a frame `({parent_flow, parent_state})` onto a stack and sets the session to the child's first state. When a transition's target is one of the child's exit names AND the stack is non-empty, flowr pops the frame, restores the parent, and follows the parent state's transition for that exit name — which may itself enter the next subflow. This is how `pipeline-flow` chains discover → explore → plan → build → deliver → shipped through five subflows.

**No position memory on escalation.** When a subflow exits on an escalation trigger (e.g. `needs-contracts`, `needs-elicitation`), the parent routes back to the subflow's entry, and re-entry lands at the child's FIRST state — not at the state where it left off. A rework loop therefore re-runs the whole subflow pass; the gates re-verify everything. This is deliberate (a contract change can ripple) but means escalation is heavier than a resume.

**Conditions and evidence.** A `next` entry shaped `{to: <state>, when: <name>}` is guarded; the named group lives under the state's `conditions:` block, a map of `{key: expression}` (operators `== != >= <= > <`, plain value = `==`). The orchestrator fires the transition by passing `--evidence key=value` for each key. flowr evaluates the assertion; it does not verify the claim is true — that is CI's job. The evidence keys the temple8 flows use are listed in `AGENTS.md`.

**attrs is free-form.** flowr treats `state.attrs` as an opaque dict; the keys `dispatch_to` / `skills` / `input artifacts` / `output artifacts` / `git branch` / `specialists` / `conditions` are this project's convention for binding a state to a dispatched agent, a procedure, artifacts, and a branch. None are enforced by the engine — they are read by the orchestrator and the agents. Renaming a key changes the convention, not the spec.

## Content

### Command reference

All commands: `uv run python -m flowr <command>`. Output is JSON by default. `--session <id>` makes any command session-aware.

| Command | Purpose |
|---|---|
| `session init <flow> --name <id>` | Create a session (auto-enters the first subflow) |
| `check --session <id>` | Current state: attrs + available transitions |
| `check --session <id> <trigger>` | A specific transition's conditions (open/blocked + the keys needed) |
| `next --session <id> [--evidence k=v …]` | Valid transitions, marked open/blocked by the evidence given |
| `transition <trigger> --session <id> [--evidence k=v …]` | Advance (fires only if guarded conditions are met) |
| `session show --name <id>` | Session state + the subflow call stack |
| `states <flow>` | List states in a flow |
| `validate <flow.yaml>` | Run the seven MUST checks on one flow file |
| `config` | Resolved config (flows_dir, sessions_dir, defaults from `pyproject.toml`) |
| `export` / `serve` | Visualisation (mermaid / viz server) |

Sessions live at `.cache/sessions/<id>.yaml` (gitignored). `--flows-dir` overrides the configured flows directory for one invocation.

### The state-driving protocol

1. `check --session <id>` → parse `dispatch_to`, `skills`, `input artifacts`, `output artifacts`, `git branch`, `conditions`.
2. Verify every `input artifacts` path exists on disk — missing = stop, do not assume (binding constraint 3).
3. Dispatch the agent named in `dispatch_to` as a subagent, with the `skills` paths (`.opencode/skills/<name>/SKILL.md`, listed order = execution order) and the input artifacts. The dispatched agent writes only to `output artifacts`.
4. The dispatched agent returns asserted evidence (e.g. `stubtest-clean=true`).
5. `transition <trigger> --session <id> --evidence k=v …` fires the guarded advance; `next --session <id>` previews open/blocked if unsure.
6. Repeat from 1 at the new state. One state = one dispatch.

### Subflow mechanics

| Event | What flowr does |
|---|---|
| Enter a state with `flow:` | push `({parent_flow, parent_state})`, set session to child's first state |
| Transition target is a child exit name + stack non-empty | pop the frame, restore parent, follow the parent's transition for that exit |
| Escalation exit (e.g. `needs-contracts`) | parent routes back to the subflow's entry → re-enters at FIRST state (no resume) |
| Terminal exit (`shipped`) | stack empties; session is done |

Parent `next` keys must match child `exits` exactly (a validation error otherwise). Within-flow cycles are allowed (the tdd red/green/refactor loop); cross-flow cycles are not.

### Conditions and evidence

A guarded transition under a state:
```yaml
states:
  - id: review-test-stubs
    conditions:
      accepted:
        interview-consistent: true
        scope-integration-e2e-only: true
        happy-paths-complete: true
    next:
      accepted: { to: write-test-py, when: accepted }
      needs-stubs-rework: author-test-stubs
```
Firing `accepted` requires all three keys; the orchestrator asserts them:
```
flowr transition accepted --session <id> \
  --evidence interview-consistent=true \
  --evidence scope-integration-e2e-only=true \
  --evidence happy-paths-complete=true
```
`needs-stubs-rework` is bare (no guard) — it fires without evidence.

### Gate evidence keys

The temple8 flows' guarded transitions and the evidence the orchestrator asserts (`=true` unless noted):

| Flow / state | Trigger | Evidence keys |
|---|---|---|
| plan / review-test-stubs | `accepted` | `interview-consistent`, `scope-integration-e2e-only`, `happy-paths-complete` |
| plan / simulate-contracts | `accepted` | `pyright-consistent`, `no-orphans`, `traceability-complete`, `layer-order-respected`, `test-stubs-consistent`, `lint-clean`, `simulation-passed` |
| tdd / red | `contract-red` | `test-status=red`, `red-reason-is-ours=true` |
| tdd / green | `test-green` | `test-status=green`, `stubtest-clean=true` |
| tdd / review | `approved` | `impl-matches-contract`, `source-quality-clean`, `stubtest-clean`, `tests-green` |
| deliver / merge | `merged` | `tests-green-on-dev`, `stubtest-clean-on-dev` |

Bare transitions (no `when:`) fire without evidence — e.g. the `select → red` advance, the escalate exits (`needs-contracts`, `needs-elicitation`, `needs-capture`), and `all-built → shipped`.

### Validation

`validate <flow.yaml>` returns `{valid: true, violations: []}` or a list of the seven MUST-check failures. Validate every flow after an edit:
```
for f in .flowr/flows/*.yaml; do uv run python -m flowr validate "$f"; done
```

## Related

- [[methodology/separation-of-concerns#evidence-vs-enforcement]] — why flowr collects asserted evidence and CI enforces
- [[methodology/agent-files]] — what `dispatch_to` resolves to (the dispatched agent's identity)
- [[methodology/skill-files]] — what `skills` resolves to (the per-state procedure)
- [[methodology/knowledge-files]] — how the dispatched agent's loaded knowledge is cited
