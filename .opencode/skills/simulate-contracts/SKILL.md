---
name: simulate-contracts
description: "Answer whether a correct implementation passing every test would yield a complete, working system — the final gate before build."
---

# Simulate Contracts

1. Load [[requirements/spec-simulation]], [[software-craft/test-stubs]] — the simulation method and test-pair drift rules.
2. Answer the gate question per [[requirements/spec-simulation]]: IF a correct implementation made every test in the set pass THEN would the result work as intended and be complete? Answer it by walking — walk the e2e path hop by hop (each type handed across, each value carried, each side effect performed tracing to a backing contract), then trace each domain value across every test that touches it for shape coherence. The tool checks below are the floor that makes the walk safe to trust; they are not the walk. IF a hop breaks or two tests disagree on a value's shape THEN name the gap precisely and stop — route back to plan, do not advance on a clean tool run alone.
3. Run pyright on the combined set. The gate is zero errors; `reportMissingModuleSource` is expected (source .pyi exist but no .py yet) and is tolerated.
4. Check no-orphans: every source .pyi symbol is exercised by at least one test, and every test reference is backed by a source .pyi.
5. Check traceability: every consolidated interview finding maps to at least one test or an explicit deferral, and every external service has a captured cassette its tests replay.
6. Check layer order: external-boundary stubs complete before adapter stubs, and so on.
7. Run stubtest on the tests to confirm zero drift between every test .pyi and its sibling .py per [[software-craft/test-stubs]]. Source stubtest waits for build — no source .py exists yet.
8. Run ruff on the whole project (`ruff check .` and `ruff format . --check`); the gate is zero violations. Plan-authored tests and source stubs must be lint-clean before build — a lint defect caught here is a defect build never has to edit around.
9. IF a test references an external exchange no captured cassette covers THEN append the finding to `.cache/<session_id>/journal.md` (service, the missing case) and fire `needs-capture`. This routes back to explore to record the missing reality, not forward to build.
