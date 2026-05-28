# Architecture Decision Records (Nygard, 2011)

## Citation

Nygard, M. (2011). "Documenting Architecture Decisions." *Cognitect Blog*. November 15, 2011. Later adopted by ThoughtWorks Technology Radar (2016). https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions

## Source Type

Blog/Article

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Architecturally significant decisions should be documented as short, immutable records capturing the context, decision, rationale, alternatives, and consequences. Each record is written once and never edited. If understanding changes, a new record supersedes the old one.

## Core Findings

1. **Five-part structure**: Title, Context (forces at play), Decision (response to forces), Status (proposed/accepted/superseded), Consequences (resulting context after decision).
2. **Immutability principle**: ADRs are never edited after acceptance. Superseded decisions remain as historical record with references to replacements.
3. **Lightweight format**: One to two pages maximum, written in Markdown, stored in version control with code.
4. **Architecturally significant scope**: Decisions affecting structure, non-functional characteristics, dependencies, interfaces, or construction techniques.
5. **Sequential numbering**: ADRs numbered monotonically and sequentially (never reused) for easy reference.
6. **Conversation with future developers**: Written in full sentences with active voice to communicate reasoning to new team members.
7. **ThoughtWorks adoption**: Added to Technology Radar in 2016, driving widespread industry adoption.

## Mechanism

ADRs work because they externalise architectural reasoning that would otherwise remain tacit, tribal knowledge. By forcing the decision-maker to articulate the context (what forces are at play), the decision (what was chosen), the reason (why this choice over alternatives), and the consequences (what becomes easier or harder), ADRs create a decision trail that new team members can read. Immutability prevents retroactive justification: you cannot rewrite history, only supersede it. The consequences of one ADR often become the context for subsequent ADRs, creating a decision pattern language.

## Relevance

Essential practice for software architecture documentation and knowledge management. Critical for distributed teams, high-turnover environments, and complex systems requiring architectural decision tracking. Widely adopted across the software industry for maintaining architectural reasoning, onboarding new developers, and preventing repeated architectural mistakes. Directly applicable to any project requiring transparent decision-making processes.

## Related Research

- (Kruchten, 2004): Importance of architecture decisions in software development
- (Brown, 2018): C4 model complementing ADR documentation with visual architecture communication