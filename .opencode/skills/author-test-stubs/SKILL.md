---
name: author-test-stubs
description: "Author test stub files (.pyi) whose signatures express the domain, relationships, and compositions, as the first contract surface."
---

# Author Test Stubs

1. Load [[software-craft/test-stubs]], [[software-craft/test-design]] — stub conventions and what-to-test patterns.
2. Read `.cache/<session_id>/journal.md` (always present — bootstrapped at plan entry by `model-data-schema`) and `.cache/<session_id>/interview-notes.md`. Two rework trigger sources feed the backlog: (a) IF the journal carries escalation findings from build (contract gaps) THEN rework the contracts it names first; (b) IF the interview notes flag findings that MODIFY an existing block (`rework — modifies existing <block>` from `interview-building-blocks`) THEN rework those contracts' `.pyi` signatures to match the changed requirement. Either source marks the affected contracts as rework; `write-test-py` re-applies the `@pytest.mark.pending` marker to the affected tests so `select-build-target` pulls them from the backlog. A finding with no rework flag is new work — author a fresh stub.
3. Author integration and E2E test stubs only — no unit-test stubs. Author in build layer order so external-boundary contracts precede adapter, then internal-data, then internal contracts.
4. Express the requirement in class and method signatures with type annotations: entity relationships, compositions, and the behaviour each test asserts. External-layer stubs assert against the captured cassettes — real shapes, not guesses.
5. External-boundary replay rule. An HTTP (httpx) adapter test MUST use `with vcr.use_cassette(cassette_path(NAME)):` as a context manager around the adapter call — in-process replay against the captured exchange per [[software-craft/external-fixtures]]. `pytester` is reserved for CLI subprocess tests ONLY; never use it for vcrpy cassette replay (it spawns a child pytest process, breaks collection, and hides the cassette contract from the type surface). Exception: a library-boundary adapter vcrpy cannot intercept (e.g. ddgs/primp) uses `monkeypatch` on the adapter's transport, not `pytester`. The wrong-vs-right pattern and the kind-dispatch table are in [[software-craft/external-fixtures]].
6. Make each stub a COMPLETE module surface: declare every module-level name the .py will expose (constants, fixtures, helper functions) plus the test class and its method signatures. The test .pyi must mirror the .py's full module surface per [[software-craft/test-stubs]].
7. Import stdlib typing only. IF a third-party library is referenced THEN do not import it in the stub — third-party imports trip mypy import-untyped, and stubtest does not require them.
8. Run ruff on the authored .pyi (`ruff check`); the PYI rules lint stubs. Fix every violation.
9. IF authoring surfaces an important new domain concept THEN add it to the glossary.
10. IF reworking an existing contract THEN change signatures here first; the body is re-marked at write-test-py.
