---
domain: software-craft
tags: [refactoring, fowler, code-quality, refactor-moves]
last-updated: 2026-07-01
---

# Refactoring Techniques

## Key Takeaways

- Refactoring moves are organised by the problem they solve: **composing methods, moving features between objects, organising data, simplifying conditional expressions, simplifying method calls, dealing with generalisation** (Fowler, 1999).
- **Extract Method is the workhorse** — most other moves depend on methods being small enough to name clearly; Long Method is the commonest smell and extraction its commonest fix.
- **Move features to the object that owns the data**: Feature Envy, Inappropriate Intimacy, and Message Chains are all resolved by relocating behaviour next to the data it depends on.
- **Replace conditionals with polymorphism or guard clauses**: Switch Statements and nested `if`s dissolve into a type hierarchy or a sequence of early returns.
- Every move runs **under green tests with the `.pyi` fixed** — a move that needs to change the `.pyi` is a contract gap escalated at review, not a refactor liberty. Mechanics live in Fowler and in the refactor skill; this is the index that points at the right move.

## Concepts

**Composing methods.** Most refactorings depend on methods being short enough to name, which makes composing methods the foundation (Fowler, 1999). Extract Method turns a fragment of a long method into a named helper; Inline Method inverts it when the name adds nothing; Replace Temp with Query turns a temporary variable into a method call so the value is available everywhere. These are the moves that make every other category possible, because they produce the small, named units the others rearrange.

**Moving features between objects.** Behaviour belongs next to the data it uses. Feature Envy — a method that reaches into another class more than its own — is fixed by Move Method; a class doing too much is split by Extract Class; a class doing too little is collapsed by Inline Class; a chain `a.b().c()` is shortened by Hide Delegate. The shared move is relocation: put the method on the object that owns the data it depends on.

**Organising data.** Primitive Obsession is fixed by wrapping a bare value in a domain type (Replace Data Value with Object — the OC-3 rule enforced after the fact); a directly-exposed collection is protected by Encapsulate Collection; a type code that selects behaviour is replaced by a State or Strategy hierarchy. The theme is giving data a home that carries both its meaning and its constraints.

**Simplifying conditionals and calls.** A complex conditional is decomposed into named guards (Decompose Conditional, Replace Nested Conditional with Guard Clauses); a conditional that switches on type is replaced by polymorphism. Method calls are simplified in parallel — Rename Method for clarity, Introduce Parameter Object and Preserve Whole Object for parameter lists, Replace Constructor with Factory Method when construction itself is the responsibility. Clear conditionals and clear calls are the readable surface of a well-factored module.

**Dealing with generalisation — under green, `.pyi` fixed.** Inheritance is refined by Pull Up / Push Down Method and Field, by Extract Superclass or Extract Interface, and by Form Template Method when two methods share a skeleton. Misapplied inheritance becomes composition via Replace Inheritance with Delegation. Throughout, the boundary is fixed: the `.py` is fluid under refactor, the `.pyi` and the tests are not, and conventions (docstrings, formatting) are CI's job, not refactor's. A refactor that needs the `.pyi` to move has found a contract gap and escalates rather than edits.

## Content

### Composing methods

| Move | What it does | When |
|---|---|---|
| Extract Method | turn a fragment into a named helper | a method is long or needs a label to read |
| Inline Method | replace a call with the body | the name adds no clarity |
| Replace Temp with Query | turn a temp into a method call | a temp holds a reused expression |
| Extract Variable | name a complex sub-expression | an expression needs a readable intermediate |

### Moving features between objects

| Move | What it does | When |
|---|---|---|
| Move Method | relocate a method to the class it envies | Feature Envy |
| Move Field | relocate a field to its heavier user | a field is used mostly elsewhere |
| Extract Class | split a class along an axis | Large Class, too many ivars |
| Inline Class | merge a too-small class into its host | Lazy Class |
| Hide Delegate | route through the middle object | Message Chains |
| Remove Middle Man | call the delegate directly | Middle Man |

### Organising data

| Move | What it does | When |
|---|---|---|
| Replace Data Value with Object | wrap a primitive in a domain type | Primitive Obsession |
| Encapsulate Collection | expose a read view, not the collection | a collection field is directly writable |
| Replace Type Code with State/Strategy | replace a type field with a hierarchy | a type field selects behaviour |

### Simplifying conditional expressions and calls

| Move | What it does | When |
|---|---|---|
| Decompose Conditional | extract condition, then, else into named methods | a conditional is hard to follow |
| Replace Nested Conditional with Guard Clauses | early-return the edge cases | nested `if/else` |
| Replace Conditional with Polymorphism | move each branch into a subtype | Switch Statements |
| Introduce Null Object | a do-nothing stand-in for `None` | repeated null checks |
| Rename Method | a name that communicates purpose | the name does not say what it does |
| Introduce Parameter Object | bundle a clump into one value | Long Parameter List, Data Clumps |
| Replace Constructor with Factory Method | delegate construction | construction is shared or conditional |

### Dealing with generalisation

| Move | What it does | When |
|---|---|---|
| Pull Up Method / Field | hoist common code to the superclass | subclasses repeat it |
| Push Down Method / Field | drop specialised code to the subclass | only some subclasses use it |
| Extract Superclass / Interface | factor common shape up | two classes share an interface |
| Form Template Method | pull a shared skeleton up, vary the steps | two methods share structure, differ in a step |
| Replace Inheritance with Delegation | hold a reference instead of subclassing | Refused Bequest |

## Related

- [[software-craft/smell-catalogue]] — the smell that names the problem a move solves
- [[software-craft/object-calisthenics]] — the rules that head the needs off at write time
- [[software-craft/solid]] — the principle a move usually restores
- [[software-craft/design-patterns]] — the larger structure applied when a move is not enough
- [[software-craft/tdd]] — the refactor phase these moves belong to
