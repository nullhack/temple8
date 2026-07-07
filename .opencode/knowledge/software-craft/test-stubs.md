---
domain: software-craft
tags: [test-stubs, pyi, stubtest, contract-surface, pep-484]
last-updated: 2026-07-01
---

# Test Stubs

## Key Takeaways

- A test stub here is a **PEP 484 `.pyi` signature file** for a test module — not a Meszaros *Test Stub* (a test double that feeds indirect inputs to the SUT). The two share a name and nothing else; disambiguate before reading further (PEP 484; Meszaros, 2007).
- When a `.pyi` and its `.py` both exist, the type checker reads **only the `.pyi`** and ignores the `.py` (PEP 484; mypy; PEP 561). Editing the `.py` never reaches the checker, so `.pyi`↔`.py` drift is **invisible to pyright**.
- `mypy.stubtest` is the **sole drift detector**: it imports the module at runtime via `inspect`, diffs the live object against the `.pyi`, and reports every mismatch. It verifies structure and signatures — **not** return-type accuracy (mypy docs).
- A test `.pyi` must mirror the test `.py`'s **complete module surface** — every module-level constant, fixture, helper, the test class, and every method signature — or stubtest flags the gap (typing.python.org).
- Author **stdlib-typing-only**; never import third-party libraries in the stub (they trip mypy `import-untyped`, and stubtest does not require them). Route any import-that-exists-only-for-types through `typing.TYPE_CHECKING`.

## Concepts

**Two meanings of "stub" — disambiguate first.** Meszaros (2007) named a *Test Stub* as a test double that replaces a depended-on component to feed controlled indirect inputs to the system under test. PEP 484 named a *stub file* (`.pyi`) as a signature-only description of a module for type checkers. The two are unrelated — one is a runtime object, the other a static type artifact — yet both are called "stub"; a reader arriving here for test-double patterns is in the wrong place. Test doubles belong to [[software-craft/test-design]]; this file is about `.pyi` signature files.

**The `.pyi` wins, so pyright hides drift.** PEP 484 is explicit: "If a stub file is found the type checker should not read the corresponding 'real' module." mypy and PEP 561 concur — "the `.pyi` file takes precedence," and "type checkers MUST maintain the normal resolution order of checking `*.pyi` before `*.py`." The consequence is asymmetric and dangerous: while the `.py` is absent or stale, the checker trusts the `.pyi` blindly and reports nothing. A stale `.pyi` is a silent lie that pyright will never expose; only a tool that reads the runtime module can.

**stubtest — the runtime diff.** mypy ships `stubtest` precisely because stubs diverge. It imports the module and introspects the live objects with `inspect`, then compares what it finds against the analysed `.pyi` (mypy docs). It catches missing definitions, renamed or re-typed arguments, and default-value mismatches, and it is the tool used to validate typeshed itself. Two limits matter: it checks structure and signatures, not whether a return type is *accurate*; and it executes the module on import, so it must run where the code and its dependencies are installed.

**Mirror the complete module surface.** A `.pyi` carries the full public interface of its module — every class, function, and constant (typing.python.org). For tests this is especially load-bearing because stubtest compares the *whole* module: a module-level constant (`BASE`, `CASSETTE`), a fixture function, or a helper omitted from the `.pyi` is a drift hit even when the test logic is correct. The test-specific difficulty is that fixture parameters are resolved by name at runtime, and attributes assigned in `setup_method` are invisible to a reader of the stub — both must be hand-declared in the `.pyi` and hand-synced, a standing drift vector with no library-stub analogue.

**Stdlib typing only; types under TYPE_CHECKING.** Importing a third-party library in a `.pyi` makes mypy report `import-untyped` for any library that ships no stubs of its own, and stubtest does not need the import — it consults the *runtime* module, which already has its dependencies. Keep the stub to stdlib typing; route any import that exists only for types through a guarded block so it is invisible at runtime.

## Content

### Two meanings of "stub"

| Term | Origin | What it is | Lives in |
|---|---|---|---|
| Test Stub | Meszaros, 2007 (xUnit Patterns) | a test **double** replacing a depended-on component to feed indirect inputs to the SUT | runtime, inside a test body |
| stub file (`.pyi`) | PEP 484 | a **signature-only** description of a module for type checkers (`...` bodies, no runtime logic) | a `.pyi` file beside its `.py` |

This knowledge is about the second. The typing.python.org guide notes that conventional `.pyi` authoring targets a *library's public interface for consumers* and explicitly lists *tests* among modules excluded from stubs — so authoring test `.pyi` deliberately is a conscious adaptation of the mechanism, justified here because the test `.pyi` is the contract surface the staged workflow authors before any body or source exists.

### Why the checker hides drift

PEP 484 fixes the resolution order: when both files are present, the `.pyi` is the single source the checker consults, and the `.py` becomes invisible — not "lower priority," ignored. This is a feature for libraries (consumers type-check against the published surface, not the implementation) but a hazard for a workflow that maintains both files by hand:

| Situation | pyright sees | Drift detected? |
|---|---|---|
| `.pyi` present, `.py` absent | the `.pyi` only; `reportMissingModuleSource` (tolerated) | n/a — expected pre-build |
| both present, in sync | the `.pyi` only | no drift — but pyright cannot confirm the `.py` matches |
| both present, `.py` drifted | the `.pyi` only | **no** — pyright is silent |

ruff, equally, lints each file independently and is not a type checker, so it detects no cross-file drift either. The one tool that does is stubtest.

### stubtest — the runtime diff

stubtest's method is dynamic, not static. From the mypy docs: it imports the package, introspects the live objects with `inspect`, then diffs the result against the analysed `.pyi`. What it catches and what it cannot:

| Catches | Does not catch |
|---|---|
| missing / redundant definitions | whether a return type is *accurate* |
| argument name / arity / annotation mismatch | internal implementation correctness |
| default-value presence and shape | runtime behaviour |
| positional-only / kind mismatches | type-checker-level soundness |

Operational notes that bear on the gate: stubtest must run in the project environment (it executes the module, so transitive deps must be installed); `--ignore-missing-stub` silences "runtime has it, stub doesn't"; `--allowlist FILE` (regex) suppresses known exceptions. The workflow scopes stubtest per cycle — `stubtest <package>.<mod> tests.<test_mod>` at green/review — and runs the whole `stubtest <package> tests` only at merge, once every `.py` exists.

### Mirror the complete module surface

stubtest compares the whole module, so a `.pyi` that omits any name the `.py` exposes is a drift hit regardless of test correctness. For a test module that means declaring every module-level constant, every fixture, every helper, the test class, and every method signature:

```
BASE: str                          # module constants the .py defines
CASSETTE: str

def sample_rate() -> Rate: ...     # helper functions

class TestRatesAdapter:            # the test class
    rates: RatesAdapter            # attr set in setup_method — hand-declared
    def setup_method(self) -> None: ...
    def test_fetches_rate(self, monkeypatch) -> None: ...
```

Two test-specific drift vectors have no library-stub analogue. First, fixture parameters (`monkeypatch`, `tmp_path`, `capsys`) are resolved by *name* through pytest's dependency injection; a type checker reading the `.pyi` cannot see that binding, so the parameter is declared for structural agreement and left unannotated (the typing.python.org guide permits unannotated arguments in partial stubs). The replay mechanism for an external-boundary adapter test (`vcr.use_cassette`, never `pytester`) is fixed by the service kind — see [[software-craft/external-fixtures]]'s replay-mechanism table; the `cassette_path(NAME)` constant is declared at module level and the `with` block is in the body, so stubtest sees the cassette and the simulation sees the replay. Second, instance attributes assigned in `setup_method` do not exist in the class body the checker reads, so they must be hand-declared at class level in the `.pyi` and updated whenever `setup_method` changes. Both drift silently if forgotten — stubtest is what eventually catches them.

### Stdlib typing only; types under TYPE_CHECKING

Importing a third-party library in a `.pyi` trips mypy's `import-untyped` for any library that ships no stubs, polluting the simulate gate with noise the test does not need. stubtest does not require the import either, because it consults the runtime module — which already has its dependencies installed. Keep the stub to stdlib typing, and route any import that exists only for types through a guarded block so it stays invisible at runtime:

```
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from converter.models import Rate   # import-only-for-types
```

This keeps the deferred-import convention intact: a pending test module whose system-under-test is not yet built still collects and skips cleanly, because the SUT import lives inside each test body, not at module top.

## Related

- [[software-craft/source-stubs]] — the source-side `.pyi` craft; the same drift mechanics from the implementation's perspective
- [[software-craft/test-design]] — what to test, and the Meszaros test doubles (the *other* meaning of "stub")
- [[requirements/spec-simulation]] — the simulate gate runs stubtest over the test set
