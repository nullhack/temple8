# TODO — temple8 clean-slate rebuild

Rebuilding temple8 on a tests-as-truth model. Requirements are elicited via the
interview funnel (discovery); every external service is empirically grounded
(explore — read docs, run authenticated probes, record real request/response
shapes as vcrpy cassettes); the requirements + captured reality are then encoded
up front (plan) as a staged contract surface: test `.pyi` → reviewed test `.py`
(bodies, each marked `@pytest.mark.pending`) → source `.pyi` derived from the
tests → simulated. Build implements each source `.py` from its `.pyi` to make
the already-written tests pass (red removes the target's pending mark); tests
are otherwise not edited during build. Tests are the source of truth for
behaviour; the one authoritative artifact for each concern tests can't store
(ORM + migrations, typed Settings, adapter cassettes) is never duplicated in
prose. Each unit of work ships as its own source `.py` + structural artifacts —
one commit.

Flow: `pipeline-flow` orchestrates five subflows.
- `discovery-flow`: `interview-general → interview-cross-cutting →
  interview-building-blocks → consolidate-interview` (exit `interview-ready`).
- `explore-flow`: `select-external-target → research-provider → write-probe →
  record-cassette` (loop, one service per pass; exits `explored-ready`,
  `needs-elicitation`).
- `plan-flow`: `author-test-stubs → review-test-stubs → write-test-py →
  derive-source-stubs → simulate-contracts` (exits `contracts-ready`,
  `needs-elicitation`).
- `tdd-flow`: `select → red → green → refactor → review → ship`
  (exits `all-built`, `needs-contracts`).
- `deliver-flow`: `merge → publish` (exit `delivered`).
Lifecycle: `discover → explore → plan → build → deliver → shipped`; `build`
re-enters `plan` on `needs-contracts`; `plan` and `explore` re-enter `discover`
on `needs-elicitation`.

## Contract chain

The contract is staged, cheap-to-skim first, executable next, source-surface
last — each step forces the next via imports. Explore grounds the external
layer in reality first (committed cassettes); plan produces the full surface
(test `.pyi` + test `.py` + source `.pyi`); build implements the source `.py`.
Drift between `.pyi` and `.py` is caught by `mypy.stubtest` (run at green,
review, ship, and merge).

Sequence (the authoritative development order):

1. **interview-general** *(discover)* — Funnel L1: seven big-picture questions
   (Who, What, Why, When/Where, Success, Failure, Out-of-scope); CIT +
   Laddering + CI Perspective; active listening L1 (paraphrase each answer). No
   category labels (priming bias). Begins the single running interview-notes
   artifact.
2. **interview-cross-cutting** *(discover)* — Funnel L2: behaviour groups,
   bounded contexts, integration points, lifecycle events; active listening L2
   (synthesis per group). Appends to interview-notes.
3. **interview-building-blocks** *(discover)* — Funnel L3: building-block names + rough
   boundaries only (no detailed spec); gap analysis (every context / quality
   attribute → ≥1 building block). Appends to interview-notes.
4. **consolidate-interview** *(discover)* — active listening L3: full synthesis
   → stakeholder approval; author `docs/glossary.md`. Exit `interview-ready`.
5. **explore external services** *(explore)* — a four-state loop, one external
   service per pass. `select-external-target` reads the interview's external
   services, cross-checks committed `tests/cassettes/<service>/`, picks the
   next un-probed one (→ `.cache/<session_id>/probe-target.md`), or exits
   `explored-ready` when none remain (pass-through when the interview named no
   external services). `research-provider` identifies the exact provider,
   researches it ONLINE (websearch + webfetch the official docs; no probe code
   until docs are read), determines the access shape, and recommends the ≤1
   advisory specialist (→ `.cache/<session_id>/probe-research.md`).
   `write-probe` authors the minimal probe script (success + ≥1 error) under
   `.cache/explore/<service>/` (gitignored throwaway). `record-cassette` runs the
   probe, RECORDS the real exchange into `tests/cassettes/<service>/` with
   decode + secret/volatile scrubbing, and appends
   `.cache/<session_id>/external-contracts.md`; then `captured` back to
   select. External services only (third-party APIs/SaaS, external managed
   DBs/stores — not DBs we design or UI we define). Only four knobs vary by
   kind (docs-focus, recorder, scrub-fields, default specialist) — they live in
   each skill's kind-dispatch table, not separate states. Re-enter `discover`
   (`needs-elicitation`, from research-provider/record-cassette) when reality
   contradicts the interview.
6. **author-test-stubs** *(plan)* — author `tests/integration|e2e/**/*_test.pyi`
   (signatures expressing domain / relationships / compositions) in layer order,
   asserting external stubs against the captured cassettes (real shapes, not
   guesses). Each test `.pyi` is a COMPLETE stub: every module-level name
   (constants, fixtures, helpers) + class + method signatures; NO third-party
   imports (they trip mypy import-untyped; stubtest doesn't need them).
   Integration + E2E ONLY (no unit tests); drawn from the interview + explore,
   not BDD features. No `.py` yet.
7. **review-test-stubs** *(plan)* — gate: consistency vs interview + ubiquitous
   language (external stubs match the cassettes); scope is integration + E2E
   only; happy-path completeness (every building block → ≥1 stub). Not a code-quality
   gate (that's next).
8. **write-test-py** *(plan)* — transform the reviewed stubs into
   `tests/**/*_test.py` bodies (no docstrings, no comments). Bodies define how
   entities relate / compose. SOLID / DRY / KISS / YAGNI / Object Calisthenics
   gate HERE. Each test is marked `@pytest.mark.pending` (conftest skips it).
   The `<package>` (system-under-test) import is DEFERRED into each test body so
   an unbuilt module collects cleanly and its pending tests skip rather than
   error; third-party / test-only imports stay at module top. The imports assert
   the surface the source stubs must provide. Reworking an EXISTING contract:
   edit the `.py` body to match the changed `.pyi` and re-apply
   `@pytest.mark.pending` so it skips until build re-selects it.
9. **derive-source-stubs** *(plan)* — derive `<package>/**/*.pyi` from the
   reviewed test `.py`: every type a test references gets a definition. No
   hardcoded layout (no `models/`, no `config.pyi`); config follows 12-factor
   (env vars; python-dotenv + gitignored `.env` for local secrets; a typed
   Settings model is optional, a normal source `.pyi` if warranted).
10. **simulate-contracts** *(plan)* — gate: would passing these tests yield a
    complete, working system? pyright (combined set consistent; every import
    resolves), no-orphans, traceability (every external service has a captured
    cassette), layer order, `stubtest tests` (test `.pyi`/`.py` drift-free —
    source stubtest waits for build, no source `.py` yet). Exit `contracts-ready`.
11. **red** *(build)* — remove the target contract's `@pytest.mark.pending`
    marks, run its tests (already written); they fail for the right reason:
    `ImportError` for new work (source absent — `.pyi` is invisible to runtime
    import; the deferred in-body import raises), or assertion failure for
    rework (source `.py` stale against the changed contract). No other test
    editing. Escalate `needs-contracts` on a contract gap.
12. **green** *(build)* — implement `<package>/**/*.py` from its `.pyi`; emit
    structural artifacts (migrations; replay the cassettes captured in explore);
    `.pyi` fixed; `stubtest` clean.
13. **refactor → review → ship** *(build)* — source `.py` fluid, `.pyi` fixed;
    SOLID/DRY/KISS/YAGNI/Object Calisthenics on the `.py`; `stubtest` + tests
    green; ship one commit per unit. (Progress is read on demand from the
    pending marks — no PROGRESS file.)
14. **merge** *(deliver)* — no `@pytest.mark.pending` markers remain on dev
    (all source built), full suite green on dev AND `stubtest` clean on dev.

Build layer order (outside-in): L1 external-boundary (external APIs, databases,
UI, UX) → L2 adapters/connectors/facades → L3 internal data representations →
L4 internals (CLI, business rules). Enforced as a rule inside `select` (pick
lowest-layer pending source stub) and `author-test-stubs` (author in order).

Read discipline: stubs (`.pyi`) are the cheap signature view — read the target
contract's `.pyi` first and open a `.py` only for the detail its stub omits;
operate on the target (recorded in `.cache/<session_id>/build-target.md` during
build), never ingest the whole project.

Design decisions:

- Discovery elicits; explore grounds external reality; plan authors contracts.
  The interview is four funnel-aligned states; explore is one empirical state;
  the technique (CIT, Laddering, CI Perspective, Funnel, Active Listening
  L1/L2/L3) lives in the `requirements/interview-techniques` knowledge file,
  loaded by each of the four `interview-*` skills (one skill per funnel state).
- Explore produces two sharply separated artifacts: committed vcrpy cassettes
  (`tests/cassettes/**` — the authoritative external contract, replayed by
  tests/CI offline) and gitignored throwaway probe scripts (`.cache/explore/` —
  reference for the green implementer, never imported by `<package>` or tests).
  Capture needs real 12-factor credentials; CI never runs explore, it replays
  the cassettes.
- Every state has its OWN skill — no skill is reused across states (the four
  interview states each have a distinct skill that loads the shared technique
  from knowledge).
- Test `.pyi` is the cheap-to-skim signature view; the test `.py` (written at
  `write-test-py`) is the executable truth. Both persist; `stubtest` keeps them
  in sync.
- Source `.pyi` is the pre-implementation design surface, derived from the test
  `.py`; `simulate-contracts` validates the combined set before any source `.py`
  body exists.
- The source `.pyi` is FIXED during build — if implementation reveals the
  contract is insufficient, escalate to plan (`needs-contracts`) rather than
  edit the stub ad hoc.
- `@pytest.mark.pending` (custom marker; root `conftest.py` hook skips pending
  tests) IS the build backlog signal - it covers BOTH new work (source not yet
  implemented) AND rework (source stale against a changed contract). The
  `<package>` import is deferred into each test body so unbuilt modules collect
  cleanly and pending tests skip rather than error. Build's red removes the mark
  from the target contract's tests; deliver's merge requires no markers remain.
  Reworking an existing contract in plan = change its `.pyi` + `.py` and
  RE-APPLY the mark, so the test skips and re-enters the build queue even though
  its source `.py` already exists.
- `mypy.stubtest` is the single drift detector for BOTH source and tests —
  pyright and ruff do NOT detect `.py`/`.pyi` drift (pyright actively hides it
  by preferring the stub).
- Config follows 12-factor: environment variables, never a hardcoded config
  artifact. A typed Settings model is optional.
- `<session_id>` is the flowr session name (the `--name` passed to
  `flowr session init pipeline-flow --name <session_id>`). Per-session artifacts
  (`interview-notes.md`, `external-contracts.md`, `build-target.md`) live under
  `.cache/<session_id>/`; shared artifacts (`docs/glossary.md`) live at the
  repo root under `docs/`.
- No docstrings: code (source, tests, stubs) carries no docstrings during
  development — `D`/pydocstyle is dropped from ruff; docstrings are never
  authored (token economy — no duplicate code/docstring snippets to sync).
- Evidence vs enforcement: flowr gate `conditions` collect EVIDENCE the agent
  asserts; flowr does not run checks. CI is the enforcement backstop — it runs
  ruff (with `PYI`), pyright, mypy.stubtest, and pytest on every push and
  verifies the asserted evidence.

Progress mechanism: the backlog is the set of tests carrying
`@pytest.mark.pending` (`uv run pytest --collect-only -m pending -q` lists
them), grouped by the source contract each exercises. The built/pending ratio
is source contracts with no pending test (built) vs with at least one pending
test (pending). It is read on demand — never written to a file.

Known constraints (revisit if they bite):

- pyright prefers `.pyi` over `.py` (PEP 484): while a `.pyi` exists, pyright
  checks the stub and ignores the `.py`. Tests opt out of `ANN`/`D`
  (`pyproject.toml` per-file-ignores), so this is moot for type-checking but
  means pyright won't catch a stale `.py` — `stubtest` must.
- After `write-test-py`, test `.pyi` and test `.py` coexist and can drift;
  `mypy.stubtest` checks the test pair STRICTLY: the test `.pyi` must declare
  every module-level name (constants, fixtures, helpers) + the class + method
  signatures, and must NOT import third-party libs (they trip mypy
  import-untyped; stubtest doesn't require them). `stubtest tests` runs at
  simulate; scoped `stubtest <package>.<mod> tests.<test_mod>` at green/review;
  whole `stubtest app tests` at merge. Source and tests are BOTH first-class
  stubtest targets.
- `stubtest` imports modules at runtime; it is a SEPARATE step from
  `static-check` (pyright); both run in `release-check`.
- `stubtest` ships with `mypy` (added to dev deps). Every `.pyi` is a second
  source of truth that must be kept synced with its `.py`; `stubtest` catches
  drift only when run, not on every edit.
- The deferred `<package>` import convention is required for the pending mark to
  produce clean skips; if a test imports the SUT at module top, an unbuilt
  module errors at collection (before the conftest hook runs) instead of
  skipping.
- Committed vcrpy cassettes can leak secrets unless `filter_headers` /
  `before_record` scrub them at record time; review cassettes before commit.

Markers: `[x]` done · `[ ]` pending · `[~]` in progress.

## Flow design debt (rework path — happy path verified in simulation, rework path untested)
- [ ] `needs-contracts` carries no persisted handoff — build/red `output artifacts: []`, so the gap relies on undocumented orchestrator prompt-stuffing. Add a `.cache/<session_id>/contract-gap.md` that `author-test-stubs` reads on re-entry, or document the prompt-stuffing convention explicitly.
- [ ] Plan authoring states (`author-test-stubs`, `write-test-py`, `derive-source-stubs`) list their OUTPUT globs but not the EXISTING instances — a fresh pass is explicit, a rework pass is implicit ("read what's on disk"). Add the existing-output globs as inputs.
- [ ] Escalations re-enter subflows at the FIRST state (flowr has no position memory); rework re-runs the whole chain and full gates. Document the cost or accept it.

## Knowledge to author (Stage 3 — derived from the skills' `[[...]]` citations)
18 distinct knowledge files cited across the 21 skills. Ordered by LIFECYCLE — the sequence in which an agent meets them as a session runs (discover → explore → plan → build → deliver); each appears once, at its first encounter. Raw material lives in `.backup/.opencode/knowledge/` — restore selectively and rewrite (the backup is beehave-stale; do NOT bulk-copy). Skills' forward-ref wikilinks resolve once these exist; track as debt until authored.

**Discover (interview funnel):**
- [x] `requirements/interview-techniques.md` — Elicitation methods (CIT, Laddering/Means-End, CI Perspective Change, Funnel, Active Listening L1-L3) applied at each funnel depth. *(interview-general, interview-cross-cutting)*. AUTHORED.
- [x] `requirements/domain-decomposition.md` — Decomposing each bounded context into DDD building blocks (aggregate-first); gap analysis as a coverage matrix (every context → ≥1 block; every quality attribute → ≥1 block). *(interview-building-blocks, review-test-stubs)*. AUTHORED.
- [x] `requirements/aggregate-boundaries.md` — Sizing and splitting aggregates: single-entity default, reference-by-identity, split on invariant seams (Evans ch 4; Vernon ch 10). *(interview-building-blocks)*. AUTHORED.
- [ ] `requirements/ubiquitous-language.md` — Curating the glossary: term extraction, genus-differentia definitions, bounded-context grouping (Evans DDD). *(consolidate-interview)*

**Explore (ground externals):**
- [ ] `software-craft/external-fixtures.md` — Capturing external reality: vcrpy record/replay, cassette hygiene (decode + scrub volatile headers/secrets), probe-script conventions, 12-factor creds, kind-dispatch table. *(research-provider, write-probe, record-cassette)*

**Plan (author contracts):**
- [ ] `software-craft/test-stubs.md` — Test `.pyi` conventions: declare every module-level name (constants/fixtures/class+methods), no third-party imports, kept in sync with `.py`; test-pair stubtest drift rules. *(author-test-stubs, simulate-contracts)*
- [ ] `software-craft/test-design.md` — Designing integration + E2E tests only (no unit): scenario selection, fixture/parametrize conventions, deferred-SUT-import, depend-on-contracts. *(author-test-stubs, write-test-py)*
- [ ] `software-craft/code-review.md` — Review criteria + checklist for impl-matches-contract and source-quality. *(review-test-stubs, review-implementation)*
- [ ] `software-craft/solid.md` — SOLID principles (SRP/OCP/LSP/ISP/DIP) applied to source + test structure. *(write-test-py, refactor-green, review-implementation)*
- [ ] `software-craft/object-calisthenics.md` — Object Calisthenics rules (1-level indent, no getters, etc.) for structural quality. *(write-test-py, refactor-green)*
- [ ] `software-craft/smell-catalogue.md` — Code-smell detection signals (long method, god class, duplication, …). *(write-test-py, refactor-green, review-implementation)*
- [ ] `software-craft/source-stubs.md` — Source `.pyi` conventions: signature-only, ellipsis body, no prescribed layout, canonical data-shape pinning; stubtest scope rules. *(derive-source-stubs, implement-from-stub)*
- [ ] `requirements/spec-simulation.md` — Mental-simulation technique: "if an impl passes these tests, is the result complete + correct?" *(simulate-contracts)*

**Build (implement):**
- [ ] `software-craft/tdd.md` — Red-green-refactor cycle; right-reason-for-failure rule; pending-mark/backlog discipline; scoped-vs-whole stubtest. *(select-build-target, confirm-red-failure, implement-from-stub)*
- [ ] `software-craft/design-patterns.md` — Design patterns (adapter, facade, …) for composing source from a stub. *(implement-from-stub)*
- [ ] `software-craft/refactoring-techniques.md` — Refactoring moves (extract method, etc.) applied under green tests with `.pyi` fixed. *(refactor-green)*

**Deliver (ship):**
- [ ] `software-craft/git-conventions.md` — Commit + branch conventions (imperative messages, one logical change, feature/dev/release branches). *(ship-unit, merge-to-dev, publish-release)*
- [ ] `software-craft/versioning.md` — Semantic versioning + release tagging. *(publish-release)*


## pyproject + tooling
- [ ] `[project].readme = "README.md"` and `[project.urls]` reference files deleted in the clean-slate commit (README.md, `docs/api/`) — pyproject points at ghosts. Author a fresh README + drop stale URLs, or remove the fields.
- [ ] Reset `version` and `description` (still "9.4.0" / "Spec-driven ... BDD traceability" — pre-clean-slate).
- [ ] Two dev-dependency sections overlap and diverge: `[project.optional-dependencies].dev` vs `[dependency-groups].dev` (the latter carries `flowr[viz]` + `pytest-beehave[html]`). Consolidate to one; decide `uv run --extra dev` vs `uv sync --group dev`.
- [ ] `conventions` task selects `ANN` (flake8-annotations) which flags the un-annotated `conftest.py` hook and diverges from `ruff check .` (main select has no ANN). Reconcile — drop `ANN` from `conventions`, or drop the `conventions` task in favour of `ruff check .`.
- [ ] Wire `stubtest` / `static-check` / coverage (`--cov`) / `doc-serve` / `doc-build` / `run` tasks to the real package once named (all target the stale `app` placeholder, matching `[tool.setuptools] packages = ["app"]`).
- [ ] Drop `beehave` / `pytest-beehave` deps + `[tool.beehave]` (feature-file stubbing is gone); keep `flowr`, `pytest`.
- [ ] Decide `requires-python` (currently `>=3.14`).
- [ ] Decide task runner: `taskipy` vs plain `uv run`.

## Package + tests skeleton
- [ ] Decide package name (old default `app`) and create the minimal package.
- [ ] `tests/integration/` — one module per boundary (config, external
      adapters, APIs, databases).
- [ ] `tests/e2e/` — CLI / object-composition / contract-chaining tests.
- [ ] `tests/cassettes/` — recorded vcrpy cassettes (captured during explore;
      committed; replayed by tests + CI offline).
- [ ] `tests/fixtures/` — static fixtures not covered by cassettes.
- [ ] No `tests/unit/` by policy.

## Structural artifacts (one authoritative home each, no prose duplicate)
- [ ] ORM models + Alembic migration skeleton — relationships / data shape.
- [ ] Typed Settings model — config parameter definitions (12-factor: env vars).
- [ ] External-adapter cassettes — recorded in explore; replayed in tests.
- [ ] `docs/glossary.md` — ubiquitous language; drives naming (from template).

## Docs
- [ ] `README.md` — author a fresh one for the rebuild (deleted in clean-slate; pyproject references it).
- [ ] `CHANGELOG.md` — decide whether to maintain (deleted; `publish-release` implies one may be wanted).

## Docs-as-derived
- [ ] Decide the derivation mechanism (tool? extraction script? manual?) that
      regenerates docs/specs from the green suite.

## Template mechanism
- [ ] Decide how downstream projects inherit this (cookiecutter / copier /
      plain copy), replacing the old `.templates/` + `template-config.yaml` +
      setup-* skills (all in `.backup/`).
