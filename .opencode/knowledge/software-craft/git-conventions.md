---
domain: software-craft
tags: [git, commits, conventional-commits, branching, squash-merge]
last-updated: 2026-07-08
---

# Git Conventions

## Key Takeaways

- Commits follow **Conventional Commits**: `<type>(<scope>): <imperative description>` — types `feat`, `fix`, `test`, `refactor`, `chore`, `docs`, `ci`; no `wip`, `temp`, or untyped commit (Conventional Commits 1.0.0).
- **One logical change per commit** — `ship-unit` commits the built contract's `.py` plus the structural artifacts it required as one change, and the `.pyi` is unchanged (contracts are fixed during build).
- **Refactor commits are separate from feature commits**; a structural change is never mixed with a behaviour addition, so history stays bisectable and every commit leaves the tests green.
- The branch model is **`feature/<session_id>` → `dev` → `release`/`main`**: the build cycle runs on a session-specific feature branch, squash-merges accumulate on `dev`, and publish targets `release` or `main`. Feature branches are short-lived and deleted after their squash-merge. The contract surface (tests + source stubs) is committed to `dev` at plan, so the feature branch carries only the source implementation — contracts consolidated in dev don't diverge across branches.
- `merge-to-dev` squash-merges the feature commits into `dev` as one commit, then verifies the whole suite and the whole-suite stubtest are clean — no pending markers remain, and no drift was smuggled in by the batch.

## Concepts

**Conventional Commits.** A commit message is a typed, scoped, imperative sentence: `feat(rates): fetch live rate from provider`, `fix(history): correct latest-first ordering`. The type carries meaning — `feat` and `fix` map to minor and patch version bumps, `refactor` signals no behaviour change, `test`/`chore`/`docs`/`ci` are self-explanatory — and the imperative mood keeps the message readable as a command the change performs. The discipline forbids `wip`, `temp`, and any untyped commit, because a history that cannot be read cannot be bisected.

**One logical change per commit.** A commit answers one question; mixing concerns produces a history where each entry means several things at once. `ship-unit` commits exactly one contract — the implemented `.py` and the migrations, fixtures, or cassettes it required — and nothing else; the `.pyi` is the same at ship as it was at plan, because contracts do not move during build. The unit of a commit is the unit of a contract.

**Refactor separate from feature.** A behaviour addition and a structural cleanup are different changes even when they land together, so they are different commits. Mixing them forces a reader (or a `git bisect`) to attribute a test failure to two unrelated changes at once; keeping them apart lets each commit stand as one defensible step, and every commit along the way leaves the tests green.

**The three-branch model.** Work flows in one direction: a session-specific `feature/<session_id>` branch carries one build cycle (red through ship), `dev` accumulates squash-merged contracts and is where integration is verified, and `release` or `main` is the publish target. The contract surface — test stubs, test bodies, and source stubs — is committed to `dev` at plan; the feature branch is cut from dev at build entry and carries only the source implementation. Keeping contracts in dev (not on feature branches) is deliberate: feature branches that hold their own contracts diverge, and reconciling them is cheaper to avoid than to do. Feature branches are short-lived — created at build entry off dev, deleted after the squash-merge — so only `dev` and the publish branch are long-lived.

**Squash-merge into dev.** The granular per-contract commits on `feature/<session_id>` collapse into one commit on `dev`, carrying the contract's summary in its message. The merge is the gate where the whole suite and the whole-suite stubtest run: by now every `.pyi` has its `.py`, every pending marker is gone, and any drift the per-cycle scope hid is exposed across the full set. The branch is deleted after the merge.

## Content

### Branch model

| Branch | Lives | Carries |
|---|---|---|
| `feature/<session_id>` | short — one build cycle | the source implementation commits (red → green → refactor → ship) |
| `dev` | long | the contract surface (committed at plan) + squash-merged source; integration truth |
| `release` / `main` | long | the publish target |

### Commit format

```
<type>(<scope>): <imperative description>
```

| Type | Means |
|---|---|
| `feat` | a new behaviour (implies a minor bump) |
| `fix` | a bug fix (implies a patch bump) |
| `test` | test-only change |
| `refactor` | structural change, no behaviour change |
| `chore` | tooling, deps, CI |
| `docs` | documentation |
| `ci` | CI configuration |

### One logical change — what ship-unit commits

| In the commit | Not in the commit |
|---|---|
| the implemented source `.py` | the `.pyi` (unchanged from plan) |
| the migration / fixture / cassette the module required | unrelated contracts |
| nothing else | a refactor folded in (separate commit) |

### Squash-merge into dev

| Step | Check |
|---|---|
| squash `feature/<session_id>` → `dev` | one commit, contract summary in the message |
| run the full suite | every test green; no pending markers remain |
| run whole-suite `stubtest <package> tests` | every source and test pair agrees — no batch drift |
| delete `feature/<session_id>` | no dangling branches |

## Related

- [[software-craft/tdd]] — the build cycle whose output ship-unit commits
- [[software-craft/code-review]] — the review that gates a commit
- [[software-craft/versioning]] — the version the publish step tags
