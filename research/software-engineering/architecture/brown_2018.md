# C4 Model (Brown, 2006–2018)

## Citation

Brown, S. (2018). *Software Architecture for Developers*, Volume 1. Leanpub. C4 model first described 2006–2011, official site launched 2018. Available at https://c4model.com

## Source Type

Practitioner Book

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Four levels of architectural abstraction (Context, Container, Component, Code) provide just enough detail at each audience level without overwhelming any single audience.

## Core Findings

1. **Hierarchical abstraction levels**: Context (system in environment), Container (deployable units), Component (modules within containers), Code (classes and functions).
2. **Audience-specific communication**: Each level answers different questions for different audiences: Context for stakeholders, Container for developers/operators, Component for internal structure, Code for detailed design.
3. **Progressive disclosure**: Starting from Context and drilling down prevents premature detail overload.
4. **Notation independence**: C4 works with any diagramming tool or notation. Boxes and lines are sufficient.
5. **Tooling independence**: Can be implemented with simple drawing tools, specialized software, or code-based approaches.
6. **Developer-friendly approach**: Focuses on developer mental models rather than formal architectural frameworks.
7. **Supporting diagrams**: System landscape, dynamic, and deployment diagrams complement the core four levels.

## Mechanism

The C4 model works because each level answers a different question for a different audience: Context for stakeholders and non-technical team members ("what does the system interact with?"), Container for developers and operators ("what are the deployable units and their tech stacks?"), Component for developers working within a container ("how is this container structured internally?"), and Code for detailed design (rarely needed as a diagram). Starting from Context and drilling down prevents premature detail and ensures the architecture communicates effectively at every level.

## Relevance

Essential methodology for software architecture documentation and communication. Widely adopted for system design, technical onboarding, and stakeholder communication. Critical for teams needing to communicate architecture across different technical skill levels and organizational roles. Directly applicable to microservices documentation, system integration planning, and technical decision-making processes.

## Related Research

- (Kruchten, 1995): 4+1 architectural view model that influenced hierarchical approach
- (Fowler, 2003): "Who Needs an Architect?" discussion on architectural communication