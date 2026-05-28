# Software Risk Management (Boehm, 1991)

## Citation

Boehm, B. W. (1991). "Software Risk Management: Principles and Practices." *IEEE Software*, 8(1), 32–41. https://doi.org/10.1109/52.62930

## Source Type

Academic Paper

## Method

Theoretical

## Verification Status

Verified

## Confidence

High

## Key Insight

Architecture risk can be systematically assessed using Probability × Impact classification, replacing intuitive risk assessment with an explicit, auditable evaluation framework.

## Core Findings

1. **Risk quantification framework**: Each identified risk is rated on two dimensions: Probability (likelihood of materialization) and Impact (severity of consequence), with risks prioritized by their product.
2. **Risk leverage concept**: The ratio of risk reduction to mitigation cost enables teams to focus effort on high-leverage interventions (significant risk reduction for low cost).
3. **Systematic risk identification**: Boehm's 10 top software risk items provide a checklist for proactive risk identification across personnel, requirements, technology, and schedule dimensions.
4. **Risk mitigation strategies**: Three primary approaches - risk avoidance (eliminate risk source), risk monitoring (track risk indicators), and risk contingency planning (prepare response plans).
5. **COCOMO model foundation**: Boehm's cost estimation models (COCOMO/COCOMO II) provide quantitative basis for impact assessment in software projects.
6. **Spiral model integration**: Risk assessment is built into the spiral software development model at each iteration cycle.

## Mechanism

Probability × Impact works because it forces decision-makers to externalize and quantify what would otherwise remain gut feelings. Low-probability high-impact risks (e.g., database vendor bankruptcy) are distinguished from high-probability low-impact risks (e.g., minor performance degradation); both may have the same exposure score but demand different mitigation strategies. The framework also introduces risk leverage: high-leverage mitigations (significant risk reduction for low cost) are prioritized over low-leverage ones (minor risk reduction for high cost).

## Relevance

Foundational framework for architectural decision records (ADRs) where each decision carries potential risks requiring explicit evaluation. Essential for project management, system design, and any development context requiring systematic risk assessment. Directly applicable to technology selection, architecture planning, and resource allocation decisions in software engineering.

## Related Research

- (Kazman, Klein & Clements, 2000): ATAM method building on Boehm's risk assessment principles
- (Fowler, 2003): Architectural decision-making frameworks incorporating risk evaluation
