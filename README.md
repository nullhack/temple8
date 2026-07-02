# temple8

> A Python project **methodology template** — a ready-to-clone foundation that
> wires the staged-contract development workflow into a new project, with the
> flow set, the agents/skills/knowledge methodology layer, CI, and tooling
> pre-configured. temple8 itself is not an application; an instance built from
> it holds the package, tests, and instance docs.

## Purpose

temple8 exists to make one workflow reproducible across Python projects: tests
are authored up front as a staged contract surface (test `.pyi` → test `.py`
marked pending → source `.pyi` → simulate), then built out one contract per
cycle under flowr orchestration, with the methodology layer (agents, skills,
knowledge), the drift gates (pyright, `mypy.stubtest`, ruff, pytest), and CI
already in place. Cloning the template removes the bootstrap cost of
re-establishing that workflow each project.

## Scope

**In** — the methodology only: flow definitions, the agent/skill/knowledge
layer, document templates, CI, the conftest pending-marker hook, and the
pyproject tooling.

**Out** — everything an instance owns: an application package, tests,
migrations, cassettes, `docs/glossary.md`, `docs/state.md`. These live in a
project instantiated from this template, not in temple8 itself. The `app`
references in `pyproject.toml` (`[tool.setuptools] packages`, task targets) are
placeholders for whatever package name the instance chooses.

## How to run

temple8 is not run as an application — it is used as a template for one.

1. Clone or copy this tree into a new project directory.
2. Create the package (replacing the `app` placeholder) and the test layout
   (`tests/integration/`, `tests/e2e/`, `tests/cassettes/`, `tests/fixtures/`);
   there is no `tests/unit/` by policy.
3. Drive the staged-contract pipeline one state at a time with flowr:

   ```
   uv run python -m flowr session init pipeline-flow --name default
   uv run python -m flowr check --session default
   uv run python -m flowr next --session default
   uv run python -m flowr transition <trigger> --session default
   ```

A reference usage — a weather-lookup CLI driven through the full pipeline —
lives outside the template tree; see the clean-slate rebuild notes.

## Secrets

Secrets (API keys, tokens, passwords) never live in the repo. The split:

- **Non-secret config** — base URLs, regions, feature flags — in the workspace
  `.env` (gitignored), loaded with `load_dotenv()` into `os.environ`.
- **Secrets** — in `~/.secrets/<project>.env`, *outside* the repo tree, loaded
  with `dotenv_values()` straight into a frozen typed `Settings` and **never**
  into `os.environ` (so `env`, `printenv`, and `/proc` cannot see them).
- **`.env.example`** is committed: every variable name, non-secret defaults
  filled, secret lines empty with a pointer to `~/.secrets/`.

Instance authors add one opencode permission rule so a direct read of the
secrets path prompts the user instead of passing silently:

```json
{ "permission": { "external_directory": { "~/.secrets/**": "ask", "*": "allow" } } }
```

Agents in this workflow never create or debug a secret: they instruct the user
how to obtain and place each credential, and on an auth failure they ask with
suggestions instead of investigating the value. The full threat model and
layered defense are in the `secrets-and-config` knowledge.

## Where things live

| Path | Holds |
|---|---|
| `.flowr/flows/` | the six flow definitions — `pipeline-flow` plus the five subflows |
| `.opencode/agents/` | role identities (who owns what decision) |
| `.opencode/skills/` | per-state procedures (one per state) |
| `.opencode/knowledge/` | reference and explanation — `methodology/`, `requirements/`, `software-craft/` |
| `.templates/` | document templates — glossary, state (living spec), README, research card |
| `.github/workflows/` | CI — ruff + flowr validate always on; pyright/stubtest/pytest guarded on package+tests |
| `conftest.py` | the `@pytest.mark.pending` skip hook (the backlog signal) |
| `pyproject.toml` | tooling — ruff (bug-catcher select, no docstrings), pytest markers, taskipy, stubtest |
| `docs/research/` | human-reference sources behind the knowledge citations |
| `AGENTS.md` | the methodology brief, routing, and flowr commands |
| `TODO.md` | what is owed and forward-planned |

## Workflow

The staged-contract pipeline runs discover → explore → plan → build → deliver
→ shipped, driven one state at a time through flowr:

- **discover** — interview funnel elicits requirements and authors the glossary;
- **explore** — every external service is grounded by recording real exchanges
  as vcrpy cassettes (the authoritative external contract);
- **plan** — tests are authored up front (`.pyi` → `.py` marked pending → source
  `.pyi` derived) and simulated before any source is built;
- **build** — each source contract is implemented one cycle at a time
  (red → green → refactor → review → ship) from its fixed `.pyi`;
- **deliver** — feature commits squash-merge into dev under the whole-suite
  gates, then publish.

Tests are the source of truth for behaviour. See `AGENTS.md` for the full
lifecycle, the gate evidence keys, and the flowr commands.
