## Main Directive

After any compression or large task, re-read these four points:

1. **Golden Rules** prevent 80% of failures — follow them
2. **Dispatch to owner** — orchestrator ROUTES, never DOES
3. **Todo is the contract** — no todo = no work
4. **Follow the flow** — flowr is source of truth for routing

## Golden Rules

1. **No skip state.** flowr check → dispatch → transition. No shortcut.
2. **No bypass dispatch.** Orchestrator route. Agent do work. Never both.
3. **No code before spec.** Features flow through define-flow → develop-flow. No tests, no stubs, no implementation until features complete and flow authorizes. `attrs.skills` and `attrs.out` define what you may write — write nothing else. Feature files have three phases — do not skip ahead:
   - **define-flow** (simulate-spec → refine-features): Feature + Rule + description only. NO Examples. `beehave generate` produces nothing at this stage. Files are per-context then split per-feature.
   - **develop-flow / feature-examples** (write-bdd-features): Examples/Scenario Outlines added to existing Rules. Now `beehave generate` can produce stubs.
   - **develop-flow / development**: `beehave generate` runs, stubs exist, TDD begins.
4. **No collapse gate.** Review design ≠ review structure. Each fail independent. Polish after accept.
5. **No split feature without stakeholder say.** Propose split. They decide core vs deferred.
6. **No enter state without `in` on disk.** Missing = stop. No assume.
7. **No ship without trace.** Every interview Q → passing test or stakeholder deferral.
8. **Match `attrs.git` before start.** Commit dev before exit project-phase flow.
9. **Merge feature → dev.** `task test-fast` pass. No dangle branch.

## Artifact Templates

Strip `.templates/` prefix + `.template` suffix → destination path.

- `.templates/docs/features/<feature_title>.feature.template` → `docs/features/my_feature.feature`
- `.templates/.cache/interview-notes/IN_YYYYMMDD_<session_id>.md.template` → `.cache/interview-notes/IN_20260430_session_management.md`

No template for non-Python file in `in`/`out` → raise error. No template for Python file → create without.

## Knowledge Resolution

`[[domain/concept]]` → `.opencode/knowledge/{domain}/{concept}.md`

| Fragment | Loads | When |
|----------|-------|------|
| `#key-takeaways` | Frontmatter + Key Takeaways | Recall principle or definition |
| `#concepts` | + Concepts | Understand without examples/procedures |
| (none) | Full file | Find violations, detect patterns, apply criteria |

## Discovery

Discover at runtime. No enumerate — goes stale.

```bash
ls .opencode/agents/                    # agent identity
ls .opencode/skills/                    # skill dirs (each has SKILL.md)
find .opencode/knowledge -name '*.md'   # knowledge files
find .templates -name '*.template'      # artifact templates
find docs/research -name '*.md'         # research notes
```

## File Naming

### Artifact Patterns in Flow Attrs

| Pattern | Meaning | Example |
|---------|---------|---------|
| `filename.md` | Specific document | `domain_spec.md` |
| `dir/<param>.ext` | Instance by parameter | `features/<feature_title>.feature` |
| `dir/*.ext` | Multiple in `in` | `.cache/interview-notes/*.md` |
| `conceptual_name` | Runtime between states | `typed-source-stubs` |

All filenames = **snake_case**. Cache folders = kebab-case (`interview-notes/`). Python folders = snake_case.

### Artifact Types

| Type | Description | Examples |
|------|-------------|----------|
| Runtime | Between states, no files | `typed-source-stubs`, `test-implementations`, `source-implementations`, `refactored-source`, `feature-commits`, `polished-source`, `git_branch`, `test-skeletons` |
| Cache | `.cache/` cross-session | `.cache/acceptance/<feature>.md`, `.cache/interview-notes/<id>.md`, `.cache/sim/results_<ts>.md` |
| Environment | Tool output, not flow | `coverage-reports`, `test-output`, `linter-output` |

**Runtime resolution**: Runtime artifacts are not file paths. Resolve via discovery. `typed-source-stubs` → `find` for source files created in previous state. `test-implementations` / `source-implementations` → `beehave status --json` shows which scenarios are implemented. `test-skeletons` → test stub files in `tests/features/`. `git_branch` → `git branch --show-current`. `feature-commits` / `polished-source` / `refactored-source` → files changed since last commit. Include resolution command in dispatch prompt when `in` contains Runtime artifacts.

`*` in `in` = multiple docs. List dir first. Read selective.

## Flowr Commands

All: `uv run python -m flowr`. Session: always `--session default`. Output: JSON default. `--text` for human.

| Command | Purpose |
|---------|---------|
| `uv run python -m flowr check --session default` | State attrs, owner, skills, transitions |
| `uv run python -m flowr check --session default <trigger>` | Transition conditions |
| `uv run python -m flowr next --session default [--evidence key=value]` | Transitions: open/blocked |
| `uv run python -m flowr transition <trigger> --session default [--evidence key=value]` | Advance state |
| `uv run python -m flowr session init <flow> --name default` | Create session |
| `uv run python -m flowr session show --name default` | Session state + call stack |
| `uv run python -m flowr session set-state <state> --name default` | Manual state update |

More: `validate`, `states`, `mermaid`, `config` → `uv run python -m flowr <command>`.

Full ref: [[workflow/flowr-operations]].

## Project Commands

See `pyproject.toml` for all tasks + config.

| Command | Purpose |
|---------|---------|
| `task test` | Tests, short tracebacks |
| `task test-fast` | Fast tests only (no slow marker) |
| `task test-build` | Full suite + coverage + hypothesis |
| `task run` | Run application |

| Command | Purpose |
|---------|---------|
| `ruff check .` | Functional lint (bugs, security, complexity) |
| `task conventions` | Full lint (naming, docstrings, formatting) |
| `ruff format .` | Auto-format |

## Session Protocol

Orchestrator ROUTES. Never DOES. Every transition through flowr.

### State Entry

`uv run python -m flowr check --session default` → parse `attrs.owner`, `attrs.skills`, `attrs.in`, `attrs.out`, `attrs.git`. Verify `in` on disk. Missing = stop. Announce one line: `→ state-name`.

### Dispatch

`attrs.owner` → agent. Call as subagent. Include in dispatch prompt:

1. **State attrs** — owner, skills, in, out, git
2. **Skill paths** — `.opencode/skills/<name>/SKILL.md` per skill in `attrs.skills` (listed order = execution order)
3. **In artifact paths** — all `attrs.in` files (resolve Runtime artifacts per Artifact Types table)
4. **Convention boundary** — if design-phase state
5. **Mandatory instruction:**
   > You MUST read every skill file listed in your dispatch context from `.opencode/skills/<name>/SKILL.md` and FOLLOW their procedures step by step. Skills are mandatory — do not skip, summarize, or improvise around them. Read all `in` artifacts before starting work. Write only to `out` artifacts. Commit to the branch specified in `git`.

Owner mapping: `PO` → product-owner, `DE` → domain-expert, `SE` → software-engineer, `SA` → system-architect, `R` → reviewer, `Design Agent` → design-agent, `Setup Agent` → setup-agent.

### Beehave

Always active in development. Runs on every `pytest` invocation: parses features, generates stubs, checks violations. Violations = **test failures** (injected as synthetic failing test items). `[beehave]` in test output = hard stop.

- `beehave generate` — stubs from `.feature` files (also runs automatically during pytest)
- `beehave check` — verify stubs align
- `beehave status --json` — coverage
- `beehave clean <feature> --force` — remove unmapped test functions (run when titles change)

Title change leaves stale stubs. Run `beehave clean <feature> --force` to remove orphans.

No skip. No `no:beehave`. No noise (`_ = value`). Every test assert observable behavior. Violations block progress.

### Convention Boundary

Design-phase states (create-py-stubs, write-test, implement-minimum, refactor, review-gate): `task conventions`/`ruff format`/pyright/docstrings/type annotations **prohibited**. Only `task test-fast`. Design changes invalidate convention work.

Dispatch during design phase:
- No convention commands in prompt
- Only verification steps skill defines
- Skill verification = ceiling, not floor

Exception: polish-code runs conventions after feature acceptance.

### Procedural Contract

One state = one dispatch. One dispatch = exactly skills in `attrs.skills`. No combine states.

### Review Loops

When review fails and transitions back (e.g., `fail → tdd-cycle`), the reviewer's findings must reach the next dispatch. Include reviewer findings verbatim in the re-dispatch prompt as a **Prior Review Findings** section. Findings include file:line citations and the specific failure reason. The receiving agent addresses each finding — do not repeat the review from scratch.

### Todo-Driven Execution

Generate todo at state entry via todowrite. Status: `pending` → `in_progress` → `completed`.

```
1. Preparation: verify branch == attrs.git, list in artifacts
2. Dispatch: call owner agent with skill paths + attrs + in artifacts
3. Skill-derived: one item per skill step, verbatim
4. Output: one per out artifact
5. Verification: constraints, tests/lint per skill
6. Anchor: next state conditions, verify evidence, transition
```

- Update todowrite after ANY step: mark `completed`, next `in_progress`
- Todo empty/missing = regenerate immediately. No todo = no work.
- One state per todo. No span states. No collapse loops.
- Self-generated items only for infrastructure (read, commit). Never core procedure.
- Orchestrator track. Subagent do.

### Anchor (State Exit)

1. `uv run python -m flowr next --session default --evidence key=value`
2. Parse: `open` vs `blocked`
3. For chosen transition: `uv run python -m flowr check --session default <trigger>` → conditions
4. Conditions met? No → stop. Gather evidence or flag user.
5. **Loop states** (tdd-cycle refactor): IF multiple `open` transitions exist (e.g., `next-example` and `all-examples-pass`), use subagent output to pick. Subagent reports `"next-example"` or `"all-examples-pass"` based on `beehave status --json`. IF ambiguous → run `beehave status --json` directly and decide.
6. Show evidence to user for confirmation.
7. `uv run python -m flowr transition <trigger> --session default --evidence key=value`
8. Generate NEW todo from next state's `flowr check --session default`

### Session Init

```bash
uv run python -m flowr session init <flow> --name default
```

Session tracks flow, state, call stack (subflows), params. First state has `flow:` → auto-enters subflow.

Three primary flows:
- `define-flow` — spec, validation, features, architecture
- `develop-flow` — select, examples, TDD, acceptance
- `deliver-flow` — squash-merge, publish, PR

### Cross-Flow Routing

develop-flow `needs-architecture` → re-enter define-flow at `architecture`. New session. `flowr session set-state architecture`.

post-mortem-flow `needs-architecture` → same procedure.

### Branch Discipline

`attrs.git` = `dev` or `feature`. Match before start. Project-phase exit requires `committed-to-dev-locally: ==verified`.

### Within a State

Announce once. Then quiet.

- **Artifact contract:** `in` = must read all before work. `out` = may create/edit. Outside `out` = no write. Flag issues in notes.
- **Cumulative edit:** Loop back to state → edit existing `out`, no recreate.
- **Out artifact protocol:** Exists → read, edit declared sections. Not exists → resolve `.templates/` path + `.template` suffix. Copy. Edit. No template for non-Python → raise error.
- **Spec docs read-only in TDD/review.** Flag inconsistencies. No fix.
- **Cite precisely:** file:line. No vague findings.
- **Fewest, quietest commands.** Suppress verbose. Scope when possible.
- **No narration.** Command + output = conversation.
