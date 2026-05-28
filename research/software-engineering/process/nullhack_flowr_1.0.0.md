# flowr 1.0.0: Non-Deterministic State Machine Specification for Workflow Kneading

## Citation

nullhack/flowr. (2026). flowr v1.0.0. GitHub. https://github.com/nullhack/flowr

## Source Type

Software Release / Specification

## Method

Specification Review (official documentation at https://nullhack.github.io/flowr/)

## Verification Status

Verified

## Confidence

High

## Key Insight

flowr 1.0.0 is the first stable release of the non-deterministic state machine specification. It formalises the YAML format with a complete specification document, formal syntax grammar, conformance levels (MUST/SHOULD/MAY), extension field semantics, and reserved key registry. The specification defines what a workflow IS (structure, states, transitions, guards) not what it DOES (no execution engine, no side effects).

## Core Findings

1. **Formal Specification**: v1.0.0 introduces a complete specification with RFC 2119 key words (MUST, SHOULD, MAY), formal syntax grammar, normative examples, and visual reference diagrams. The specification is the contract; the CLI is a reference implementation.

2. **Condition Operators**: The `~=` (approximate match) operator is removed. Supported operators: `==`, `!=`, `>=`, `<=`, `>`, `<`. Plain values without operator prefix are implicit `==`. Numeric extraction applies to both sides (e.g., `>=80%` vs `75%` compares 80 vs 75).

3. **`when` Forms**: The `when` field on transitions accepts three forms: a dict (inline condition-map), a string (reference to a named condition group), or a list (mix of named refs and inline dicts). All conditions are AND-combined.

4. **Named Condition Groups**: States define `conditions:` blocks with reusable condition sets. Transitions reference them by name in `when:` clauses. Unknown references to groups defined on other states are validation errors.

5. **Extension Fields and Reserved Keys**: Flow definitions MAY contain non-reserved fields that the validator ignores. Reserved keys: `flow`, `version`, `params`, `exits`, `attrs`, `states`, `id`, `next`, `to`, `when`, `conditions`, `flow-version`. The `attrs` field is the designated extension point for implementation-specific data.

6. **Params with Defaults**: `params` supports both simple string lists (required) and objects with `name` and optional `default` fields. Params without defaults must be provided at invocation time.

7. **Conformance Levels**: MUST (required for all conforming implementations), SHOULD (recommended, optional), MAY (optional extension). Conforming implementations must satisfy all MUST rules.

8. **Validation Rules**: Seven MUST-level checks at load time: every `next` target resolves, no ambiguous targets, parent `next` keys match child `exits`, no cross-flow cycles, exit names referenced by at least one state, named condition references resolve, params without defaults provided.

9. **Subflow Semantics**: `flow:` on a state makes it a subflow invocation. `flow-version` constrains compatible child versions via semver ranges. Parent `next` keys must match child `exits` exactly. Call-stack push on entry, pop on exit. Cross-flow cycles forbidden, within-flow cycles allowed.

10. **Session Model**: Sessions track `flow`, `state`, `name`, `created_at`, `updated_at`, `stack`, `params`. Atomic writes (temp-file-then-rename). Filesystem is the source of truth.

11. **Semver Conventions**: Adding a new exit is a minor bump. Adding states is a patch. Removing or renaming exits is a major (breaking) change.

12. **CLI Reference**: Commands include `validate`, `states`, `check`, `next`, `transition`, `mermaid`, `config`, and session subcommands (`init`, `show`, `set-state`, `list`). All commands output JSON by default with `--text` for human-readable. `--session` flag makes any command session-aware.

## Mechanism

flowr defines what a workflow IS, not what it DOES. No execution engine, no side effects, no opinions about retries, timeouts, or error handling. A YAML file declares structure. A validator checks integrity. Tools query, track, and visualise. The format is the foundation. By giving a precise definition to the format, shared tooling (validators, editors, visualisers, session trackers) works across any project that adopts the specification.

## Relevance

flowr is the workflow engine that powers temple8's flow-based delivery system. The 1.0.0 release stabilises the specification that the golden rules depend on: session management replaces manual session editing (Rule 1), flow name resolution simplifies CLI usage, configuration from pyproject.toml removes hardcoded paths, and the formal validation rules enforce structural integrity at load time.

## Related Research

Connects to finite state machine theory (Harel, 1987), workflow management patterns (Russell et al., 2006), and the temple8 knowledge files on flowr specification and operations.
