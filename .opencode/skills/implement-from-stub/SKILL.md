---
name: implement-from-stub
description: "Write the minimum production code to turn the target's tests green, implementing the .py from its fixed .pyi."
---

# Implement From Stub

1. Load [[software-craft/source-stubs]], [[software-craft/tdd]], [[software-craft/design-patterns]] — stub sync, the cycle, and implementation patterns.
2. Implement — or, for rework, re-implement — the .py from its .pyi. The .pyi signature is the spec; fill or correct the body to satisfy it and pass the tests. Keep the .py consistent with its sibling .pyi.
3. Emit the structural artifacts the module requires, keyed on what it is: IF an ORM model THEN emit an Alembic migration (the migration is the schema spec); IF an external adapter THEN replay the cassettes captured in explore. Config follows 12-factor — a Settings module, if implemented, reads environment variables via dotenv; it is a normal source module, not a special artifact.
4. IF the body cannot satisfy the .pyi without changing it THEN that is a contract gap — do not edit the stub; escalate at review.
5. Run stubtest scoped to the modules built this cycle — the source module(s) and the test module(s) whose pending marks were removed. The whole-suite stubtest waits until every source .py exists, because unbuilt sibling stubs would false-fail per [[software-craft/source-stubs]], [[software-craft/tdd]].
6. Stubtest imports the runtime module, so every transitive runtime dependency must be installed in the project venv. IF an import is used only for types THEN prefer `if typing.TYPE_CHECKING:` so stubtest does not pull heavy runtime deps for type-only references.
