---
domain: software-craft
tags: [source-stubs, typed-stubs, package-structure]
last-updated: 2026-05-08
---

# Source Stubs

## Key Takeaways

- Stubs are created at two levels: project-level creates the package skeleton; feature-level creates typed source stubs per feature.
- Typed stubs are derived from the three contract types in technical design (API, event, interface); they compile but have no behaviour.
- Source stubs contain the absolute minimum to compile and trace: Protocol signatures with `raise NotImplementedError` bodies, no docstrings, no type hints beyond the contract.
- Package structure mirrors the module structure from technical design; the domain package depends on nothing.
- Feature branches are created from the latest main.
- Create artifacts in this order: branch, directories, port interfaces, Protocol stubs, run beehave generate to create test stubs, verify with `beehave check` and `beehave status` for development stage confirmation per [[software-craft/test-stubs#concepts]].

## Concepts

**Two-Level Stub Creation**. Stubs are created at two levels of granularity. **Project-level**: the SA creates the package skeleton only: directory structure mirroring the module layout, `__init__.py` files, port interfaces (Protocol abstractions from hexagonal architecture), and aggregate root class signatures. No entity, value object, or use case stubs are created at this level. **Feature-level**: the SA creates minimum typed stubs for the entities, value objects, and use cases referenced by the current feature's Examples. These feature-level stubs are breadcrumbs from the domain spec. The SE can add, remove, or modify them as the real implementation shape emerges from TDD.

**Typed Stubs from Contracts**. At feature level, Protocol interfaces are derived from the three contract types defined in technical design: API contracts (REST endpoints → Protocol methods), event contracts (domain events → dataclasses with event schema), and interface definitions (hexagonal ports → Protocol abstractions). These stubs compile but have no behaviour. They serve as the architecture's skeleton.

**Minimum Stub Principle**. Source stubs contain the absolute minimum needed to compile and trace. Protocol method signatures with `raise NotImplementedError` bodies: no docstrings, no type hints beyond the contract (return types and parameter types required by the Protocol). Docstrings, type hints, and lint compliance (ruff check, ruff format) are added when reviewers require them, not proactively. Adding them early is waste because refactoring changes code shape and invalidates them.

**Package Structure from Module Structure**. The module structure section of technical design maps directly to the package layout: each module becomes a Python package, each Protocol becomes a file in that package, and each test module mirrors its production counterpart. The domain package depends on nothing; infrastructure packages depend on domain Protocols, never the reverse.

**Branch Setup**. Implementation begins on a feature branch (`feat/<stem>`) created from the latest main. Branch naming follows [[software-craft/git-conventions]].

**Creation Order**. Create artifacts in this order: (1) feature branch from main, (2) package directories from module structure, (3) port interfaces and aggregate root signatures, (4) per-feature: Protocol stubs from contracts + run `beehave generate <feature_id>` to create test stubs per [[software-craft/test-stubs#key-takeaways]], (5) run `beehave check` to verify all Examples have corresponding test stubs.

## Related

- [[architecture/contract-design]]: the three contract types that define stub shapes
- [[architecture/technical-design]]: module structure and package layout
- [[software-craft/test-stubs]]: test stub format and title-based traceability chain
