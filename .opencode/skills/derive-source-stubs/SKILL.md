---
name: derive-source-stubs
description: "Derive the source stub files (.pyi) from the reviewed tests — every type the tests reference gets a definition."
---

# Derive Source Stubs

1. Load [[software-craft/source-stubs]] — source stub conventions and the canonical data-shape rule.
2. Read the test .py imports, parameter types, and return types: they are the specification of the source surface. Emit a matching .pyi signature (with an ellipsis body) for every type the tests reference, wherever the source lives.
3. Do not prescribe layout — no hardcoded module structure. External connector and adapter stubs are not a separate category; they live under the package alongside everything else.
4. Handle config by 12-factor: environment variables are the default, with dotenv loading a gitignored `.env` for local secrets. A typed Settings model is optional and, if warranted, is a normal source stub.
5. IF a value's representation is ambiguous (e.g. a database URL passed as bare string) THEN pin one canonical form once (the `sqlite:///path` URL form) and state it in the stub so every consumer agrees per [[software-craft/source-stubs]].
