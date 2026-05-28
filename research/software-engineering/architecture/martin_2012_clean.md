# Clean Architecture (Martin, 2012)

## Citation

Martin, R. C. (2012). "The Clean Architecture." *8th Light Blog*. Later expanded in *Clean Architecture: A Craftsman's Guide to Software Structure and Design* (2017), Prentice Hall. ISBN 978-0-13-449416-6.

## Source Type

Practitioner Book

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

The dependency arrow always points inward: from infrastructure toward application toward domain. The domain knows nothing about frameworks, databases, or external services.

## Core Findings

1. **Dependency Rule**: Source code dependencies must point inward only. Outer layers can depend on inner layers, but inner layers must never depend on outer layers.
2. **Concentric layer structure**: Four layers from outside to inside: Frameworks/Drivers → Interface Adapters → Application Business Rules (Use Cases) → Enterprise Business Rules (Entities).
3. **Framework independence**: The architecture doesn't depend on frameworks; frameworks are tools to be used, not architectures to be conformed to.
4. **Testable in isolation**: Business rules can be tested without UI, database, web server, or any external element because dependencies point inward.
5. **Database independence**: Business rules are not bound to the database. You can swap Oracle for SQL Server, MongoDB, CouchDB, or something else without affecting business rules.
6. **UI independence**: The UI can change without changing the rest of the system. Web UI could be replaced with console UI without changing business rules.
7. **Building on previous architectures**: Clean Architecture synthesizes Hexagonal Architecture (Cockburn, 2005), Onion Architecture, Screaming Architecture, and DCI into a unified approach.

## Mechanism

Clean Architecture builds on Hexagonal Architecture and layer-based approaches by making the dependency rule explicit: source code dependencies must point inward only. The outermost layers (frameworks, drivers, UI, database) are details that can be changed without affecting inner layers. The innermost layer (entities, use cases) contains business rules that have no knowledge of the outside world. This ensures that the domain is both testable in isolation and insulated from infrastructure churn. Dependency Inversion Principle enables this by having high-level modules define interfaces that low-level modules must implement.

## Relevance

Foundational architecture pattern for creating maintainable, testable, framework-independent systems. Essential for microservices design, domain-driven design implementation, and any system requiring long-term maintainability. Critical for applications where business logic must evolve independently of technical infrastructure choices.

## Related Research

- (Parnas, 1972): Information hiding principles underlying Clean Architecture's dependency rule
- (Cockburn, 2005): Hexagonal Architecture that Clean Architecture builds upon and generalizes