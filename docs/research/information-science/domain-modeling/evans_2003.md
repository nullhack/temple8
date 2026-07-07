# Domain-Driven Design (Evans, 2003)

## Citation

Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.
URL: https://www.domainlanguage.com/ddd/

## Method

Theoretical

## Confidence

High

## Key Insight

Complex software must be built around shared domain model - a ubiquitous language used by both domain experts and developers in conversation, code, and documentation.

## Core Findings

1. **Ubiquitous Language**: Single terminology shared between domain experts and developers eliminates translation costs and catches misunderstandings early
2. **Bounded Contexts**: Define where terms have single meaning, preventing incoherent unified models when terms mean different things in different subdomains
3. **Aggregates**: Define transactional consistency boundaries - all invariants within aggregate must hold after each operation
4. **Context Mapping Patterns**: Upstream/Downstream, Anti-corruption Layer, Conformist, Open-host Service define how separate bounded contexts interact
5. **Strategic vs. Tactical Design**: Strategic focuses on bounded contexts and context mapping; tactical focuses on entities, value objects, services

## Mechanism

Ubiquitous language eliminates translation costs between domain experts and developers. When "Order" means same thing in conversation and code, misunderstandings are caught early. Bounded contexts prevent alternative unified model becoming incoherent. Aggregates enforce transactional consistency boundaries with operations spanning aggregates accepting eventual consistency.

## Relevance

Essential for complex software architecture, microservices design, team organization, domain modeling. Applied in enterprise software development, distributed systems architecture. Foundational for strategic system design aligning technical implementation with business domains and expert knowledge.

## Related Research

Connects to (Brandolini, 2012) on Event Storming for domain discovery, (Vernon, 2013) on DDD implementation. Part of broader software architecture approaches alongside microservices, CQRS, event sourcing. Related to Conway's Law and team topologies for organizational design.