# SOLID Principles (Martin, 2000)

## Citation

Martin, R. C. (2000). Design Principles and Design Patterns. Object Mentor. [PDF archived at Internet Archive]

## Source Type

Practitioner Book

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Five object-oriented design principles that reduce coupling and increase maintainability when applied together.

## Core Findings

1. **Single Responsibility Principle (SRP)**: A class should have only one reason to change. Each class should have only one responsibility.
2. **Open-Closed Principle (OCP)**: Software entities should be open for extension but closed for modification.
3. **Liskov Substitution Principle (LSP)**: Derived classes must be substitutable for their base classes without altering program correctness.
4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interface methods they don't use.
5. **Dependency Inversion Principle (DIP)**: Depend on abstractions, not concrete implementations.
6. The SOLID acronym was coined around 2004 by Michael Feathers to make these principles memorable.

## Mechanism

Each principle addresses specific coupling pathologies: SRP prevents god-objects by enforcing single responsibility; OCP prevents modification cascades by enabling extension over modification; LSP prevents behavioral contract violations in inheritance hierarchies; ISP prevents fat interfaces that force unnecessary dependencies; DIP enables loose coupling by inverting dependencies toward abstractions. Together they reduce change propagation and make systems more testable.

## Relevance

Foundational for modern software architecture and clean code practices. Directly applicable to module design, interface definitions, and refactoring strategies. Essential for creating maintainable codebases that can evolve without breaking existing functionality.

## Related Research

- (Fowler, 1999): Refactoring patterns that support SOLID principles
- (Beck, 2002): Test-driven development practices that reinforce these design principles