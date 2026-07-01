---
name: research-provider
description: "Ground one external service in its real behaviour by reading the provider's official docs and determining its access shape, before any probe code is written."
---

# Research Provider

1. Load [[software-craft/external-fixtures]] — the kind-dispatch table (docs-focus, recorder, scrub-fields, default specialist).
2. Identify the exact provider — the specific service and version, not just its kind.
3. Research online: websearch the provider and webfetch its official docs. Read for reference, authentication/credentials scheme, client/SDK, error catalog, rate limits, pagination, idempotency, known gotchas. Do not write probe code until the docs are read.
4. Determine the access shape: endpoint base/URI, protocol, credentials source (a 12-factor environment variable), request/response shape, and both success and failure modes.
5. Recommend at most one advisory specialist for this provider. IF the provider raises auth/secrets/PII concerns THEN recommend security; IF schema/message-shape THEN data; IF user-facing flows THEN ux; IF project-specific semantics THEN domain.
6. Dispatch on the service kind (HTTP API, external database, message queue/event stream, object storage, other) for the docs-focus and default-specialist per [[software-craft/external-fixtures]] — the kind table is the one knob that varies.
7. IF the docs reveal the service behaves differently than the interview assumed THEN signal a mismatch.
