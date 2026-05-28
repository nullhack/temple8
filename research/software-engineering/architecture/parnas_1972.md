# Information Hiding (Parnas, 1972)

## Citation

Parnas, D. L. (1972). "On the criteria to be used in decomposing systems into modules." *Communications of the ACM*, 15(12), 1053–1058. https://doi.org/10.1145/361598.361623

## Source Type

Academic Paper

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

The correct criterion for decomposing a system into modules is **information hiding**: each module hides a design decision that is likely to change. Modules should reveal only what callers need while hiding implementation details.

## Core Findings

1. **Information hiding principle**: Each module should hide one specific design decision that is likely to change, creating a stable interface while allowing implementation flexibility.
2. **Decomposition by change-prone decisions**: Rather than decomposing by execution steps (procedure-based), decompose by decisions most likely to change (data structures, algorithms, I/O formats, external protocols).
3. **Module interface stability**: The module's public interface should be change-stable while the implementation remains change-free from the caller's perspective.
4. **Coupling reduction**: Information hiding prevents tight coupling by making modules depend only on abstract interfaces, not concrete implementations.
5. **Foundation for modern principles**: This 1972 paper established the theoretical foundation for SOLID principles (especially Dependency Inversion), Hexagonal Architecture, and Domain-Driven Design bounded contexts.
6. **Engineering professionalization**: Parnas was among the first to apply traditional engineering principles to software design, earning professional engineering licenses and advocating for software engineering as a legitimate engineering discipline.

## Mechanism

Decomposing by execution steps (procedure-based) creates tight coupling to implementation order. Decomposing by change-prone decisions (information-hiding) allows each decision to be changed independently without affecting other modules. The mechanism works by identifying decisions most likely to change (data structures, algorithms, I/O formats, external service protocols), then making each such decision a module boundary. The module's public interface exposes only what callers need; all implementation details remain hidden and changeable.

## Relevance

Foundational principle for all modern software architecture. Essential for creating maintainable, evolvable systems where changes to implementation details don't cascade through the entire codebase. Critical for microservices design, API development, library design, and any system requiring long-term maintainability. Directly applicable to bounded context identification, dependency injection, and modular system design.

## Related Research

- (Martin, 2000): SOLID principles building on Parnas's information hiding foundation
- (Cockburn, 2005): Hexagonal Architecture applying information hiding to external dependencies