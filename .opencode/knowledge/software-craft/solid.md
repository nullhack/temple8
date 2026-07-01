---
domain: software-craft
tags: [solid, design-principles, oop, code-quality]
last-updated: 2026-07-01
---

# SOLID

## Key Takeaways

- **SRP** — a class has one reason to change; multiple responsibilities mean multiple change axes that conflict (Martin, 2000).
- **OCP** — entities are open for extension, closed for modification: add behaviour by adding code, not by editing existing code.
- **LSP** — subtypes are substitutable for their base types; a subclass that breaks the parent's contract violates Liskov substitution.
- **ISP** — clients depend only on the interface they use; split fat interfaces into small, cohesive ones.
- **DIP** — depend on abstractions, not concretions; high-level policy and low-level detail both depend on abstractions.
- SOLID is applied **when a smell triggers it**, never speculatively — it is part of the quality bar a review enforces, not a checklist to satisfy in advance of a problem.

## Concepts

**Single Responsibility (SRP).** Martin (2000) frames responsibility as an axis of change: a class with more than one reason to change has more than one responsibility, and when requirements shift it changes in unrelated ways that couple concerns which never belonged together. The test is not "does it do one thing?" but "does it change for one reason?" — a class that edits both currency rates and audit logs will be touched by both a rate-change and an audit-change request, and those are two responsibilities however neatly the methods are named.

**Open-Closed (OCP).** Adding a variant should add code, not edit it. When behaviour is selected by `if/elif` on a kind field, every new variant forces a change to every switch — the type is open for modification and closed for extension, the inverse of the principle. The fix is polymorphism (or Strategy/State): a new variant is a new type that fits an existing interface, and the dispatch sites are unchanged.

**Liskov Substitution (LSP).** Liskov's (1987) subtyping rule, named as a principle by Martin: anywhere a base type is expected, any subtype must work without surprise. A subclass that overrides a method to do nothing, to raise, or to narrow a precondition breaks the parent's contract and will trip a caller that relied on it. The smell is *Refused Bequest*; the fix is usually delegation or pushing the method down, not a fragile inheritance.

**Interface Segregation (ISP).** A client forced to depend on methods it never uses is coupled to changes that do not concern it. A fat interface split into one role-interface per client keeps each dependent small and each change local. The signal is a client importing an interface for two of its ten methods — the other eight are load it does not need.

**Dependency Inversion (DIP).** High-level policy should not reach into low-level detail; both should sit behind abstractions. A module that imports a concrete database adapter is welded to that adapter's implementation; define a Protocol and inject the adapter, and the policy becomes independent of the mechanism. In this workflow the boundary is also where the cassettes and fixtures attach — the abstraction is what lets the real adapter and its replay double satisfy the same contract.

## Content

### Violation → smell → fix

| Principle | Smell | Signal | Fix |
|---|---|---|---|
| SRP | Divergent Change | one class changes for multiple unrelated reasons | Extract Class by axis of change |
| SRP | Large Class | too many fields or methods | Extract Class, Extract Subclass |
| OCP | Switch Statements | `if/elif` on a kind/type/status, edited per variant | Replace Conditional with Polymorphism; Strategy; State |
| OCP | Shotgun Surgery | one variant forces edits across many call sites | move dispatch into the type hierarchy |
| LSP | Refused Bequest | subclass overrides to do nothing or to raise | Push Down Method; Replace Inheritance with Delegation |
| LSP | Alternative Classes w/ Different Interfaces | two classes, same job, different signatures | Extract Superclass; unify behind a Protocol |
| ISP | Fat Interface | client depends on methods it does not call | Extract Interface per client role |
| DIP | Direct Dependency on Concrete | module imports a concrete class | define a Protocol; inject it |
| DIP | Hard-coded Construction | `__init__` builds its own dependencies | inject dependencies; Factory if construction varies |

### Applied when triggered, not speculatively

SOLID is part of the quality bar `review-implementation` and `refactor-green` enforce, alongside Object Calisthenics and the smell catalogue. It is applied *when a smell points at it* — a Divergent Change points at SRP, a Switch Statement at OCP — not run at a class on the chance it might be violating something. Speculative SOLID produces abstraction for its own sake (the Speculative Generality smell), which is itself a defect the review then rejects.

## Related

- [[software-craft/smell-catalogue]] — each SOLID violation manifests as a named smell
- [[software-craft/object-calisthenics]] — the rules that prevent the violations at write time (OC-7 enforces SRP; OC-4 enforces DIP)
- [[software-craft/design-patterns]] — patterns that resolve violations (Strategy resolves OCP)
- [[software-craft/refactoring-techniques]] — the moves that fix a violation once found
