# YAGNI ("You Aren't Gonna Need It") (Beck & Jeffries, 1999)

## Citation

Beck, K., & Jeffries, R. (1999). Extreme Programming principle, originated on the Ward Cunningham Wiki and in comp.software.extreme-programming discussions. Later articulated in Beck, K. (2000). *Extreme Programming Explained*, Addison-Wesley.

## Source Type

Practitioner Book

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Never add functionality until it is required by a failing test or current requirement - speculative code adds complexity without delivering value.

## Core Findings

1. **Principle Definition**: "Always implement things when you actually need them, never when you just foresee that you need them" (Ron Jeffries)
2. **Cognitive Bias Protection**: YAGNI counteracts planning fallacy (overestimating likelihood of predicted needs) and sunk cost bias
3. **Design Priority**: YAGNI operates as highest-priority design rule (YAGNI > KISS > DRY > OC > SOLID > patterns)
4. **XP Integration**: Used with continuous refactoring, automated unit testing, and continuous integration
5. **Expert Validation**: John Carmack noted "rarely architecting for future requirements turns out net-positive"

## Mechanism

YAGNI protects against two cognitive biases: planning fallacy (overestimating likelihood that predicted future needs will materialize) and sunk cost (reluctance to remove expensive-to-write code). By deferring all implementation until demanded by tests or requirements, YAGNI keeps codebase minimal and focused. Must be used with supporting practices like continuous refactoring to avoid technical debt.

## Relevance

Essential for lean software development, preventing over-engineering and feature creep. Applied in TDD workflows, API design, architecture decisions. Fundamental principle in Extreme Programming and Agile methodologies for maintaining code simplicity and reducing maintenance burden.

## Related Research

Connects to (Beck, 2002) on TDD practices, (Fowler, 1999) on refactoring support, (Gamma et al., 1994) on design patterns as lower priority. Part of broader XP methodology alongside KISS principle and DRY principle. Related to Lean principles of waste elimination.