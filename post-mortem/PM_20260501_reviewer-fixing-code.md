# PM_20260501_reviewer-fixing-code: Reviewer fixing code instead of rejecting and routing back to TDD

## Failed At

review-gate (Design/Structure/Conventions review). Stakeholder: "Why are reviewers not done properly? Why is R fixing code instead of moving the state back to TDD with a description of what needs to be changed?"

## Root Cause

The reviewer role was conflated with the implementer role. Three process violations occurred simultaneously:

1. Reviewer approved code smells as "minor" or "acceptable trade-off" instead of listing them as findings.
2. Orchestrator fixed spec docs and code directly instead of routing REJECTED back to TDD.
3. Lint/type errors were auto-fixed during review instead of reported as findings for the SE to fix.

## Missed Gate

The review-gate state. Each review tier should produce APPROVED or REJECTED without modifying any files. On REJECTED, the flow routes back to the TDD cycle. The SE implements fixes, not the reviewer.

## Fix

1. Added three rules to `code-review.md` Key Takeaways:
   - "The reviewer MUST NOT modify any files: produce APPROVED or REJECTED report only. On REJECTED, the flow routes back to the TDD cycle; the SE implements fixes, not the reviewer."
   - "'Minor' is not a pass: code smells that are acknowledged must still be listed as findings for the SE to evaluate."
   - "Lint and type errors are findings to report, not to fix during review. The SE fixes them in the next TDD cycle."
2. Updated `review-design/SKILL.md` step 6: smell findings are listed, not dismissed as "minor", referencing `code-review#key-takeaways`.
3. Updated `review-conventions/SKILL.md`: added `code-review#key-takeaways` to load list and added explicit rule that reviewer MUST NOT modify files: lint errors are findings, not auto-fix opportunities.
4. Strengthened `code-review.md` Concepts section with same rules.

## Restart Check

SA verifies that:
- [ ] All three review sub-gates produce APPROVED/REJECTED verdicts without modifying any files
- [ ] On REJECTED, the flow transitions back to TDD with a findings document
- [ ] No code or spec doc changes are made during the review-gate state
- [ ] Code smells are explicitly listed in findings rather than dismissed as "minor"