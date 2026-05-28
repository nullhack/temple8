# AI Writing Markers: Community and Web Sources Synthesis

## Citation

Multiple community and web sources: Wikipedia "Signs of AI writing", Reddit community detection lists (300+ comment threads), Humanize AI Pro detection tool, Humaneer detection platform, Noren detection tool, Avasdream analysis, humanize-writing GitHub project, Towards AI (delve origin study).

## Source Type

Synthesis (Community + Industry + Web)

## Method

Crowdsourced Analysis and Tool Data

## Verification Status

Unverified (community-sourced, multiple independent reports)

## Confidence

Medium (convergent evidence from multiple independent sources)

## Key Insight

Community detection lists, web tools, and crowdsourced analyses converge on consistent markers across all tiers (vocabulary overrepresentation, structural formulas, filler phrases, and chatbot artifacts), providing independent validation of academic and industry findings.

## Core Findings

1. **Wikipedia "Signs of AI writing"**: Community-maintained page cataloguing AI writing markers including pivotal, beacon, showcase/showcasing, meticulous/meticulously, garner, bolster, "Not X, but Y" construction, rule of three, synonym cycling. GPT-4 era hallmarks identified.
2. **Reddit community lists**: 300+ comment threads flagging consistent markers including nuanced, foster, kaleidoscope, "Let's dive in"/"Let's explore" as chatbot artifacts. Community members report these markers are "instant tells" in professional and academic contexts.
3. **Humanize AI Pro**: Detection tool data showing filler phrase overrepresentation: "It's worth noting that" (31x), "It's important to note" (27x), "In today's digital age" (24x), "In the realm of" (22x), "It is important to understand" (20x).
4. **Noren**: Detection tool identifying leverage (verb, 13x), "Whether you're a [X] or a [Y]" as template scaffolding.
5. **Avasdream**: Analysis identifying significance inflation (everything is pivotal/crucial/groundbreaking), -ing trailing clauses that restate what was already said, and uniform sentence length (low burstiness) as key structural markers.
6. **Humaneer**: Detection tool corroborating leverage, utilize, and other Tier 1 vocabulary markers.
7. **humanize-writing GitHub**: Open-source reference providing the detection heuristic (5+ hits = likely AI) used to score text on 13 dimensions.
8. **Towards AI**: Publication tracing the "delve" origin to RLHF annotation bias, providing the root-cause mechanism for vocabulary overrepresentation.

## Mechanism

Convergent evidence from multiple independent sources (community, industry tools, academic citations) increases confidence that these markers are real and persistent across LLM generations. The fact that diverse detection methodologies (single-word frequency, n-gram analysis, structural pattern matching, community intuition) identify overlapping marker sets suggests the underlying cause (RLHF + formal training data + repetition penalty) produces consistent, detectable patterns.

## Relevance

Provides the broadest evidence base for AI writing markers, complementing the focused academic and industry analyses. Community sources are particularly valuable for identifying emerging markers and chatbot artifacts that formal studies may not capture. The humanize-writing GitHub detection heuristic offers a practical scoring system.

## Related Research

- WriteHuman 2026 analysis: quantitative backbone from 80K+ pair dataset
- Scientometrics delve study (2024): academic validation of RLHF annotation bias
- Pangram Labs n-gram research: n-gram level statistical analysis
- TextVisualization.app corpus analysis: extreme single-word frequency ratios
