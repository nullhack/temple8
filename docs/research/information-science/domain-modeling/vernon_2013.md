# Implementing Domain-Driven Design (Vernon, 2013)

## Citation

Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.
URL: https://www.informit.com/store/implementing-domain-driven-design-9780321834577

## Method

Case Study

## Confidence

High

## Key Insight

Context mapping provides nine inter-context relationship patterns describing how bounded contexts relate to each other, preventing model pollution and reducing integration friction.

## Core Findings

1. **Nine Context Mapping Patterns**: Shared Kernel, Customer-Supplier, Conformist, Anticorruption Layer, Separate Ways, Open Host Service, Published Language, Big Ball of Mud, Partnership
2. **Relationship Trade-offs**: Each pattern carries specific coordination costs and risk implications requiring careful selection
3. **Pattern Selection Guidance**: Use ACL when downstream has limited influence; Customer-Supplier when teams can negotiate; Open Host Service for many standardized consumers
4. **Social Contract Explicit**: Context maps make team relationships, obligations, and constraints transparent
5. **Practical DDD Implementation**: Extends Evans' foundational work with concrete implementation patterns and guidance

## Mechanism

Context mapping makes social and technical contracts between teams explicit. Customer-Supplier demands upstream awareness; Conformist accepts upstream dominance; Anticorruption Layer isolates from model drift. Named relationships clarify obligations and constraints, preventing accidental coupling and model contamination.

## Relevance

Essential for microservices architecture, distributed systems design, team organization. Applied in bounded context definition, API design, organizational patterns. Critical for implementing DDD at scale in complex enterprise environments with multiple development teams.

## Related Research

Vaughn Vernon builds on (Evans, 2003) foundational DDD work. Author of "Reactive Messaging Patterns with the Actor Model" (2015), "Domain-Driven Design Distilled" (2016). Leading DDD practitioner and educator providing concrete implementation guidance for Evans' theoretical framework.
