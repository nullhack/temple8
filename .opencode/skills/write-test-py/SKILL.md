---
name: write-test-py
description: "Transform the reviewed test stubs into executable test bodies, with the code-quality gate applied here."
---

# Write Test Py

1. Load [[software-craft/solid]], [[software-craft/object-calisthenics]], [[software-craft/smell-catalogue]], [[software-craft/test-design]] — the quality criteria and body patterns.
2. Read `.cache/<session_id>/journal.md` IF present — it carries escalation findings from build. Edit the bodies of the contracts it names to match the reworked stubs; skip if absent (first pass).
3. Write the test bodies — no docstrings, no comments; the body is the spec. Bodies define how entities relate, compose, and collaborate: wire classes, data, and objects following best practices.
4. Apply the code-quality gate here: SOLID, DRY, KISS, YAGNI, Object Calisthenics per [[software-craft/solid]], [[software-craft/object-calisthenics]]. IF a smell is present THEN reject it per [[software-craft/smell-catalogue]].
5. Mark each test with the pending marker; the conftest hook skips pending tests so the suite stays green-with-skips until source is built.
6. Defer the system-under-test import into each test body so an unbuilt module collects cleanly and its pending tests skip rather than error at collection. Keep third-party and test-only imports at module top.
7. Keep the .py's module-level names and method signatures in exact agreement with its .pyi — stubtest checks the pair strictly.
8. Run the dev ruff check (`ruff check .`) on the authored test files; fix every violation so build receives bug-clean tests. Restructure lint (`SIM`, `RUF`) and `ruff format` are merge-time per [[software-craft/docstring-lifecycle]] — do not format here.
9. IF reworking an existing contract THEN edit the body to match the changed .pyi and re-apply the pending marker to the affected tests so they skip until build re-selects them.
