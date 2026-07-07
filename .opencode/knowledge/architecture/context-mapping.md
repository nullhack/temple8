---
domain: architecture
tags: [ddd, context-mapping, bounded-contexts, acl, integration-patterns]
last-updated: 2026-07-02
---

# Context Mapping

## Key Takeaways

- A context map names **how two bounded contexts relate** — the social and technical contract between them. Nine relationship patterns cover the design space (Vernon, 2013; Evans, 2003).
- Each pattern carries obligations and a coordination cost; naming it makes both teams' (or both modules') responsibilities explicit and prevents silent model pollution.
- The **Anti-Corruption Layer (ACL)** is the workhorse pattern in this workflow: a translation boundary that prevents an upstream model from leaking into the downstream. Every external adapter is an ACL.
- Patterns are **decided at `derive-source-stubs`** — when the system-architect defines the type surface that bridges contexts, the relationship becomes a type/relationship decision (ACL → an adapter class; Shared Kernel → a shared value-objects module; etc.).
- The relationship is distinct from the **exchange** — `[[software-craft/external-fixtures]]` captures the recorded request/response reality; this knowledge names the structural relationship around it.
- "Integration point" is the seam; every seam must name its pattern, its mechanism (sync API / event / shared store), and its contract, or it is a coupling failure waiting to land.

## Concepts

**Why map contexts.** A bounded context (Evans, 2003) is where a ubiquitous-language term has one meaning; across contexts, the same word may name different things. When two contexts must integrate, the relationship is itself a design decision with consequences: who owns the contract, who translates, who conforms, who is isolated. Vernon (2013) catalogues nine such relationships; choosing one is choosing the obligations and coupling that follow. Leaving the relationship unnamed is the most common source of integration drift — each side assumes a different contract until production disagrees.

**The nine patterns.** Partnership (close collaboration, shared change); Shared Kernel (an explicitly-shared small model, with the cost of joint ownership); Customer-Supplier (upstream serves downstream's needs); Conformist (downstream accepts the upstream model wholesale); Anti-Corruption Layer (downstream translates upstream into its own model); Separate Ways (no integration — split instead); Open Host Service (upstream publishes a standard protocol to many); Published Language (a documented interchange schema, often with OHS); Big Ball of Mud (a messy boundary to contain, not extend).

**The ACL is the workhorse.** Most external integrations in this workflow are ACLs: the external service has its model (its field names, its error shapes, its volatility); our domain has ours; the adapter translates between them so the domain's ubiquitous language stays clean even while consuming the foreign service. The RatesAdapter / WeatherAdapter pattern — a class that takes our settings, calls the foreign API, and returns our value object — is an ACL by construction. The cassette (per `[[software-craft/external-fixtures]]`) records what the foreign side actually says; the adapter is the ACL that turns that into our terms.

**Decided at the type surface.** `derive-source-stubs` is where the relationship becomes concrete: the system-architect, having read the test bodies and the external contracts, decides for each cross-context dependency whether it is an ACL (→ an adapter class + a replayed cassette), a Shared Kernel (→ a shared value-object module imported by both), a Conformist client (→ a thin caller that accepts the upstream types), or an OHS/Published Language (→ an exposed contract plus its schema). The pattern choice shapes the `.pyi` surface the tests then demand.

**Relationship ≠ exchange.** Two knowledge files are easily conflated. `[[software-craft/external-fixtures]]` is about the *recorded exchange* — capture once, replay forever, scrub secrets. This knowledge is about the *structural relationship* — which of the nine patterns wraps the exchange. The adapter is an ACL (context-mapping) that replays a cassette (external-fixtures); both apply, at different layers.

## Content

### The nine patterns, mapped to this workflow's building blocks

| Pattern | What it is | In this workflow |
|---|---|---|
| Anti-Corruption Layer | downstream translates upstream into its own model | the **external adapter** (RatesAdapter, WeatherAdapter) + its replayed cassette |
| Shared Kernel | a small model two contexts jointly own | a shared **value-objects module** (e.g. a shared `LookupRecord`); costly — only when both truly co-change it |
| Customer-Supplier | upstream serves downstream's needs; downstream has influence | two internal contexts where one explicitly serves the other |
| Conformist | downstream accepts the upstream model as-is | a thin client that imports upstream types wholesale (no translation); cheap but couples the models |
| Open Host Service + Published Language | upstream publishes a standard protocol/schema to many consumers | an **exposed API contract** + its schema, when *we* are the upstream |
| Partnership | two contexts co-developing in tight collaboration | rare in a single-package app; common in larger orgs |
| Separate Ways | no integration — the contexts solve it independently | the answer when integration cost exceeds benefit; split instead |
| Big Ball of Mud | a messy boundary to contain, not extend | a legacy/external mess wrapped behind an ACL — never imported directly |

### Selecting the pattern

The choice turns on three questions. **Who has influence?** If the downstream has none over the upstream (a third-party API, a regulated service) → ACL. If both negotiate → Customer-Supplier. If the downstream willingly conforms → Conformist. **How many consumers?** One → direct integration; many → Open Host Service + Published Language. **Is integration worth it?** If the cost exceeds the benefit → Separate Ways. When unsure, default to the ACL — it is the safest (it isolates our model) and the one this workflow's adapter pattern already implements.

### Every integration point names three things

A seam between contexts is undefined until it names: (1) its **pattern** (above), (2) its **mechanism** (synchronous API / asynchronous event / shared store / file exchange), and (3) its **contract** (the schema, versioning, backward compatibility, error handling). An undefined seam is the primary source of coupling failures — flag it at `derive-source-stubs` rather than discovering it at build.

## Related

- [[software-craft/external-fixtures]] — the recorded exchange that the ACL wraps (relationship vs exchange; distinct layers)
- [[requirements/domain-decomposition]] — identifying the bounded contexts that this knowledge then relates
- [[requirements/aggregate-boundaries]] — the intra-context boundary (consistency); this knowledge is the inter-context boundary (relationship)
- [[architecture/quality-attributes]] — interoperability and model-purity are quality attributes the patterns address
