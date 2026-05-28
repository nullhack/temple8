# Design and Code Inspections (Fagan, 1976)

## Citation

Fagan, M. E. (1976). "Design and Code Inspections to Reduce Errors in Program Development." *IBM Systems Journal*, 15(3), 182–211.

## Source Type

Academic Paper

## Method

Experiment

## Verification Status

Verified

## Confidence

High

## Key Insight

Structured inspections using checklists detect 60-90% of defects before testing, far more than unstructured walkthroughs by forcing reviewers to articulate specific failures.

## Core Findings

1. **Defect Detection Rate**: Structured inspections detect 60-90% of defects before testing phase
2. **Cost Effectiveness**: Fixing defects in early phases costs 10-100x less than fixing in maintenance phase
3. **Six-Phase Process**: Planning, Overview, Preparation, Inspection meeting, Rework, Follow-up
4. **Role-Based Review**: Author, Reader, Reviewers, Moderator, Recorder each have specific responsibilities
5. **Checklist-Driven**: Systematic checking against specific quality attributes prevents confirmation bias

## Mechanism

Fagan inspections constrain reviewer attention to overcome confirmation bias. Unstructured reviews allow skimming and overlooking defects through expectation confirmation. Structured inspection requires checking each quality attribute individually, forcing System 2 thinking. Self-declaration checklists (AGREE/DISAGREE criteria) prevent vague "looks good" approvals that hide defects.

## Relevance

Essential for code quality assurance, defect prevention, software inspection processes. Applied in formal review procedures, quality gates, peer review systems. Foundational for static analysis, code review practices, and quality assurance in software development lifecycle.

## Related Research

Connects to (Tversky & Kahneman, 1974) on confirmation bias, (Kahneman, 2011) on System 1/2 thinking. Part of broader software quality methodologies alongside testing, static analysis. Related to inspection techniques, peer review processes, and formal verification approaches.