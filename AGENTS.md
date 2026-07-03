# AGENTS.md

A Python project with the staged-contract workflow wired in (flow set,
agents/skills/knowledge, CI, tooling). Drive the pipeline one state at a time
through flowr.

## Operating discipline

1. **flowr is the single router.** Every state change runs through flowr — no improvised routing, no skipping states.
2. **The owner does the work.** Each state names one owner in `dispatch_to`; the orchestrator dispatches it, and the owner produces the artifacts and asserts the evidence. The orchestrator never authors the work.
3. **The state's contract is binding.** Read every `input artifact` before starting — missing means stop, not assume. Write only to `output artifacts`.
4. **Assert only verified evidence; CI is the backstop.** A gate fires on the owner's asserted evidence; assert nothing you did not check — CI catches the lie (`ruff` / `pyright` / `mypy.stubtest` / `pytest`).
5. **Branch discipline.** Match the state's `git branch`; merge `feature` → `dev` only under the whole-suite gates. No dangling branches.
6. **Every requirement traced.** Each interview finding maps to a test or an explicit deferral; an untraced requirement is a gap the simulate gate rejects.

## Driving a state

One state at a time. The orchestrator keeps **one todo per state, regenerated at
state entry** — the todo *is* this five-phase loop. "No todo = no work": work
outside the loop is untracked. One state per todo; regenerate on every
transition.

1. **Read** — `flowr check --session <id>`; parse `dispatch_to`, `skills`, `input artifacts`, `output artifacts`, `git branch`, `conditions`.
2. **Verify inputs** — every `input artifact` exists on disk. Missing = stop (discipline 3).
3. **Dispatch** — call the `dispatch_to` owner with the `skills` paths (`.opencode/skills/<name>/SKILL.md`) and the input artifacts. The owner writes only to `output artifacts` and returns asserted evidence.
4. **Verify outputs + evidence** — the `output artifacts` were produced and the transition's `conditions` evidence is real (discipline 4).
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
refactor → review → ship); **deliver** squash-merges to dev and publishes.
`@pytest.mark.pending` is the backlog signal (new work + rework); an empty
backlog is done. flowr's gates collect EVIDENCE the agent asserts; CI is the
enforcement backstop (ruff / pyright / `mypy.stubtest` / pytest). When prose and
a test disagree, the test wins.

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
| `.flowr/flows/` | flow definitions |
| `.opencode/`, `.templates/`, `.github/` | methodology, templates, CI |

Gitignored (local working state, regenerated on demand):

| Path | Holds |
|------|-------|
| `.cache/<session_id>/` | interview notes, external contracts, probe research, build target |
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

The flow binds each state to its owner (`dispatch_to`), procedure (`skills`),
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
