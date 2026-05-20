## Golden Rules

Post-mortem analysis shows these practices prevent most project failures. Violating them triggers costly rework. Defects caught later cost 10–100× more to fix (Boehm, 1981).

1. **Never skip a flow state.** Every state boundary goes through flowr check → dispatch to owner → flowr transition. No shortcuts, no manual session edits, no jumping ahead.
2. **Never bypass owner dispatch.** Each state has an owner agent. The orchestrator dispatches to that agent with skills loaded. It never does the work itself. One agent, one hat at a time.
3. **Never collapse progressive gates.** Multi-step gates (review: design → structure) are separate for a reason. Each one can fail independently and send work back. Conventions (naming, docstrings, formatting) are enforced in a separate polish state after feature acceptance.
4. **Never decompose a feature without stakeholder approval.** If a feature is too large for INVEST, propose the split to the stakeholder with rationale. They decide what's core vs. deferred.
5. **Verify inputs exist before entering a state.** Every state's `in` artifacts must be readable on disk. If they're missing, stop and reconstruct them. Don't proceed with assumed knowledge.
6. **A feature is not done until every interview requirement is traced.** Every stakeholder Q&A must map to either a passing traceable test or an explicit stakeholder deferral. Untraced requirements = incomplete delivery.
7. **Respect git branch discipline.** Every state declares `git: dev`, `git: feature`, or `git: main` in its attrs. **Verify the current branch matches `attrs.git` before starting any work.** If the branch is wrong, checkout or create the correct branch before proceeding. Never switch branches mid-state. Before exiting a project-phase flow (discovery, architecture, branding, setup), set `committed-to-dev-locally: ==verified` evidence. Changes must be committed to dev before advancing.
8. **Every feature branch must be merged back to dev.** A feature is not delivered until its commits are squash-merged into local dev and `task test-fast` passes on dev. The develop-flow exits to deliver-flow which handles the merge, but the orchestrator must never leave a feature branch dangling — if the session ends mid-feature, resume and complete the merge before starting new work.

## Project Structure
- `.flowr/flows/`: YAML state machine definitions (source of truth for routing)
- `.cache/sessions/`: runtime session state
- `.templates/`: artifact templates (strip `.templates/` prefix and `.template` suffix → destination path)
- `.opencode/`: agents, skills, and knowledge

## Artifact Templates

When creating a document, use the template in `.templates/` that matches the artifact type. Strip the `.templates/` prefix and `.template` suffix to determine the destination path. For example:
- `.templates/docs/adr/ADR_YYYYMMDD_<adr_id>.md.template` → `docs/adr/ADR_20260430_my_decision.md`
- `.templates/docs/features/<feature_title>.feature.template` → `docs/features/my_feature.feature`
- `.templates/.cache/interview-notes/IN_YYYYMMDD_<session_id>.md.template` → `.cache/interview-notes/IN_20260430_session_management.md`
- `.templates/.cache/sim/simulation_results_YYYYMMDDTHHMMSS.md.template` → `.cache/sim/simulation_results_20260517T143000.md`
- `.templates/.cache/acceptance/<feature_title>.md.template` → `.cache/acceptance/domain_value_objects.md`

If no template exists for an artifact type, create the document without one.

## Knowledge Resolution
`[[domain/concept]]` → `.opencode/knowledge/{domain}/{concept}.md`

### Progressive Knowledge Loading

Knowledge files use 4-section progressive disclosure. Choose the level that matches the task depth:

| Fragment | Loads | When to Use |
|----------|-------|-------------|
| `#key-takeaways` | Frontmatter + Key Takeaways | Quick reference or reminders when knowledge is already familiar |
| `#concepts` | Frontmatter + Key Takeaways + Concepts | Understanding concepts without detailed examples or procedures |
| (no fragment) | Entire file | Performing evaluation, review, or implementation that needs detection heuristics, examples, tables, and procedures |

**Rule of thumb:** If the agent needs to **find violations, detect patterns, or apply detailed criteria**, load the full document. If it only needs to **recall a principle or definition**, `#key-takeaways` is sufficient.

### Extraction Commands

```bash
sed '/^## Concepts/Q' file.md    # Frontmatter + Key Takeaways only
sed '/^## Content/Q' file.md     # Frontmatter + Key Takeaways + Concepts
cat file.md                       # Full document
```

Examples:
- `[[requirements/invest#key-takeaways]]`: quick reference for INVEST criteria
- `[[requirements/invest#concepts]]`: understanding what each letter means with context
- `[[software-craft/smell-catalogue]]`: full catalogue needed to detect code smells during review

## Discovery
Do not enumerate files, as they go stale. Discover what exists at runtime:

```bash
ls .opencode/agents/                    # agent identity definitions
ls .opencode/skills/                    # skill directories (each has SKILL.md)
find .opencode/knowledge -name '*.md'   # knowledge files
find .templates -name '*.template'   # artifact templates
find docs/research -name '*.md'          # research source notes (cited by knowledge files)
```

## File Naming Conventions

### Artifact Names in Flow Attrs

Artifact names in `in` and `out` lists use these conventions:

| Pattern | Meaning | Example |
|---------|---------|---------|
| `filename.md` | A specific document | `domain_spec.md`, `product_definition.md` |
| `dir/<param>.ext` | A specific instance identified by parameter | `features/<feature_title>.feature`, `.cache/interview-notes/<session_id>.md`, `adr/<adr_id>.md` |
| `dir/*.ext` | Multiple documents of that type available in `in` | `.cache/interview-notes/*.md`, `adr/*.md` |
| `conceptual_name` | A runtime artifact that passes between states within a flow | `typed-source-stubs`, `test-implementations` |

Placeholders in template filenames and flow artifact paths use the `<type_id>` pattern where **type** identifies the document kind and **_id** signals snake_case formatting. See template filenames for the canonical placeholder names.

**File naming rule:** All filenames use **snake_case** (e.g., `domain_value_objects.feature`, `ADR_20260504_protocol_adapters.md`). **Cache folders** use kebab-case for multi-word names (e.g., `interview-notes/`, `post-mortem/`). **Python/test folders** use snake_case (e.g., `tests/features/`).

**Wildcards (`*`)** in `in` indicate that multiple documents of that type are available. List the directory contents first, then read selectively based on the task. When a state creates a single instance, use a `<parameter>` name instead.

**Runtime artifacts** (not backed by files) use descriptive names that make their purpose clear: `typed-source-stubs` (source files with type signatures only), `test-skeletons` (test files with structure only), `test-implementations` (tests with bodies), `source-implementations` (production code with behavior), `refactored-source` (code after refactoring pass), `feature-commits` (git commits for one feature), `merged-commits` (commits merged to local dev), `root-cause-analysis` (analysis findings), `polished-source` (code after convention application).

**Cache artifacts** are persisted to `.cache/` for cross-session durability. They are not spec documents but process evidence that survives session boundaries: `.cache/acceptance/<feature_title>.md` (PO acceptance record with traceability matrix), `.cache/interview-notes/<session_id>.md` (raw stakeholder input, archival after discovery), `.cache/sim/simulation_results_<timestamp>.md` (simulation evidence per iteration).

**Environment artifacts** are produced by tooling rather than flow states: `coverage-reports` (test coverage output), `test-output` (test runner output), `linter-output` (linter output). These exist on disk after running the relevant tool and are referenced in `in` but not in any state's `out`.

## Flowr Commands

All commands output **JSON by default**. Use `--text` for human-readable output. All commands require the virtual environment: `source .venv/bin/activate`. See [[workflow/flowr-operations]] for full command reference, output formats, and workflow pattern.

Commands accept short flow names (e.g., `define-flow`) or full file paths. Use `--session <name>` to resolve flow/state from a session instead of specifying them explicitly.

| Command | Purpose |
|---------|---------|
| `python -m flowr check <flow> <state>` | Show state attrs, owner, skills, and transitions |
| `python -m flowr check <flow> <state> <target>` | Show conditions for a specific transition |
| `python -m flowr check --session` | Show current session state (read-only) |
| `python -m flowr check --session <trigger>` | Show conditions for a transition via session |
| `python -m flowr next <flow> <state> [--evidence key=value]` | Show all transitions with status markers (`open`/`blocked`) |
| `python -m flowr next --session [--evidence key=value]` | Show transitions from session state with status |
| `python -m flowr transition <flow> <state> <trigger> [--evidence key=value]` | Advance to the next state |
| `python -m flowr transition <trigger> --session [--evidence key=value]` | Advance using session (auto-updates session) |
| `python -m flowr validate [<flow>]` | Validate flow definition(s) |
| `python -m flowr validate --session` | Validate the current (sub)flow from session |
| `python -m flowr states <flow>` | List all states in a flow |
| `python -m flowr states --session` | List states in the current (sub)flow from session |
| `python -m flowr mermaid <flow>` | Export flow as Mermaid diagram |
| `python -m flowr config` | Show resolved configuration with sources |
| `python -m flowr session init <flow> [--name <name>]` | Create a session at the flow's initial state |
| `python -m flowr session show [--name <name>]` | Display current session state and call stack |
| `python -m flowr session set-state <state> [--name <name>]` | Manually update session state |
| `python -m flowr session list` | List all sessions |

## Project Commands

Check `pyproject.toml` for taskipy tasks and tool configuration. Common commands:

| Command | Purpose |
|---------|---------|
| `task test` | Run tests with short tracebacks |
| `task test-fast` | Run fast tests only (excludes slow marker) |
| `task test-build` | Run full test suite with coverage, hypothesis stats, and HTML report |
| `task run` | Run the application |

Linting and formatting:

| Command | Purpose |
|---------|---------|
| `ruff check .` | Functional lint (bugs, security, complexity) |
| `task conventions` | Full lint (all rules including naming, docstrings, formatting) |
| `ruff format .` | Auto-format |

## Session Protocol

Every state transition must go through flowr. Do not skip steps or guess transitions. See [[workflow/flowr-operations]] for the full command reference.

1. **State entry:** Run `python -m flowr check --session` to see current state, owner, skills, and available transitions (JSON output: parse `attrs.owner`, `attrs.skills`, `attrs.in`, `attrs.out`, `transitions`). Verify all `in` artifacts exist on disk. If any are missing, stop and flag rather than proceeding with assumed knowledge. Announce the state in one line, e.g. `→ specify-feature`. No preamble, no recap of how you got here.
2. **Dispatch to owner agent:** The state's `owner` field names the responsible agent. Call that agent as a subagent with the state's `skills` loaded, passing the state attrs as context. Owner mapping: `PO` → product-owner, `DE` → domain-expert, `SE` → software-engineer, `SA` → system-architect, `R` → reviewer, `Design Agent` → design-agent, `Setup Agent` → setup-agent.
3. **Do the work:** Load and execute the skill(s) listed in the state's `skills` field. Read all `in` artifacts before starting work — they are mandatory context. Write only to `out` artifacts. Commit changes to the branch indicated by the state's `git` attribute (`dev` or `feature`). Never switch branches mid-state.
4. **State exit:** The anchor item in the todo handles this (see [[workflow/todo-anchor-protocol#key-takeaways]]).

### Convention Boundary

Convention checks (full lint via `task conventions`, `ruff format`, pyright, docstrings, type annotations) are **prohibited** during design-phase states (create-py-stubs, write-test, implement-minimum, refactor, review-gate). Only `task test-fast` is permitted. The default `ruff check .` runs functional rules only (bug-catching, security, complexity). Design changes invalidate convention work. Conventions are applied in the polish state after feature acceptance.

When dispatching an agent during design phase:
- Do NOT include convention tool commands in the prompt
- Only include verification steps that the skill explicitly defines
- The skill's verification steps are the ceiling, not the floor

Exception: The polish-code skill explicitly runs convention commands (`task conventions`, `ruff format`, `task static-check`) after feature acceptance.

### Procedural Contract

**One state = one dispatch.** Every state transition produces exactly one agent dispatch with exactly the skills listed in the state's `skills` field. Never combine multiple states into a single dispatch. The orchestrator's job is routing, not doing. See [[workflow/todo-anchor-protocol#concepts]] for the full protocol.

### Todo-Driven State Execution

At state entry, generate a procedural todo list using the todowrite tool. Format: `[X]` completed, `[ ]` pending, `[~]` anchor (always last).

1. **Preparation** (`[ ]`): verify current branch matches `attrs.git` (checkout or create if wrong). List available `in` artifacts.
2. **Dispatch** (`[ ]`): dispatch to the owner agent listed in `attrs.owner` as a subagent with skills loaded. The orchestrator MUST NOT do the work itself — only route. Owner mapping: `PO` → product-owner, `DE` → domain-expert, `SE` → software-engineer, `SA` → system-architect, `R` → reviewer, `Design Agent` → design-agent, `Setup Agent` → setup-agent.
3. **Load skills** (`[ ]`): read every skill file listed in `attrs.skills` from `.opencode/skills/<skill_name>/SKILL.md`. This step is MANDATORY — never skip it.
4. **Skill-derived work items** (`[ ]`): one todo item per numbered step in the skill, using the skill's own language verbatim. These are the substantive work items. Self-generated items are only permitted for infrastructure (read artifacts, commit) — never for the core procedure.
5. **Output** (`[ ]`): one per `out` artifact
6. **Verification** (`[ ]`): check constraints, run tests/lint if applicable
7. **Anchor** (`[~]`, always last): flowr next → pick transition → flowr transition → rewrite todo

The todo is the execution contract. Every item must be marked `[X]` before the anchor fires. One state per todo; never span multiple states or collapse loop iterations. Full protocol: [[workflow/todo-anchor-protocol]].

**Todo discipline**: After completing ANY step, update the todowrite tool to mark it `[X]` and set the next step `[ ]` to `in_progress`. If the todo list is empty or missing, regenerate it immediately — working without a todo means working without a contract. Never let the todo go stale between steps.

### Session Init

Before starting a flow, create a session to track progress:

```bash
python -m flowr session init <flow> --name <name>
```

For project-level flows, use a descriptive name like `project`. For feature flows, use the feature name. The session tracks the current flow, state, call stack (for subflows), and params (including `feature-id`). When the first state has a `flow:` field, `session init` auto-enters the subflow.

The three primary flows are independently invocable:
- `define-flow` — spec creation, validation, feature refinement, and architecture (discovery → spec-validation → refine-features → architecture)
- `develop-flow` — feature selection, example writing, TDD implementation, acceptance (per feature cycle)
- `deliver-flow` — squash-merge, publish decision, PR creation

### Cross-Flow Routing

When develop-flow exits `needs-architecture`, the orchestrator must re-enter define-flow at the `architecture` state. Start a new define-flow session and use `flowr session set-state architecture` to skip to the architecture state. The architecture-flow fast-path (`architecture-complete: ==verified`) means re-running is cheap when no changes are needed.

When post-mortem-flow exits `needs-architecture`, follow the same procedure: re-enter define-flow at `architecture`.

### Branch Discipline

States declare their git context in `attrs.git`:
- `git: dev`: all changes are committed to the local dev branch
- `git: feature`: all changes are committed to the current feature branch

Before exiting a project-phase flow (define, branding, setup), the exit transition requires `committed-to-dev-locally: ==verified` evidence. This guarantees project artifacts are persisted before advancing to the next phase.

### Within a State

Announce the state once at the top, then go quiet:

- **Respect the artifact contract:** The state's attrs define what the owner agent may read and write:
  - `in`: Mandatory context. All `in` artifacts must be read in full before starting work. For wildcard patterns (`*.md`), list the directory first, then read all discovered files. The `in` list defines what you *must* read — no skipping, no selective reading.
  - `out`: May create or edit. Section sub-lists indicate which sections the state should produce or update. Follow the **out artifact protocol** (see below).
  - Files not in `out` must not be written to. If findings affect an artifact outside the output contract, flag them in output notes and defer the change to the step that owns that artifact.
  - The flow contract must always be followed unless the stakeholder explicitly asks to break it.
  - **Cumulative editing:** When a flow loops back to a state that was previously executed (e.g., `needs-reinterview` → `stakeholder-interview` → `domain-discovery`), the `out` artifact is **edited**, not recreated. The agent reads the existing file, incorporates new information, and adjusts existing content. This is especially important for `domain_spec.md` and `glossary.md` which accumulate knowledge across multiple discovery iterations.
- **Out artifact protocol:** Before writing to any `out` artifact:
  1. Check if the file exists on disk.
  2. **If it exists** → read it, then edit only the sections declared in the flow's `out` section sub-lists. Preserve existing content outside those sections.
  3. **If it does not exist** → resolve the template path: take the destination path, prepend `.templates/`, append `.template` (e.g., `docs/spec/domain_spec.md` → `.templates/docs/spec/domain_spec.md.template`). Copy the template to the destination path, then edit the declared sections. Strip any template placeholders during editing.
  4. **If no template exists** for a non-Python file referenced in `in`/`out`, raise an error for the stakeholder to decide.
  5. **Environment artifacts** (e.g., `coverage-reports`, `test-output`, `linter-output`) are produced by tooling rather than flow states. They exist on disk after running the relevant tool and are referenced in `in` but not in any state's `out`.
- **Specification documents are read-only during development.** During TDD and review cycles, the SE and reviewer may ONLY modify production code and test code. Spec document inconsistencies must be FLAGGED in output notes, not fixed directly. Spec docs are owned by other flow states and can only be changed through the appropriate flow step, after code is reviewed and approved.
- **Flag issues with precise citations.** When flagging a problem during review or adversarial analysis, include file:line references (e.g., "domain_spec.md:23 conflicts with login.feature:15"). Vague findings create rework.
- **Do the work with the fewest, quietest commands.** Suppress verbose output. If a command can be scoped with a flag, pipe, or limit, use it. Don't dump full files or directory listings when a targeted query answers the question.
- **No narration between steps.** The command and its output are the conversation. Don't echo what you're about to do or what you just did.