# UnitTest (Fowler, 2014)

## Citation

Fowler, M. (2014). "UnitTest." *martinfowler.com*, bliki entry, 5 May 2014 (revised 24 Oct 2014, 9 Mar 2017).
URL: https://martinfowler.com/bliki/UnitTest.html

## Method

Definitional practitioner essay; distinguishes two schools of unit testing.

## Confidence

High — the canonical statement of the solitary/sociable distinction.

## Key Insight

Unit tests divide on the axis of collaborator treatment (solitary replaces them with test doubles, sociable lets the real ones run), not on test size; the "solitary"/"sociable" terms were coined by Jay Fields, and the choice between them is the real divide between the classicist and mockist schools.

## Core Findings

1. The "a unit test is small" definition is the wrong axis; "unit" is situational (a class, a cluster, a function).
2. The real axis is solitary (collaborators replaced with doubles) versus sociable (real collaborators exercised) — terms due to Jay Fields.
3. The classicist school (Fowler's) prefers sociable tests, reaching for doubles only at awkward or non-deterministic collaborations; the mockist school insists on solitary.
4. Doubles for external resources (databases, remote services) are a useful guideline for non-determinism and speed, not an absolute rule.

## Mechanism

A sociable unit test lets the real object graph run within the test, so a failure traces a real interaction; a solitary test severs that graph so each unit is blamed in isolation. The mockist school argues isolation localises fault and drives design through role interfaces; the classicist school argues real interactions are where defects live and that excessive mocking couples tests to implementation. Fowler's contribution is to name the axis (crediting Fields) rather than legislate the size, so a team chooses on design grounds.

## Relevance

Grounds the workflow's two-grain sociable-only policy: integration tests (one boundary/adapter with real internal wiring + replayed cassette) and e2e tests (the full system through the entry point), with no solitary unit tests — the policy follows Fowler's classicist/sociable default.

## Related Research

- Meszaros 2007 (xUnit test patterns)
- Fields (Working Effectively with Unit Tests) — origin of the solitary/sociable terms
