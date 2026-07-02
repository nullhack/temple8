# Refactoring.Guru (Shvets, 2014)

## Citation

Shvets, A. (2014–present). *Refactoring.Guru*. https://refactoring.guru/
URL: https://refactoring.guru/

## Method

Case Study

## Confidence

High

## Key Insight

Refactoring follows systematic catalog of 66 techniques triggered by 21 code smells, creating diagnostic chain from problem identification to pattern application.

## Core Findings

1. **Smell-first methodology**: 21 code smells organized into 5 categories (Bloaters, OO Abusers, Change Preventers, Dispensables, Couplers) drive refactoring decisions.
2. **Systematic technique catalog**: 66 refactoring techniques organized into 6 categories (Composing Methods, Moving Features between Objects, Organizing Data, Simplifying Conditional Expressions, Simplifying Method Calls, Dealing with Generalization).
3. **Pattern-smell connection**: Each of 22 GoF design patterns triggered by specific code smell, creating motivation for pattern application.
4. **Diagnostic methodology**: Smell → refactoring technique → design pattern progression prevents speculative application.
5. **Visual learning approach**: Comprehensive illustrations and examples make complex concepts accessible to practitioners.

## Mechanism

The catalog provides smell-first approach: identify code smell, then apply corresponding refactoring technique or design pattern. Five smell categories group related pathologies: Bloaters (structures grown too large), OO Abusers (misapplied OOP), Change Preventers (changes that ripple), Dispensables (dead weight), Couplers (excessive inter-object dependency). Each smell entry links to refactoring techniques that resolve it, and each pattern entry explains which smell triggers it. Creates diagnostic chain where each step is motivated by previous one rather than applied speculatively.

## Relevance

Essential reference for code quality improvement, refactoring practice, and design pattern application. Widely used by developers for systematic code improvement and architectural decision-making. Provides practical methodology for identifying and resolving code quality issues.

## Related Research

- (Fowler, 1999): Foundational refactoring catalog and methodology
- (Gamma et al., 1995): Original Gang of Four design patterns catalog