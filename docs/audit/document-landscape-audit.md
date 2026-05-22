# Document Landscape Audit

**Date:** 2026-05-06
**Session:** doc-audit
**Hypothesis:** The development process produces too many documents and writes too much.
**Method:** Trace every file artifact across all 12 flow definitions. Map production → consumption. Apply MoSCoW against the rebuild-from-scratch test: *if we lose all code, which documents must exist for agents to rewrite the system, serving business, architect, and developer audiences?*

---

## 1. Complete Artifact Inventory

11 persistent file artifacts produced across the full lifecycle. Runtime artifacts (typed_source_stubs, test_skeletons, feature_commits, merged_commits, acceptance_evidence, approval_record, design_review_evidence, structure_review_evidence, conventions_review_evidence, root_cause_analysis, requirements_assessment, git_branch) are excluded: they are generated and consumed within a single session and never persist across flow boundaries.

| # | Artifact | Produced By (flow → state) | Sections Written | File Count |
|---|----------|---------------------------|------------------|------------|
| 1 | `interview-notes/<session>.md` | discovery → stakeholder-interview | pain_points, business_goals, terms_to_define, quality_attributes + General Q&A, Feature Q&A | N (one per interview) |
| 2 | `domain_model.md` | discovery → event-storming (event_map, context_candidates, aggregate_candidates) then discovery → domain-modeling (bounded_contexts, entities, relationships, aggregate_boundaries, summary) | 8 sections | 1 |
| 3 | `glossary.md` | discovery → language-definition | append-only entries | 1 |
| 4 | `product_definition.md` | discovery → scope-boundary (core sections), architecture → architecture-assessment (deployment, quality_attributes), planning → definition-of-done (definition_of_done) | 9 sections + Deployment checklist | 1 |
| 5 | `features/<name>.feature` | discovery → feature-discovery (title, description, rules_business, constraints), planning → feature-breakdown (rules), planning → feature-examples (examples) | 6+ sections | N (one per feature) |
| 6 | `context_map.md` | architecture → context-mapping | context_relationships, context_map_diagram, integration_points, anti_corruption_layers | 1 |
| 7 | `technical_design.md` | architecture → technical-design | architectural_style, quality_attributes, stack, module_structure, api_contracts, event_contracts, interface_definitions, c4_diagrams, dependencies, configuration_keys | 10 sections | 1 |
| 8 | `system.md` | architecture → technical-design (context, container, module_structure, delivery), architecture → adr-draft (key_decisions, active_constraints) | 7+ sections | 1 |
| 9 | `adr/<slug>.md` | architecture → adr-draft | status, context, interview, decision, reason, alternatives, consequences, risk_assessment | N (one per decision) |
| 10 | `branding.md` | branding → setup-branding (identity, release_naming, wording), branding → design-colors (visual) | 4 sections | 1 |
| 11 | `post-mortem/<slug>.md` | post-mortem → document-findings + extract-lessons + action-items | failed_at, root_cause, missed_gate, fix, restart_check | N (one per failure) |

---

## 2. Consumption Matrix

How many states READ each document. Higher consumption = higher system value.

| Artifact | Read By (states) | Read Count |
|----------|-----------------|------------|
| `domain_model.md` | event-storming, language-definition, domain-modeling, scope-boundary, feature-discovery, architecture-assessment, context-mapping, technical-design, review-signoff, feature-examples, create-py-stubs, project-structuring, design-review, structure-review | **14** |
| `glossary.md` | language-definition, domain-modeling, scope-boundary, feature-discovery, context-mapping, technical-design, adr-draft, review-signoff, feature-examples, create-py-stubs, project-structuring, design-review, structure-review, conventions-review | **14** |
| `product_definition.md` | scope-boundary, feature-discovery, architecture-assessment, context-mapping, technical-design, adr-draft, review-signoff, feature-selection, feature-breakdown, feature-examples, definition-of-done, ready, project-structuring, design-review, conventions-review | **15** |
| `features/<name>.feature` | feature-discovery, feature-breakdown, feature-examples, create-py-stubs, definition-of-done, ready, project-structuring, structure-review (verify-traceability), commit, acceptance, local-merge, pr-creation | **12** |
| `technical_design.md` | architecture-assessment, feature-discovery, feature-selection, feature-breakdown, technical-design, adr-draft, review-signoff, create-py-stubs, project-structuring, design-review | **10** |
| `context_map.md` | architecture-assessment, technical-design, adr-draft, review-signoff, project-structuring, design-review | **6** |
| `system.md` | architecture-assessment, technical-design, adr-draft, review-signoff, design-review | **5** |
| `interview-notes/*.md` | event-storming, language-definition, domain-modeling, feature-discovery, feature-breakdown | **5** |
| `adr/*.md` | adr-draft, review-signoff, project-structuring, design-review | **4** |
| `branding.md` | design-colors, design-assets | **2** |
| `post-mortem/*.md` | document-findings, extract-lessons, action-items (all within post-mortem flow only) | **3** |

---

## 3. MoSCoW Classification: Document Level

### MUST (lose code = cannot rebuild without these)

| Artifact | Justification |
|----------|--------------|
| `domain_model.md` | The WHAT. Bounded contexts, entities, relationships, aggregates. Without it, no agent knows what the system models. Consumed by 14 states. |
| `glossary.md` | The WORDS. Shared language that keeps code, specs, and tests coherent. Without it, agents generate inconsistent naming. Consumed by 14 states. |
| `technical_design.md` | The HOW. Stack, API contracts, event contracts, interfaces, module structure. The blueprint agents need to generate code structure. Consumed by 10 states. |
| `product_definition.md` | The WHY & WHO. Scope boundaries, users, quality attributes. Prevents scope creep and drives architecture. Consumed by 15 states. |
| `features/<name>.feature` | The BEHAVIOR. Rules + BDD examples are the executable specification. These ARE the tests. Without them, no agent knows what correct behavior looks like. Consumed by 12 states. |
| `system.md` | The TRUTH. Current-state system overview, key decisions, active constraints. Evolves with the system. The only document that reflects what IS (vs what was planned). Consumed by 5 states. |

### SHOULD (important for quality, audit trail, or re-interview)

| Artifact | Justification |
|----------|--------------|
| `context_map.md` | Context relationships, integration points, anti-corruption layers. Could be merged into domain_model.md or system.md (see §5). Valuable for architect audience but content overlaps with domain_model bounded_contexts and system.md interactions. |
| `adr/<slug>.md` | Decision records. The RATIONALE. Prevents re-litigating past decisions during rebuild. Without ADRs, agents may repeat rejected alternatives. Light consumption (4 states) but high-value per read. |
| `interview-notes/*.md` | Source material from stakeholders. Enables re-interview without starting from scratch. After discovery, only consumed by feature-discovery and feature-breakdown; both could work from synthesized documents. Archive-worthy. |

### COULD (nice to have, project-specific value)

| Artifact | Justification |
|----------|--------------|
| `branding.md` | Only consumed within branding flow. After branding is done, the real artifacts are logo.svg, banner.svg, and CSS in code. Useful if re-branding. |
| `post-mortem/<slug>.md` | Lessons learned. Prevents repeating failures. Only consumed within post-mortem flow. Valuable for process improvement but not needed for system rebuild. |

### WON'T (not needed for rebuild, one-time artifacts)

| Artifact | Justification |
|----------|--------------|
| `template-config.yaml` | One-time setup artifact. After project initialization, this has no rebuild value. |
| `docs/assets/logo.svg` | Binary asset. Cannot be regenerated from spec (must be kept in git, but it's not a "document"). |
| `docs/assets/banner.svg` | Same as logo.svg. |

---

## 4. Section-Level MoSCoW for MUST Documents

### 4.1 `domain_model.md` (8 sections → 3 lifecycle phases)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| `Summary` | **MUST** | 3-5 sentence domain overview. First thing any agent reads. |
| `Event Map` | **COULD** | Intermediate workshop artifact (event-storming output). Gets refined into bounded_contexts/entities by domain-modeling. After domain-modeling completes, this is historical scratch. No state after domain-modeling reads event_map specifically. |
| `Context Candidates` | **COULD** | Same: intermediate. Synthesized into `Bounded Contexts`. |
| `Aggregate Candidates` | **COULD** | Same: intermediate. Synthesized into `Aggregate Boundaries`. |
| `Bounded Contexts` | **MUST** | Core artifact. Defines what each context owns and its integration points. |
| `Entities` | **MUST** | Core artifact. Entity names, types, which context they belong to, aggregate root flags. |
| `Relationships` | **MUST** | Core artifact. How entities relate, cardinality, and notes. |
| `Aggregate Boundaries` | **MUST** | Core artifact. Root entities, invariants enforced, context membership. |
| `Changes` | **COULD** | Audit trail. Useful but not required for rebuild. |

**Finding:** 3 of 8 sections are intermediate scratch that only exist to feed the domain-modeling state. Once domain-modeling produces Bounded Contexts/Entities/Relationships/Aggregate Boundaries, the top 3 sections become read-only history. **Potential: archive or collapse event_map, context_candidates, aggregate_candidates after domain-modeling completes.**

### 4.2 `product_definition.md` (9+ sections, 3 writers)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| `What IS` | **MUST** | Scope definition. Prevents scope creep. |
| `What IS NOT` | **MUST** | Boundary. Complements IS. |
| `Why` | **SHOULD** | Business justification. Helps agents understand intent but is implicit in features. |
| `Users` | **MUST** | Personas. Determines who features serve. |
| `Quality Attributes` | **MUST** | Measurable scenarios that drive architecture. Referenced by architecture-assessment, technical-design, definition-of-done, review-gate. Written by scope-boundary, updated by architecture-assessment. |
| `Out of Scope` | **MUST** | Explicit non-goals. Boundary enforcement. |
| `Delivery Order` | **REMOVED** | Feature selection order is now derived at selection time from the context map dependency graph and WSJF scoring. |
| `Definition of Done` | **MUST** | Quality gates per feature. Written by definition-of-done state. Consumed implicitly by review and acceptance. |
| `Deployment` | **MUST** | Deployment type and checklist. Written by scope-boundary, updated by architecture-assessment. |
| `Branch Strategy` | **COULD** | Conventions. Could live in AGENTS.md or CONTRIBUTING.md instead. |
| `Scope Changes` | **COULD** | Audit trail. |
| `Project Conventions` | **SHOULD** | Container for DoD, Deployment, Branch Strategy. The container section itself is structural. |

**Finding:** This document is written by 3 different states across 2 flows (discovery → scope-boundary, architecture → architecture-assessment, planning → definition-of-done). This makes it a coordination bottleneck: multiple agents write to it at different lifecycle stages. No redundancy found in sections; each section carries unique information.

### 4.3 `technical_design.md` (10 sections)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| `Feature` | **MUST** | Links design to feature files. Traceability. |
| `Architectural Style` | **MUST** | The fundamental structural choice. |
| `Quality Attributes` | **MUST** | Technical mapping of quality attributes to architectural decisions + ADR refs. **Overlap note:** product_definition also has quality_attributes at the business level. This section maps them to technical decisions. Different abstraction levels (both needed). |
| `Stack` | **MUST** | Language, framework, database, messaging. Without this, agents cannot choose technologies. |
| `Module Structure` | **MUST** | Directory layout per bounded context. **Overlap note:** system.md also has Module Structure. technical_design defines the TARGET layout; system.md reflects the CURRENT layout. Both needed. |
| `API Contracts` | **MUST** | Endpoint definitions with request/response schemas. Directly used by project-structuring and create-py-stubs. |
| `Event Contracts` | **MUST** | Event schemas with producers/consumers. Same direct usage. |
| `Interface Definitions` | **MUST** | Python Protocol classes. The port interfaces that agents implement against. |
| `C4 Diagrams` | **SHOULD** | Visual architecture reference. Useful for human review, agents consume text preferentially. |
| `Dependencies` | **MUST** | External packages and why they're included. Prevents agents from adding redundant alternatives. |
| `Configuration Keys` | **MUST** | Env vars and config schema. |
| `Changes` | **COULD** | Audit trail. |

**Finding:** All 10 sections carry unique, non-recoverable information. No sections can be eliminated. The `C4 Diagrams` section explicitly acknowledges overlap with system.md in its template comment: *"This document focuses on the current feature's technical design, system.md focuses on the overall system state."*

### 4.4 `features/<name>.feature` (6 sections across 3 writers)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| `title` | **MUST** | Feature identity. |
| `description` | **MUST** | What and why. |
| `Rules (Business)` | **COULD** | Coarse rules from discovery (feature-discovery state). **Superseded by `rules` after feature-breakdown runs.** The refined `rules` section contains the same information in INVEST-validated form. |
| `Constraints` | **MUST** | Non-functional requirements specific to this feature. References product_definition quality_attributes. |
| `Rules` | **MUST** | INVEST-validated rule blocks with user stories. The actual specification. |
| `Examples` | **MUST** | Given/When/Then BDD scenarios. These ARE the test specification. The most critical section for code generation. |
| `Questions` | **SHOULD** | Open/resolved Q&A. Useful for audit but not needed for rebuild. |
| `Changes` | **COULD** | Audit trail. |

**Finding:** `Rules (Business)` and `Rules` are the same information at different refinement levels. After feature-breakdown runs, `Rules (Business)` is superseded. **Potential: replace `rules_business` with `rules` in-place during feature-breakdown, eliminating the redundant section.**

### 4.5 `system.md` (7+ sections)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| `Summary` | **MUST** | System overview. |
| `Delivery` | **MUST** | How users interact with the system. |
| `Context (C4 Level 1)` | **MUST** | Actors, systems, interactions at the highest level. |
| `Container (C4 Level 2)` | **MUST** | Containers within each boundary, their tech and responsibility. |
| `Module Structure` | **MUST** | Current module layout. **Overlap note:** also in technical_design. system.md = current state; technical_design = target design. After implementation they should converge. |
| `Domain Model Documentation` | **MUST** | Why each context exists, aggregate boundary rationale. **Overlap note:** bounded context "why" is here AND in domain_model. domain_model has the WHAT (entities, relationships); system.md has the WHY (rationale for separation). Complementary. |
| `Active Constraints` | **MUST** | System-wide constraints from ADRs. Prevents agents from violating past decisions. |
| `Key Decisions` | **MUST** | ADR summary bullets. Quick reference without reading all ADRs. |
| `Changes` | **COULD** | Audit trail. |

**Finding:** system.md serves a distinct purpose from technical_design.md and domain_model.md. It's the evolved truth, what the system IS right now, while the others are blueprints. The overlaps are intentional: system.md references and summarizes the others. No sections can be eliminated.

### 4.6 `glossary.md` (1 section, append-only)

| Section | MoSCoW | Analysis |
|---------|--------|----------|
| Term entries | **MUST** | Each entry: term, definition (genus+differentia), aliases, example, source. Append-only. |

**Finding:** Simple, purpose-built, no redundancy. Every state that reads it uses it for consistent naming. Cannot be reduced.

---

## 5. Cross-Document Redundancy Analysis

### 5.1 `context_map.md` vs `domain_model.md`: Overlap

| Information | context_map.md | domain_model.md |
|------------|---------------|-----------------|
| Bounded context names | Context Relationships (upstream/downstream) | Bounded Contexts (responsibility, entities) |
| Integration between contexts | Integration Points (mechanism, contract) | Bounded Contexts (integration_points column) |
| Context responsibilities | (not present, only relationships) | Bounded Contexts (responsibility column) |
| Anti-corruption layers | Anti-Corruption Layers (full ACL definitions) | (not present) |
| Relationship patterns (Customer-Supplier, etc.) | Context Relationships (pattern column) | (not present) |

**Verdict:** Partial overlap in bounded context names and integration points, but each document adds unique information. context_map has DDD strategic patterns and ACL definitions; domain_model has entities, aggregates, and responsibilities. **They are complementary, not redundant.** However, context_map is only consumed by 6 states vs domain_model's 14. **Potential merge:** Fold context_map's 4 sections into domain_model.md as a `Context Map` section. This would eliminate 1 document at the cost of making domain_model.md larger. The domain_model template already has an `Integration Points` column in the Bounded Contexts table. The context_map provides the detail behind those integration points.

### 5.2 `system.md` Module Structure vs `technical_design.md` Module Structure

Both have a `Module Structure` section. The templates clarify the distinction:
- technical_design: *"Contract-first design: API and event schemas are defined here before implementation begins."*
- system.md: *"Current-state description of the production system. Contains only completed features."*

**Verdict:** Intentional overlap at different lifecycle stages. technical_design = target; system.md = current state. During greenfield, they're identical. After multiple features, they diverge then converge as features are completed. **No action needed.** The template comment in technical_design explicitly acknowledges this: *"These may overlap with system.md."*

### 5.3 `product_definition.md` Quality Attributes vs `technical_design.md` Quality Attributes

Both have a `Quality Attributes` section:
- product_definition: Business-level scenarios (stimulus → response → measure) with priority
- technical_design: Technical mapping (which architectural decision addresses each attribute) with ADR refs

**Verdict:** Different abstraction levels. product_definition answers "what quality do we need?"; technical_design answers "how does the architecture deliver it?" **No action needed.**

### 5.4 `system.md` Domain Model Documentation vs `domain_model.md`

- domain_model: WHAT entities exist, their types, relationships, aggregate boundaries, invariants
- system.md: WHY each context exists (business capability, separation rationale), WHY aggregates are grouped (transactional invariant explanation)

**Verdict:** Complementary. domain_model is the formal model; system.md is the rationale. **No action needed.**

### 5.5 `domain_model.md` Changes Tables: Repeated Pattern

5 of the 6 spec documents (domain_model, product_definition, technical_design, context_map, system) have identical `Changes` audit tables with columns: Date, Source, Change, Reason. Feature files have a similar `Changes` table.

**Verdict:** Consistent convention, not redundancy. Each table tracks changes to THAT document. **No action needed**, but consider if the Changes sections are worth their weight. They add ~5 lines per change but are never consumed by any agent state. They exist for human audit only. **Potential:** Could be optional or auto-generated from git history.

### 5.6 Deep Overlap Analysis: domain_model.md ↔ system.md ↔ technical_design.md

This section traces every shared data field across the three core spec documents to determine whether overlaps are true redundancy (same information, same angle) or complementarity (same entity, different angle).

#### Overlap 1: Bounded Context names + descriptions

| Field | domain_model.md | system.md | technical_design.md |
|-------|----------------|-----------|-------------------|
| Context name | Bounded Contexts table: `Context` | Why Each Context Exists: `Bounded Context` | Module Structure: `<bounded-context>/` in directory tree |
| Context description | Bounded Contexts: `Responsibility` (what this context owns) | Why Each Context Exists: `Business Capability` (what business need it serves) | (not present, only directory names) |

**Analysis:** The context name appears in all three. domain_model and system.md both have a one-line description, but at different angles:
- domain_model "Responsibility" = what the context owns technically (entities, data)
- system.md "Business Capability" = why the context exists for the business

These could diverge. Example: a context named "Billing" might have responsibility "owns invoices, payments, refunds" in domain_model but business capability "revenue collection and financial compliance" in system.md. **Complementary, not redundant.**

**Verdict:** Context name is duplicated (unavoidable cross-reference). Descriptions serve different audiences. **No action.**

#### Overlap 2: Aggregate names + invariants

| Field | domain_model.md | system.md |
|-------|----------------|-----------|
| Aggregate name | Aggregate Boundaries: `Aggregate` | Aggregate Boundary Rationale: `Aggregate` |
| Invariant text | Aggregate Boundaries: `Invariants` ("business rules this aggregate enforces") | Aggregate Boundary Rationale: `Transactional Invariant` ("what must always be true within this aggregate") |
| Root entity | Aggregate Boundaries: `Root Entity` | (not present) |
| Grouping rationale | (not present) | Aggregate Boundary Rationale: `Why These Entities Are Grouped` |

**Analysis:** The aggregate name is duplicated. More critically, the **invariant text is semantically identical**: "business rules this aggregate enforces" and "what must always be true within this aggregate" describe the same thing. domain_model adds the root entity and context membership; system.md adds the grouping rationale (WHY these entities form this aggregate). The invariant itself is duplicated.

**Verdict:** **True redundancy on the invariant description.** system.md's "Transactional Invariant" restates domain_model's "Invariants" in slightly different words. The grouping rationale is unique to system.md. **Action:** system.md could reference domain_model for the invariant text and only provide the unique "Why These Entities Are Grouped" column, reducing this from 3 columns to 2 + a cross-reference.

#### Overlap 3: Module Structure

| Field | technical_design.md | system.md |
|-------|-------------------|-----------|
| Format | Directory tree (code block) showing `src/<bounded-context>/domain|application|infrastructure|api/` | Flat table: Module, Responsibility, Bounded Context |
| Lifecycle | Written during architecture → technical-design (target) | Written during architecture → technical-design (current state), updated per completed feature |
| Purpose | Codegen blueprint: agents use this to create directory scaffolding | Reference: agents use this to find where things live in the current system |

**Analysis:** Same information at different representations. technical_design shows the hierarchical structure (tree); system.md shows a flat mapping with responsibility per module. During greenfield they carry identical data. After N features, system.md reflects what exists while technical_design reflects what's being added.

The tree format is critical for the `structure-project` and `create-py-stubs` states: they need to know the exact directory hierarchy. The table format is critical for `design-review`: they need to verify modules map to bounded contexts. Both representations serve different consumption patterns.

**Verdict:** Intentional overlap with different representations for different use cases. **No action.** The template comment in technical_design explicitly acknowledges this: *"These may overlap with system.md."*

#### Overlap 4: C4 Diagrams

| Field | technical_design.md | system.md |
|-------|-------------------|-----------|
| C4 Level 1 | C4 Diagrams section (reference/embed, feature-scoped) | Context (C4 Level 1): full actors, systems, interactions tables |
| C4 Level 2 | C4 Diagrams section (reference/embed, feature-scoped) | Container (C4 Level 2): full containers, interactions tables |

**Analysis:** system.md IS the C4 diagram (in table form) for the current system. technical_design may embed C4 diagrams for the specific feature being designed. The template explicitly states: *"This document focuses on the current feature's technical design, system.md focuses on the overall system state."*

**Verdict:** Different scope (feature vs system). **No action.**

#### Overlap 5: Summary paragraphs

| Document | Summary describes |
|----------|------------------|
| domain_model.md | "the domain, its core concepts, and primary business capabilities" |
| system.md | "what the system currently does, who uses it, and its primary boundaries" |

**Analysis:** Both are 3-5 sentence overviews but from different perspectives. domain_model = domain lens (what the business is about); system.md = system lens (what the software does). A rebuild reader benefits from both: domain_model explains the problem space, system.md explains the solution space.

**Verdict:** Different angles on the same reality. **No action.**

#### Overlap 6: Integration between contexts

| Field | domain_model.md | system.md |
|-------|----------------|-----------|
| How contexts connect | Bounded Contexts: `Integration Points` column (one-liner per context) | Context Interactions: full table with `Interaction`, `Behaviour`, `Technology` |

**Analysis:** domain_model has a one-column summary ("how it connects to other contexts"). system.md has full interaction descriptions with behavior and technology. These are at different levels of detail.

**Verdict:** domain_model provides a quick reference; system.md provides the full picture. **No action.**

#### Summary: True Redundancies vs Intentional Overlaps

| Overlap | Type | Same information? | Action |
|---------|------|-------------------|--------|
| Context names (all 3 docs) | Cross-reference | Same name, unavoidable | None |
| Context descriptions (DM ↔ SM) | Complementary | Different angle (technical vs business) | None |
| **Aggregate invariants (DM ↔ SM)** | **True redundancy** | **Semantically identical** | **SM could cross-ref DM instead of restating** |
| Module Structure (TD ↔ SM) | Intentional overlap | Same data, different format (tree vs table) | None |
| C4 Diagrams (TD ↔ SM) | Complementary | Different scope (feature vs system) | None |
| Summary paragraphs (DM ↔ SM) | Complementary | Different perspective (domain vs system) | None |
| Integration points (DM ↔ SM) | Complementary | Different detail level | None |

**Net finding across these three documents:** Only 1 true redundancy found: aggregate invariants restated in system.md. All other overlaps are intentional (different format, different scope, different audience angle). The three documents form a coherent stack:

```
domain_model.md     →  WHAT the system models (domain perspective)
system.md           →  WHAT the system IS right now (current-state perspective)
technical_design.md →  HOW to build the next feature (implementation perspective)
```

Each layer consumes the one below it. No document can be eliminated without losing a perspective that at least one agent state requires.

---

## 6. Rebuild Test: What Is Strictly Necessary

**Scenario:** All source code, tests, and configuration are lost. Only spec documents remain. Agents must regenerate the system.

### Minimum Viable Documentation Set

| # | Document | What It Provides for Rebuild | Sections Required |
|---|----------|------------------------------|-------------------|
| 1 | `domain_model.md` | Bounded contexts, entities, value objects, relationships, aggregate boundaries with invariants | Summary, Bounded Contexts, Entities, Relationships, Aggregate Boundaries (4 of 8 sections) |
| 2 | `glossary.md` | Consistent naming across all generated code | All entries |
| 3 | `technical_design.md` | Stack choice, module layout, API contracts, event contracts, port interfaces, dependencies, config keys | All 10 sections (C4 Diagrams optional) |
| 4 | `product_definition.md` | Scope boundaries, users, quality attributes, definition of done, deployment checklist | 7 of 8+ sections (Why optional, Branch Strategy not needed) |
| 5 | `features/*.feature` | Per-feature: rules (user stories) and examples (BDD Given/When/Then) | title, description, Rules, Examples, Constraints (5 of 6+ sections) |
| 6 | `system.md` | Current-state architecture, key decisions, active constraints | Summary, Delivery, Context, Container, Module Structure, Domain Model Documentation, Active Constraints, Key Decisions (8 of 9+ sections) |

### What rebuild would miss without SHOULD documents

| Without | Impact |
|---------|--------|
| `context_map.md` | Agents would not know DDD relationship patterns between contexts (Customer-Supplier vs Conformist, etc.) or anti-corruption layer definitions. Integration points exist in domain_model but without the strategic pattern context. **Moderate impact on inter-context communication design.** |
| `adr/*.md` | Agents would not know WHY decisions were made or what alternatives were rejected. Risk of repeating rejected approaches. **High impact on architecture quality over time.** |
| `interview-notes/*.md` | Agents could not re-interview stakeholders with context. Would start from scratch. **Low impact on rebuild: the synthesized documents carry the knowledge.** |

---

## 7. Findings Summary

### Documents That Earn Their Place (no action needed)

1. **domain_model.md**: Core domain artifact. 14-state consumption. Only issue: 3 of 8 sections are intermediate scratch that outlive their usefulness.
2. **glossary.md**: Simple, purpose-built, no fat. 14-state consumption. Leave as-is.
3. **technical_design.md**: All 10 sections carry unique information. 10-state consumption. Leave as-is.
4. **product_definition.md**: All sections carry unique information despite being written by 3 different states. 15-state consumption. Leave as-is.
5. **system.md**: Distinct from technical_design (current vs target). 5-state consumption but high-value per read. Leave as-is.
6. **features/*.feature**: The executable spec. 12-state consumption. One redundancy: `rules_business` vs `rules`.

### Documents With Actionable Findings

| Document | Finding | Recommendation |
|----------|---------|---------------|
| `domain_model.md` | 3 sections (Event Map, Context Candidates, Aggregate Candidates) are intermediate workshop output that gets synthesized into the final 4 sections. After domain-modeling, nobody reads them. | **Archive or collapse after domain-modeling completes.** These sections have audit value but zero rebuild value. |
| `features/*.feature` | `Rules (Business)` (from discovery) is superseded by `Rules` (from planning/feature-breakdown). Same information at different refinement levels. | **Replace `rules_business` with `rules` in-place during feature-breakdown.** Eliminates one redundant section per feature file. |
| `context_map.md` | Only 6-state consumption. Partial overlap with domain_model's bounded_contexts. Unique value: DDD strategic patterns, ACL definitions. | **Potential merge into domain_model.md** as a `Context Map` section. Reduces artifact count by 1. Trade-off: domain_model becomes larger; context_map has a different owner (SA) and lifecycle stage. **Defer unless artifact count is a priority.** |

### Documents That Are Correctly Positioned

| Document | Audience | Lifecycle | Verdict |
|----------|----------|-----------|---------|
| `interview-notes/*.md` | Business (source material) | Discovery only, then archive | Keep as SHOULD. Archive after feature-discovery. |
| `adr/*.md` | Architect, Developer (rationale) | Written once, referenced forever | Keep as SHOULD. High value per read. |
| `branding.md` | Design Agent, Business | Written once in branding flow | Keep as COULD. Not needed for rebuild. |
| `post-mortem/*.md` | Process improvement | Written on rejection only | Keep as COULD. Not needed for rebuild. |

---

## 8. Recommendations (MoSCoW)

### Must Do

1. **No documents should be eliminated.** The hypothesis "too many documents" is **not supported** by the evidence. 6 MUST documents carry non-overlapping, non-recoverable information. 3 SHOULD documents add audit/rational value. The total artifact count (11 persistent docs) is appropriate for a system that must be rebuildable from spec.

### Should Do

2. **Archive domain_model.md intermediate sections** (Event Map, Context Candidates, Aggregate Candidates) after domain-modeling completes. They are workshop scratch that adds noise to the document once the synthesized sections exist. This saves ~40% of domain_model.md's rendered length for rebuild readers.
3. **Eliminate `rules_business` section in feature files** by having feature-breakdown replace it with the refined `rules` section in-place rather than adding a parallel section. This removes the only true redundancy found in feature files.
4. **De-duplicate aggregate invariants between domain_model.md and system.md.** system.md's "Transactional Invariant" column restates domain_model's "Invariants" column. Replace system.md's invariant text with a cross-reference (e.g. "See domain_model.md → Aggregate Boundaries") and keep only the unique "Why These Entities Are Grouped" column.

### Could Do

5. **Merge context_map.md into domain_model.md** as a `Context Map` section. Reduces artifact count by 1. Trade-off: different owners (DE vs SA), different lifecycle stages, domain_model becomes larger. Only worth doing if artifact count is a pressing concern.
6. **Make `Changes` audit tables optional or auto-generated** from git history. 5 documents have them; no agent state consumes them. They serve human audit only.
7. **Move `Branch Strategy` from product_definition.md** to AGENTS.md or a CONTRIBUTING.md convention file. It's a process convention, not a product specification.

### Won't Do (Explicitly Rejected)

8. **Merge system.md and technical_design.md**. They serve different purposes (current state vs target design) and are consumed at different lifecycle stages. The overlap is intentional and documented.
9. **Merge product_definition quality_attributes and technical_design quality_attributes**. Different abstraction levels (business vs technical mapping).
10. **Eliminate glossary.md**. It's the highest-consumption document alongside domain_model.md. Every naming decision depends on it.
11. **Reduce interview-notes to ephemeral**. They enable re-interview and serve as source material for feature-discovery. Archive after discovery, but don't delete.

---

## 9. Quantitative Summary

| Metric | Count |
|--------|-------|
| Total persistent file artifacts | 11 |
| MUST documents (rebuild-critical) | 6 |
| SHOULD documents (high value) | 3 |
| COULD documents (project-specific) | 2 |
| Total sections across all MUST documents | ~45 |
| Sections that are intermediate scratch (archive candidates) | 3 (domain_model: Event Map, Context Candidates, Aggregate Candidates) |
| Sections that are truly redundant (elimination candidates) | 1 (feature: rules_business superseded by rules) |
| Intentional overlaps (different abstraction levels, different format/scope/angle) | 6 (context names × 3, module_structure × 2, C4 diagrams × 2, summaries × 2, integration detail × 2, context descriptions × 2) |
| True redundancies (same information restated) | 1 (aggregate invariants: domain_model ↔ system.md) |
| **Net reduction potential** | **4 sections removable (archive 3 + eliminate 1), 1 field de-duplication (aggregate invariants), potentially 1 document mergeable** |

**Verdict on the hypothesis:** The process does NOT produce too many documents. 11 persistent artifacts for a rebuildable system serving 3 audiences (business, architect, developer) is lean. The real finding is not excess documents but **4 sections of excess content** within otherwise necessary documents: 3 intermediate sections in domain_model.md that outlive their usefulness, and 1 superseded section in feature files. Addressing these 4 items would tighten the documentation without losing any rebuild capability.

---

## 10. Reading Pattern Problem

The audit identified a secondary issue: **too many documents are read too often.**

### Heavy Reader States (5+ spec docs)

| State | Docs Read | Documents |
|-------|-----------|-----------|
| review-signoff | 7 | context_map, technical_design, system, adr/*, product_definition, domain_model, glossary |
| project-structuring | 7 | features, technical_design, domain_model, glossary, context_map, adr/*, product_definition |
| design-review | 7 | domain_model, glossary, technical_design, context_map, system, product_definition, adr/* |
| adr-draft | 6 | technical_design, context_map, domain_model, product_definition, glossary, system |
| architecture-assessment | 5 | product_definition, domain_model, system, technical_design, context_map |
| technical-design | 5 | context_map, domain_model, glossary, system, product_definition |
| feature-discovery | 5 | product_definition, domain_model, glossary, interview-notes, technical_design |

### The system.md Intent Gap

system.md was designed as a **summary/index document**: read first instead of reading all raw sources. But the flow `in` lists enumerate every document at every state, so agents read everything anyway. system.md sits in the pile as an equal, not as a shortcut.

**Impact:** Agents load 5-7 documents into context for a single state, burning tokens on raw ADRs and interview notes when a well-maintained summary would suffice for most work.

**Potential fix:** If system.md absorbed context_map's unique content and became the true "system truth" summary, downstream `in` lists could shrink from 7 docs to: `system.md + feature file + (1 task-specific doc)`. Only architecture-phase states that PRODUCE documents would need the full pile.

### Dependency Visualization

See `.flowr/flows/document-dependencies.yaml` for the full document dependency graph (viewable via `task regenerate-flowviz`). Each document state carries:
- `sections`: all section titles
- `reads_from` / `summarizes`: dependency relationships
- `consumed_by`: which flow states read it
- `role`: raw-source | specification | summary | operational
