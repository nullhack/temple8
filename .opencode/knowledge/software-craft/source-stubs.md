---
domain: software-craft
tags: [source-stubs, pyi, contract, derive-from-tests, pep-484]
last-updated: 2026-07-01
---

# Source Stubs

## Key Takeaways

- A source stub is a PEP 484 `.pyi` **derived from the test bodies** — the inverse of conventional stub authoring. Every type the tests construct, every method they call, every relationship they assert is the specification of the source surface; the stub records exactly that and nothing speculative.
- `...` bodies only (PEP 484); never `raise NotImplementedError`. The stub is signature-only and compiles for the type checker with no runtime behaviour — behaviour lands in build's green.
- The source `.pyi` is a **fixed contract during build**: green implements the `.py` to satisfy it; refactor cannot edit it; if the body cannot satisfy the `.pyi` without changing it, that is a contract gap escalated at review — never an in-place stub edit.
- **No prescribed layout**, and config is twelve-factor: environment variables plus a gitignored `.env`; a typed Settings model is optional and, if warranted, a normal source stub. External adapters and connectors sit under the package alongside everything else, not as a separate category.
- Structural artifacts are **keyed on what a module is**: an ORM model carries an Alembic migration (the migration IS the schema spec); an external adapter replays the cassettes captured in explore.
- stubtest gates the source pair at green/review/merge — it imports the runtime module (transitive deps must be installed), runs scoped per cycle (the whole-suite run waits until every `.py` exists), and type-only imports go under `TYPE_CHECKING`. The drift mechanics are those of the test pair ([[software-craft/test-stubs]]).

## Concepts

**Derived from the tests, not imagined.** Conventional `.pyi` authoring describes an existing or imagined library's public interface for consumers (typing.python.org). Here the source `.pyi` is derived from the test bodies the plan phase already wrote: each type the tests construct, each method they call, each composition they wire is a demand for a definition, and the stub supplies it with an ellipsis body, placed wherever the source lives. Nothing enters the stub that no test references — speculative generality is structurally impossible, because the tests are the truth and the stub is their shadow.

**Signature-only; `...` not `NotImplementedError`.** PEP 484 specifies that a stub's function bodies be a single ellipsis. `raise NotImplementedError` is runtime behaviour — it executes, and a stub that executes is no longer a pure signature. A `.pyi` with `...` bodies compiles for the type checker and is inert at runtime; the green step replaces each `...` with a real body in the sibling `.py`, never in the `.pyi`.

**Fixed during build.** Once derived, the source `.pyi` is frozen for the whole build cycle: green writes the `.py` to satisfy it, refactor restructures the `.py` while the `.pyi` stays put, and the tests (already written) stay put too. If implementation discovers the `.pyi` is wrong — a missing parameter, a wrong return type, an impossible signature — the response is never to edit the stub in place; it is to escalate a contract gap at review, which routes back to plan for a proper re-derivation. The frozen stub is what keeps the contract the single source of truth.

**No layout, no config artifact.** The tests say where the source lives and what it is called; the stub does not prescribe a package structure on top. Adapters, connectors, and domain types live under the package alongside one another. Configuration is twelve-factor: environment variables are the default, loaded locally from a gitignored `.env`, and a typed Settings model is optional — if it earns its place, it is a normal source stub alongside the rest.

**Structural artifacts keyed to the module.** Some modules carry an artifact beyond the `.py` pair. An ORM model owns an Alembic migration — the migration is the schema spec, born in green, committed in ship, never edited only appended. An external adapter replays the cassettes captured during explore (`VCR_RECORD_MODE=none`). The stub itself does not generate these; it declares the module's surface, and green emits whatever that surface implies.

**stubtest, scoped.** The source pair is drift-checked by `mypy.stubtest` at green, review, and merge. The run is scoped to the modules built this cycle, because a whole-suite stubtest before every `.py` exists fails on unbuilt sibling stubs. stubtest imports the runtime module, so every transitive dependency must be installed in the project venv; imports that exist only for types go under `if typing.TYPE_CHECKING:` so stubtest does not drag heavy runtime deps in for type-only references. The mechanism — why the checker hides drift, why stubtest is the only detector — is the same as for the test pair.

## Content

### Derived from the tests

| The test body asserts | The stub must declare |
|---|---|
| `RatesAdapter(base).fetch_rate("USD")` returns a `Rate` | class `RatesAdapter` with `__init__(self, base: str)` and `fetch_rate(...) -> Rate` |
| `History(db_url).record(c)` then `.recent()` | class `History` with `__init__(self, db_url: str)`, `record(...)`, `recent()` returning the iterator the test consumes |
| `Settings.from_env()` yields `.api_base` and `.db_url` | class `Settings` (frozen) with those attributes and the `from_env()` classmethod |

If a value's representation is ambiguous across tests — a database URL passed as a bare filesystem path in one and a `sqlite:///path` URL in another — pin one canonical form once (the URL form) and state it in the stub, so every consumer agrees rather than each test improvising a shape the others break on.

### Signature-only

```
class Rate:
    base: str
    value: float
    def __init__(self, base: str, value: float) -> None: ...
    def convert(self, amount: float) -> float: ...
```

No `raise NotImplementedError`, no `pass` body, no docstring — `...` only. The `.py` written in green fills these bodies with real logic; the `.pyi` never carries it.

### Fixed during build

| Phase | Who moves | Who stays |
|---|---|---|
| green | the `.py` (written to satisfy the `.pyi`) | `.pyi`, tests |
| refactor | the `.py` (restructured for quality) | `.pyi`, tests |
| review (gap found) | escalate to plan — re-derive | nothing edited in place |

The asymmetry is deliberate: the `.pyi` and the tests are the contract, and contracts do not move while one party is implementing. A green or refactor that needs to change the `.pyi` is signalling the contract was wrong, which is a plan-phase decision, not a build-phase liberty.

### No layout, no config artifact

The package takes whatever shape the tests import from. Configuration is twelve-factor — environment variables are the source, a gitignored `.env` carries local secrets, `python-dotenv` loads it. A `Settings` model is optional; if it is worth the code, it is one normal source stub among the rest, reading `os.environ` in its `from_env()`.

### Structural artifacts keyed to the module

| Module kind | Extra artifact | Born in | Lifecycle |
|---|---|---|---|
| ORM model | Alembic migration (the schema spec) | green | committed in ship; a new cycle adds a new migration, never edits an old one |
| external adapter | replayed cassette (`VCR_RECORD_MODE=none`) | explore | committed; re-recorded only on a real mismatch |

The stub declares the module's surface; green emits whatever that surface implies. A pure domain service with no persistence and no external boundary carries no extra artifact at all.

### stubtest, scoped

stubtest gates the source pair the same way it gates the test pair; the mechanics — `.pyi`-preferred hides drift from pyright, stubtest imports at runtime via `inspect`, it checks structure not return-type accuracy — are in [[software-craft/test-stubs]]. The source-specific discipline is scoping: `stubtest <package>.<mod> tests.<test_mod>` at green/review covers only the modules touched this cycle, because sibling source `.pyi` whose `.py` are not yet built would all false-fail a whole-suite run. The whole-suite `stubtest <package> tests` runs once, at merge, when every `.py` exists.

## Related

- [[software-craft/test-stubs]] — the shared drift mechanics (`.pyi`-preferred; stubtest as the sole detector); the test pair
- [[software-craft/tdd]] — the red/green/refactor cycle that implements these stubs
- [[software-craft/design-patterns]] — patterns the implementation may apply to satisfy a stub cleanly
- [[software-craft/solid]], [[software-craft/object-calisthenics]] — the quality bar the implementation is held to
