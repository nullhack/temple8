# Example Mapping (Wynne, 2015)

## Citation

Wynne, M. (2015). "Introducing Example Mapping." *Cucumber Blog*. https://cucumber.io/blog/bdd/example-mapping-introduction/

## Source Type

Blog/Article

## Method

Case Study

## Verification Status

Verified

## Confidence

High

## Key Insight

Inserting a "rules" layer between stories and examples prevents redundant or contradictory acceptance criteria - visual arrangement reveals story complexity and knowledge gaps before development begins.

## Core Findings

1. **Four Card Types**: Story (yellow), Rules (blue), Examples (green), Questions (red) using colored index cards in visual mapping
2. **Quality Signals**: Many rules → story needs splitting; many examples per rule → rule too complex; many red cards → story not ready; no red cards → conversation may be insufficient
3. **Time-boxed Process**: Well-understood, well-sized story should map in ~25 minutes with thumb-vote to determine development readiness
4. **Rules Layer Value**: Groups related examples under business rules they illustrate, preventing duplicated logic and making business constraints explicit
5. **"Friends Episode" Naming**: Rough examples using informal names ("The one where customer forgot receipt") instead of formal Gherkin during mapping

## Mechanism

Collaborative session involves stakeholders placing colored cards on table/wall. Visual arrangement provides instant feedback on story complexity. Rules layer acts as intermediary between high-level stories and concrete examples, preventing redundancy and revealing natural slicing points.

## Relevance

Essential for BDD story refinement, three amigos sessions, backlog grooming. Applied in agile requirements discovery, acceptance criteria definition, story sizing. Foundational technique for preventing oversized stories entering sprints and discovering unknown unknowns systematically.

## Related Research

Created by Matt Wynne (Cucumber Project Lead) in 2015. Builds on (North, 2006) BDD practices and three amigos concept. Complements (Wake, 2003) INVEST criteria by providing structured discovery technique. Part of broader BDD ecosystem alongside Gherkin, specification workshops, deliberate discovery practices.