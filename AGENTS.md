# AGENTS.md

A Python project with the staged-contract workflow wired in (flow set,
agents/skills/knowledge, CI, tooling). Drive the pipeline one state at a time
through flowr.

## Binding constraints

1. **flowr is the single router.** Every state change runs through flowr — no improvised routing, no skipping, no pre-empting a later state's work. One state's work is exactly its `output artifacts`; the next begins only when the orchestrator transitions.
2. **The orchestrator dispatches; the dispatched agent does the work.** The orchestrator MUST invoke the state's `dispatch_to` agent — it never authors the work. The handoff gives the agent: `skills` paths, `input artifacts`, `output artifacts` (write only here), and the evidence keys to assert. The agent produces the artifacts and asserts evidence; it does not transition.
3. **The state's contract is binding.** Read every `input artifact` before starting — missing means stop, not assume. Write only to `output artifacts`.
4. **Assert only verified evidence; CI is the backstop.** On a **guarded** transition flowr fires only on the dispatched agent's asserted evidence (`--evidence k=v`); assert nothing you did not check — CI catches the lie (`ruff` / `pyright` / `mypy.stubtest` / `pytest`). **Unguarded** transitions (discovery, explore) carry no flowr gate — the orchestrator verifies the output artifacts and the stakeholder's approval IS the gate.
5. **Branch discipline.** Match the state's `git branch`: discovery/explore/plan/deliver run on `dev`; build runs on `feature/<session_id>`, cut from dev at build entry. The contract surface is committed to `dev` at plan; the feature branch carries only the source implementation. Squash-merge `feature/<session_id>` → `dev` only under the whole-suite gates, then delete the branch. No dangling branches.
6. **Every requirement traced.** Each interview finding maps to a test or an explicit deferral; an untraced requirement is a gap the simulate gate rejects.
7. **Only the orchestrator transitions.** Producing artifacts is not finishing — the orchestrator's verified `flowr transition` is. A dispatched agent never runs `flowr transition` / `flowr session`, never assumes the next state, never declares the flow done.
8. **Todo-first.** The first action on entering a state is to create its one-state todo (the loop below). No todo = no work. Only the orchestrator holds the todo; regenerate it after every transition.

## Driving a state

**Two hats.** AGENTS.md addresses the **orchestrator** — the agent holding the flowr session that drives state to state. A **dispatched agent** (invoked via a state's `dispatch_to`) does one state's work and returns. Its operating contract is ordered and mandatory:

- **(0) Load the named skill** via the `skill` tool — the skill is the procedure; do not improvise.
- **(1) Execute the skill's Load step** — resolve every `[[wikilink]]` and Read each cited knowledge file before any other step. The skill and its knowledge citations ARE the method; skipping them collapses the work to the agent's native lens.
- **(2) Follow the skill's steps in order** — read every `input artifact`, write only to `output artifacts`, assert only verified evidence.
- **(3) Never transition, skip, or hold the todo** — produce, return, stop (7).

If you were invoked to do a state's work, you are the dispatched agent.

One state at a time. The orchestrator keeps **one todo per state** — the todo *is* this loop:

0. **Create the todo** — `todowrite` the phases below before any other action (8).
1. **Read** — `flowr check --session <id>`; parse `dispatch_to`, `skills`, `input artifacts`, `output artifacts`, `git branch`, `conditions`.
2. **Verify inputs** — every `input artifact` exists on disk. Missing = stop (3).
3. **Dispatch** — invoke `dispatch_to` with a handoff whose **first instruction** is to load the skill and follow it. Use this template verbatim, filling the slots from `check`:

   > Load the skill `<skills[0]>` via the `skill` tool and follow its steps in order, beginning with its Load step — resolve every `[[wikilink]]` and Read each cited knowledge file before working.
   > Inputs (read all): `<input artifacts>`. Outputs (write only here): `<output artifacts>`. Evidence keys to assert (guarded only): `<conditions keys>`. Boundary: do only this state's work; do not transition, skip, or hold the todo — the orchestrator moves the flow (2, 7).

   It returns the output artifacts and asserted evidence.
4. **Verify outputs + evidence** — the `output artifacts` were produced; if the transition is guarded, its `conditions` evidence is real (4).
5. **Transition** — `flowr transition <trigger> --session <id> --evidence k=v …`, then regenerate the todo from the next state's `check`.

Routing is one flow with five subflows: `pipeline-flow` → discovery → explore →
plan → build → deliver → shipped. Escalations re-enter the target subflow at its
first state (no position memory): build → plan on a contract gap; plan/explore →
discover on insufficient elicitation. Gate evidence keys + the full
session/subflow mechanics: [[workflow/flowr-operations]].

| Command | Purpose |
|---------|---------|
| `uv run python -m flowr session init pipeline-flow --name <id>` | Start |
| `uv run python -m flowr check --session <id>` | State attrs + transitions |
| `uv run python -m flowr check --session <id> <trigger>` | A transition's conditions |
| `uv run python -m flowr next --session <id>` | Open / blocked transitions |
| `uv run python -m flowr transition <trigger> --session <id> --evidence k=v` | Advance |

## Parsimony

Fewest, quietest commands — suppress verbose flags, scope to the target (read
the `.pyi` before the `.py`). No narration: command + output is the
conversation, not a running commentary. Cite precisely (`file:line`), never
vague. Do not repeat yourself — each fact stated once, in its canonical home
(the flow, the knowledge, the test, the ADR), and cited elsewhere. Scrub AI
markers (`delve`, `tapestry`, `rather than`, `plays a crucial role`) from
authored prose per [[writing/ai-language-markers]]. Maximise signal; minimise
tokens.

## Workflow

Tests are the source of truth. The pipeline authors a staged contract surface,
then builds it: **discover** elicits requirements (interview funnel → glossary);
**explore** grounds external reality (vcrpy cassettes — the authoritative
external contract); **plan** writes tests up front (`*_test.pyi` → `*_test.py`
`@pytest.mark.pending` → source `.pyi` → simulate); **build** implements each
source `.py` from its fixed `.pyi` one contract per cycle (red → green →
refactor → review → ship); **deliver** squash-merges the feature branch to dev
(then deletes it), optionally publishes on approval, and **refresh** closes the
cycle:
regenerates `docs/state.md` from the current tests, summarizes the carry-over
cache files to ~1000 words so the next cycle starts compact, and closes the
docstring lifecycle (regenerate the public source surface then strip all `.py`
— source and test — docstring-free for the next cycle). Rework enters the backlog from two trigger sources: build-escalation
findings in the journal, and discovery findings in the interview that flag a
modification to an existing block; both surface as `@pytest.mark.pending` at
plan so `select-build-target` pulls them. An empty backlog is done. flowr's
gates collect EVIDENCE the agent asserts; CI is the enforcement backstop (ruff /
pyright / `mypy.stubtest` / pytest). When prose and a test disagree, the test
wins.

Authoring detail (staged contracts, evidence vs enforcement, the docstring/lint
lifecycle, separation-of-concerns, secrets/config) lives in the knowledge layer
— discover it, do not restate it here.

## Project layout

Committed (the source of truth):

| Path | Holds |
|------|-------|
| `<package>/` | source — `.pyi` stubs + `.py` bodies |
| `tests/integration/`, `tests/e2e/` | integration + E2E tests only (no unit) |
| `tests/cassettes/`, `tests/fixtures/` | recorded vcrpy cassettes; fixtures |
| `migrations/` | Alembic migrations — the schema spec |
| `docs/glossary.md` | ubiquitous language |
| `docs/state.md` | living specification — regenerated each cycle by refresh from the tests |
| `.flowr/flows/` | flow definitions |
| `.opencode/`, `.templates/`, `.github/` | methodology, templates, CI |

Gitignored (local working state, regenerated on demand):

| Path | Holds |
|------|-------|
| `.cache/<session_id>/` | interview notes, external contracts, data model, journal (carry-over, summarized to ~1000 words at cycle close); build target, probe target/research (transient per-pass) |
| `.cache/explore/` | throwaway probe scripts (run once; never imported) |
| `.cache/sessions/` | flowr session state |
| `.env` | non-secret local config (12-factor) |
| `~/.secrets/<project>.env` | secrets (out-of-workspace; `dotenv_values()` into a frozen Settings; opencode `external_directory`-gated) |

## Agents, skills & knowledge

Under `.opencode/` (loaded on demand, not every session):

| Path | Holds |
|------|-------|
| `.opencode/agents/{role}.md` | role identity (who I am, what I decide) |
| `.opencode/skills/{skill}/SKILL.md` | per-state procedure (how to do the work) |
| `.opencode/knowledge/{domain}/{concept}.md` | reference & explanation (what and why) — domains: `methodology/`, `requirements/`, `software-craft/`, `workflow/`, `architecture/`, `writing/`, `design/` |

Discover rather than enumerate:

    ls .opencode/agents/
    ls .opencode/skills/
    find .opencode/knowledge -name '*.md'

The flow binds each state to its dispatched agent (`dispatch_to`), procedure (`skills`),
and artifacts (`input artifacts` / `output artifacts`); agents, skills, and
knowledge stay single-concern and free of routing. Wikilinks cite knowledge on
demand: `[[domain/concept]]` resolves to `.opencode/knowledge/{domain}/{concept}.md`,
and a `#section` fragment selects depth. Authoring conventions live in the
`methodology/` domain.

## Project commands

Tasks are defined in `pyproject.toml` under `[tool.taskipy.tasks]`. Package-dependent commands (`task run`, `task test`, `task stubtest`, …) target the package named in `[tool.setuptools] packages`.

| Command | Purpose |
|---------|---------|
| `task test` | Run tests |
| `task test-fast` | Fast tests only |
| `task lint` | ruff check (dev: bug-catchers only) |
| `task lint-merge` | merge: + SIM/RUF + ruff format |
| `task strip-docstrings` | strip docstrings from a source .py (tdd select) |
