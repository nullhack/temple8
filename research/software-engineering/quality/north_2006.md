# Behaviour-Driven Development (North, 2006)

## Citation

North, D. (2006). "Introducing BDD." *Better Software Magazine*, March 2006. Originally published at dannorth.net.

## Source Type

Blog/Article

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

BDD refines TDD by writing tests in domain language of business (Given/When/Then), making them specifications rather than verification tools.

## Core Findings

1. **Test Method Names as Sentences**: Using "should" template (The class *should* do something) keeps tests focused and creates readable documentation
2. **Behaviour vs Test Vocabulary**: Word "behaviour" eliminates TDD coaching confusion - what to test, when to delete tests, test naming becomes clear
3. **Given/When/Then Template**: Structured format captures acceptance criteria as executable specifications that business stakeholders can validate
4. **Ubiquitous Language for Analysis**: BDD provides consistent vocabulary bridging technical and business domains throughout entire analysis process
5. **Business Value Focus**: "What's the next most important thing the system doesn't do?" drives feature prioritization and development direction

## Mechanism

By requiring tests written in domain vocabulary (not implementation language), BDD forces shared understanding between domain experts and developers. "Given a registered user / When user logs in / Then user sees welcome message" specifies observable behaviour stakeholders care about, not technical implementation steps. Eliminates implementation coupling from specifications.

## Relevance

Foundational for behavior-driven development practices, acceptance test-driven development, specification by example. Essential for bridging business-technical communication gaps, creating living documentation, automated acceptance testing frameworks like Cucumber.

## Related Research

Created by Dan North, influenced by Eric Evans' Domain-Driven Design ubiquitous language concept, Chris Matts' business value focus. Led to development of JBehave framework, Ruby RSpec project, Cucumber framework. Foundational for modern BDD tools and practices, specification by example methodologies.