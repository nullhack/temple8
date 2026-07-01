---
domain: requirements
tags: [domain-decomposition, bounded-context, aggregate, gap-analysis, coverage]
last-updated: 2026-07-01
---

# Domain Decomposition

## Key Takeaways

- The build unit is a **DDD building block** — primarily an **aggregate** (the
  transactional-consistency core), with domain services, application services,
  repositories, anti-corruption layers, and value objects as supporting blocks.
  It is coarser than an entity, an operation, or a test (those are downstream).
- Capture **names + rough boundaries only** — coarse-then-detailed. The spec
  (signatures, invariants, types) is deferred to plan and build (Patton, 2014).
- Decompose along **bounded-context borders**: each block belongs to one
  context; a candidate straddling two contexts is two blocks, or signals a
  missing context. Sizing and splitting rules live in
  [[requirements/aggregate-boundaries]] (Evans, 2003; Vernon, 2013).
- **Gap analysis is a coverage matrix**: every bounded context → ≥1 block; every
  quality attribute → ≥1 block that carries it (Wiegers, *Software
  Requirements*, 2nd ed). An empty row is a gap; a dense cell is a block doing
  too much.
- **Flag gaps, do not fill them** — a gap is a detection signal, not an
  authoring trigger. Escalate to elicitation; preserve trace-to-stakeholder.

## Concepts

A *building block* is the unit a context is built from. Evans (2003, Part II)
names the set: entities, value objects, domain services, repositories,
factories, and — binding them — aggregates. Of these, the **aggregate** is the
load-bearing one: it is the only block that owns transactional consistency, so
identifying aggregates is the centre of gravity of decomposition. Services,
repositories, and anti-corruption layers exist to support aggregates or bridge
contexts; value objects are leaves. A block is a *capability* ("rate
conversion"), never a *mechanism* ("RatesRepository").

*Coarse-then-detailed* governs the grain at which blocks are captured. Patton
(2014) makes the same point for stories — they are *discovered*, not authored
upfront. At this level a block is a name and a rough boundary; its operations,
invariants, and types arrive later, in the test stubs of plan and the
implementation of build.

The *bounded context* is the decomposition boundary. Inside one context a
ubiquitous-language term has exactly one meaning (Evans, 2003); a block is owned
by exactly one context. A candidate that genuinely serves two contexts is two
blocks, or evidence that the context map is wrong. How big each block is — the
consistency boundary — is the separate question answered in
[[requirements/aggregate-boundaries]].

*Gap analysis* reframes completeness as coverage, following the requirements
traceability matrix (Wiegers, *Software Requirements*, 2nd ed; Gotel &
Cleland-Huang, 2012). Two kinds of row must each map to at least one block:
bounded contexts (does every context have something living in it?) and quality
attributes (is every non-functional concern — performance, security,
auditability — carried by some block?). Quality attributes are not themselves
blocks; they are concerns a block must satisfy.

*Flag, don't fill* keeps decomposition honest. A gap means the interview did
not surface enough — the response is to elicit more, not to invent a block to
fill the cell. Filling silently destroys traceability: a fabricated block has no
stakeholder and no CIT anchor.

## Content

### What a block is — and aggregate-first

Evans (2003) Part II lays out the building blocks of a model-driven design:
**entities** (identity-defined), **value objects** (immutable, compared by
value), **services** (stateless operations that belong to no one entity),
**repositories** (abstract the persistence of an aggregate), **factories**
(encapsulate construction), and **modules** (the code-level partition). Chapter
4 introduces the **aggregate**: a cluster treated as a single unit for data
changes, with one root entity that enforces the cluster's invariants.

Aggregate-first means: when decomposing a context, look for the
transactional-consistency cores first. Ask "what must be true, together, at the
end of one transaction?" — that invariant cluster is an aggregate. Everything
else arranges itself around the aggregates: repositories persist them,
anti-corruption layers translate foreign concepts into them, application
services orchestrate them, value objects describe their leaves. The rates sim
illustrates the mix: a *Conversion* aggregate (root + invariant), a
*RatesAdapter* anti-corruption layer, a *Settings* value object, a *convert*
application service. Naming a block as a capability — "rate conversion" — keeps
the door open to its eventual tactical shape; naming it as a mechanism —
"RatesRepository" — prematurely fixes it.

### Coarse-then-detailed: names before spec

Patton (2014) describes a two-dimensional map: a *backbone* of user activities
above, with stories beneath as one-line titles, refined gradually and sliced
horizontally into releases. The same shape governs blocks: the bounded contexts
form the backbone, and the blocks are the titles beneath them. At this level a
block is captured as a **name and a rough boundary** — what context it lives in,
what it neighbours, roughly what it is responsible for. Its operations,
invariants, parameter types, and return types are *not* designed here; they are
expressed in the test stubs (plan) and fixed in the implementation (build).
"Stories are discovered, not written" (Patton, 2014) — blocks are elicited from
the interview, not architected at the whiteboard.

### The bounded context as decomposition unit

Evans (2003) defines a bounded context as the boundary within which a
ubiquitous-language term has exactly one meaning. Vernon (2013) sharpens the
alignment: a context maps to a business capability, a transactional boundary,
and — often — a team. A block is owned by exactly one context. When a candidate
spans two contexts, one of two things is true: it is two blocks (one per
context, possibly linked by identity or a context-map relationship), or the
contexts are mis-drawn and should merge or be re-mapped. The consistency
boundary *within* a context — how big each aggregate is, when to split — is the
subject of [[requirements/aggregate-boundaries]].

Brandolini (2012) offers an alternative lens on the same boundary: **Event
Storming**. Domain events are placed on a timeline first; clusters of events
surface bounded contexts and aggregates collaboratively, and the commands
attached to events reveal intent. The boundary is the same; the entry point
(events, not nouns) is different. Either lens is a valid way to find the blocks
of a context.

### Gap analysis as a coverage matrix

Wiegers (*Software Requirements*, 2nd ed) frames requirements traceability as a
matrix that links each requirement forward to the design and test elements that
realise it. Gotel & Cleland-Huang (2012) generalise: a traceability matrix
correlates two baselined artefacts many-to-many; cells are marked where a
relationship exists.

Applied to decomposition, the matrix has two row kinds and one column kind:

| | block A | block B | block C |
|---|---|---|---|
| **bounded context: pricing** | × | | |
| **bounded context: billing** | | × | |
| **quality attribute: auditability** | | × | × |
| **quality attribute: performance** | × | | |

A **bounded context** row asks: does something live here? A **quality
attribute** row asks: is this non-functional concern (security, performance,
auditability, ...) carried by at least one block? Quality attributes are not
blocks themselves; they are concerns a block must satisfy. An **empty row** — a
context or quality with no block — is a gap. A **dense cell** — one block
carrying many concerns — is a signal the block is over-complex and may need
splitting (see [[requirements/aggregate-boundaries]]). Build the matrix as you
go, not reconstructed at the end (Gotel & Cleland-Huang, 2012).

### Flag, do not fill

A gap in the coverage matrix is a detection, not a work item. The honest
response is to return to elicitation — the funnel's earlier levels, or another
interview pass — and surface the missing block or quality from the stakeholder.
Inventing a block to fill the cell destroys the property that makes the matrix
trustworthy: every block traces back to a stakeholder need and a CIT-anchored
interview finding. A fabricated block has neither, and it will drift the moment
it is built.

## Related

- [[requirements/aggregate-boundaries]] — sizing and splitting the blocks
  identified here.
- [[requirements/ubiquitous-language]] — the shared language a bounded context
  bounds.
- [[requirements/interview-techniques]] — CIT, Laddering, and the Active
  Listening protocol that surface blocks.
