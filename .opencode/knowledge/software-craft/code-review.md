---
domain: software-craft
tags: [code-review, adversarial-review, fail-fast, structured-report, inspection]
last-updated: 2026-07-01
---

# Code Review

## Key Takeaways

- The reviewer's default hypothesis is **"this is probably broken — prove otherwise."** Adversarial review, actively hunting for defects, catches more than cooperative "looks good" review, because accountability shifts the search from confirming that it works to finding where it breaks (Fagan, 1976; Tetlock, 1985).
- **Fail fast**: stop at the first defect, write a minimal REJECTED report, and do not continue. The first defect may invalidate everything that follows, so accumulating findings on a doomed pass wastes effort (Fagan, 1976).
- The reviewer **never modifies files**; the output is APPROVED or REJECTED, never an edit. "Minor" is not a pass — an acknowledged smell is still a finding that must be listed.
- **Two review modes run in this workflow, each with its own criteria**: review-test-stubs checks coverage, scope, and happy-path completeness against the interview (NOT code quality — that is gated later on the bodies); review-implementation checks correctness, quality, drift, and green tests against the contract.
- Each criterion is recorded as **Criterion / Verdict / Evidence / Action**. The structure forces a specific judgment per check and refuses the vague "looks good" approval that self-declaration exists to prevent (Hattie & Timperley, 2007).

## Concepts

**Adversarial review.** Fagan's (1976) inspections detected the bulk of defects before testing by fixing the process: separate the objectives so the team focuses on one at a time, classify error types and rank their frequency, then describe how to spot each type and condition the team to seek the high-occurrence, high-cost ones. The mechanism that makes it work is stance: Tetlock (1985) showed that accountability to an unknown audience shifts a reviewer out of confirmation bias ("looking for reasons it works") into adversarial search ("looking for reasons it breaks"). The reviewer begins from the assumption that the change is faulty and demands evidence to the contrary; vague approval is the failure mode the stance exists to prevent.

**Fail fast.** Fagan's inspection stops at the first defect found, because a defect early in the artefact may invalidate the assumptions on which the rest of the review depends. Translated to a contract review: the moment a real defect is found, the reviewer writes a minimal REJECTED report — the defect, its file:line evidence, the required action — and stops. Accumulating further findings on a pass whose foundation is already broken wastes the reviewer's effort and the author's attention; the author fixes the defect, resubmits, and the reviewer starts over on a sound base.

**Report-only; "minor" is never a pass.** The reviewer produces a verdict, not a patch: APPROVED or REJECTED, with findings, never an in-place edit, because the moment the reviewer starts fixing things the author stops owning the work and the review stops being independent. Within a review, "minor" is not a passing grade — a code smell that is acknowledged is still a finding and is still recorded. Downgrading a real defect to silence it defeats the inspection; the severity may shape the ordering of fixes, not whether they are reported.

**Two review modes, one method.** The workflow runs two reviews, each aligned to its phase. review-test-stubs reviews the `.pyi` set for coverage, scope, and happy-path completeness *against the interview* — it deliberately does not judge code quality, because the bodies do not exist yet; quality is gated later, on the `.py`. review-implementation reviews the built source *against its contract* for correctness, quality, drift, and green tests. The method — adversarial, fail-fast, structured — is the same in both; only the criteria change.

**Structured self-declaration.** Hattie and Timperley (2007) show that feedback forces learning only when it demands a specific judgment; a checklist of AGREE/DISAGREE on named criteria prevents the "I skimmed it and nothing jumped out" approval. The PASS/FAIL record — Criterion, Verdict, Evidence, Action — is that device: each check must be articulated against a named criterion with file:line evidence, so approval is explicit about what was verified rather than gestured at.

## Content

### Adversarial review

Fagan (1976) reported that structured inspection caught most defects before any test execution, and the SmartBear Cisco study (2006) — the largest published peer-review dataset — quantified the pace at which the inspection stays effective:

| Practice | Finding |
|---|---|
| review < 200–400 LOC at a time | defect density drops sharply above this |
| review < 300–500 LOC/hour | faster review misses defects |
| author preparation | the author's own annotation before review saves reviewer time on obvious defects |

The stance is the part that travels: the reviewer adopts "I will actively search for defects, not confirm correctness," and conditions the search toward the error types this codebase produces most. A review that begins from "probably fine" is, in Fagan's terms, an inspection with its objective inverted.

### Fail fast

The protocol is a loop, not a batch:

1. review against the first criterion;
2. IF a real defect is found THEN write a minimal REJECTED report (defect, file:line evidence, required action) and STOP;
3. ELSE proceed to the next criterion;
4. repeat until every criterion is checked → APPROVED.

The discipline is to stop, not to stockpile. A second finding written on top of a first that may have invalidated it is effort spent on a pass the author cannot act on without re-review anyway.

### Report-only; "minor" is not a pass

The reviewer's output is a verdict plus findings, never an edit. Conventions — formatting, naming, the no-docstring policy — are NOT a review concern in this workflow: ruff (with `PYI`) runs in CI as the enforcement backstop, and review is spent on contract, quality, drift, and behaviour. Within the review's own criteria, no defect is too small to report: a smell that is noticed is a finding, recorded at whatever severity; it is never downgraded out of the report to keep a change moving.

### Two review modes, one method

| Mode | Phase | Criteria | NOT judged here |
|---|---|---|---|
| review-test-stubs | after test `.pyi` authoring | coverage against the interview; scope (integration + E2E only); happy-path completeness | code quality (no bodies yet) |
| review-implementation | after green | impl-matches-contract; source-quality-clean (SOLID/DRY/KISS/YAGNI/Object Calisthenics, per [[software-craft/solid]] and [[software-craft/object-calisthenics]]); stubtest-clean; tests-green | — |

Both modes apply the same adversarial, fail-fast, structured method; the difference is only what the criteria are. A happy-path gap at review-test-stubs and a SOLID violation at review-implementation are both REJECTED with the same kind of report.

### The PASS/FAIL report

For every criterion checked, the reviewer records a row, whether the verdict is PASS or FAIL:

| Field | Holds |
|---|---|
| Criterion | the named quality attribute being checked |
| Verdict | PASS or FAIL |
| Evidence | file:line reference and the specific observation |
| Action | the required change (FAIL only) |

A REJECTED report is the first FAIL row plus nothing more — the defect, the evidence, the action. APPROVED is the complete table with every row at PASS. There is no third verdict; "looks good" is not one of them.

## Related

- [[software-craft/test-design]] — the criteria a review checks tests against
- [[software-craft/test-stubs]] — the `.pyi` surface review-test-stubs inspects
- [[software-craft/solid]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]] — the quality bar review-implementation enforces
- [[software-craft/source-stubs]] — the source `.pyi` a contract review reads first
