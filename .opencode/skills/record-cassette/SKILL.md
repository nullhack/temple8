---
name: record-cassette
description: "Execute the probe against the real service and record the exchange into a committed cassette, scrubbed of secrets and volatility."
---

# Record Cassette

1. Load [[software-craft/external-fixtures]] — the recorder and scrub-field kind-dispatch table.
2. Execute the probe script and capture the real request/response with the transport-appropriate recorder.
3. IF HTTP THEN record with vcrpy and `decode_compressed_response=True` so gzip/br bodies are stored decoded, not opaque blobs per [[software-craft/external-fixtures]]. Dispatch the recorder on the service kind (HTTP API, external database, message queue, object storage, other) — the recorder is the one knob that varies per kind.
4. Scrub the cassette to deterministic and safe-to-commit. IF HTTP THEN `filter_headers` strips `Authorization` and `before_record_response` strips volatile headers — `date`, `age`, `server`, `last-modified`, `content-encoding`, `transfer-encoding`, `vary`, `cf-ray`, `report-to`, `nel`. Dispatch the scrub-field list on the service kind.
5. IF a cassette has an opaque/churning body or a leaked secret THEN it fails the external contract — re-scrub before commit.
6. Append to the shared external-contracts notes the confirmed endpoint base, auth scheme, gotchas, AND the exact request shape captured per interaction (method, path, query parameters, required headers). The cassette is the contract and vcr matches on the request, so the implementer must reproduce this exact shape — record it explicitly, do not leave it implicit in the cassette.
7. IF the live exchange contradicts the research or the interview THEN signal a mismatch.
