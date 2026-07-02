---
domain: software-craft
tags: [external-fixtures, cassettes, vcrpy, record-replay, deterministic-tests]
last-updated: 2026-07-01
---

# External Fixtures

## Key Takeaways

- Anchor external-layer tests to REAL captured behaviour, never imagined data — an imagined fixture bakes in the developer's guess and misses the surprises (extra fields, odd types, error shapes) that a real capture exposes before production does.
- Capture once, replay forever: record the real exchange into a committed, replayable artifact; tests and CI replay it offline (HTTP via vcrpy with `record_mode="once"`, CI under `VCR_RECORD_MODE=none`). The capture IS the authoritative external contract.
- The recorder varies by service kind — vcrpy records HTTP only; databases, queues, and object stores each need their own capture strategy. The kind-dispatch table is the one knob set that changes.
- Scrub every cassette twice — for SAFETY (strip credentials, keys, PII) and for DETERMINISM (strip volatile values that churn run-to-run, so replay is stable). vcrpy will not scrub for you (Moskvin, 2025).
- The capture is the truth: never hand-edit a cassette to make a test pass — fix the code, or re-record when reality has genuinely shifted.
- The recorded request binds the implementation: vcrpy matches `method/scheme/host/port/path/query` by default, so every query parameter the probe sent becomes contract — capture the exact request shape in external-contracts.md and reproduce it.

## Concepts

**Why real captures beat imagined data.** Imagining what an external service returns introduces a systematic bias: tests verify against what the developer thinks the service does, not what it does. A real capture anchors the test to observable truth and catches the surprise — the undocumented field, the error that returns 200 not 4xx, the stringly-typed number — at capture time, before it ships. The rule "stub only dependencies that live outside the service: calls to other microservices, third-party APIs, outbound queues — anything that introduces latency, rate limits, or data you don't control" draws the boundary precisely (Turmyshev, 2026); in-project databases and UI are NOT external and are not captured here.

**Capture once, replay forever.** The real exchange is recorded a single time into a committed, replayable artifact, and every later run replays it without touching the service. For HTTP that artifact is a vcrpy cassette: the first run records the request/response pairs, later runs intercept matching requests and return the recorded responses, and CI runs with `VCR_RECORD_MODE=none` so a missing or drifting cassette fails loudly instead of silently re-recording (vcrpy, 8.0). The cassette is the authoritative external contract — the thing tests assert against and the reference the build-time adapter implementation honours. The recording vehicle is a throwaway probe script under `.cache/explore/` (gitignored, never imported); the cassette it produces is committed at `tests/cassettes/<service>/`.

**The recorder varies by kind.** vcrpy intercepts HTTP client libraries; it has nothing to say about a database cursor, a queue consumer, or an object store. Each kind needs its own capture strategy, and the strategy is the one knob set that genuinely changes per kind — the kind-dispatch table below is the artifact the explore skills load. The pattern is constant (capture the real exchange, replay it offline); only the recorder, the scrub-fields, and the docs-focus move.

**Scrub for safety and determinism.** Two independent concerns apply to every cassette. Safety: credentials, API keys, and PII must never reach the committed file — for HTTP, `filter_headers=["authorization"]` strips the request auth header and `filter_post_data_parameters` / `filter_query_parameters` strip secrets from the body and query. Determinism: anything that changes run-to-run (a `date`, a `cf-ray`, a row timestamp, a queue offset, a storage `ETag`) must be stripped or normalised, or replay will churn and the cassette will not diff cleanly. MVP Factory (2026) is blunt: external state is the single largest source of replay non-determinism, and you want it gone. vcrpy does neither scrub for you (Moskvin, 2025) — `before_record_response` (and `before_record_request`) are the hooks where you do it.

**The capture is the truth.** A cassette is a recording of reality, not a desired outcome. If an adapter test fails against a captured cassette, the code is wrong (or the contract drifted) — never edit the cassette to make the test pass. When reality itself has shifted — the service changed its response, the schema evolved — re-record (our flow signals this as a mismatch and re-enters discovery), and the old capture is replaced, not patched. Fixing the code instead of the fixture is what keeps the test honest.

## Content

### Why real captures beat imagined data

The developer who writes a fixture from memory writes what they remember, and memory smooths over exactly the details that bite in production — the extra nested object, the field the API returns as a string when the docs say integer, the error the service represents with a 200 and a `result: "error"` body rather than a 4xx. A real capture surfaces those at capture time, when they are cheap. The boundary is "anything that introduces latency, rate limits, or data you don't control" (Turmyshev, 2026): third-party APIs and SaaS, external managed databases, message queues you don't own, object stores you call. In-project databases and the UI are not external — they are designed here, specified by tests and migrations, and have no cassette.

### Capture once, replay forever

The model is record-once-replay-forever. vcrpy's default `record_mode="once"` records when the cassette is absent and replays when it is present; CI overrides to `record_mode="none"` so the build fails on a missing or unmatched cassette rather than silently re-recording (vcrpy, 8.0). The cassette is committed at `tests/cassettes/<service>/` and is the authoritative external contract: the adapter test in build replays it, and the adapter implementation is what makes a real call matching the recorded request. The recording is done by a throwaway probe script under `.cache/explore/<service>/` (gitignored, never imported by the package or the tests) that runs once with real credentials the user supplies in `~/.secrets/<project>.env` per [[software-craft/secrets-and-config]] (loaded with `dotenv_values()`, never into `os.environ`), and the cassette it leaves behind is what everyone after consumes. Credentials live in the environment and the probe, never in the cassette — the scrub step exists to guarantee that.

vcrpy matches a recorded request field-for-field on `method/scheme/host/port/path/query` by default (vcrpy, 8.0), and `query` is in that set — so an incidental parameter the probe sent (an API default like `format=json`, a locale like `language=en`) becomes contract the implementation must reproduce, or replay fails on a no-match. This is why the exact request shape is captured into `external-contracts.md` at record time, and why the build-time adapter conforms to the cassette rather than the reverse: the cassette is the authority both the adapter test and the e2e replay, so a request the implementation invents that the probe never sent will not match. A service with several endpoints records ONE cassette holding every interaction, not one cassette per endpoint, so an e2e that chains several calls (geocode then forecast; lookup then detail) replays from a single `vcr.use_cassette`.

### The recorder varies by kind

vcrpy is HTTP-only. Each other kind has its own recorder; the pattern (capture the real exchange, replay offline) is constant.

| Kind | docs-focus | recorder | scrub-fields | default specialist |
|---|---|---|---|---|
| HTTP API (REST/GraphQL) | OpenAPI spec / official docs; auth scheme; error catalog | vcrpy (`record_mode="once"`) over the real client (httpx/requests) | `filter_headers=["authorization"]`; `before_record_response` strips volatile headers (`date`, `age`, `server`, `last-modified`, `content-encoding`, `transfer-encoding`, `vary`, `cf-ray`, `report-to`, `nel`); `decode_compressed_response=True`; scrub PII from bodies | integration-engineer |
| External database | schema docs; SQL dialect; connection parameters | record real queries + result-sets as a fixture (VCR-style driver interception, e.g. `pytest-adbc-replay`) or a committed fixture dump seeded into a test DB | connection string + password; volatile row values (timestamps, sequences, generated IDs) | data-architect |
| Message queue / event stream | message schema (registry); broker protocol; partition/offset model | capture real messages (key, headers, payload) with the schema version pinned; replay via an embedded broker or a fake consumer (MVP Factory, 2026; Keploy) | broker credentials; offsets, timestamps, producer IDs that churn | data-architect |
| Object storage | storage API; object model; auth (access keys / assumed roles) | capture real object metadata + a representative blob; replay via a mock client | access keys / tokens; volatile metadata (`ETag`, `last-modified`, `version-id`) | integration-engineer |
| Other | research-determined | capture the real exchange in its wire format | research-determined (credentials + volatile fields) | research-determined |

### Scrub for safety and determinism

Two independent scrubs apply to every cassette, and vcrpy performs neither (Moskvin, 2025) — you wire them through its hooks.

**Safety** — nothing that unlocks the real service or identifies a real person reaches the commit. For HTTP: `filter_headers=["authorization"]` drops the request auth header; `filter_post_data_parameters` and `filter_query_parameters` redact secrets embedded in the body or query; `before_record_response` is where body PII (emails, IDs, names) is redacted, either by explicit JSON path or via a detector (Moskvin's `vcrpy-secrets` demonstrates both manual-path and Presidio/detect-secrets approaches). For non-HTTP kinds the credentials move (connection strings, broker tokens, access keys) but the rule does not.

**Determinism** — anything that changes between recordings is stripped or normalised, so a replayed test is stable and a cassette diff in a pull request means the service changed, not that time passed. For HTTP that is the volatile-header list above; `decode_compressed_response=True` decompresses gzip/deflate bodies before recording (so the cassette is readable text, not an opaque blob) and before any custom response filtering (vcrpy, 8.0) — with the caveat that you avoid it when decompression is itself the behaviour under test. For non-HTTP kinds the volatile values move (row timestamps and sequences, queue offsets and producer IDs, storage `ETag`s and `version-id`s) but the principle does not: external state is the largest source of replay non-determinism, and the scrub exists to eliminate it (MVP Factory, 2026).

### The capture is the truth

A cassette records what the service actually did. If the adapter test fails against it, the implementation is wrong or the contract drifted — never hand-edit the cassette to make the test pass, because the moment you do, the test is asserting against a wish, not reality. When the service itself changes — a new required field, a restructured error — the correct response is to re-record (our flow signals a mismatch and re-enters discovery), replacing the stale capture entirely. Version control holds the history of what the cassette used to be; the working tree holds only what the service does now.

## Related

- [[software-craft/test-design]] — the adapter test that replays a cassette and asserts against the captured shapes
- [[software-craft/source-stubs]] — the adapter implementation, authored from its stub to match the recorded request and honour the captured response
- [[software-craft/secrets-and-config]] — the credentials the probe runs with live out-of-workspace; the scrub here is the commit guard, the lifecycle guard lives there
