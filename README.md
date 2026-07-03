# temple8

> A Python project **methodology template** — a copier template that wires the
> staged-contract development workflow into a new project, with the flow set, the
> agents/skills/knowledge methodology layer, CI, and tooling pre-configured.
> temple8 itself is not an application; an instance built from it holds the
> package, tests, and instance docs.

## What it is

temple8 makes one workflow reproducible across Python projects: tests are
authored up front as a staged contract surface (test `.pyi` → test `.py` marked
pending → source `.pyi` → simulate), then built out one contract per cycle under
flowr orchestration, with the methodology layer (agents, skills, knowledge), the
drift gates (pyright, `mypy.stubtest`, ruff, pytest), and CI already in place.
Instantiating the template removes the bootstrap cost of re-establishing that
workflow each project.

## Instantiate a project

temple8 is a [copier](https://copier.readthedocs.io/) template. To start a new
project from it:

```
uv tool install copier
copier copy gh:nullhack/temple8 my-project
```

Answer the questionnaire (project and package name, description, author,
version, repo URL, optional git reset, and which optional layers to keep).
Copier renders `pyproject.toml` + the README, creates the package and the test
skeleton, and hands you a fresh repo ready for the first `flowr session init`.

The `project-instantiator` agent and its `instantiate-project` skill (in
`.opencode/`) guide the same flow end to end — gather the parameters, run the
copy, verify, and start the first pipeline session. They live in the template
and are excluded from instances.

## Scope

**In** — the methodology only: flow definitions, the agent/skill/knowledge
layer, document templates, CI, the conftest pending-marker hook, the copier
template, and the pyproject tooling.

**Out** — everything an instance owns: an application package, tests,
migrations, cassettes, `docs/glossary.md`, `docs/state.md`. These live in a
project instantiated from this template, not in temple8 itself.

## What an instance gets

- `pyproject.toml` rendered with the project's name, package, and tooling.
- a fresh `README.md` from the instance template.
- `<package>/__init__.py` and the `tests/{integration,e2e,cassettes,fixtures}/` skeleton.
- `.env.example` (the committed env contract).
- the whole methodology layer (`.opencode/`, `.flowr/`, `.templates/`) verbatim.
- a fresh git history (optional, default on).

Optional layers an instance may keep or drop at instantiation: the `design/`
knowledge + asset templates (for projects with a UI surface) and `docs/research/`
(the source-card reference library behind the knowledge citations).

## Where things live

| Path | Holds |
|---|---|
| `copier.yml` | the instantiation questionnaire + tasks |
| `pyproject.toml.jinja`, `README.md.jinja` | the rendered instance files |
| `.flowr/flows/` | the six flow definitions |
| `.opencode/` | agents, skills, knowledge (methodology, requirements, software-craft, workflow, architecture, writing, design) |
| `.templates/` | document templates — glossary, state, research card, ADR, `.env.example`, social-card, logo |
| `.github/workflows/` | CI — ruff + flowr validate always on; pyright/stubtest/pytest guarded on package+tests |
| `docs/research/` | human-reference sources behind the knowledge citations |

## Workflow

The staged-contract pipeline runs discover → explore → plan → build → deliver →
shipped, driven one state at a time through flowr. See `AGENTS.md` for the full
operating discipline, the driving loop, and the flowr commands.
