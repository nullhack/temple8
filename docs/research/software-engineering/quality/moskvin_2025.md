# Redacting Secrets and PII from VCR.py Cassettes (Moskvin, 2025)

## Citation

Moskvin, I. (2025). "Redacting secrets and PII from VCR.py cassettes." *imoskvin.com*, 30 November 2025. Companion repository: github.com/IllyaMoskvin/vcrpy-secrets.
URL: https://imoskvin.com/blog/redacting-vcrpy-cassettes/

## Method

Practitioner blog article with working code; first-hand.

## Confidence

High — verified primary source; the cited claim ("vcrpy does not scrub for you") is the article's opening premise.

## Key Insight

VCR.py records HTTP exchanges verbatim and does not scrub secrets or PII, so cassettes meant to be committed must be redacted by the developer at record time — and a field-specific redaction (named JSON paths) beats a generic ML scrubber on cost, speed, and reliability.

## Core Findings

1. Cassettes are designed to be committed; secrets and PII are not — VCR.py performs no scrubbing, the developer must.
2. For request-side secrets, the built-in `filter_headers`, `filter_query_parameters`, and `filter_post_data_parameters` suffice.
3. For response-body secrets, three options exist: redact specific fields ("whack-a-mole"), build a generic scrubber (Presidio + detect-secrets), or commit encrypted cassettes.
4. The generic scrubber is over-engineered — ~670 MB of dependencies, a probabilistic ML model, over-aggressive redaction, and it still needs per-field configuration to perform well, which defeats its one-size-fits-all promise.
5. Moskvin lands on redacting specific fields via JSON Pointer (RFC 6901) paths and a `before_record_response` hook — ~86 KB of dependencies, fast, and fully controlled.

## Mechanism

VCR.py exposes `before_record_request` and `before_record_response` hooks that run before the cassette is serialized to disk; redaction applied inside those hooks is guaranteed to reach the committed YAML. The article's `create_redactor` builds a hook that parses the JSON body, applies a JSON Patch (RFC 6902) `replace` at each named pointer path, and re-serializes — so the redaction is structural and deterministic, not pattern-guessed.

## Relevance

Grounds the safety scrub in the record-cassette state: VCR.py will not strip credentials, keys, or PII, so the probe must wire `filter_headers` plus a `before_record_response` hook to do it before the cassette is committed. The article's conclusion — prefer named-field redaction over a generic detector — is the pragmatic default the workflow adopts.

## Related Research

- Turmyshev 2026 (the service-boundary rule that decides what gets captured at all)
