---
domain: software-craft
tags: [design-patterns, gof, oop, refactor, architecture]
last-updated: 2026-07-01
---

# Design Patterns

## Key Takeaways

- Patterns are applied **only when a smell triggers them**, never speculatively — the smell points at the gap, the pattern supplies the structure (Gamma et al., 1994; Shvets, 2014).
- The patterns this workflow's architecture actually hosts are few and recur: **Adapter** at each external boundary, **Repository** for persistence, **Facade** / application service at the entry point, **Strategy / State** for variant behaviour, **Factory** for construction that must not be scattered.
- **Creational** smells (the same object built in several places, telescoping setup) trigger Factory Method or Builder.
- **Structural** smells (branching on a type field, feature envy, parallel hierarchies) trigger Strategy, Adapter, Move Method, or Bridge.
- **Behavioural** smells (one class's state field sprouting conditionals, fan-out notification, two functions sharing a skeleton) trigger State, Observer, or Template Method.
- The core heuristic: if adding a variant means editing existing functions, that is the smell a pattern removes — the code should be open for extension and closed for modification (OCP).

## Concepts

**Applied when triggered, not collected.** A pattern is a structural fix for a recurring problem, and the problem announces itself as a smell (Gamma et al., 1994; Shvets, 2014). Applying a pattern without the smell is Speculative Generality — an abstraction bought against a future that never arrives — which the smell catalogue rejects on sight. The discipline is to let the smell name the gap and the pattern fill it, never to fit the code to a pattern because the pattern is familiar.

**A small, recurring set.** This workflow's outside-in layering produces a handful of patterns repeatedly. An external service attaches behind an **Adapter** that presents the boundary as a protocol the domain understands; persistence sits behind a **Repository** that loads and stores aggregates; the entry point (a CLI, a request handler) is a thin **Facade** or application service composing the pieces; variant behaviour is **Strategy** or **State**, not a type field with a switch; construction that several callers share is a **Factory**. Most contracts need none of these; when one does, the smell makes it obvious which.

**Creational, structural, behavioural.** The GoF categories still sort the triggers. Creational smells cluster around *how objects are built* — scattered `__init__` calls, telescoping constructors — and yield Factory or Builder. Structural smells cluster around *how types are wired* — a switch on a kind, a method that envies its neighbour, two hierarchies growing in lockstep — and yield Strategy, Adapter, Move Method, or Bridge. Behavioural smells cluster around *how responsibility is distributed* — a state machine outgrowing its class, a change fanning out to many listeners, two algorithms sharing a skeleton — and yield State, Observer, or Template Method.

**Open for extension, closed for modification.** The single thread through pattern selection is the Open-Closed Principle: a place in the code that must be edited every time the domain grows is a defect, and the pattern that removes it is the one that lets a new variant arrive as a new type fitting an existing interface. Procedural code is open to modification; the pattern closes it and opens it to extension instead.

## Content

### Smell → pattern lookup

| Smell | Pattern |
|---|---|
| same object constructed in 3+ places | Factory Method |
| multi-step setup before an object is valid | Builder |
| `if/elif` branching on a type/kind/status field | Strategy (behaviour varies) or State (transitions) |
| a method uses another class's data more than its own | Move Method |
| two hierarchies growing in lockstep | Bridge |
| one state field sprouting conditionals across methods | State |
| a change fans out to many listeners directly | Observer |
| two functions share an algorithm skeleton, differ in a step | Template Method |
| an external service with the wrong interface | Adapter |
| a complex subsystem needs one simple entry point | Facade |
| primitive and composite objects must be treated the same | Composite |

### The patterns this workflow hosts

| Pattern | Where it appears in this flow |
|---|---|
| Adapter | wraps an external service behind a protocol the domain speaks (the cassettes replay through it) |
| Repository | loads and stores aggregates; hides the persistence mechanism behind a collection-like interface |
| Facade / application service | the entry point — a CLI command, a handler — that composes the pieces and owns no domain logic |
| Strategy / State | replaces a type-field switch with a polymorphic hierarchy |
| Factory | centralises construction shared by several callers |
| value object | a small, immutable, domain-typed wrapper (OC-3) — `Rate`, `Amount`, not bare `float` |

A contract that needs none of these is the common case; a contract that needs one announces it through a smell that the review and refactor steps surface.

## Related

- [[software-craft/smell-catalogue]] — the smells that trigger pattern selection
- [[software-craft/solid]] — OCP, the principle behind "open for extension, closed for modification"
- [[software-craft/refactoring-techniques]] — the smaller moves applied before a pattern is warranted
- [[software-craft/source-stubs]] — the `.pyi` an adapter or repository is implemented to satisfy
