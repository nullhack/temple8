---
domain: software-craft
tags: [test-design, observable-behavior, test-coupling, semantic-alignment, abstraction-level]
last-updated: 2026-05-14
---

# Test Design

## Key Takeaways

- Tests should specify observable behaviour, not verify implementation: a test that breaks when refactoring preserves behaviour is coupled to the wrong thing (Meszaros, 2007).
- The semantic alignment rule: tests must operate at the same abstraction level as the acceptance criterion they verify. If the AC says "the user presses W," the test sends W through the input mechanism, not through an internal method call.
- Test coupling exists on a spectrum: feature tests (most resilient) > unit contract tests > property-based tests > white-box tests (most brittle, avoid).
- One observable behaviour per test: each test should fail for exactly one reason and pass for exactly one reason.
- Hard-coded values are acceptable when the test only requires that value; parameterising prematurely couples the test to assumptions about future needs.
- Spec Value Fidelity: every value in the specification carries domain intent; the test must use it in a way that reflects that intent — no noise patterns to satisfy traceability.
- Property tests: all invariant/structural rules, not just @bug Examples. Examples alone cannot prove an invariant (MacIver, 2016).

## Concepts

**Observable Behaviour vs Implementation Coupling** (Meszaros, 2007; Google Testing Blog, 2013; Martin, 2017). A test coupled to implementation uses private methods, internal state, or implementation-specific assertions. When the implementation changes (even if behaviour is identical), coupled tests fail. This produces false negatives that erode trust in the suite. Decoupled tests use public interfaces and assert on observable outcomes, remaining green through refactoring because they verify what the system does, not how it does it.

**Semantic Alignment Rule**. Tests must operate at the same abstraction level as their acceptance criteria. If the AC says "the user presses W," the test should send W through the actual input mechanism. If the AC says "`update_player` receives 'W'," the test calls `update_player("W")` directly. Mismatched abstraction levels create either brittle tests (too low-level) or vague tests (too high-level).

**Test Coupling Spectrum** (Meszaros, 2007; Feathers, 2004; MacIver, 2016; King, 1991). Feature tests exercise the system through its public interface and are most resilient to refactoring. Unit contract tests verify a module's protocol (its inputs, outputs, and invariants) without depending on internals. Property-based tests (e.g., Hypothesis) verify invariants across a range of inputs rather than specific cases. White-box tests inspect internal state or private methods and are the most brittle. Avoid them unless characterising legacy code (Feathers, 2004).

**Characterization Tests** (Feathers, 2004). When modifying code without existing tests, write characterization tests first: tests that document what the code currently does, not what it should do. This creates a regression net before any changes. Characterization tests are temporary. Once the code is under test, replace them with specification tests that assert desired behaviour.

**Semantic Depth**. A test that exists for an Example but exercises domain logic directly instead of through the entry point described in the acceptance criterion has correct structural traceability but wrong semantic depth. Every feature test must exercise the entry point the AC describes: if the AC specifies a command-line invocation, the test must invoke the command handler; if the AC specifies an API call, the test must call the API endpoint. Structural traceability (every Example has a test function) without semantic depth (every test exercises the right entry point) creates a false sense of coverage.

**Spec Value Fidelity**. Every literal, placeholder, and Examples table column in a specification exists because the PO judged it domain-meaningful — an entity identifier, a boundary value, a configuration, a concrete expected outcome. The test must use each value in a way that reflects that domain purpose. Noise patterns that satisfy structural traceability without domain meaning — assigning to `_`, stuffing strings into assert messages, helper functions whose sole purpose is consuming a literal — violate this fidelity. If a spec value does not fit naturally in the test, the mismatch signals a spec clarity issue, not a test workaround opportunity.

**Invariant Property Tests**. Structural (invariant) rules describe properties that must hold across all inputs, not specific behaviours. Examples alone cannot prove an invariant — they only confirm it holds for the selected cases (MacIver, 2016). When a Rule asserts an invariant (e.g., "total must equal sum of parts," "output must be sorted," "balance must never go negative"), the specification pre-mortem and behavior pre-mortem surface candidate counterexamples. These counterexamples become assertions in a Hypothesis property test (`tests/unit/`) that verifies the invariant across a generated range of inputs, catching failure modes that no finite set of hand-picked Examples could have found.

## Content

### Test Coupling Spectrum

| Level | What it tests | Resilience | When to use |
|---|---|---|---|
| Feature test | Observable behaviour through public interface | Highest | Every Example acceptance criterion |
| Unit contract test | Module protocol (inputs, outputs, invariants) | High | Complex domain logic with clear contracts |
| Property test | Invariants across input ranges | Moderate | Bug requirements; all structural/invariant rules |
| White-box test | Internal state or private methods | Lowest | Legacy characterization only |

### Semantic Alignment Examples

| Acceptance Criterion | Correct Test | Wrong Test |
|---|---|---|
| "The player moves north" | Send W through input handler, assert position changes | Call `_update_coordinates(0, 1)` directly |
| "`update_player` receives 'W'" | Call `update_player("W")`, assert it returns the expected state | Simulate keyboard event at OS level |
| "An invalid move is rejected" | Send invalid input, assert error response | Check `_valid_moves` list internally |

### One Behaviour Per Test

- Each test should fail for exactly one reason
- Each test should pass for exactly one reason
- If a test has multiple assertions, they must all verify the same behaviour from different angles
- Multiple behaviours → multiple tests, each traced via title-based mapping

### Test Location Convention

| Directory | Contents | Traceability |
|-----------|----------|-------------|
| `tests/features/<feature_slug>/` | BDD example tests: one test per Example in the feature file | Title-based mapping (pytest-beehave) |
| `tests/unit/` | Unit contract tests: coverage-boosting tests for implementation branches not covered by BDD examples | No Example mapping |
| `tests/unit/` | Property tests: invariant verification across input ranges | No Example mapping (except `@bug` examples); all structural/invariant rules must have one |

**Rule:** `tests/features/` is exclusively for BDD example tests that trace back to Examples in the feature file via pytest-beehave's title-based mapping. Coverage-boosting tests that exercise implementation branches not covered by any Example are unit contract tests and belong in `tests/unit/`, not `tests/features/`. A test not mapped to an Example in `tests/features/` violates the traceability contract enforced by `beehave check`.

## Related

- [[software-craft/tdd]]: the RED-GREEN-REFACTOR cycle that produces these tests
- [[software-craft/code-review]]: reviewing whether tests meet these quality criteria
- [[requirements/gherkin]]: the specification format that drives test design
- [[software-craft/source-stubs]]: creating typed stubs that maintain semantic alignment
- [[requirements/pre-mortem]]: behavior pre-mortem surfaces counterexamples for property tests
