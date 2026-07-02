---
domain: software-craft
tags: [design-patterns, gof, oop, refactor, architecture]
last-updated: 2026-07-02
---

# Design Patterns

## Key Takeaways

- Patterns are applied **only when a smell triggers them**, never speculatively — the smell points at the gap, the pattern supplies the structure (Gamma et al., 1994; Shvets, 2014).
- The GoF sort the patterns into three families by what they structure: **creational** (how objects are built), **structural** (how types are wired together), **behavioural** (how responsibility is distributed).
- The single thread through selection is the **Open-Closed Principle**: a place in the code edited every time the domain grows is the defect a pattern removes, turning modification into extension.
- **Prefer the simplest structure that removes the smell.** A pattern is one option alongside the smaller refactoring moves, not a default — reach for it when the simpler move (Extract Method, Move Field, a parameter object) cannot carry the weight (KISS, YAGNI).
- Patterns are **language-neutral structures**; the idiom that realises them is the host language's choice (a function reference, a generic, a trait). The pattern names the relationship; the language supplies the syntax.

## Concepts

**Applied when triggered, not collected.** A pattern is a named structural fix for a recurring problem, and the problem announces itself as a smell (Gamma et al., 1994; Shvets, 2014). Applying a pattern without the smell is Speculative Generality — an abstraction bought against a future that never arrives, which the smell catalogue rejects on sight. The discipline is to let the smell name the gap and the pattern fill it, never to fit the code to a pattern because the pattern is familiar.

**Three families.** Creational patterns address *how objects are built* — scattered construction, telescoping setup — and yield Factory, Builder, Prototype. Structural patterns address *how types are wired* — a switch on a kind, parallel hierarchies, an incompatible interface — and yield Strategy, Adapter, Bridge, Composite, Facade. Behavioural patterns address *how responsibility flows* — a state machine outgrowing its class, a change fanning out to listeners, two algorithms sharing a skeleton — and yield State, Observer, Template Method, Visitor. The family is read off the smell, not chosen in advance.

**Open for extension, closed for modification.** Procedural code is open to modification: every new variant edits an existing branch. The pattern closes that branch and opens it to extension instead — a new variant arrives as a new type fitting an existing interface. This is the OCP heartbeat: a site that must be re-edited on every domain change is the precise defect the pattern removes.

**Simplest structure that removes the smell.** A pattern is not the first move; it is the move that remains after Extract Method, Move Field, or a parameter object have proven insufficient. Reaching for Abstract Factory where a function would do, or Builder where two arguments would suffice, imports structure the smell did not justify. The rule is KISS and YAGNI applied to structure itself: the lightest fix that dissolves the smell is the right one, and a pattern earns its weight only when the lighter moves cannot carry it.

**Language-neutral; idiom is local.** A Strategy is a polymorphic family whether it is realised by a class hierarchy, a function reference, or a first-class callable; an Adapter is a translation layer whether it wraps by composition or by a language's trait. The pattern names the relationship; the host language supplies the idiomatic syntax. Modern languages fold several GoF patterns into single constructs (a callable replaces Command and Strategy; a generator replaces Iterator; a protocol/interface replaces Adapter scaffolding) — the pattern is still present where the relationship is, just without ceremony.

## Content

### The catalog

| Pattern | Intent | Triggers (smell) |
|---|---|---|
| **Creational** | | |
| Factory Method | one object creation, deferred to subclasses | same object constructed in 3+ places; construction scattered |
| Abstract Factory | a family of related objects, kept consistent | cross-family construction that must not mix |
| Builder | separate complex construction from its representation | telescoping constructor; multi-step setup before valid |
| Prototype | new objects by copying a prototype | expensive or duplicated construction; state-only differences |
| Singleton | one instance, global access | shared state accessed widely *(use with caution — often a coupling smell)* |
| **Structural** | | |
| Adapter | make an incompatible interface usable | an external service with the wrong interface |
| Bridge | split abstraction from implementation; vary both | parallel inheritance hierarchies |
| Composite | treat individuals and compositions uniformly | primitive and composite must be handled the same (trees) |
| Decorator | add behaviour without subclassing | combinatorial explosion of optional behaviours |
| Facade | one simplified entry to a subsystem | a complex subsystem needs one simple front |
| Flyweight | share fine-grained state | vast numbers of near-identical objects |
| Proxy | a placeholder controlling access | lazy load, access control, remote indirection |
| **Behavioural** | | |
| Chain of Responsibility | pass a request along handlers until one handles | a request with an unknown handler; sequential fallback |
| Command | encapsulate a request as an object | queueing, undo, parameterised callbacks |
| Iterator | sequential access without exposing structure | traversal coupled to the collection's representation |
| Mediator | centralise how peers interact | many-to-many coupling between colleagues |
| Memento | capture and restore internal state | rollback / undo of state |
| Observer | notify dependents of state change | a change fans out to many listeners |
| State | change behaviour as internal state changes | one state field sprouting conditionals across methods |
| Strategy | a family of interchangeable algorithms | variant behaviour selected by a flag or switch |
| Template Method | a skeleton with steps deferred to subclasses | two functions share a skeleton, differ in a step |
| Visitor | separate an operation from the structure it runs on | operations accumulating on a stable class set |

### Patterns at the type surface

A pattern becomes visible at the **type-definition layer** — the signatures, relationships, and compositions that the contract surface declares — before any behaviour is written. A signature that branches on a kind field (a `type: str` later switched on) is Strategy or State asking to be born; two hierarchies declared in lockstep are Bridge; construction repeated across several entry points is Factory; a type that exposes another's internals to its callers is a Facade waiting to hide the subsystem. The defining step is where these signals are read, because the relationship is the contract: the shape declared there is what every caller will depend on, and reshaping it later costs more than reading it now. A pattern chosen at the type surface is chosen from the smells the relationships themselves emit.

### The patterns this workflow hosts

| Pattern | Where it appears in this flow |
|---|---|
| Adapter | wraps an external service behind an interface the domain speaks (cassettes replay through it) |
| Repository | loads and stores aggregates; hides persistence behind a collection-like interface |
| Facade / application service | the entry point — a CLI command, a handler — that composes the pieces and owns no domain logic |
| Strategy / State | replaces a type-field switch with a polymorphic family |
| Factory | centralises construction shared by several callers |
| value object | a small, immutable, domain-typed wrapper — the domain value, not a bare primitive |

A contract that needs none of these is the common case; a contract that needs one announces it through a smell that the review and refactor steps surface.

## Related

- [[software-craft/smell-catalogue]] — the smells that trigger pattern selection
- [[software-craft/solid]] — OCP, the principle behind "open for extension, closed for modification"
- [[software-craft/refactoring-techniques]] — the smaller moves tried before a pattern is warranted
- [[software-craft/source-stubs]] — the type surface where pattern relationships are first declared
