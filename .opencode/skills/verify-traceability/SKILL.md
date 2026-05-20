---
name: verify-traceability
description: "Verify example-to-test traceability via beehave check and semantic depth"
---

# Verify Traceability

Available knowledge: [[software-craft/test-design#key-takeaways]], [[requirements/gherkin#key-takeaways]], [[software-craft/test-stubs#concepts]]. `in` artifacts: read all before starting work.

1. Run `beehave status --json` per [[software-craft/test-stubs#concepts]]. IF the feature stage is `ok` with no violations → structural traceability is verified; skip to step 2. IF not `ok` → run `beehave check` per [[software-craft/test-stubs#concepts]] to get the detailed violation list and verify all are resolved.
2. Verify semantic depth per [[software-craft/test-design#concepts]]: for each Example that describes a user-facing command or API invocation, verify the corresponding test exercises the entry point described in the acceptance criterion (e.g., command handler, API endpoint), not just the domain logic in isolation. A test that calls domain methods directly when the AC describes a user-facing command is a semantic alignment gap: it has structural traceability but wrong semantic depth.
