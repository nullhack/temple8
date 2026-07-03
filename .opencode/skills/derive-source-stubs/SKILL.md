---
name: derive-source-stubs
description: "Derive the source stub files (.pyi) from the reviewed tests — every type the tests reference gets a definition."
---

# Derive Source Stubs

1. Load [[software-craft/source-stubs]], [[software-craft/solid]], [[software-craft/object-calisthenics]], [[software-craft/design-patterns]], [[architecture/context-mapping]] — source stub conventions, the quality principles, the pattern catalog, and the inter-context relationship patterns.
2. Read `.cache/<session_id>/journal.md` IF present — it carries escalation findings from build. Adjust the source stubs of the contracts it names; skip if absent (first pass).
3. Read the test .py imports and bodies — every type constructed, method called, and relationship asserted in a body is the specification of the source surface. Emit a matching .pyi signature (with an ellipsis body) for every type the tests reference, wherever the source lives.
4. Define types, relationships, and compositions to satisfy SOLID and Object Calisthenics per [[software-craft/solid]], [[software-craft/object-calisthenics]]. IF a relationship emits a smell at the type surface (a kind-field that will switch, parallel hierarchies, construction scattered across callers, refused bequest) THEN reach for the matching pattern per [[software-craft/design-patterns]] — but KISS/YAGNI first: prefer the simplest structure that removes the smell, and prefer Python idioms (a Protocol, a dataclass, a first-class callable, a generator, a decorator) over GoF ceremony. Do not apply a pattern speculatively; Speculative Generality is the smell that rejects it.
5. IF a relationship bridges two bounded contexts (an external service, an upstream module, a shared data shape) THEN pick the inter-context pattern per [[architecture/context-mapping]] — default to an Anti-Corruption Layer (an adapter that translates the foreign model into ours) for any external dependency; reach for Shared Kernel only for a small value-object set both contexts truly co-own.
6. Do not prescribe layout — no hardcoded module structure. External connector and adapter stubs are not a separate category; they live under the package alongside everything else.
7. Handle config per [[software-craft/secrets-and-config]]: non-secret config in the workspace `.env`; secrets in `~/.secrets/<project>.env` (out-of-workspace), loaded with `dotenv_values()` into a frozen typed Settings, never into `os.environ`. A Settings model is optional and, if warranted, is a normal source stub.
8. IF a value's representation is ambiguous (e.g. a database URL passed as bare string) THEN pin one canonical form once (the `sqlite:///path` URL form) and state it in the stub so every consumer agrees per [[software-craft/source-stubs]].
