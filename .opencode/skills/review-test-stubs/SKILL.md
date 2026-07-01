---
name: review-test-stubs
description: "Review the test stubs for coverage, scope, and happy-path completeness against the interview — not for code quality."
---

# Review Test Stubs

1. Load [[software-craft/code-review]], [[requirements/feature-discovery]] — review method and gap analysis.
2. Treat this review as coverage and scope against requirements, not code quality — quality is gated later on the bodies.
3. Check consistency: every stub maps to an interview requirement and uses the glossary's ubiquitous language; external-layer stubs match the captured cassettes.
4. Check scope: integration and E2E only; IF a unit test leaked in THEN reject it.
5. Check happy-path completeness: the stub set, once implemented, would exercise the full happy paths of every identified feature. IF a feature or quality attribute maps to no stub THEN flag the gap per [[requirements/feature-discovery]].
