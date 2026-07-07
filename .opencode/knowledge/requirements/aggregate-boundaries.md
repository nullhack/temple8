---
domain: requirements
tags: [aggregate, consistency-boundary, sizing, splitting, ddd]
last-updated: 2026-07-01
---

# Aggregate Boundaries

## Key Takeaways

- An aggregate is a **transactional-consistency boundary**: one root entity, its
  internal objects, and the invariants the root enforces. One transaction
  touches one aggregate (Evans, 2003).
- **Design smaller aggregates** (Vernon, 2013): favour single-entity
  aggregates. Large aggregates breed contention, latency, and false coupling.
- **Reference other aggregates by identity**, never by object reference. It
  keeps boundaries firm and lets consistency across aggregates be eventual.
- **Split when** a candidate holds two unrelated invariants, serves two
  contexts, or changes in ways that never co-occur. The seam is where
  transactional consistency *ends*.
- **Do not split when** invariants genuinely cross and always co-change (shared
  kernel, tightly-coupled siblings). Size follows the invariant, not the noun.

## Concepts

An *aggregate* is the unit of transactional consistency. Evans (2003, ch 4)
defines it as a cluster of domain objects treated as one for data changes: a
single *root entity* is the only member referenced from outside, and the root is
responsible for enforcing the cluster's invariants. Everything that must be true
*together*, at the end of one transaction, lives inside one aggregate;
everything else is outside.

*Smaller is better* is Vernon's (2013) first rule of aggregate design. The
temptation is to group everything that "belongs together" into one big
aggregate; the cost is contention (many transactions serialise on one root),
latency (locking a large object graph), and false coupling (two unrelated
reasons to change, fused). A single-entity aggregate — root alone, no internals
— is the safe default; internals are added only when an invariant demands them.

*Reference by identity* is the boundary-firmness rule. Aggregates reference each
other by identity (a foreign key on the root), never by holding an object
reference to another aggregate's internals. This keeps the consistency boundary
honest — you cannot accidentally traverse into another transaction's state —
and it makes eventual consistency between aggregates natural.

*Splitting* answers "is this one aggregate or two?" The test is the invariant:
if two parts have unrelated invariants, serve different contexts, or change in
ways that never co-occur, they are two aggregates. The seam is precisely where
transactional consistency stops being required.

*Not splitting* answers the same question the other way. Some candidates look
like two aggregates but have invariants that genuinely cross and always
co-change — a shared kernel, or two small siblings whose state is meaningless
apart. There, one aggregate spanning both is correct. Size follows the
invariant, not the noun.

## Content

### What an aggregate is

Evans (2003, ch 4): an aggregate is a cluster of associated objects treated as a
unit for data changes. It has:

- a single **aggregate root** — an entity referenced from outside;
- **internal objects** — entities and value objects reachable only through the
  root;
- **invariants** — consistency rules the root enforces across the cluster.

Outside code holds references only to the root; the root controls all access to
internals. A transaction loads one aggregate through its root, mutates it, and
the root validates the invariants before commit. One transaction, one
aggregate — this is what makes the boundary a *consistency* boundary.

### Size: smaller is better

Vernon (2013, ch 10) makes aggregate sizing the central design decision and
argues, against intuition, for **small** aggregates. The forces:

- **Contention**: every transaction that touches the aggregate locks its root.
  A large aggregate is a serialisation point many transactions fight over.
- **Latency**: loading a large object graph, and validating invariants across
  it, costs more than loading a small one.
- **False coupling**: two unrelated reasons to change, fused in one root, break
  the single-responsibility property and make every change riskier.

A **single-entity aggregate** (root alone, no internal objects) is Vernon's
preferred default. Internal objects are added only when an invariant genuinely
spans them — when two parts must be consistent *together* within one
transaction. The rates-sim *Conversion* is a single-entity aggregate: the root
holds the amount, source, target, and result, and no invariant requires a
larger cluster.

### Referencing other aggregates

Aggregates reference each other **by identity**, not by object reference. A root
holds the identity (a value-object id or a foreign key) of another aggregate,
never a pointer to its internals. Three reasons:

- **Boundary integrity**: there is no way to traverse into another aggregate's
  state mid-transaction; the consistency boundary cannot be accidentally
  punctured.
- **Independence**: each aggregate can be loaded, locked, and committed without
  loading the other.
- **Eventual consistency**: changes that span aggregates are propagated by
  events, not by one transaction mutating two roots — so the system stays
  available under partition.

The rates sim keeps *History* (a repository) separate from the *Conversion*
aggregate: History references conversions by identity and persists them, it does
not enlarge the aggregate.

### When to split

A candidate is two aggregates when any of these holds:

- **Two unrelated invariants** — the cluster enforces two rules that share no
  state; each rule could hold independently.
- **Two contexts** — the candidate serves two bounded contexts, and the
  ubiquitous language differs across them.
- **Non-co-occurring change** — the two parts are changed by different
  operations and never in the same transaction.

The seam is where transactional consistency *stops being required*. Everything
inside the seam must be consistent together in one transaction; everything
outside can be eventually consistent. Splitting along the seam keeps each
aggregate a true consistency boundary rather than an arbitrary grouping.

### When not to split

A candidate that *looks* like two aggregates may be one, when:

- **A shared invariant genuinely crosses** both parts — one rule spans them and
  must hold at every commit, so they cannot be separated without losing
  consistency.
- **Tightly-coupled siblings** — two small objects whose state is meaningless
  apart (a line item without its parent, an address without its owner).
- **A shared kernel** — a small, deliberately shared model that two contexts
  agree to co-own.

The rule is the same in both directions: **size follows the invariant, not the
noun**. If an invariant binds the parts, they are one aggregate; if it does not,
they are two.

## Related

- [[requirements/domain-decomposition]] — discovering the blocks whose sizes
  this file governs.
- [[requirements/ubiquitous-language]] — the terms a context owns, which the
  aggregate root expresses.
