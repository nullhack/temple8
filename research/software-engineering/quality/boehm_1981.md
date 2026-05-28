# Software Engineering Economics (Boehm, 1981)

## Citation

Boehm, B. W. (1981). *Software Engineering Economics*. Englewood Cliffs, NJ: Prentice-Hall. ISBN 0-13-822122-7.

## Source Type

Practitioner Book

## Method

Case Study

## Verification Status

Verified

## Confidence

High

## Key Insight

The cost of fixing a software defect escalates by roughly an order of magnitude at each subsequent lifecycle phase, from 1× during requirements to 100× after deployment.

## Core Findings

1. **Phase-dependent cost escalation**: Based on TRW and IBM project data, the relative cost to fix a defect grows exponentially with phase: requirements (1×), design (~5×), implementation (~10×), unit test (~20×), acceptance test (~50×), and operations (~100–1000×).
2. **Quantified defect origin**: Roughly 60–80% of defects originate in requirements and design, yet the majority of fix effort is expended during later phases when those defects are discovered.
3. **Early investment leverage**: Investing in requirements verification and design reviews yields disproportionately high returns because each defect caught early avoids the multiplicative cost of late-phase remediation.
4. **COCOMO foundation**: The data underpins the Constructive Cost Model (COCOMO), which quantifies how project attributes (complexity, team capability, schedule pressure) affect effort and defect rates.
5. **Software cost dominance**: Boehm demonstrated that software costs (not hardware) would dominate system budgets, reversing the prevailing assumption of his era.

## Mechanism

The exponential cost curve arises because late-phase defect fixes require re-traversing all upstream work: re-specifying, re-designing, re-implementing, and re-verifying. A requirements error found in operations forces revisiting every downstream artifact, whereas catching it during requirements review costs only the specification revision. The mechanism is compounding rework. Each phase that passes with an undetected defect adds a layer of dependent decisions and artifacts that must also be corrected.

## Relevance

Directly justifies investment in upfront specification (event storming, domain modeling, ubiquitous language) and early validation (BDD scenarios, TDD) in our workflow. The 10× per phase curve means that a defect caught in review costs 1× what it would cost in production, validating the economic case for design-phase quality gates and the "shift left" principle embedded in our flow.

## Related Research

- (Boehm, 1991): Risk management framework building on COCOMO cost data
- (Fagan, 1976): Code inspection as a cost-effective early detection technique
- (Beck, 2002): TDD as a practice that shifts defect detection leftward
- (Boehm & Basili, 2005): Condensed "Top 10 Defect Reduction" list restating the 100× cost ratio with updated data