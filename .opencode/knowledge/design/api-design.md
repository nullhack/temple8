---
domain: design
tags: [api-design, rest, http, problem-details, rfc-9457, pagination, idempotency]
last-updated: 2026-07-02
---

# API Design

## Key Takeaways

- An HTTP API is a user interface for developers; the same interaction-design rules apply — predictable, legible, with errors that help the consumer recover.
- Model **resources** (nouns), not procedure calls (verbs); the standard methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) carry the verb, and the URL names the resource (`/orders/{id}`, not `/getOrder`).
- Use **HTTP status codes** semantically and consistently: `2xx` success, `3xx` redirection, `4xx` the client made a mistake, `5xx` the server did. Do not overload `200` with an error body.
- Errors use **RFC 9457 Problem Details** — `application/problem+json` with `type` (a URI), `title`, `status`, `detail`, `instance`, plus optional extensions (`errors`, `code`, `traceId`). RFC 9457 (2023) supersedes RFC 7807 (2016); it is the current standard (Dalal, 2023).
- **Paginate** collections from the start (cursor pagination preferred over offset for stability under insertion); **version** the API deliberately (URL path or header); make safe-to-repeat operations **idempotent**.
- The API contract is documented in an **OpenAPI** description; the problem-detail schemas appear there so consumers know exactly what each endpoint can return.

## Concepts

**Resources, not procedures.** REST models the domain as resources identified by URIs, acted on by the standard HTTP methods. A URL names a thing (`/users/42/orders`); the method names the action (`POST` to create, `GET` to read). The benefit is predictability: a consumer who knows the resource model can guess the URLs and methods, and the contract is uniform across the API rather than bespoke per endpoint (Fielding, 2000).

**Status codes carry outcome.** The status code is the API's exit-code equivalent — the consumer's fastest, most reliable branch. `200`/`201`/`204` for success (created, no-content); `400` for a malformed request, `401` unauthenticated, `403` forbidden, `404` absent, `409` conflict, `422` semantically invalid; `5xx` for server-side failure. Returning `200` with `{"error": "..."}` in the body defeats the consumer's status-based branching and is a common API smell.

**Problem Details (RFC 9457).** Rather than invent a per-API error format, RFC 9457 defines a standard `application/problem+json` document: `type` (a URI identifying the problem type — the consumer's primary key, does not need to resolve), `title` (short summary, stable per type), `status` (the HTTP status), `detail` (this occurrence's specifics), `instance` (the specific URI occurrence), plus extensions like `errors` (a validation array with JSON Pointer locations), `code` (an API-specific code), or `traceId`. It is the current IETF standard, superseding RFC 7807 (Dalal, 2023).

**Pagination, versioning, idempotency.** Collections too large to return whole are paginated; cursor pagination (a token pointing to the next page) is more stable than offset/limit because it does not skip or duplicate when items are inserted between calls. Versioning is a deliberate choice — a URL path segment (`/v1/`) is the most visible; a header is cleaner but less discoverable. Operations the consumer might retry (charging, sending) are made idempotent via an idempotency key so a duplicate request does not double the effect.

**OpenAPI is the contract.** The API is described in an OpenAPI document: every path, method, request/response schema, and the problem-detail responses each endpoint can return. The schema for `application/problem+json` is defined once and `$ref`-ed where it applies. The document is the source both consumers and the test suite consult.

## Content

### Status code semantics (the load-bearing set)

| Code | Meaning | Use |
|---|---|---|
| 200 OK | success with a body | standard read/update response |
| 201 Created | a new resource was created | `POST` that creates |
| 204 No Content | success, nothing to return | `DELETE`, a `PUT` returning no body |
| 400 Bad Request | malformed syntax | the consumer's request is unparseable |
| 401 Unauthorized | no/failed authentication | auth missing or invalid |
| 403 Forbidden | authenticated but not allowed | auth fine, authorization fails |
| 404 Not Found | the resource does not exist | (or 401 if you hide existence) |
| 409 Conflict | state conflict | duplicate, stale version |
| 422 Unprocessable Entity | semantic violation | well-formed but invalid |
| 5xx | the server failed | never the consumer's fault |

### RFC 9457 problem+json (the error body)

```
HTTP/1.1 404 Not Found
Content-Type: application/problem+json

{
  "type": "https://example.com/errors/user-not-found",
  "title": "User not found",
  "status": 404,
  "detail": "User 42 does not exist.",
  "instance": "/users/42"
}
```

`type` is the consumer's primary identifier (a URI, stable per problem type); `title` is the same for every occurrence of that type; `detail` is specific to this occurrence. Extensions (`errors` with JSON Pointers for validation, `code`, `traceId`) carry more without breaking the base shape (Dalal, 2023).

### Pagination shapes

| Style | Shape | When |
|---|---|---|
| cursor | `?cursor=<token>&limit=N` + a `next_cursor` in the response | the default — stable under insertion, preferred at scale |
| offset/limit | `?offset=N&limit=M` | simple collections stable enough that skip/duplicate is acceptable |

## Related

- [[design/interaction-design]] — predictability, errors-that-recover, and consistency apply to the API surface
- [[design/cli-design]] — a CLI wrapping an API composes the two design surfaces
- [[software-craft/external-fixtures]] — the cassette captures a real API exchange; this knowledge designs the contract the adapter implements
