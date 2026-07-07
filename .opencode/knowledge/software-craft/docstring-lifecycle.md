---
domain: software-craft
tags: [docstrings, lint, lifecycle, token-economy, format]
last-updated: 2026-07-02
---

# Docstring and Lint Lifecycle

## Key Takeaways

- Docstrings are human-language duplicates of code; during active development they cost tokens on every read and drift on every edit, so source `.py` is kept **naked** across red/green/refactor/review/ship and regenerated at deliver/merge from the stable code.
- Tests and stubs carry no docstrings, ever — tests ARE the spec (their names and bodies document behaviour) and PEP 484 stubs are signature-only (a docstring in a `.pyi` is forbidden — PYI021).
- Models add docstrings by training instinct; instruction alone does not suppress it. The `select` state enforces nakedness **mechanically** by running `scripts/strip_docstrings.py` over the target source `.py` at cycle entry, removing any docstring carried over from the last merge — the script is the backstop, not the prompt.
- Lint splits the same way: **bug-catchers run throughout** (the dev `ruff` select); restructuring lint (`SIM`, `RUF`) and `ruff format` run **at merge** via `task lint-merge`, so a dev edit is not churned by readability reordering mid-cycle.
- ruff itself cannot ban or remove docstrings (no rule flags a docstring's *presence* in `.py`; `PYI021` is `.pyi`-only), which is why the strip is a script and the docstring ban is not encoded as a ruff rule.

## Concepts

**Naked during dev, dressed at merge.** A docstring restates the code beneath it in prose. While the code is being written and rewritten — the whole of red/green/refactor/review — that prose is a stale duplicate dragging on every read (more tokens) and every edit (a code change forces a duplicate change, or the duplicate drifts). The phased answer is to keep source `.py` docstring-free for the entire build cycle and generate the docstrings once, at deliver/merge, from code that has stabilised. The duplication tax is paid once per cycle at merge, not continuously through dev. Tests and stubs are excluded: a test's documentation IS its body (editing the body edits the spec), and a stub is a PEP 484 signature (`...` only; a docstring there is a PYI021 violation).

**The instinct is real; the script is the backstop.** Models are trained on docstring-rich code and reach for them by reflex — strong enough that an instruction ("do not write docstrings during build") leaks. The mechanical defence runs at `select`: the strip script walks the target `.py`'s AST, finds every docstring node, and deletes its line range, surgically, without reformatting the surrounding code. Whatever the instinct slipped in is gone before red runs. The strip runs at cycle entry, not on every commit, because the source `.py` is re-read and re-edited through the cycle and a single entry-point strip keeps it naked for the duration.

**Lint splits dev from merge.** The same churn argument applies to lint that restructures for readability — `SIM` collapsing a nested `with`, `ruff format` reordering imports and whitespace. Mid-cycle, a format pass inflates the diff with non-semantic changes and fights the edit in progress. The dev `ruff` select is bug-catchers only (`A`, `ASYNC`, `B`, `C9`, `DTZ`, `ERA`, `F`, `G`, `LOG`, `PYI`, `S`) — `PYI` stays because it scopes to `.pyi` and enforces the naked-stub rule without touching `.py`. The restructure set (`SIM`, `RUF`) plus `ruff format` move to `task lint-merge`, run by `merge-to-dev` after the docstrings are generated, so dev stays quiet and the merged result is clean.

**Why ruff cannot do this.** ruff's `D`/pydocstyle rules either *require* docstrings (D100–D107) or police their *style* (D200+); none flags a docstring's *presence* as a violation, and ruff has no autofix that strips docstrings from `.py` (the project verified this at the start — `PYI021` strips them only in `.pyi`). So "no docstrings during dev" is not expressible as a ruff rule; the AST strip script is the substitute, and the `D` rules are not used at all (the merge step *generates* docstrings; it does not *enforce* their presence via lint).

## Content

### The lifecycle

| Phase | Source `.py` docstrings | Tests / stubs | Lint |
|---|---|---|---|
| plan (author/review/write/derive/simulate) | n/a (no `.py` yet) | naked (permanent) | dev select, `.pyi` via `PYI` |
| build (select/red/green/refactor/review/ship) | **naked** — `select` strips the target | naked | dev select only |
| deliver (merge) | **generated** for the shipped surface | naked | `task lint-merge` (add `SIM`, `RUF`, `format`) |

### The strip mechanic

`scripts/strip_docstrings.py <file>` parses the file, collects the `[lineno, end_lineno]` of every module/class/function docstring, and deletes those line ranges from the bottom up (so earlier line numbers stay valid). Every other line — formatting, comments, blanks — is preserved; the script does not reformat. It assumes a body is not docstring-only (true for real rework `.py`); it runs at `select` over the chosen target source `.py`, so red/green/refactor operate on naked code for the whole cycle.

### The merge generate step

`merge-to-dev`, after the squash-merge, regenerates docstrings for the public surface of every contract shipped this cycle (modules, classes, public functions and methods). The prose is faithful to the code, never a mechanical restatement of the signature; the *why* of an architectural decision lives in an ADR, not a docstring. Then `task lint-merge` runs (`ruff check --extend-select SIM,RUF .` plus `ruff format .`) and the result is committed on dev. The next cycle's `select` strips these docstrings from whatever file it touches next — they are a derived, regenerable view, never a carried artifact.

### The lint split

| Set | Where | Rules |
|---|---|---|
| dev (always) | plan-simulate gate; build gates; `ruff check .` | `A`, `ASYNC`, `B`, `C9`, `DTZ`, `ERA`, `F`, `G`, `LOG`, `PYI`, `S` |
| merge (deliver only) | `task lint-merge` | add `SIM`, `RUF`; then `ruff format .` |

`PYI` stays in the dev set because it applies only to `.pyi` and enforces the naked-stub rule (PYI021); it does not churn `.py`. `SIM` is deferred because it restructures (the nested-`with` collapse that once forced a mid-build test edit is the canonical case); `RUF` is mixed and deferred with it for simplicity.

## Related

- [[software-craft/tdd]] — the red/green/refactor cycle that runs on naked code
- [[software-craft/code-review]] — review gates the cycle output; the docstring state at review is naked
- [[software-craft/source-stubs]] — stubs are signature-only (PYI021); the docstring ban there is permanent
- [[software-craft/git-conventions]] — the squash-merge at which docstrings are regenerated
