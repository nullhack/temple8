# Spring Boot Integration Testing: Full Context, Stubbed Boundaries, Zero Flakiness (Turmyshev, 2026)

## Citation

Turmyshev, D. (2026). "Spring Boot Integration Testing: Full Context, Stubbed Boundaries, Zero Flakiness." *DEV Community* / *bitdive.io blog*, 26 February 2026.
URL: https://dev.to/dmitry_turmyshev/spring-boot-integration-testing-full-context-stubbed-boundaries-zero-flakiness-1kcn

## Method

Practitioner blog article.

## Confidence

High — verified primary source; the boundary rule cited in `external-fixtures` is quoted verbatim from this article.

## Key Insight

An integration test runs the full service context (real beans, real database, real HTTP stack) and stubs only what crosses the service boundary — never the internal chain — because the bugs that ship to production live at the seams that unit tests mock away.

## Core Findings

1. Internal to the service (run real in the test): the full application context, business logic, data access (repositories, ORM mappings, SQL), infrastructure (`@Transactional`, validation, caching), the HTTP layer, and adapters.
2. External to the service (stubbed): other microservices, third-party APIs, outbound message queues, and — verbatim — "any dependency that introduces network latency, rate limits, or data you don't control."
3. A service can pass 100% unit coverage and still break production at the mocked seams: serializer misconfiguration, missing validation, transaction-proxy self-invocation, queries that fail the real schema, DTO field renames, security filters, aspect side effects.
4. The governing rule: stub only what crosses the boundary; never mock internal services or repositories for convenience, because that severs exactly the chain the integration test exists to exercise.

## Mechanism

The test enters through the real HTTP endpoint and exits through a real database write, with every internal bean live; only the responses of the outside world are replaced — a bean mock for interface clients, a WireMock/MockWebServer for the real HTTP serialization path, an embedded broker or producer mock for queues. Because the seams run real, a break at any link (serialization, transaction, query, mapping) surfaces as a test failure rather than hiding behind a stub.

## Relevance

Grounds the capture boundary in `external-fixtures`: a cassette captures only what lives outside the service — third-party APIs and SaaS, external managed databases, queues you do not own, object stores you call. In-project databases and UI are internal: designed here, specified by tests and migrations, and never captured in a cassette. The "latency, rate limits, or data you don't control" criterion is the test for whether a dependency is external.

## Related Research

- Moskvin 2025 (how to scrub the external captures this boundary rule produces)
