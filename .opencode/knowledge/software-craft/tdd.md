---
domain: software-craft
tags: [tdd, red-green-refactor, yagni, kiss, contract-driven]
last-updated: 2026-07-01
---

# Test-Driven Development

## Key Takeaways

- The cycle is **red → green → refactor** (Beck, 2002). In this workflow the tests already exist — authored in plan with a `@pytest.mark.pending` mark — so red *removes the mark and confirms the right failure*, it does not write a test.
- **The right-reason rule**: a new contract fails with `ImportError` (source `.py` absent, the deferred in-body import cannot resolve); a reworked contract fails with an assertion (source stale against the changed contract). A red for any other reason — a typo, a bad fixture, a test that violates its own contract — is rejected, not patched.
- Green writes the **minimum code** to turn the tests green, implementing the `.py` from its fixed `.pyi`. YAGNI and KISS override every other principle; a hard-coded value is correct when the test needs only that value (Beck & Jeffries, 1999; North, 2006).
- Refactor restructures the `.py` while the `.pyi` and the tests stay **frozen and green**; it is design-only, never convention compliance — conventions run in CI. A change that needs the `.pyi` is a contract gap escalated at review.
- The cycle runs **per contract** — a source module and the tests that exercise it — in outside-in dependency order; stubtest is scoped to the modules built this cycle.
- Source `.py` is kept **naked of docstrings** across the whole cycle — `select` strips any carried over from the last merge, and docstrings are regenerated at deliver/merge from the stable code per [[software-craft/docstring-lifecycle]]. Tests and stubs are naked permanently.

## Concepts

**The cycle, adapted.** Beck's (2002) red/green/refactor cycle is the spine, but the entry conditions differ from classical TDD. Here the plan phase has already written the tests as executable specifications (North, 2006), each marked pending so the suite stays green-with-skips. Red is therefore the act of un-marking the target contract's tests and confirming they fail for the right reason; green and refactor then proceed exactly as in classical TDD. The tests drive the implementation because they pre-exist it; what is removed is the test-authoring step, not the test-first discipline.

**The right-reason rule.** A red that fails for the wrong reason is a broken contract, not a green target. The two right reasons track the two kinds of work: building a contract that has never been implemented yields an `ImportError`, because the deferred import inside each test body cannot resolve a module that does not exist; re-implementing a contract that has changed yields an assertion failure, because the stale source no longer satisfies the revised tests. A red caused by anything else — a name typo, a fixture that does not resolve, a test that contradicts its own `.pyi` — is a defect in the test or the stub, and the response is to reject and escalate, never to patch the test so it fails for an acceptable reason.

**Minimum code, YAGNI first.** Green writes the simplest code that passes the tests, and "simplest" is enforced by a priority: YAGNI (Beck & Jeffries, 1999) trumps everything — if no test requires it, it is not written — and KISS trumps DRY, because a small duplication is often simpler than the wrong abstraction. Hard-coded values are not just permitted but correct when the test supplies only that value; a configurable constant invented for a future the tests do not describe is exactly the speculative generality YAGNI forbids.

**Refactor under green, design only.** Refactor improves the `.py`'s structure while every test stays green, because the tests are the safety net that makes restructuring safe. Two boundaries are fixed: the `.pyi` does not move (a refactor that needs to change it has found a contract gap, escalated at review), and conventions do not run (no docstrings, no formatting pass — those are merge-time per [[software-craft/docstring-lifecycle]]). Refactor is where SOLID, Object Calisthenics, and the smell catalogue are applied, each when its symptom appears, never speculatively.

**Per contract, in dependency order.** The unit of work is one contract: a source module and the tests that exercise it, taken through the whole cycle. Contracts are picked in outside-in dependency order so that a module is built only after the modules it imports; a shared foundation module with no external boundary of its own is pulled in alongside the first contract that depends on it. stubtest runs scoped to the modules built this cycle, because the whole-suite run would false-fail on unbuilt sibling stubs.

## Content

### The cycle, adapted

| Phase | Classical TDD | This workflow |
|---|---|---|
| red | write a failing test | un-mark an existing test; confirm it fails for the right reason |
| green | minimum code to pass | implement `.py` from its fixed `.pyi` |
| refactor | improve structure, stay green | improve `.py`; `.pyi` and tests frozen; design only |

The discipline test-first is preserved — the tests still precede the implementation — by the plan phase writing them ahead of time, not by the build phase writing them inline.

### The right-reason rule

| Red reason | Kind of work | Verdict |
|---|---|---|
| `ImportError` on the deferred in-body import | new contract (source absent) | right reason — proceed to green |
| assertion failure against changed tests | rework (source stale) | right reason — re-implement |
| `NameError`, fixture resolution, test contradicts its `.pyi` | test or stub defect | reject — escalate, do not patch |

Removing the `@pytest.mark.pending` decorator can orphan its `import pytest` when the test used pytest for nothing else (no `raises`, no `approx`, no parametrize); dropping that now-unused import is part of red — a lint side-effect of un-marking, not a behaviour edit, so it stays within the no-test-editing discipline.

### Minimum code, YAGNI first

- if the test needs only `42`, return `42` — do not invent a configurable constant;
- no parameter, abstraction, or branch the test does not exercise;
- a small duplication beats a premature abstraction (KISS over DRY);
- when the trivial implementation passes, the next test is the cure, not more code.

### Refactor under green, design only

| Allowed in refactor | Not allowed |
|---|---|
| restructure the `.py` | edit the `.pyi` (escalate a contract gap) |
| apply SOLID / Object Calisthenics / smell fixes when triggered | edit the tests |
| design improvement only | convention compliance (docstrings, formatting — merge-time per [[software-craft/docstring-lifecycle]]) |

### Per contract, in dependency order

- one contract per cycle: a source module and its tests, red through ship;
- pick the lowest-layer contract first; a module is built after what it imports;
- a shared foundation module rides alongside the first contract that needs it;
- stubtest is scoped: `stubtest <package>.<mod> tests.<test_mod>` this cycle, whole-suite at merge.

## Related

- [[software-craft/test-design]] — what a good test looks like (the specifications red un-marks)
- [[software-craft/test-stubs]] — the `.pyi`/`.py` pair whose drift green keeps clean
- [[software-craft/source-stubs]] — the fixed `.pyi` green implements to
- [[software-craft/refactoring-techniques]] — the moves refactor applies
- [[software-craft/code-review]] — the review that gates the cycle's output
- [[software-craft/docstring-lifecycle]] — source `.py` stays naked through the cycle; docstrings regenerate at merge
