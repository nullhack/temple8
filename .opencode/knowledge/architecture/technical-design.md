---
domain: architecture
tags: [technical-design, architectural-styles, c4-diagrams, hexagonal-architecture, module-structure]
last-updated: 2026-04-29
---

# Technical Design

## Key Takeaways

- Architectural style must be selected based on quality attributes and deployment constraints, not personal preference.
- C4 diagrams provide four levels of abstraction (Brown, 2018): Context (system in environment), Container (deployable units), Component (modules within containers), Code (classes and functions).
- Module structure follows separation of concerns: domain logic must not depend on infrastructure (Cockburn, 2005; Evans, 2003).
- API contracts, event contracts, and interface definitions are the boundaries between modules. Design them before implementation.

## Concepts

**Architectural Styles**: Common styles and when to choose them per [[architecture/quality-attributes#concepts]].

**C4 Diagrams** (Brown, 2018): Four levels of architectural visualization: Context (actors and external systems), Container (deployable units and their tech stacks), Component (internal modules and their responsibilities), Code (individual classes, rarely needed). Always start with Context, then Container. Component diagrams are optional. Code diagrams are rarely necessary.

**Module Structure**: Dependency direction and layer separation per [[architecture/contract-design#concepts]]. Organize by bounded context first (Evans, 2003), then by layer (domain, application, infrastructure).

**Contract-First Design**: Per [[architecture/contract-design#concepts]].

## Content

### Architectural Style Selection

Style selection table per [[architecture/quality-attributes#content]].

Hybrid approaches are valid: a monolith with hexagonal internals, or microservices with event-driven communication between them.

### C4 Diagram Guidelines

- Context diagram: always include. Shows the system boundary and external actors.
- Container diagram: always include. Shows deployable units and tech choices.
- Component diagram: include when module structure is non-trivial
- Code diagram: only for complex algorithms or critical paths

### Module Structure Template

```
feature_title/
  domain/        # Business logic, zero infrastructure imports
  application/   # Use case orchestration
  infrastructure/ # External concerns (DB, HTTP, queues)
  api/           # Delivery mechanism (routes, serializers)
```

## Related

- [[architecture/assessment]]
- [[architecture/quality-attributes]]
- [[architecture/contract-design]]