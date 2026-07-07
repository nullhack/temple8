---
domain: software-craft
tags: [code-smells, refactoring, fowler, code-quality]
last-updated: 2026-07-01
---

# Smell Catalogue

## Key Takeaways

- **Bloaters** (Long Method, Large Class, Primitive Obsession, Long Parameter List, Data Clumps) are structures that grew too large; extract function or class, replace the primitive with an object, introduce a parameter object (Fowler, 1999).
- **Object-Oriented Abusers** (Switch Statements, Temporary Field, Refused Bequest, Alternative Classes with Different Interfaces) misapply OOP; reach for polymorphism, Extract Class, or delegation (Fowler, 1999).
- **Change Preventers** (Divergent Change, Shotgun Surgery, Parallel Inheritance Hierarchies) make change ripple; restructure along the axis of change or move the data (Fowler, 1999; Shvets, 2014).
- **Dispensables** (Duplicate Code, Lazy Class, Data Class, Dead Code, Speculative Generality) are dead weight to delete, inline, or merge — and a Comment is the symptom of code that should have been extracted or renamed instead.
- **Couplers** (Feature Envy, Inappropriate Intimacy, Message Chains, Middle Man, Incomplete Library Class) over-couple objects; move the method, hide the delegate, collapse the middle man, or extend a class you cannot modify via a foreign method (Fowler, 1999; Shvets, 2014).

## Concepts

**Bloaters** grow by accretion — one more line, one more field, one more parameter — until they block the reader. They are rarely introduced deliberately; they creep in because adding is cheaper than extracting. Long Method needs a section label to read; Large Class accretes responsibilities until its name swells with nouns; Primitive Obsession uses a bare `int` where an `Age` or a `Quantity` would carry meaning; Long Parameter List and Data Clumps signal that related values have not yet been recognised as the object they want to be (Fowler, 1999; Shvets, 2014).

**Object-Oriented Abusers** are OOP applied incompletely. A Switch Statement selects on a kind field where polymorphism would dispatch; Temporary Field holds a value set on only some paths; Refused Bequest is a subclass that inherits what it does not want; Alternative Classes with Different Interfaces are two types doing one job under two names. Each is the wrong tool being used part-way — inheritance where delegation fits, conditionals where a type hierarchy belongs (Shvets, 2014).

**Change Preventers** are the most damaging because they resist change. Divergent Change sends one class in several unrelated directions; Shotgun Surgery scatters one concept across many classes; Parallel Inheritance Hierarchies force new subclasses in lockstep. The shared symptom is that a single, coherent change makes the codebase bleed in many places at once, and the fix is to re-group code around the axes that actually change together (Fowler, 1999).

**Dispensables** carry no weight. Duplicate Code repeats logic it should share; Lazy Class and Data Class earn too little of their keep; Dead Code is unreachable; Speculative Generality is abstraction bought on credit against a future that never arrives. A Comment belongs here in spirit: a comment that explains *what* the code does is usually standing in for an extraction or a rename that would make the comment unnecessary — and in a workflow that forbids comments outright, that pressure becomes the rule that the code itself has to be clear (Fowler, 1999).

**Couplers** over-bind objects. Feature Envy reaches into a neighbour's data more than its own; Inappropriate Intimacy reads another's privates; Message Chains navigate `a.b().c().d()`; Middle Man forwards every call without adding a thought. Each replaces one coupling with another unless the fix moves behaviour to where the data already lives, so the conversation between objects shortens to the immediate neighbours (Fowler, 1999; Shvets, 2014).

## Content

### Bloaters

| Smell | Signal | Fix |
|---|---|---|
| Long Method | a section needs a label to understand; > ~10 lines | Extract Method; Decompose Conditional |
| Large Class | too many fields/methods; name stuffed with nouns | Extract Class; Extract Subclass |
| Primitive Obsession | a bare primitive standing for a domain value | Replace Data Value with Object; Introduce Parameter Object |
| Long Parameter List | 3+ params, or a group recurring across signatures | Introduce Parameter Object; Preserve Whole Object |
| Data Clumps | the same 2–3 values always travel together | Extract Class; Introduce Parameter Object |

### Object-Oriented Abusers

| Smell | Signal | Fix |
|---|---|---|
| Switch Statements | `if/elif` or `match` on a kind/type/status | Replace Conditional with Polymorphism; State; Strategy |
| Temporary Field | a field set on only some paths; `None` "shouldn't happen" | Extract Class; Introduce Null Object |
| Refused Bequest | a subclass overrides to do nothing or to raise | Push Down Method; Replace Inheritance with Delegation |
| Alternative Classes w/ Different Interfaces | two classes, one job, different names | Rename Method; Extract Superclass; unify behind a Protocol |

### Change Preventers

| Smell | Signal | Fix |
|---|---|---|
| Divergent Change | one class changes for multiple unrelated reasons | Extract Class along each axis of change |
| Shotgun Surgery | one concept change edits many classes | Move Method/Field; Inline Class; co-locate |
| Parallel Inheritance Hierarchies | a new subclass here forces one there | Move Method/Field to flatten or unify |

### Dispensables

| Smell | Signal | Fix |
|---|---|---|
| Duplicate Code | the same logic in 2+ places | Extract Method; Pull Up Method; Form Template Method |
| Lazy Class | a class that does too little | Inline Class; Collapse Hierarchy |
| Data Class | fields with getters/setters, no behaviour | Move Method into it; Encapsulate Field |
| Dead Code | unreachable, unused | delete it |
| Speculative Generality | abstraction with no current caller | Inline Class/Method; remove the unused parameter |
| Vacuous Test | an assertion a trivial implementation (constant, identity, `assert True`) satisfies | rewrite the assertion to pin observable behaviour per [[software-craft/test-design]] |

### Couplers

| Smell | Signal | Fix |
|---|---|---|
| Feature Envy | a method uses another class's data more than its own | Move Method |
| Inappropriate Intimacy | reaching into another's privates | Move Method/Field; Extract Class; delegation |
| Message Chains | `a.b().c().d()` | Hide Delegate; Extract Method |
| Middle Man | most methods are one-line forwards | Inline Class; Remove Middle Man |
| Incomplete Library Class | a library class you need to extend but cannot modify | Introduce Foreign Method; Introduce Local Extension |

## Related

- [[software-craft/refactoring-techniques]] — the moves each smell entry points at
- [[software-craft/solid]] — the principle a smell usually violates
- [[software-craft/object-calisthenics]] — the rules that head the smells off at write time
- [[software-craft/code-review]] — the review that names a smell a defect
