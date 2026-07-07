# flowr 1.0.0: Non-Deterministic State Machine Specification (nullhack, 2026)

## Citation
nullhack/flowr. (2026). flowr v1.0.0. GitHub.
URL: https://github.com/nullhack/flowr · Docs: https://nullhack.github.io/flowr/

## Method
Specification review (the official v1.0.0 specification document and reference CLI).

## Confidence
High — the specification is the contract; the CLI is a reference implementation.

## Key Insight
flowr 1.0.0 is the first stable release of a non-deterministic state machine specification: it formalises a YAML format that declares what a workflow IS (structure — states, transitions, guards) and deliberately not what it DOES (no execution engine, no side effects, no opinions on retries/timeouts/error handling). The format is the foundation; shared tooling (validators, editors, visualisers, session trackers) works across any project that adopts it.

## Core Findings
1. **Formal specification** with RFC 2119 key words (MUST/SHOULD/MAY), a formal syntax grammar, normative examples, and visual reference diagrams. The specification is the contract.
2. **Condition operators**: `~=` removed; supported are `==`, `!=`, `>=`, `<=`, `>`, `<`, with plain values as implicit `==` and numeric extraction on both sides (e.g. `>=80%` vs `75%` compares 80 vs 75).
3. **`when` forms**: a dict (inline condition-map), a string (named condition-group reference), or a list mixing both; all conditions AND-combine.
4. **Named condition groups**: states define `conditions:` blocks; transitions reference them by name in `when:`. Unknown cross-state references are validation errors.
5. **Extension + reserved keys**: `attrs` is the designated extension point for implementation-specific data. Reserved: `flow, version, params, exits, attrs, states, id, next, to, when, conditions, flow-version`.
6. **Params with defaults**: simple string lists (required) or objects with `name` + optional `default`; params without defaults must be supplied at invocation.
7. **Conformance levels**: MUST (required), SHOULD (recommended), MAY (optional).
8. **Validation (seven MUST checks at load)**: every `next` target resolves; no ambiguous targets; parent `next` keys match child `exits`; no cross-flow cycles; exit names referenced by ≥1 state; named condition references resolve; params without defaults provided.
9. **Subflow semantics**: `flow:` on a state invokes a subflow; `flow-version` constrains compatible child versions via semver ranges; parent `next` keys must match child `exits` exactly; call-stack push on entry, pop on exit; cross-flow cycles forbidden, within-flow cycles allowed.
10. **Session model**: tracks `flow, state, name, created_at, updated_at, stack, params`; atomic writes (temp-file-then-rename); filesystem is the source of truth.
11. **Semver conventions**: adding an exit = minor; adding states = patch; removing/renaming exits = major (breaking).

## Mechanism
flowr defines what a workflow IS, not what it DOES. A YAML file declares structure; a validator checks integrity; tools query, track, and visualise. Because the format is precisely defined, validators/editors/visualisers/session-trackers interoperate across any conforming project. The non-determinism is in the routing: a state may declare several `next` transitions, and the orchestrator (an external agent) decides which to fire by asserting evidence against the guarded conditions — flowr never executes the work itself.

## Relevance
flowr is the workflow engine that powers temple8's staged-contract pipeline. This card grounds the `workflow/flowr-operations` knowledge: the session model, the subflow call-stack, the conditions/evidence model, the validation rules, and the CLI surface that the orchestrator drives one state at a time. The "binding constraints" (no skip state, no bypass dispatch, evidence-based transitions) are direct consequences of this specification.

## Related Research
Connects to finite state machine theory (Harel, 1987) and workflow management patterns (Russell et al., 2006).
