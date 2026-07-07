<div align="center">

<img src="docs/assets/banner.svg" alt="temple8" width="100%"/>

<br/><br/>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=for-the-badge)](https://nullhack.github.io/temple8/coverage/)
[![CI](https://img.shields.io/github/actions/workflow/status/nullhack/temple8/ci.yml?style=for-the-badge&label=CI)](https://github.com/nullhack/temple8/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-%E2%89%A53.13-blue?style=for-the-badge)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-10.0.0-5c3d1e?style=for-the-badge)](https://github.com/nullhack/temple8/releases)

**From spec to shipped: state-machine orchestration for spec-driven agent work. Any workflow. Any LLM. Zero lock-in.**

</div>

---

You have tried to ship features with AI assistants. The agent writes code, you review it, and somehow the spec still drifts from the implementation. Tests pass but the feature doesn't match what stakeholders asked for. Architecture decisions vanish into commit messages nobody reads. The review cycle is a black box: either everything passes or nothing does, with no structured progression. And the spec itself is never tested — a contract surface that two implementations could satisfy, or that no implementation could, sails through review undetected.

**temple8 replaces ad-hoc agent orchestration with state machines that route every step through the right agent with the right skills at the right time, and treats the contract surface itself as a compiler would: simulated end-to-end before any source exists.**

Flow definitions in YAML declare what happens at each state: who owns it, what they may read, what they must produce, and which conditions gate the next transition. No agent guesses what to do next. No step is skipped. Artifacts are scoped to each state's input/output contract. The contract is *compiled* — simulated hop-by-hop against the data model and the requirements — so a spec that two implementations could satisfy, or that one cannot, is caught before a single source file is written.

---

## Who is this for?

### Developers moving from vibe coding to agentic engineering

You have shipped code with AI assistants and hit the wall: the agent writes code, you review it, the spec drifts. Vibe coding works for prototypes. It breaks at scale. temple8 replaces "prompt and pray" with spec-driven development: BDD scenarios from interviews, title-based traceability from Example to test function, red-green-refactor cycles enforced by default, a compiler-style simulation gate that disconfirms specs before code, and three-tier review that catches what linters miss — including vacuous assertions that pass without asserting anything.

### Teams wanting structured agent orchestration without lock-in

Your team follows a real methodology: Scrum, Kanban, SAFe, or something custom. Multi-agent orchestration should adapt to it, not the other way around. temple8 flows are YAML state machines you define, extend, or replace. Named specialists per state. No subscription, no vendor account, no code leaving your infrastructure. MIT licensed.

### Anyone evaluating spec-driven development

Spec-driven development is gaining traction across AI coding tools. You want to try it without committing to a cloud IDE or a monthly subscription. temple8 is a project template: clone it, run it locally with any LLM, see if the process discipline works for your team. Already have a Python project? Use [agents-smith](https://github.com/nullhack/agents-smith) to add temple8's agentic capabilities with one command.

---

## What it does

```
flowr check      →  inspect a state's owner, skills, and transitions
flowr next       →  see which transitions pass given your evidence
flowr transition →  advance to the next state with evidence
```

**State machines route the work.** YAML flows define the delivery pipeline: discovery, exploration, data modeling, planning, TDD cycles, review gates, delivery. Each state declares an owner, skills, input/output artifacts, and guard conditions. The engine validates transitions. The agent executes.

**Workflows are configurable.** The default flows cover spec-driven software development. Replace or extend them for your team's process: Kanban, SAFe, ITIL, or any custom pipeline. If it is a state machine, flowr can express it.

**Agents execute it.** Each state's `owner` dispatches to the right specialist — Product Owner, System Architect, Data Architect, Software Engineer, Reviewer, Release Engineer — loaded with the skills and knowledge the state names. Input/output contracts constrain scope. Evidence gates prevent premature transitions.

**Branch discipline is explicit.** Every state declares `git: main` or `git: feature`. Project-phase work commits to main. Feature work commits to a feature branch. No ambiguity about where changes belong.

**The contract is compiled, not just validated.** Before any source `.py` exists, `simulate-contracts` walks the staged contract surface hop-by-hop — the way a compiler walks an AST — simulating how the real app would run against the data model and the requirements, and journaling one observation per hop. Spec-diff catches what two implementations could both satisfy. Build-implied gaps catch effects with no mechanism, side effects no observer sees, and models that disagree. A spec that survives this gate is a spec worth building.

**Data is modeled before it is planned.** A dedicated `model-data-schema` state runs at plan entry: the Data Architect classifies the workload (OLTP / OLAP / hybrid), authors `data-model.md` as a binding contract, and traces every field to a stakeholder need. Downstream states — test stubs, source stubs, simulation — read it as a required input. No more "we built the contract surface, then discovered the schema was wrong."

**Simplicity is a traced requirement.** Each interview funnel level asks a simplicity question — smallest surface, speculative vs grounded, load-bearing vs collapsible — and `consolidate-interview` drops speculative items before they become contracts. The `review-test-stubs` gate runs an inverted-traceability check (every test maps to a finding, or it goes) alongside a vacuous-assertion sweep that names five smells: hasattr-only, no-op helper, lower-bound-only, constant-satisfiable, tautology. A contract surface that survives this is neither over- nor under-engineered.

**Replay is unambiguous.** HTTP adapters replay through `vcr.use_cassette()`; CLI subprocess tests use `pytester`; library-boundary adapters (ddgs, primp) use `monkeypatch`. The skill layer names the kind and the fixture — no agent picks the wrong replay mechanism again.

---

## Quick start

### New project from the copier template

temple8 is a [copier](https://copier.readthedocs.io/) template. `copier copy`
renders `pyproject.toml` + a fresh `README.md`, creates the package and the
test skeleton, and hands you a new repo ready for the first
`flowr session init` — without inheriting temple8's own git history.

```bash
uv tool install copier
copier copy gh:nullhack/temple8 my-project
cd my-project
curl -LsSf https://astral.sh/uv/install.sh | sh  # skip if uv is already installed
uv sync --all-extras
opencode && @setup-project                        # personalise for your project
uv run task test && uv run task lint && uv run task static-check
```

Answer the questionnaire (project and package name, description, author,
version, repo URL, optional git reset, and which optional layers to keep —
design knowledge + asset templates, and the `docs/research/` reference
library). The `project-instantiator` agent and its `instantiate-project` skill
(in `.opencode/`) guide the same flow end to end — gather the parameters, run
the copy, verify, and start the first pipeline session. They live in the
template and are excluded from instances.

### Clone the template directly

```bash
git clone https://github.com/nullhack/temple8
cd temple8
curl -LsSf https://astral.sh/uv/install.sh | sh  # skip if uv is already installed
uv sync --all-extras
opencode && @setup-project                        # personalise for your project
uv run task test && uv run task lint && uv run task static-check
```

### Existing project

```bash
pip install agents-smith
smith clone                              # adds temple8's agents, flows, skills, and knowledge
```

---

## Commands

```bash
uv run task test            # full suite + coverage
uv run task test-fast       # fast, no coverage (use during TDD loop)
uv run task test-build      # full suite + HTML/coverage/hypothesis report
uv run task lint            # ruff check (dev: bug-catchers)
uv run task lint-merge      # merge: + SIM/RUF + ruff format
uv run task static-check    # pyright type checking
uv run task stubtest        # mypy.stubtest against the package stubs
uv run task validate-flows  # flowr validate on every flow YAML
uv run task strip-docstrings  # strip docstrings from a source .py (tdd select)
uv run task run             # run the app
```

---

## The pipeline

```
discover → explore → plan → build → deliver → shipped
```

| Subflow | What happens | Entry state |
|---|---|---|
| discover | interview funnel → glossary of ubiquitous language | `interview-general` |
| explore | ground external services in recorded vcrpy cassettes | `select-external-target` |
| plan | data model → test stubs → review → test bodies → source stubs → simulate | `model-data-schema` |
| build | one contract per cycle: red → green → refactor → review → ship | `select-build-target` |
| deliver | squash-merge to `dev`, regenerate docstrings, whole-suite gates | `merge-to-dev` |

`flowr` is the single router. Every state change runs through it — no improvised routing, no skipping states. The state's contract is binding: every input artifact must exist before work starts, and work writes only to the declared output artifacts. CI (`ruff` / `pyright` / `mypy.stubtest` / `pytest`) is the enforcement backstop for evidence the dispatched agent asserts.

See `AGENTS.md` for the binding constraints and the driving loop.

---

## FAQ

### How is this different from Kiro?

temple8 evolved over years of accumulated practice, not as a response to Kiro. Both identified the same pain points in AI-assisted development. The standards differ: Kiro uses EARS notation and property-based testing; temple8 uses BDD, TDD, and DDD with three-tier progressive review and a compiler-style spec simulation gate. Kiro is a cloud IDE on Bedrock. temple8 is a local project template with any LLM. MIT licensed, zero cost.

### How is this different from Cursor or Copilot?

Cursor and Copilot help write code. temple8 provides the process that decides what to write, in what order, and what review it passes before shipping. Think of them as the engine and temple8 as the map. Use both together.

### How does this relate to Claude Code or opencode?

Claude Code and opencode are general-purpose agent runners. temple8 gives them a process: YAML state machines, scoped agent roles, and evidence-based transitions. Without temple8, they follow prompts. With it, they follow a workflow.

### Do I need to replace my existing tools?

No. temple8 is a project template: flows, agent definitions, skills, and knowledge files you drop into any Python project. Keep your editor. Bring your own LLM via opencode or a compatible agent runner. Already have a Python project? Use [agents-smith](https://github.com/nullhack/agents-smith) to add temple8's agents, skills, and flows with one command: `smith clone`.

### Is this only for software development?

The default flows cover software development (discovery, exploration, data modeling, TDD cycles, review). Any repeatable process with steps and conditions can be expressed as a flowr state machine: ops runbooks, compliance audits, content pipelines, incident response.

---

## Documentation

- **[Product Definition](https://nullhack.github.io/temple8/)**: product boundaries, users, and scope
- **[System Overview](https://nullhack.github.io/temple8/)**: architecture, domain model, module structure, and constraints
- **[Glossary](https://nullhack.github.io/temple8/)**: living domain glossary
- **`AGENTS.md`**: binding constraints and the state-driving loop
- **`.opencode/knowledge/`**: the methodology, requirements, software-craft, workflow, architecture, writing, and design reference layer

---

## License

MIT. See [LICENSE](LICENSE).

**Author:** [@nullhack](https://github.com/nullhack) · [Documentation](https://nullhack.github.io/temple8)

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/nullhack/temple8.svg?style=for-the-badge
[contributors-url]: https://github.com/nullhack/temple8/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nullhack/temple8.svg?style=for-the-badge
[forks-url]: https://github.com/nullhack/temple8/network/members
[stars-shield]: https://img.shields.io/github/stars/nullhack/temple8.svg?style=for-the-badge
[stars-url]: https://github.com/nullhack/temple8/stargazers
[issues-shield]: https://img.shields.io/github/issues/nullhack/temple8.svg?style=for-the-badge
[issues-url]: https://github.com/nullhack/temple8/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/nullhack/temple8/blob/main/LICENSE
