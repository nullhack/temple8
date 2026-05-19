---
domain: requirements
tags: [gherkin, acceptance-criteria, specification, examples, bdd, scenario-outline, hypothesis]
last-updated: 2026-05-19
---

# Gherkin Specification Format

## Key Takeaways

- Write declarative Examples that describe behaviour, not UI steps; use `Example:` not `Scenario:` for single-case examples (BDD, North, 2006).
- Use `Scenario Outline:` with `<placeholder>` syntax and an `Examples:` table when the same behavioural outcome must be verified across 3+ input/output value combinations.
- Feature, Rule, and Example/Scenario Outline titles must be 2–6 words and unique within the feature file — pytest-beehave uses title-based mapping (title → `test_<slug>` function name) for traceability. Titles must contain ONLY Unicode letters, digits, and spaces — no hyphens, periods, underscores, or special characters (they break slug generation).
- Quoted strings (`"value"`) and bare numbers (`42`, `-3`) in steps are extracted by beehave as literals and verified present in test function bodies via `beehave check`. Every literal carries domain meaning in the test — use literals that identify entities, boundaries, configurations, or error cases the reader needs to see.
- `<placeholder>` names in steps become Python function parameters in generated test stubs. Names must be valid Python identifiers (not keywords, not builtins). Every column in an Examples table must be referenced in the scenario steps — columns not referenced in steps are test data, not specification. If the expected outcome varies independently across examples, an output column is appropriate. If it is a deterministic function of inputs, express the relationship in the `Then` step (e.g., `Then the result is the minimum of <a> and <b>`) rather than adding a computed column.
- Bug Examples use `@bug` and require both a specific feature test and a Hypothesis property test.
- After criteria commit, Examples are frozen; changes require `@deprecated` on the old Example and a new Example with a new unique title.
- Two Examples with the same `Then` outcome but different input values test the same behaviour; partition by behaviour outcome, not by input value (Wynne, 2015; Adzic, 2011).

## Concepts

**Declarative vs Imperative Gherkin**: Declarative Examples describe behaviour, not UI steps (BDD, North, 2006). "Given a registered user Bob / When Bob logs in / Then Bob sees a personalized welcome" is correct. "Given I type 'bob' in the username field / When I click the Login button / Then I see 'Welcome, Bob'" is imperative and wrong. Declarative Examples express what the user observes, not how the system implements it.

**Example vs Scenario Outline**: Use `Example:` for single-case examples. Use `Scenario Outline:` when the same behavioural outcome must be verified across 3+ different input/output value combinations. Scenario Outline uses `<placeholder>` syntax in Given/When/Then steps and an `Examples:` table with concrete data rows. This avoids repeating identical step structures with different values.

**Title Length and Character Constraint**: Feature, Rule, and Example/Scenario Outline titles must be 2–6 words and unique within the feature file. Titles must contain ONLY Unicode letters, digits, and spaces — no hyphens (`-`), periods (`.`), underscores (`_`), or other special characters. The title is slugified to produce the test function name (`test_<slug>`), and special characters either break slug generation or produce ambiguous identifiers. Too short produces ambiguous identifiers (e.g. `test_stuff`), too long produces unwieldy ones. Count words by splitting on whitespace.

**Placeholder Syntax**: `<variable_name>` in Given/When/Then steps. Beehave extracts these and generates Hypothesis `@given(var_name=strategy)` decorators in test stubs. Placeholder names must be valid Python identifiers, not keywords (`for`, `class`), and not builtins (`list`, `str`). When used with Scenario Outline, the Examples table column headers must match the placeholder names.

**Literal Extraction**: Quoted strings (`"value"`, `'value'`) and bare numbers (`42`, `-3`, `3.14`) in Given/When/Then steps are extracted by beehave as literals. `beehave check` verifies these literals appear in the test function body, providing structural traceability. Per Spec Value Fidelity ([[software-craft/test-design#concepts]]), every literal in a step must carry domain meaning — it should identify an entity, boundary, configuration, or error case that matters to the reader.

**Hypothesis Integration**: Scenario Outline generates `@given` decorated stubs with inferred Hypothesis strategies (`st.integers()`, `st.floats()`, `st.booleans()`, `st.text()`) plus `@example` decorators for each Examples table row. Plain Examples generate bare function stubs. For tests hitting external services, use `@settings(max_examples=N)` to control load. For unit/domain tests, Hypothesis defaults are fine.

**Meaningful Examples Tables**. Every column in an Examples table must be referenced in at least one step — unreferenced columns are test data, not specification. Output columns (e.g., `<expected>`) are appropriate when the expected value varies independently across rows (e.g., different tax rates per country, different error codes per input). When the expected outcome is a deterministic function of inputs, do not add an output column; express the relationship in the `Then` step. Per Spec Value Fidelity ([[software-craft/test-design#concepts]]), every value in the table exists to be used meaningfully in the test.

**Example Format and Title-Based Mapping**: Each Example uses the `Example:` keyword (not `Scenario:`), includes `Given/When/Then` in plain English. pytest-beehave maps Examples to test functions by title: the function name is `test_<example_title_slug>`. Titles must be unique within the feature file. Descriptive titles serve as the traceability link between feature specification and test code — no `@id` tags are needed.

**Single Observable Outcome per Then**: `Then` must be a single, observable, measurable outcome. No "and" combining multiple behaviours in one `Then`. Split into separate Examples instead. Observable means observable by the end user, not by a test harness.

**Frozen Examples**: After criteria commit, Examples are frozen. Changes require `@deprecated` on the old Example and a new Example with a new unique title. No editing or deleting committed Examples. This prevents scope creep and maintains traceability from test to acceptance criterion.

**Bug Examples**: When a defect is reported, add an `@bug` Example. Implement both a specific test and a Hypothesis property test covering the whole class of inputs. Both are required.

**Behavioral Distinctness**: Two Examples are behavior-distinct only when they produce different `Then` outcomes (Wynne, 2015; Adzic, 2011). Partitioning by behaviour outcome rather than by input value avoids the combinatorial explosion of value-distinct testing. Two Examples with the same `Then` but different input values test the same behaviour — keep one, discard the duplicates. For action and behavioural rules, each distinct outcome gets one representative Example. For structural (invariant) rules, one representative Example suffices because the invariant holds across all inputs; full coverage is deferred to a Hypothesis property test per [[software-craft/test-design#concepts]].

**Scenario Outline and Behavioral Distinctness**: Scenario Outline is an exception to the "same Then = duplicate" rule. When the same behavioural outcome should hold across multiple concrete value combinations (e.g. "order rejected for invalid quantity" for quantities -1, 0, and 99999999), use Scenario Outline to express the parameterized variation. Each Examples table row is a distinct input, but they all verify the same behavioural rule — the parameterization is the point.

## Content

### Declarative vs Imperative

| Imperative (wrong) | Declarative (correct) |
|---|---|
| Given I type "bob" in the username field | Given a registered user Bob |
| When I click the Login button | When Bob logs in |
| Then I see "Welcome, Bob" on the dashboard | Then Bob sees a personalized welcome |

### Title Conventions

- Feature, Rule, and Example/Scenario Outline titles must be 2–6 words
- Titles must be unique within the feature file
- Titles must contain ONLY Unicode letters, digits, and spaces — no hyphens, periods, underscores, or special characters
- Title becomes the test function name: `test_<example_title_slug>`
- Titles should be descriptive enough to serve as the test identifier
- No `@id` tags — the title is the traceability link
- After criteria commit, changing a title breaks the traceability chain — deprecate and create a new Example instead
- Word count rationale: too short = ambiguous test name, too long = unwieldy identifier, not searchable

### When to Use Scenario Outline vs Example

| Situation | Use | Why |
|---|---|---|
| Single input/output case | `Example:` | No parameterization needed |
| 3+ value variants of same outcome | `Scenario Outline:` | Avoids repeating identical step structures |
| 2 value variants | `Example:` × 2 | Not enough variants to justify outline |
| Fuzzing an invariant across many values | `Scenario Outline:` | Hypothesis `@given` + `@example` integration |

### Scenario Outline Format

```gherkin
Scenario Outline: <2-6 word title>
  Given a <product> in the cart with quantity <qty>
  When the customer submits the order
  Then the order total reflects <product> at quantity <qty>

  Examples:
    | product | qty |
    | Widget  | 1   |
    | Widget  | 5   |
    | Gadget  | 3   |
```

Rules:
- Use `Scenario Outline:` keyword (not `Example:`)
- `<placeholder>` names must match Examples table column headers exactly
- At least 3 data rows in the Examples table
- Placeholder names must be valid Python identifiers (not keywords, not builtins)
- Same behavioural outcome (`Then`) across all rows

### Literal Syntax in Steps

Literals in Given/When/Then steps are extracted and verified:

| Syntax | Type | Example in Step | Verified In Test Body |
|--------|------|-----------------|----------------------|
| `"quoted string"` | str | `Then the output contains "temple8"` | `"temple8"` |
| `'single quoted'` | str | `Then the error is 'not found'` | `"not found"` |
| bare integer | int | `Then the process exits with code 2` | `2` |
| bare negative | int | `Then the balance is -5` | `-5` |
| bare float | float | `Then the rate is 3.14` | `3.14` |

`beehave check` verifies every literal from the step appears in the test function body. Tests must use the exact literal values from the spec — no paraphrasing.

### Hypothesis Strategy Inference

When Scenario Outline has an Examples table, beehave infers Hypothesis strategies from column values:

| Column Values | Inferred Strategy |
|---------------|-------------------|
| All integers | `st.integers()` |
| All floats | `st.floats()` |
| All booleans (true/false) | `st.booleans()` |
| Mixed or text | `st.text()` |

Override by defining a strategy variable in the test file with the same name as the placeholder. For external service tests, add `@settings(max_examples=N)` to control load.

### Example Format Rules

- `Example:` keyword for single cases (not `Scenario:`)
- `Scenario Outline:` keyword for parameterized cases with `<placeholder>` syntax
- `Given/When/Then` in plain English
- `Then` must be a single, observable, measurable outcome: no "and"
- Observable means observable by the end user, not by a test harness
- Declarative, not imperative: describe behaviour, not UI steps
- Each Example/Scenario Outline must be observably distinct from every other
- Title must be unique within the feature file and 2–6 words

### Feature Title and Filename Convention

pytest-beehave derives the test directory name from the Feature title (slugified). The feature filename stem MUST match the Feature title slug. For example: Feature title "CLI Entrypoint" → slug `cli_entrypoint` → filename `cli_entrypoint.feature` → test directory `tests/features/cli_entrypoint/`. A mismatch between title slug and filename stem causes `misplaced-test` errors.

### Frozen Examples Rule

After criteria commit, Examples are frozen. Any change to committed Examples requires:
1. `@deprecated` on the old Example
2. A new Example with a new unique title

No editing or deleting committed Examples.

### Bug Example Format

When a defect is reported:

```gherkin
@bug
Example: <what the bug is>
  Given <conditions that trigger the bug>
  When <action>
  Then <correct behaviour>
```

Implement both:
1. The specific test in `tests/features/<feature_slug>/`
2. A Hypothesis property test covering the whole class of inputs

### Common Mistakes

- "Then: It works correctly": not measurable
- "Then: The system updates the database and sends an email": split into two Examples
- Multiple behaviours in one Example: split them
- Examples that test implementation details ("Then: the Strategy pattern is used")
- Imperative UI steps instead of declarative behaviour descriptions
- Two Examples with the same `Then` but different input values: duplicate behaviour coverage per [[requirements/gherkin#concepts]]
- Duplicate Example titles within a feature file: breaks pytest-beehave mapping
- Titles shorter than 2 words or longer than 6 words: produces ambiguous or unwieldy test identifiers
- Using Scenario Outline for single-value or two-value cases: over-engineering, use plain Example instead
- Using `Scenario:` keyword: use `Example:` for single cases or `Scenario Outline:` for parameterized cases
- Placeholder names that are Python keywords or builtins: beehave rejects these at parse time
- Paraphrasing literal values in test code instead of using exact values from the spec: fails `beehave check`
- Titles containing hyphens, periods, underscores, or special characters: only Unicode letters, digits, and spaces are allowed
- Adding literals to steps that lack domain meaning: every literal must identify an entity, boundary, configuration, or error case that justifies its presence in both the specification and the test

### Feature File Path Convention

Feature files are located at `docs/features/<file>.feature`. The flow works on one feature at a time, so `<file>.feature` refers to a single feature file, not a glob pattern.

### Test Path and Traceability Conventions

Test path conventions (`tests/features/<feature_slug>/`), the feature-test vs unit-test boundary, and two-dimensional traceability (structural + semantic) are defined in [[software-craft/test-design]].

## Related

- [[requirements/invest]]: INVEST criteria for Rule blocks
- [[requirements/moscow]]: prioritizing Examples as Must/Should/Could
- [[requirements/decomposition]]: splitting Rules with too many Examples
- [[requirements/pre-mortem]]: finding hidden failure modes in rules
- [[software-craft/test-design]]: property-based testing for invariant rules
- [[software-craft/test-stubs]]: how beehave generates test stubs from feature files
- [[software-craft/external-fixtures]]: real data fixtures for external adapter mocking
