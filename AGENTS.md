# AGENTS.md

temple8 — Python project template.

This branch (`refactor/clean-slate`) is a clean-slate rebuild. The previous
spec-driven orchestration layer — `flowr`, `beehave`, the agent/skill/knowledge
tree, `.flowr/`, `.templates/`, `docs/` — was removed from the working tree and
preserved locally in `.backup/` (gitignored), fully recoverable from
`origin/main`. The rebuild re-introduces pieces selectively and authored fresh:
the flow set and the `.opencode/` methodology layer (agents, skills, knowledge)
are rebuilt against the new staged-contract workflow; the `beehave`/BDD layer is
dropped; `.templates/` and `docs/` are forward-planned.

## Workflow

Tests are the source of truth. Discovery elicits requirements via the interview
funnel; explore empirically grounds every external service (read docs, run
authenticated probes, record real request/response shapes as vcrpy cassettes —
the authoritative external contract); plan authors the tests up front —
integration and E2E only — as a staged contract surface: test `.pyi` (signatures
expressing the domain), then the test `.py` bodies (no docstrings, no comments;
the body is the spec; each test marked `@pytest.mark.pending`), then the source
`.pyi` derived from what the tests reference. Build implements each source `.py`
from its `.pyi` to make the already-written tests pass (red removes the target's
pending mark); tests are otherwise not edited during build. The
`@pytest.mark.pending` mark is the backlog signal (covers new work and rework);
the built/pending ratio (source contracts with vs without a pending test) is the
progress record; an empty backlog is "done". Stubs (`.pyi`) are the cheap
signature view: read the target's `.pyi` first and open a `.py` only for the
detail its stub omits. `mypy.stubtest` is the drift detector for BOTH source
and test `.pyi` (gated at simulate for tests, green/review/merge for source).
flowr's gate `conditions` collect EVIDENCE the dispatched agent asserts
(`stubtest-clean=true`, etc.); flowr does not run the checks itself. CI is the
enforcement backstop: it runs `ruff` (with `PYI`), `pyright`, `mypy.stubtest`,
and `pytest` on every push and fails the build on any drift or violation,
verifying what the agent asserted. When prose and a test disagree, the test wins.

We write integration tests (config, external adapters, APIs, databases) and
E2E tests (CLI, object composition, contract chaining) only; no unit tests.
Code (source, tests, stubs) carries no docstrings during development —
`D`/pydocstyle is dropped and docstrings are never authored (token economy).
Tests depend on contracts, never internals. They are held to production-grade
standards (SOLID, YAGNI, Object Calisthenics, DRY, KISS, no smells).

Concerns tests exercise but cannot store live in exactly one authoritative
artifact, never duplicated in prose: DB relationships and data shape live in
ORM models + Alembic migrations (the migration IS the schema spec); config
parameter definitions live in a typed Settings model; external-adapter
contracts live in recorded fixtures/cassettes (captured during explore). A lean
glossary of ubiquitous language drives naming.

Routing is one flow with five subflows: `pipeline-flow` orchestrates
`discovery-flow` + `explore-flow` + `plan-flow` + `tdd-flow` + `deliver-flow`. Drive it one state at a time:

| Command | Purpose |
|---------|---------|
| `uv run python -m flowr session init pipeline-flow --name default` | Start |
| `uv run python -m flowr check --session default` | Current state attrs + transitions |
| `uv run python -m flowr next --session default` | Open/blocked transitions |
| `uv run python -m flowr transition <trigger> --session default` | Advance |

Lifecycle: `discover` (interview funnel → glossary) → `explore` (ground
external services → vcrpy cassettes) → `plan` (author test `.pyi` → review test
`.pyi` → write test `.py` (marked `@pytest.mark.pending`) → derive source `.pyi`
→ simulate) → `build` (per source stub: red → green → refactor → review → ship)
→ `deliver` (merge to dev → publish) → `shipped`. Build escalates back to
`plan` on a contract gap; `plan` and `explore` escalate to `discover` when the
interview itself is insufficient. See `TODO.md` for what's owed.

## Project layout

Committed (the source of truth):

| Path | Holds |
|------|-------|
| `<package>/` | source — `.pyi` stubs + `.py` bodies |
| `tests/integration/`, `tests/e2e/` | integration + E2E tests only (no unit) |
| `tests/cassettes/` | recorded vcrpy cassettes — the external contract |
| `tests/fixtures/` | test fixtures |
| `migrations/` | Alembic migrations — the schema spec |
| `docs/glossary.md` | ubiquitous language |
| `.flowr/flows/` | flow definitions |
| `.opencode/`, `.templates/`, `.github/` | methodology, templates, CI |

Gitignored (local working state, regenerated on demand):

| Path | Holds |
|------|-------|
| `.cache/<session_id>/` | interview notes, external contracts, probe research, build target |
| `.cache/explore/` | throwaway probe scripts (run once to record cassettes; never imported) |
| `.cache/sessions/` | flowr session state |
| `.backup/` | previous system (recoverable from `origin/main`) |
| `.env` | non-secret local config (12-factor) |
| `~/.secrets/<project>.env` | secrets (out-of-workspace; `dotenv_values()` into a frozen Settings, gated by opencode `external_directory`) |

## Agents, skills & knowledge

The methodology layer lives under `.opencode/` (not loaded every session —
discovered on demand):

| Path | Holds | Loaded |
|------|-------|--------|
| `.opencode/agents/{role}.md` | Role identity (who I am, what I decide) | When the role is dispatched |
| `.opencode/skills/{skill}/SKILL.md` | Procedure (how to do the work) | When a state's `skills` names it |
| `.opencode/knowledge/{domain}/{concept}.md` | Reference & explanation (what and why) | On demand, via wikilinks |

Discover rather than enumerate:

    ls .opencode/agents/
    ls .opencode/skills/
    find .opencode/knowledge -name '*.md'

The flow binds each state to its owner (`dispatch_to`), its procedure
(`skills`), and its artifacts (`input artifacts` / `output artifacts`); the
agent, skill, and knowledge files stay single-concern and free of routing.
Wikilinks cite knowledge on demand: `[[domain/concept]]` resolves to
`.opencode/knowledge/{domain}/{concept}.md`, and a `#section` fragment selects
how deep to load (`#key-takeaways`, `#concepts`, or the whole file). Authoring
conventions live in the `methodology/` knowledge domain.

## Project commands

Tasks are defined in `pyproject.toml` under `[tool.taskipy.tasks]`. The `app/`
package is the placeholder, so package-dependent commands (`task run`,
`task test`, `task stubtest`, ...) resolve only once the package is created.

| Command | Purpose |
|---------|---------|
| `task test` | Run tests |
| `task test-fast` | Fast tests only |
| `task lint` | ruff check + format check |
| `ruff format .` | Auto-format |
