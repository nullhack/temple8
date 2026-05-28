# Hexagonal Architecture (Ports & Adapters) (Cockburn, 2005)

## Citation

Cockburn, A. (2005). "Hexagonal Architecture." *Alistair Cockburn's blog*. Originally discussed on the Portland Pattern Repository wiki in the early 2000s; formalized as "Ports and Adapters" in 2005.

## Source Type

Blog/Article

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Software should be designed so that the domain core has no dependency on any external technology or delivery mechanism. The domain exposes ports (interfaces) that define what it needs; adapters implement those ports for specific technologies.

## Core Findings

1. **Dependency inversion principle**: Infrastructure depends on domain abstractions, not the other way around, making the domain testable in isolation and swappable in deployment.
2. **Ports and adapters pattern**: Ports are domain-defined interfaces; adapters are infrastructure implementations that connect external systems to the domain through these ports.
3. **Technology independence**: The same domain logic can be exercised through any delivery mechanism (HTTP, CLI, message queue, test harness) without modification.
4. **Symmetrical architecture**: All external dependencies (databases, UI, external services, test harnesses) are treated equally as adapters, eliminating the traditional "top" and "bottom" of layered architectures.
5. **Framework isolation**: The domain remains independent of frameworks, databases, and UI technologies, enabling easier testing and technology evolution.
6. **Business logic protection**: Core business rules are isolated from infrastructure concerns, making them more maintainable and less brittle to external changes.

## Mechanism

By reversing the dependency so that infrastructure depends on domain abstractions (not the other way around), the domain becomes testable in isolation and swappable in deployment. The hexagonal shape represents that there are multiple ways to interact with the application - through different ports - and each port can have multiple adapters. This ensures the domain remains independent of frameworks, databases, and UI, and that the same domain logic can be exercised through any delivery mechanism without modification.

## Relevance

Foundational pattern for clean architecture, domain-driven design, and microservices architecture. Essential for creating testable, maintainable systems that can evolve independently of infrastructure concerns. Critical for understanding how to structure applications to achieve technology independence and high testability. Directly applicable to API design, service architecture, and any system requiring multiple integration points.

## Related Research

- (Martin, 2017): Clean Architecture building on Cockburn's dependency inversion principles
- (Fowler, 2003): Architectural decision-making frameworks that support ports and adapters pattern