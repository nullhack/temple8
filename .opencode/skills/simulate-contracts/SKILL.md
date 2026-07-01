---
name: simulate-contracts
description: "Answer whether a correct implementation passing every test would yield a complete, working system — the final gate before build."
---

# Simulate Contracts

1. Load [[requirements/spec-simulation]], [[software-craft/test-stubs]] — the simulation method and test-pair drift rules.
2. Answer one question: IF a correct implementation made every test in the set pass THEN would the result work as intended and be complete per [[requirements/spec-simulation]]?
3. Run pyright on the combined set. The gate is zero errors; `reportMissingModuleSource` is expected (source .pyi exist but no .py yet) and is tolerated.
4. Check no-orphans: every source .pyi symbol is exercised by at least one test, and every test reference is backed by a source .pyi.
5. Check traceability: every consolidated interview finding maps to at least one test or an explicit deferral, and every external service has a captured cassette its tests replay.
6. Check layer order: external-boundary stubs complete before adapter stubs, and so on.
7. Run stubtest on the tests to confirm zero drift between every test .pyi and its sibling .py per [[software-craft/test-stubs]]. Source stubtest waits for build — no source .py exists yet.
