---
name: review-gate
description: "Two-tier review with fail-fast: design -> structure"
---

# Review Gate

Available knowledge: [[software-craft/code-review]], [[software-craft/test-design]], [[software-craft/test-stubs]], [[software-craft/smell-catalogue]], [[software-craft/object-calisthenics]], [[software-craft/solid]], [[software-craft/tdd]], [[software-craft/design-patterns]], [[architecture/reconciliation#key-takeaways]]. `in` artifacts: read all before starting work.

**Fail-fast rule**: Stop at first failure in any tier. Do NOT proceed to next tier if current tier fails.

## Tier 1: Design Review

1. Verify implementation aligns with domain spec per [[software-craft/code-review#concepts]]: entities match domain spec, value objects enforce invariants, use cases follow aggregate boundaries.
2. Verify implementation aligns with architectural decisions per [[software-craft/code-review#concepts]]: ADR compliance, quality attributes met.
3. Verify all `# Constraints:` in the .feature file are met in the implementation. For technology constraints, read domain_spec.md `### Technology Requirements` table and execute the Verification instruction for each row (grep imports, check file existence, inspect config). Zero evidence → FAIL. For quality attribute constraints, verify thresholds are enforced.
4. Verify implementation aligns with feature specification: all Examples have corresponding test implementations, behavior matches Gherkin steps.
5. Verify each design principle adversarially per the priority order in [[software-craft/tdd#content]]. Load the full document for detection at each sub-step. Fail-fast at first violation:

   a) YAGNI per [[software-craft/tdd#concepts]]: no premature abstractions, no speculative generalization, no future-proofing beyond what failing tests require.
   b) KISS per [[software-craft/tdd#concepts]]: simplest solution chosen; no over-engineered alternatives where a direct approach suffices.
   c) DRY per [[software-craft/tdd#concepts]]: no duplicated logic or duplicated knowledge. Duplication is acceptable only when DRY would create wrong coupling.
   d) ObjCal per [[software-craft/object-calisthenics]]: verify all 9 rules with detection heuristics.
   e) Smells per [[software-craft/smell-catalogue]]: detect each smell with file:line evidence.
   f) SOLID per [[software-craft/solid]]: verify each principle with detection heuristics.
   g) Patterns per [[software-craft/design-patterns]]: every pattern must be justified by a requirement, not added speculatively.
6. **FAIL-FAST**: If any design violations found → exit `fail` with specific citations (file:line). Do NOT proceed to structure review.

## Tier 2: Structure Review

7. Run `beehave status --json` per [[software-craft/test-stubs#concepts]]. IF feature stage is `ok` with no violations → structural traceability is clean. IF not `ok` → run `beehave check` per [[software-craft/test-stubs#concepts]] and verify all violations resolved.
8. Verify test quality per [[software-craft/test-design#concepts]]: tests follow AAA pattern, clear assertions, behavior-focused not implementation-coupled.
9. Run `task test` and verify all tests pass with coverage.
10. Run `ruff check .` and verify no functional lint violations (the default ruff config only includes bug-catching rules).
11. **FAIL-FAST**: If any structure violations found → exit `fail` with specific citations.
