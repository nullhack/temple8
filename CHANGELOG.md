# Changelog

All notable changes to this template will be documented in this file.

## [v9.3.0] - 2026-05-28: V10 Agentic Reform

### Changed

- **AGENTS.md**: full rewrite — caveman-style throughout, Main Directive at top, Golden Rules tightened, feature lifecycle phases documented, runtime artifact resolution convention, review loop relay protocol, loop exit detection in anchor, multi-skill ordering explicit, beehave violations = test failures, convention boundary for design-phase states
- **refactor/SKILL.md**: added `beehave check` before `task test-fast` (step 9), added loop exit detection via `beehave status --json` (step 10)
- **write-test/SKILL.md**: added no-docstrings rule for test functions with self-heal ruff instruction
- **review-gate/SKILL.md**: added no-docstrings enforcement in structure review (step 8)
- **structure-feature/SKILL.md**: clarified `out: git_branch` as Runtime artifact meaning branch creation
- **todo-anchor-protocol.md**: synced notation to native status fields, added loop resolution and review relay to anchor checklist
- **test-design.md**: added comment/docstring noise pattern to Spec Value Fidelity
- **test-stubs.md**: documented auto-generation on every pytest, stale stub accumulation, `beehave clean --force` usage
- **skill-design/principles.md**: added imperative language standard for skill writing
- **pyproject.toml**: added `"D"` to `per-file-ignores` for `tests/**` (no docstrings required in tests)

### Simulation-Driven

- Walked full 24-state define-flow → develop-flow path for "Add Task" feature
- Identified and resolved 5 critical pain points: runtime artifact ambiguity, feature file lifecycle, multi-skill ordering, review feedback survival, loop exit detection

## [v9.2.1] - 2026-05-22: Steadfast Hephaestus

### Fixed

- **`flowr serve` crash**: upgraded flowr from 1.1.0 to 1.2.0 (Whole Rye) which includes the missing static frontend assets in the wheel. The `flowr serve` command now finds `index.html`, `css/`, and `js/` and starts the visualization server without errors.
- **Dropped `html` extra**: `flowr[html,viz]` changed to `flowr[viz]` — the `html` extra never existed in flowr and caused a resolution warning.

### Changed

- **flowr**: `>=1.1.0` → `>=1.2.0`
- **flowr[viz]**: `>=1.0.0` → `>=1.2.0`

## [v9.1.0] - 2026-05-20: beehave 1.0.0 Knowledge Integration

### Added

- **`[dependency-groups]`**: added `flowr>=1.0.0` to dev dependency group (PEP 735).

### Changed

- **`test-stubs.md` (software-craft)**: full rewrite incorporating beehave 1.0.0 features — `beehave status` (6 development stages, `--json`, `--include-unmapped`), `beehave list`/`list -v`, `beehave clean`, collision detection, feature stem = title slug requirement, and behavioral notes (validate_all_titles crash, generate pre-flight scope, single-feature check skip). Added `## Content` section with reference tables.
- **`select-feature/SKILL.md`**: replaced manual per-feature checking with `beehave status --json` for project-wide development stage overview. Added `[[software-craft/test-stubs#key-takeaways]]` to available knowledge.
- **`accept-feature/SKILL.md`**: added `beehave status --json` as pre-check before `beehave check`. Added `[[software-craft/test-stubs#concepts]]` to available knowledge.
- **`verify-traceability/SKILL.md`**: added optional `beehave status --json` summary view. Added `[[software-craft/test-stubs#concepts]]` to available knowledge.
- **`review-gate/SKILL.md`**: added `[[software-craft/test-stubs]]` to available knowledge for consistency.
- **`source-stubs.md` (software-craft)**: updated creation order to include `beehave status` for development stage confirmation.
- **`gherkin.md` (requirements)**: updated Related link to reference `beehave status` for development stage tracking.

## [v9.0.0+20260518] - 2026-05-18: Adversarial Audit

### Breaking

- **Define-flow reorder**: `spec-validation → architecture → refine-features → validated` (was `spec-validation → refine-features → architecture → validated`). Architecture now runs before refine-features so quality_attributes, integration_points, and technology_stack are finalized before feature constraints are frozen.
- **Architecture skippable**: architecture-assessment sets `architecture-complete: ==verified` and exits immediately when no architecture changes needed — no spec mutations on the skip path.

### Added

- **Decomposition decision tree**: replaced 5 stale triggers (">8 candidate Examples", ">2 concerns", undefined "concerns") with behavioral decision tree: group by Then-outcome → collapse Scenario Outlines → count Must behaviors → >8 Musts splits Rule. Structural triggers: >1 bounded context, "and" joining independently testable outcomes, no beneficiary, duplicate Rule.
- **WSJF scoring wired**: `select-feature` now scores all features by dependency count (lowest first), then WSJF (Value/Effort) per `[[requirements/wsjf#key-takeaways]]`. Delivery order derived at selection time from context map dependency graph.
- **AI language markers expanded**: Tier 1 +25 words (navigate, harness, seamless, boilerplate, etc.), Tier 4 +4 phrases, new Tier 7 Claude-Specific Structural Patterns (8 patterns), Claude detection dimension in scoring table.
- **Domain spec template**: Integration Points section now requires Mechanism, Error handling, Ownership fields (synced with context-mapping knowledge).

### Changed

- **Adversarial audit — 47 knowledge files, 39 skills**: comprehensive deduplication, stale content removal, and cross-reference alignment across all domains.
- **Knowledge deduplication** (12 files): invest.md, moscow.md, decomposition.md, feature-discovery.md, technical-design.md, assessment.md, flowr-operations.md, todo-anchor-protocol.md, agent-design/principles.md, skill-design/principles.md, color-systems.md, project-assets.md — inline duplications replaced with cross-references to canonical sources.
- **Skill deduplication** (10 files): refactor, review-gate, simulate-spec, fix-spec, review-simulation, create-py-stubs, verify-traceability, write-bdd-features, accept-feature, refine-features — inline knowledge restatements replaced with references.
- **ADR structure aligned**: `adr.md` now documents Interview section and "Alternatives Considered" field name matching the actual template.
- **Owner mapping consolidated**: removed from flowr-operations.md and todo-anchor-protocol.md; lives only in AGENTS.md.
- **"As the system, I want..." removed**: all user story format examples replaced with Rule-native language ("Rule with no beneficiary").
- **spec-architecture.md Terminology Map**: removed "story, user story" from deprecated column to prevent agents interpreting it as a format hint.

### Removed

- **`spec-architecture.md`** (requirements): fully covered by rule-derivation, spec-simulation, feature-discovery, gherkin, feature-boundaries, and the flow YAML files themselves. Zero references, highest drift risk.
- **`rule-derivation.md`** (requirements): fully covered by spec-simulation.md (simulation rule discovery) and feature-discovery.md (traceability/gap verification). Zero skill references.
- **`domain-modeling.md`** (domain-modeling): merged into event-storming.md as `### Formalization` subsection (Entity/VO distinction, relationship types, table formats, boundary heuristics). Zero skill references.

### Fixed

- **gherkin.md:173**: "3 words or longer than 8" → "2 words or longer than 6" to match canonical 2-6 word constraint.
- **Glossary template drift**: "3-8 word title" → "2-6 word title" on lines 23, 28, 37.
- **versioning.md:43-44**: broken `[[process/...]]` references → plain text URLs (semver.org, calver.org).
- **create-domain-spec/SKILL.md:11**: misrouted reference from `[[domain-modeling/behavioral-contracts#concepts]]` → `[[domain-modeling/event-storming#concepts]]` for bounded context identification.
- **moscow.md:14**: removed duplicate Key Takeaway (identical to line 11).
- **Gh-159**: spec-to-feature pipeline gap resolved by define-flow reorder — architecture runs before refine-features, ensuring delivery items are validated against complete spec documents before feature files are frozen.
- **Gh-144**: technical_design.md.template redundancies resolved by knowledge dedup — technical-design.md no longer duplicates quality-attributes, contract-design, or assessment content.
- **Gh-143**: mandatory artifact reads, out-artifact lifecycle protocol, and cumulative editing guidance now in AGENTS.md Session Protocol.

## [v8.6.0+20260515] - 2026-05-15: Dialogic Chronos

### Added

- **Technology Requirements chain**: `domain_spec.md` template now has a `### Technology Requirements` table (Context/Requirement/Verification columns). simulate-spec writes tech constraints to `.feature` files. review-gate Tier 1 verifies each constraint against implementation. accept-feature traces technology Q&As to implementation evidence.
- **Title verification checks**: All 6 skills that write Feature/Rule/Example titles now have explicit 2–6 word count (split on whitespace) and uniqueness verification steps.

### Changed

- **Terminology standardisation** (~30 files): walkthrough replaces standalone "scenario" in simulation context. Rule block replaces "story"/"user story". Example block replaces "BDD scenario"/"BDD example". behavior hint replaces "scenario hint"/"Scenarios:".
- **Spec architecture restructured**: behavioral rules now live exclusively in `.feature` files (single source of truth). `domain_spec.md` is structural model only with behavioral sections as derived summaries referencing `.feature` rules. `simulation_results.md` reduced to pain points + walkthrough provenance.
- **Simulation writes directly to `.feature`**: simulate-spec creates coarse `.feature` files per bounded context with `Rule:` blocks. Planning refines: feature-discovery splits/renames, feature-breakdown adds `Behavior hints:`, feature-examples converts hints to Gherkin.
- **`As a/I want/So that` deprecated**: `cli_entrypoint.feature` refactored to `Rule: title` + behavioral description + `Behavior hints:` format. Connextra user story format removed project-wide.
- **`# Business rules:` replaced**: `.feature` template simplified — no more `# Business rules:` comment blocks. Rules originate as `Rule:` blocks during simulation.
- **Title convention 3–8 → 2–6 words**: gherkin.md, test-stubs.md, and 6 skill files updated to new word range. Feature titles must also be 2–6 words and unique across all `.feature` files.
- **Gherkin knowledge gaps closed**: simulate-spec, discover-features, and break-down-feature now load `[[requirements/gherkin#key-takeaways]]` for title and behavioral distinctness rules.

### Removed

- **Duplicate `discover-rules` skill**: nested `.opencode/skills/discover-rules/discover-rules/SKILL.md` deleted. Consolidated single skill now maps aggregate invariants to Rule blocks.
- **Stale terminology**: "story", "user story", standalone "scenario" (except `Scenario Outline:` Gherkin keyword), `Scenario:` keyword references purged from all knowledge, skills, flows, and templates.

### Fixed

- **Technology requirements silently dropped**: review-gate now verifies domain_spec.md technology mandates. accept-feature traces technology Q&As. Prevents class of bug where stakeholder-required technologies (DSPy, PostgreSQL, gRPC) pass through entire flow undetected (PM_20260515_dspy_not_implemented).

## [v8.3.0+20260506] - 2026-05-06: Rigorous Euclid

### Added

- **README FAQ section**: Five questions covering Kiro, Cursor/Copilot, Claude Code/opencode, tool compatibility, and non-software workflows.
- **README "Who is this for" rewrite**: Refocused around vibe coding, agentic engineering, and spec-driven development adoption.
- **agents-smith quick start**: New "Existing project" quick-start block using [agents-smith](https://github.com/nullhack/agents-smith) for one-command adoption.
- **Workflow flexibility paragraph**: New "What it does" paragraph explaining that flows are not hardcoded and any state machine process fits.

### Changed

- **Tagline**: "From zero to hero: production-ready Python, without the ceremony." → "From zero to hero: Spec-driven agent orchestration. Any workflow. Any LLM. Zero lock-in."
- **Branding sync**: `docs/branding/branding.md` tagline updated to match README.
- **flowr 1.0.0 adoption**: Upgraded dependency from `>=0.5` to `>=1.0.0`. Knowledge files synced to the official v1.0.0 specification.
- **`~=` operator removed**: The approximate numeric match operator is no longer in the specification. Condition operators are now: `==`, `!=`, `>=`, `<=`, `>`, `<`. Plain values without operator prefix are implicit `==`.
- **`when` forms**: Updated documentation to cover all three `when` forms: dict (inline), string (named ref), list (AND-combined mix).
- **Conformance levels**: Added MUST/SHOULD/MAY conformance levels and extension field semantics. Reserved keys registry added.
- **Validation rules streamlined**: Consolidated to seven MUST-level checks matching the specification.
- **Research note**: Renamed `nullhack_flowr_0.4.0.md` to `nullhack_flowr_1.0.0.md` with full specification review.

## [v8.2.0+20260505] - 2026-05-05: Discriminating Epicurus

### Added

- **Feature discovery state**: New `discover-features` skill replaces `specify-feature` with adversarial analysis. Discovery-flow updated (v4→v5) with feature-discovery state that reads `technical_design.md` alongside `product_definition.md`.
- **Todo-driven execution**: Procedural contract and anchor protocol extracted to `.opencode/knowledge/workflow/todo-anchor-protocol.md`. FAA-style checklist, loop prevention, one-state-per-todo enforcement, anti-patterns, and owner mapping table.
- **Convention Boundary**: Convention checks (ruff, pyright, lint, format) are prohibited during design-phase states. Only `test-fast` is permitted. The design-before-conventions principle is enforced in AGENTS.md.
- **@id format**: 8-char hex default for scenario IDs, with respect for existing formats. Verified at baseline via `verify-traceability` skill.
- **Silent quality gates**: INVEST validation and example quality checks are silent gates (not artifact content). Features that fail these gates loop back for respecification without polluting the feature file.
- **Gherkin steps preservation**: `write-test` skill preserves Gherkin steps in docstrings as immutable specification. Agents must not modify them.
- **Todo anchor protocol knowledge file**: Created `.opencode/knowledge/workflow/todo-anchor-protocol.md` with FAA checklist, loop prevention, one-state-per-todo enforcement, anti-patterns, and owner mapping table.

### Changed

- **flowr 0.5.0 adoption**: Upgraded dependency from `>=0.4` to `>=0.5`. All knowledge files and templates updated for JSON-first output, enhanced `next` command (shows all transitions with `"open"`/`"blocked"` status markers and condition hints), new session commands (`states --session`, `validate --session`, `check --session <trigger>`), and subflow exit resolution through parent transition map.
- **Skill/protocol separation**: Removed "Write results to artifacts" and "Advance the flow" boilerplate from all 41 skills. Updated `skill-design/principles.md` to list these as patterns NOT to include (orchestrator handles them).
- **AGENTS.md refactored**: Replaced ~40 lines of verbose Procedural Contract + Todo-Driven Execution with ~15 lines referencing `[[workflow/todo-anchor-protocol]]`. Flowr Commands table updated with 0.5.0 commands. Session Protocol step 1 mentions JSON parsing. Session Init mentions auto-entering subflow. `flowr` moved from production dependencies to dev-only dependencies.
- **flowr-operations.md rewritten**: Output Formats section with JSON examples for all commands. Command Reference table updated. Key Takeaways updated for JSON-first workflow.
- **flowr-spec.md updated**: Added JSON-First Output and Subflow Exit Resolution concepts. Subflow Model expanded with chaining, recursive entry, and auto-enter details. Design Principles expanded with JSON-first and complete transition visibility.
- **TODO template**: Slimmed from 47 lines to 21 lines. Essential flowr JSON cheatsheet added. Removed redundant Procedural Contract, Anchor Checklist, and State Metadata sections (now in knowledge files).
- **Knowledge decoupled from flow state names**: Knowledge files no longer reference specific flow state names, making them reusable across different flow configurations.
- **Flow version bumps**: discovery-flow 4→5, planning-flow 5→6.
- **Frozen Examples Rule**: Removed from feature template, moved to `write-bdd-features` skill where it belongs.

## [v8.1.0+20260502] - 2026-05-02

### Added

- **Git branch discipline**: Every state in all 12 flow YAML files now declares `git: main` or `git: feature` in its attrs. Agents must work on the declared branch and never switch mid-state. Golden Rule #7 added to AGENTS.md.
- **Committed-to-main guards**: Project-phase exit transitions (discovery, architecture, planning, branding, setup) now require `committed_to_main_locally: ==verified` evidence before advancing. Ensures artifacts are persisted before moving to the next phase.
- **flowr 0.4.0 adoption**: Upgraded dependency from `>=0.3` to `>=0.4`. Added `[tool.flowr]` config section to pyproject.toml (flows_dir, sessions_dir, default_flow, default_session).
- **Session management**: `.flowr/sessions/` directory for persisting workflow progress. AGENTS.md updated with session init, `--session` flag usage, and session-based workflow pattern.
- **Flow params**: Feature-scoped flows (planning, development, delivery, tdd-cycle, review-gate, feature-development) now declare `params: [feature_title]` for session parameter tracking.
- **Flowr commands**: AGENTS.md and knowledge files updated with session commands (`init`, `show`, `set-state`, `list`), `--session` flag on check/next/transition, `config` command, short flow name resolution, and `--evidence-json` flag.
- **flowr-spec.md knowledge**: Session model (flow, state, name, stack, params), configuration resolution, MUST/SHOULD severity levels on validation rules, atomic session writes principle.
- **flowr-operations.md knowledge**: Session commands, session-based workflow pattern, configuration section, evidence syntax with condition operators.
- **Research note**: `docs/research/software-engineering/process/nullhack_flowr_0.4.0.md` documenting flowr 0.4.0 analysis.

### Changed

- **Flow version bumps**: main-flow 7→8, discovery-flow 3→4, architecture-flow 4→5, planning-flow 4→5, feature-development-flow 6→7, development-flow 4→5, delivery-flow 4→5, tdd-cycle-flow 2→3, review-gate-flow 2→3, post-mortem-flow 2→3, branding-flow 2→3, setup-project-flow 2→3.

## [v8.0.0+20260501] - 2026-05-01

### Added

- **Flow attrs simplification**: Replaced `input_artifacts`/`edited_artifacts`/`output_artifacts` with `in`/`out` across all 12 flow YAML files and 28 SKILL.md files. `in` is read-only; `out` may create or edit with optional section hints.
- **Artifact naming clarity**: Renamed runtime artifacts for descriptiveness (`py_stubs`→`typed_source_stubs`, `test_stubs`→`test_skeletons`, `test_bodies`→`test_implementations`, `function_bodies`→`source_implementations`, `refactored_code`→`refactored_source`, `commits`→`feature_commits`, `local_main_commits`→`merged_commits`, `root_cause`→`root_cause_analysis`).
- **Feature test stub template**: `.templates/tests/features/<rule_slug>_test.py.template` with `@pytest.mark.skip`, Gherkin docstrings, `raise NotImplementedError`.
- **Two-phase stub creation**: `create-py-stubs` skill (SA creates typed stubs and test stubs per feature in planning flow); `structure-project` now creates package skeleton only.
- **`verify-traceability` skill**: Verifies 1-1 correspondence between `@id` tags in feature files and test functions in `tests/features/`. Catches missing tests (feature not done) and orphan tests (should be in `tests/unit/`).
- **Semantic depth traceability**: `@id` tests must exercise the entry point the acceptance criterion describes (CLI handler, API endpoint), not just domain logic in isolation. Checks added to `verify-traceability`, `review-structure`, and `accept-feature` skills.
- **Spec compliance check**: `define-done` skill now verifies that interface elements documented in the technical design (CLI flags, config keys, API parameters) exist in the implementation.
- **Test location convention**: `tests/features/` is exclusively for `@id`-linked BDD scenario tests. Coverage-boosting tests belong in `tests/unit/`. Added to `test-design.md`, `tdd.md`, and `gherkin.md` knowledge files.
- **Feature selection dependency rule**: Only Dependency=0 features are eligible for selection, regardless of WSJF score. Clarified in `wsjf.md` and `select-feature/SKILL.md`.
- **Generic flowr exit steps in skills**: All 41 SKILL.md files now end with "Advance the flow with necessary evidence, choosing the appropriate next state based on the work completed" instead of hardcoding `flowr advance <transition>`. Agents learn how from `[[workflow/flowr-operations]]` knowledge and AGENTS.md Session Protocol.
- **`[[workflow/flowr-operations]]` knowledge file**: Full command reference for `flowr check`, `next`, `transition`, `states`, `validate`, `mermaid` with evidence flags and workflow pattern.
- **Real flowr commands in AGENTS.md**: Replaced fictional `flowr status`/`flowr advance` with actual CLI commands (`python -m flowr check`, `next`, `transition`). Owner dispatch promoted to top-level step 2 in Session Protocol.
- **Template-safe references**: Removed project name from AGENTS.md title and versioning.md example.
- **`[[software-craft/test-design]]` loaded by TDD skills**: Added to `write-test` and `implement-minimum` skill load lists so agents have test location and coupling knowledge during RED and GREEN phases.
- **Full knowledge loading for review skills**: `review-design` loads 9 full docs, `review-structure` loads 3 full docs, `review-conventions` loads 2 full docs. Evaluation/review/detection needs full documents, not fragments.
- **`task regenerate-flowviz`**: Regenerates `.flowr/viz/data.js` from flow YAML definitions.
- **`task validate-flows`**: Validates all flow definitions.

### Changed

- **Flow artifact fixes**: Removed `stories.md` intermediate from planning flow (feature-breakdown writes Rules, bdd-features writes Examples directly into `.feature`). Added `interview-notes/*.md` to stakeholder-interview.in. Replaced `review_gate_evidence` with three individual review evidences.
- **Architecture-assessment conditions**: Added `architecture_complete` condition. Fixed `no_architecture_exists` to check `technical_design_md` and `context_map_md` (not `system.md`).
- **MoSCoW prevention**: MoSCoW classification is internal triage only, must NOT appear as Gherkin tags. Updated `moscow.md`, `write-bdd-features` SKILL.md, `feature.feature.template`.
- **Minimum stub principle**: Protocol signatures + `raise NotImplementedError`, no docstrings, no type hints beyond contract. Docstrings/type hints/lint added when reviewers require them.
- **Reviewer role**: Reviewer MUST NOT modify files: only APPROVED/REJECTED reports. 'Minor' is not a pass: acknowledged smells are still findings.
- **Terminology**: 'cosmetic' → 'conventions', 'Completion Phase' → 'Conventions Phase'.
- **On-demand reading**: `in` artifacts are read on demand, not eagerly. Applies to all files: spec documents, production code, and test code.
- **Spec doc protection**: Specification documents are read-only during TDD. SE may ONLY modify production code and test code. Gaps flagged in output notes.
- **Session protocol**: AGENTS.md Session Protocol uses real flowr CLI commands (`check` for state entry, `next` for available paths, `transition` for advancing). Owner dispatch is top-level step 2. Skills use generic exit instructions referencing `[[workflow/flowr-operations]]`.
- **Artifact existence guarantee**: File artifacts in `in`/`out` are created from templates lazily. Missing non-Python templates raise error. Environment artifacts produced by tooling.
- **WSJF selection rules**: Clarified: only Dependency=0 features eligible. Ties broken by Value. If all blocked, resolve dependency first then re-score.
- **Flowviz moved to `.flowr/viz/`**: Interactive D3 visualization data now lives under `.flowr/viz/` instead of `flowviz/`.
- **Removed `scripts/flowr-utils.sh` and `scripts/generate-svg.sh`**: Agents use `python -m flowr` directly. SVG generation was broken for all but one flow.
- **Research files**: All 71+ research files converted to v8 template format with Source Type, Method, Verification Status, Confidence, Key Insight, Core Findings, Mechanism, Relevance, Related Research. Citation reference fixes (Tetlock 1983→1985, Brown 2006→2018, king_1991_mutation→demillo_lipton_sayward_1978).

### Removed

- **`stories.md` intermediate**: Feature-breakdown writes Rules directly into `.feature`, bdd-features writes Examples directly. No separate stories file.
- **`scripts/flowr-utils.sh`**: Agents use `python -m flowr` commands directly per AGENTS.md.
- **`scripts/generate-svg.sh`**: Only worked for tdd-cycle-flow; mermaid-cli compatibility issues with all other flows.
- **`review_gate_evidence`**: Replaced by three individual evidences (design_review_evidence, structure_review_evidence, conventions_review_evidence).

## [v8.0.0+20260430] - Methodical Theseus - 2026-04-30

### Added

- **Flow-based delivery system**: Hierarchical state machines (`.flowr/flows/`) replace monolithic agents/skills: main-flow → discovery → architecture → feature-development, with planning/development/delivery/post-mortem subflows
- **Identity-only agents**: 5 agents (product-owner, domain-expert, system-architect, reviewer, software-engineer) matching flow owners: no routing, artifacts, or skill lists in agent files
- **Procedure-only skills**: 26 skills mapped to flow states: no identity or routing logic
- **Progressive knowledge**: Split/rewrote 15+ knowledge files with `#key-takeaways`/`#concepts` fragments for token-efficient loading
- **Flowviz**: Interactive D3+dagre visualization for all 10 flows (`flowviz/`)
- **Document templates**: 11 templates in `.templates/` with instance path mapping in `AGENTS.md`
- **Research library**: 41 structured research notes under `docs/research/` with citation metadata
- **Versioning scheme**: Semver (`major.minor.patch`) in pyproject.toml; git tags append `+YYYYMMDD` build metadata; PyPI uses semver core only (see `[[software-craft/versioning]]`)
- **`software-engineer` agent**: Identity-only agent for the SE flow owner role

### Changed

- **Delivery flow v3**: `publish-decision` replaces `batch-decision`; both `accumulate` and `approved` transitions exit as `next-feature`; removed self-loop from main-flow
- **AGENTS.md**: Added Template Instances table mapping templates to output paths; fixed `Temple9` → `Temple8`; progressive knowledge loading with token savings table
- **`pyproject.toml`**: Version `7.2.20260423` → `8.0.0` (correct semver); fixed `validate-flows` task; removed deleted scripts; deduplicated dev deps; removed invalid pytest option
- **`.gitignore`**: Fixed literal `\n` in directory entries; added `flowviz/data.js`
- **`template-config.yaml`**: Removed non-existent Docker file references; fixed test path; fixed version reset comment (was `0.1.YYYYMMDD`, now `0.1.0`)
- **`scripts/generate-flowviz-data.py`**: Fixed 9 lint errors (C901, D103, FURB110, FURB192, I001)
- **`select-feature/SKILL.md`**: Removed stale `docs/features/in-progress/` reference
- **`decide-batch-action/SKILL.md`**: Removed flow transition routing (skills = procedure only)
- **`.github/workflows/tag-release.yml`**: Git tags now use `v{version}+{YYYYMMDD}` format (semver + build metadata)
- **`.github/workflows/pypi-publish.yml`**: Updated tag example to new format

### Removed

- **Monolithic agents/skills**: `architect`, `define-scope`, `implement`, `verify`, `update-docs`, `run-session`, `flow`, `git-release`, `create-agent`, `create-knowledge`, `create-skill`, `design-assets`, `design-colors`, `check-quality`, `apply-patterns`, `version-control`, all replaced by flow-driven architecture
- **`FLOW.md` and `WORK.md`**: Replaced by `.flowr/flows/` YAML state machines and `.flowr/sessions/` runtime state
- **Stale docs**: `docs/research/` (flat files), `docs/features/completed/`, `docs/features/in-progress/`, `docs/adr/` old ADRs, `docs/product-definition.md`, `docs/glossary.md`, `docs/system.md`, `docs/scope_journal.md`, `docs/assets/workflow.svg`
- **11 obsolete scripts**: `assign_ids.py`, `check_adrs.py`, `check_commit_messages.py`, `check_feature_file.py`, `check_knowledge.py`, `check_oc.py`, `check_stubs.py`, `check_version.py`, `check_work_md.py`, `detect_state.py`, `score_features.py`, `update_index_html.py`
- **`designer.md` and `setup-project.md`** agents: `designer` absorbed into branding skill; `setup-project` to be reintroduced as flow-driven standalone

---

## Pre-v8 History

Releases v1.0.0 through v7.2 used a hybrid calver scheme where the date occupied the semver patch field (e.g. `v7.2.20260423`). Starting with v8.0.0, the versioning scheme uses proper semver `major.minor.patch` in `pyproject.toml` with `+YYYYMMDD` build metadata in git tags only. For the full pre-v8 changelog, see [v7.2.20260423](https://github.com/nullhack/temple8/releases/tag/v7.2.20260423).

Key milestones:

- **v1.0** (2026-03-12): Initial release: 7-phase TDD, agents, skills, CI
- **v2.0** (2026-04-11): V1→V2 architecture transition, CI/CD, Docker, security
- **v3.0** (2026-04-14): 6-step/3-role redesign (PO, Developer, Reviewer)
- **v4.0** (2026-04-16): Per-test Design Self-Declaration, `template-config.yaml`, post-mortem protocol
- **v5.0** (2026-04-18): Design patterns skill, `create-agent`, `software-engineer` agent, 5-step delivery workflow
- **v6.0** (2026-04-19): PO Self-Declaration, Reviewer Stance Declaration, 2-stage discovery model, bug handling protocol
- **v7.0** (2026-04-22): PyPI pipeline, flow state machine, project renamed to temple8
- **v7.2** (2026-04-23): CLI entrypoint, 10 validation scripts, Mermaid→markdown, CI updates