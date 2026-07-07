---
domain: software-craft
tags: [test-design, observable-behaviour, sociable-tests, spec-value-fidelity, property-tests]
last-updated: 2026-07-01
---

# Test Design

## Key Takeaways

- A test specifies **observable behaviour through the public interface**, not the implementation; a test that fails under a behaviour-preserving refactor is coupled to the wrong thing and erodes trust in the suite (Meszaros, 2007).
- This project writes **sociable tests at two grains only** — integration (narrow: a boundary or adapter with its real internal wiring and a replayed cassette or fixture) and E2E (broad: the whole system through its entry point). Internal collaborators run real; there are no solitary unit tests that mock them away (Fowler, 2014; Vocke).
- **One observable behaviour per test**: each test fails for exactly one reason and passes for exactly one reason, so a failure points unambiguously at the broken contract.
- **Spec value fidelity**: every literal in a test carries domain intent — an identifier, a boundary, an expected outcome; noise patterns that satisfy structure without meaning (assigning to `_`, padding assert messages) are forbidden.
- Invariants that must hold across *all* inputs are proven by **property tests** (Hypothesis), never by any finite set of examples; examples confirm a case, only a generated range can probe a rule (MacIver, 2016).

## Concepts

**Observable behaviour, not implementation.** Meszaros (2007) draws the line that organises everything else: a test ought to verify what the system *does* through its public interface, never *how* it does it through its privates. A test that reaches into internal state or private methods is coupled to the implementation, so it breaks when the implementation changes even though behaviour is preserved — a false negative that trains the team to ignore red tests. Testing through the public interface leaves the test agnostic to the internal structure: a different class layout or a rewritten algorithm keeps the suite green as long as the observable outcome holds.

**Sociable, at two grains — never solitary.** Fowler (2014) separates *solitary* unit tests (every collaborator replaced by a double) from *sociable* ones (real collaborators run), and Vocke notes the term "unit" is too contested to carry the meaning alone. This project takes the sociable, classicist side and fixes the grains: a *narrow* integration test exercises one external boundary or adapter with its real internal wiring, replacing only the external collaborator with a replayed cassette or fixture; a *broad* E2E test exercises the full system through its entry point. Internal collaborators are never mocked away — that is the solitary style explicitly rejected here, because mocking the insides reimplements the implementation in the test and couples the two.

**One behaviour per test.** A test that asserts several independent behaviours fails ambiguously: the red signal points at the test, not at the broken behaviour. The discipline is one observable behaviour per test — one reason to fail, one reason to pass — so the title of the failing test names the broken contract directly. Multiple assertions are permitted only when they verify the same behaviour from different angles.

**Spec value fidelity.** Every value in a specification exists because it carries domain meaning — an entity identifier, a boundary value, a configuration, a concrete expected outcome. The test must use each value in a way that reflects that intent, not invent noise to satisfy a structural check. Assigning a literal to `_`, stuffing it into an assert message, or building a helper whose only purpose is to consume it, all satisfy traceability while signifying nothing; if a spec value does not fit naturally into the test, the mismatch signals a spec problem, not a test workaround.

**Property tests prove invariants; examples only confirm cases.** MacIver (2016) makes the limit plain: no finite set of hand-picked examples can prove an invariant — a general rule that must hold for all inputs can only be probed by generating inputs across the space. When a rule is structural ("the total always equals the sum of parts", "output is always sorted", "balance never goes negative"), a Hypothesis property test asserts the property over a generated range and finds failure modes no hand-picked set could reach. Examples remain the right tool for specific behaviours and exact outcomes; properties are for the rules that claim universality.

## Content

### Observable behaviour, not implementation

The coupling shows up the moment a behaviour-preserving refactor lands:

| Test style | What it touches | Under a behaviour-preserving refactor |
|---|---|---|
| observable-behaviour | public interface, returned values, raised errors, observable state | stays green — the contract held |
| implementation-coupled | private methods, internal state, call sequences | goes red — the insides moved |

The cost of coupling is trust: a suite that red-flags refactors gets ignored, and the real failures get lost in the noise. Testing through the public interface is what makes aggressive refactoring safe — the test guards the behaviour while the implementation underneath is restructured freely.

### Sociable, at two grains

| Grain | Scope | Replaced with a double | Runs real |
|---|---|---|---|
| integration (narrow) | one external boundary or adapter + its internal wiring | the external collaborator (via cassette/fixture, per [[software-craft/external-fixtures]]) | all internal collaborators |
| E2E (broad) | the whole system, entry point to edge | nothing inside the system (only the external world, via cassette) | everything |

The line that is *never* crossed is mocking an internal collaborator. Replacing the outside of the system at a boundary is principled — it isolates the system from a service it does not own; replacing the inside rewrites the implementation inside the test, so a change to the implementation has to be made twice and the two copies drift. This is the classicist position Fowler describes, taken at the narrow and broad grains only; the solitary middle is deliberately empty.

### One behaviour per test

- one reason to fail, one reason to pass;
- multiple assertions allowed only when they verify the same behaviour from different angles;
- two independent behaviours become two tests, each named for what it asserts;
- the failing test's name is the diagnosis — if it reads "test_X" and points at nothing specific, it is testing too much.

### Spec value fidelity

| The spec supplies | Fidelity looks like | Noise looks like |
|---|---|---|
| `"USD"` as a base currency | pass it as the base; assert on the rate it yields | assign it to `_`; stuff it in an assert message |
| `10` as an amount | convert it; assert the converted amount | bury it in a helper that consumes it |
| `8.77` as the expected result | assert equality against it | derive it from the computation under test (tautology) |

If a value the interview supplied does not fit the test naturally, that is a signal the spec is unclear about why the value matters — not licence to absorb it as noise.

### Vacuous assertions

A vacuous assertion is one a trivial implementation satisfies — a constant return, an empty collection, an identity function, a `return True`. A test that cannot fail under a trivial impl tests nothing, and the worst case is that it sails through every gate and ships as if it were a contract. The discipline: for every assertion in a test body, ask whether it would fail under a trivial implementation of the system under test; if it would not, the assertion is the smell, not the test surface.

| Smell | Example | Why it's vacuous |
|---|---|---|
| `hasattr`-only | `assert hasattr(report, "generated_at")` | asserts the attribute exists, nothing about its value — a constant attribute passes |
| no-op helper | `_to_jsonable(value: object) -> object: return value` | identity function passes as "JSON-serialisable"; `return True`, `assert True` are the same |
| lower-bound-only | `assert x >= 0` against an empty fixture | trivially true when no value is negative |
| constant-satisfiable | a renderer test that a constant-string renderer passes | any constant output satisfies — the assertion pins nothing about the renderer's behaviour |
| tautology | `assert result == compute(...)` where `result` is `compute(...)` | the expected value is derived from the computation under test; the test cannot fail |

The vacuous-assertion check is gated at `review-test-stubs` (the `vacuous-assertion-free` evidence key), not deferred to `simulate-contracts`. A vacuous test that reaches the simulation gate has already failed the review gate; the simulation catches what review missed, but review is where the smell belongs.

### Property tests prove invariants

An example can only confirm a rule holds for the chosen case; it cannot prove the rule holds generally. Hypothesis (MacIver, 2016) generates inputs across the declared strategy and shrinks any failing case to the smallest counterexample, so a property test is the right tool when the requirement is universal:

| Requirement shape | Right tool |
|---|---|
| "converts 10 USD to 8.77 EUR" (specific case) | an example test with literal values |
| "the converted amount rounds to cents" (universal rule) | a Hypothesis property over generated amounts |
| "history is always latest-first" (universal ordering) | a Hypothesis property over generated histories |

Property tests live alongside the example tests in the same suite; they are not a separate layer, just the tool that matches a universal claim.

## Related

- [[software-craft/test-stubs]] — the `.pyi` signature file each test is authored against first
- [[software-craft/external-fixtures]] — the cassettes and fixtures that replace the external collaborator at the boundary
- [[software-craft/code-review]] — the review method that checks these criteria are met
- [[software-craft/smell-catalogue]] — a vacuous test is dead weight in the Dispensables sense; the smell catalogue cross-links back
- [[software-craft/solid]], [[software-craft/object-calisthenics]] — the design discipline the bodies are held to
