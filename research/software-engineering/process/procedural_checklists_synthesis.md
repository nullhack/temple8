# Procedural Checklists and Initiation Anchors (Synthesis, 2026)

## Citation

- Federal Aviation Administration. (2017). *Checklist Design* (AC 120-71b). U.S. Department of Transportation.
- Gawande, A. (2009). *The Checklist Manifesto: How to Get Things Right*. Metropolitan Books.
- World Health Organization. (2008). *WHO Surgical Safety Checklist Implementation Manual* (1st ed.).
- Haynes, A. B., et al. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. *New England Journal of Medicine*, 360, 491–499.
- Finley, J. R. (2018). Self-Generated Memory Cues: Effective Tools for Learning, Training, and Remembering. *Policy Insights from the Behavioral and Brain Sciences*, 5(2), 189–197.

## Source Type

Industry Standard

## Method

Aviation incident analysis (Boeing 299 crash, 1935), prospective sequential time-series study (8 hospitals, WHO SSC), regulatory guidance synthesis (FAA AC 120-71b)

## Verification Status

Verified

## Confidence

High

## Key Insight

Checklists must be anchored to clear external cues that cannot be forgotten, and each gate requires explicit challenge-response confirmation before proceeding. Floating initiation and collapsed phases are the primary failure modes.

## Core Findings

1. **Initiation anchors prevent skip failures.** FAA AC 120-71b §5.1.5: checklist initiation must be anchored to a clear external cue (e.g., reaching 2,000 feet before hold-short line). "Floating" initiation (no external trigger) has high risk of being forgotten entirely.
2. **Challenge-response ensures explicit confirmation.** Aviation uses two-person read-respond. WHO SSC uses three phases (Sign In, Time Out, Sign Out) with a coordinator who must confirm completion before the team proceeds.
3. **Interruption recovery requires restarting.** FAA AC 120-71b §5.2.3: if a checklist is interrupted and position is unclear, the section must be reaccomplished from the beginning. Partial completion is never trusted.
4. **Cue distinctiveness prevents overload.** Finley (2018): effective cues are distinctive (single mapping), encoding-specific (overlap with task context), and stable (consistent across environments). Cue overload degrades reliability.
5. **Structured pause points drive the effect.** Haynes et al. (2009): WHO SSC reduced complications 11.0%→7.0% and mortality 1.5%→0.8%. The mechanism was not individual items but forced communication at phase transitions.
6. **Multi-phase collapse loses fail-fast.** Collapsing checklist phases (e.g., running all review tiers in one pass) eliminates independent gates. Each phase can fail independently and should stop the sequence.

## Mechanism

Checklists work by externalizing procedural memory into explicit confirmation steps at phase boundaries. The initiation anchor creates a reliable trigger that cannot be forgotten. Challenge-response forces attention reset at each item. Interruption recovery prevents partial-completion confidence. Together these prevent the three main failure modes: forgetting to start, skipping items, and trusting incomplete sequences.

## Relevance

Applied to agentic workflow orchestration: the `[~]` anchor item in the todo template is the initiation anchor for state exit. The 6-point anchor checklist (dispatch completed, single-state scope, flowr next checked, transition executed, todo rewritten, no state skipped) is the challenge-response gate. The single-dispatch rule prevents multi-state collapse. If the anchor reveals a problem, the state is reaccomplished from the beginning (interruption recovery). This maps directly to FAA AC 120-71b's pattern of flow → checklist → confirmation at each phase boundary.

## Related Research

- [[software-craft/tdd]]: two-phase quality gate (design-phase: test-fast only; convention-phase: lint/format)
- [[workflow/flowr-operations]]: flowr commands for state transitions
- [[requirements/pre-mortem]]: pre-mortem analysis as a checklist item before example writing
