---
domain: software-craft
tags: [object-calisthenics, design-constraints, code-quality, oop]
last-updated: 2026-07-01
---

# Object Calisthenics

## Key Takeaways

- OC-1: one level of indentation per method — deep nesting signals mixed concerns.
- OC-2: no `else` — guard clauses and early returns carry every branch.
- OC-3: wrap all primitives and strings in small domain types — `Age`, not `int`.
- OC-4: one dot per line — `a.b.c` is a Law of Demeter violation.
- OC-5: do not abbreviate — a long name means the scope is too broad or the concept unclear.
- OC-6: keep entities small — classes ≤ 50 lines, packages ≤ 10 classes.
- OC-7: no more than two instance variables per class — more signals multiple responsibilities (Bay, 2008).
- OC-8: first-class collections — a class holding a collection holds nothing else.
- OC-9: no getters, setters, or properties — tell an object to do work, do not ask for its data.

## Concepts

**An exercise, not a law.** Bay (2008) introduced the nine rules as a *calisthenic* — a 1000-line project written under deliberately excessive constraints to force a developer out of the procedural groove and into an object-oriented one. The rules are not universally attainable on real code; their value is the design habit they build, and once the habit is there they become guidelines applied where they clarify. This workflow applies them that way: as the quality bar a review enforces, with the understanding that a rule bent for good reason is a discussion, not an automatic rejection.

**Control-flow and size force decomposition.** The first two rules (one indent, no `else`) and the sixth (small entities) attack the same habit from three angles: nested branches, alternative branches, and sheer length all grow a method past a single decision. Forced apart, each decision becomes a named method with a single responsibility, and a class that cannot exceed fifty lines has to distribute its behaviour across collaborators rather than accrete it. The result is a forest of small objects in place of one large procedure.

**Domain typing and encapsulation keep behaviour home.** Wrapping primitives (OC-3) and first-class collections (OC-8) give the type system enforcement power — an `Age` cannot be added to a `Score` — and give behaviour a natural home attached to the data it describes. One dot per line (OC-4) and no getters (OC-9) finish the job: if a caller cannot reach through an object to its neighbour's data, it has to *tell* the object to act, and the behaviour stays where the data lives instead of leaking into the caller.

**Names and cohesion expose the design.** Refusing abbreviations (OC-5) forces the cost of a too-broad scope to be paid in a name too long to read, which pressures the scope down. Capping instance variables at two (OC-7) is the most consequential constraint: each variable is a cohesive cluster of responsibility, and a third cluster is the signal that a collaborator wants extracting. Together these rules surface design pressure as naming and structure the team can see and act on.

## Content

### The exercise

Bay's chapter in the *ThoughtWorks Anthology* (Pragmatic Bookshelf, 2008) prescribes a small project — about 1000 lines — written strictly under all nine rules at once. The restrictions are intentionally merciless: they exist to break procedural reflex, not to be met comfortably. At the end of the exercise the rules relax into guidelines; on real code they are applied where the pressure they apply produces a clearer design, not as a pass/fail gate applied blindly. A 51-line class is not a defect; it is a prompt to ask what responsibility could be its own object.

### The nine rules

| Rule | Mechanism | What it forces |
|---|---|---|
| OC-1 one indent | extract each nested block | one decision per method |
| OC-2 no `else` | guard clauses, early returns, polymorphism | one path per method; no branch-tracking |
| OC-3 wrap primitives | a small class per domain value | type safety; behaviour attached to data |
| OC-4 one dot | ask the neighbour, do not reach through it | encapsulation; Law of Demeter |
| OC-5 no abbreviations | refuse to shorten | scope pressure; clear concepts |
| OC-6 small entities | class ≤ 50 lines, package ≤ 10 classes | distribution over accretion |
| OC-7 two ivars | cap instance variables at two | one cohesive responsibility per class |
| OC-8 first-class collections | a collection is a class's only field | collection behaviour has a home |
| OC-9 no getters/setters | tell, do not ask | behaviour stays with the data |

### Applied as a guideline, enforced as a bar

`write-test-py`, `refactor-green`, and `review-implementation` all cite Object Calisthenics as part of the quality bar. The bar is real — a smell-laden implementation is rejected — but the rules operate as the diagnostic behind the bar, not as a literal counter. A reviewer who counts dots, indentation levels, or instance variables and rejects on the count alone has mistaken the calisthenic for the law; one who reads a Long Method, notices the fourth level of nesting, and asks for an extraction has used the rule as it was intended.

## Related

- [[software-craft/solid]] — the principles the rules prevent violations of (OC-7 → SRP; OC-4 → DIP)
- [[software-craft/smell-catalogue]] — the smells the rules head off (Primitive Obsession, Message Chains, Large Class)
- [[software-craft/refactoring-techniques]] — the moves that bring code back under a rule once broken
- [[software-craft/code-review]] — the review that applies the bar
