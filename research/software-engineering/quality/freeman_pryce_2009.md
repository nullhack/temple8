# GOOS: Growing Object-Oriented Software, Guided by Tests (Freeman & Pryce, 2009)

## Citation

Freeman, S., & Pryce, N. (2009). *Growing Object-Oriented Software, Guided by Tests*. Addison-Wesley.

## Source Type

Practitioner Book

## Method

Case Study

## Verification Status

Verified

## Confidence

High

## Key Insight

Acceptance tests and unit tests operate at two separate nested timescales - outer loop writes failing acceptance tests before implementation; inner loop drives implementation with unit-level Red-Green-Refactor cycles.

## Core Findings

1. **Double Loop TDD**: Outer loop (acceptance tests) provides direction (what to build); inner loop (unit tests) provides momentum (how to build it)
2. **Nested Timescales**: Acceptance test stays red throughout all inner cycles and goes green only when feature is complete
3. **Direction vs Momentum**: Acceptance tests prevent over-engineering by defining "done"; unit tests drive good internal design
4. **Integration Safety**: Acceptance tests catch integration issues early while unit tests provide rapid feedback
5. **Mock Objects**: Use test doubles to maintain fast, isolated unit tests while preserving design feedback

## Mechanism

Outer loop begins with failing acceptance test for next feature, then enters inner loop of Red-Green-Refactor unit test cycles. Inner loop repeats (write failing unit test, make it pass with minimal code, refactor) until acceptance test passes. This structure provides safety nets at both levels for refactoring and ensures comprehensive test coverage.

## Relevance

Essential for advanced TDD practices, BDD implementation, acceptance test-driven development. Applied in enterprise software development, continuous integration, behavior-driven development. Foundational for understanding relationship between unit and acceptance testing in agile methodologies.

## Related Research

Connects to (Beck, 2002) on TDD fundamentals, (North, 2006) on BDD practices. Part of broader testing methodologies alongside ATDD, specification by example. Related to mock object patterns and test double strategies for maintainable test suites.