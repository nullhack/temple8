---
domain: software-craft
tags: [versioning, semver, pep-440, calver, release]
last-updated: 2026-07-01
---

# Versioning

## Key Takeaways

- **SemVer 2.0.0** is `major.minor.patch`: a breaking change bumps `major`, a backward-compatible feature bumps `minor`, a fix bumps `patch`. A `0.major.minor` line carries no stability promise — any release may break (semver.org).
- For a Python project the version in `pyproject.toml` must satisfy **PEP 440**; SemVer's `X.Y.Z` is a subset PEP 440 accepts. A `+local` build segment is stripped by package indexes, so `pyproject.toml` carries the core `X.Y.Z` only (PEP 440; SemVer §10).
- **CalVer** (`YYYY.MM.DD`, `YYYY.MINOR.MICRO`) fits time-released projects with no compatibility promise — it records *when*, not *whether compatible* (calver.org).
- The `version` field in `pyproject.toml` is the **single source of truth**; tags and release notes derive from it, never the reverse.
- `publish-release` chooses among **release notes, a PR to `main`, or a tagged release** (`v{version}`), per the project's release policy.

## Concepts

**SemVer, the default.** Semantic Versioning gives a dependency resolver something to reason about: `pkg>=1.2.0,<2.0.0` works because the major version signals a compatibility break. The bump rules are precise — a backward-incompatible change is a major bump however small the code, a backward-compatible addition is a minor bump, a fix is a patch. The special case is `0.x`: below 1.0.0 the spec declares the public API unstable, so a `0.2.0 → 0.3.0` step is allowed to break a consumer, and the major-version compatibility signal is understood to be absent.

**PEP 440 for Python.** A Python project's version is read by tooling that obeys PEP 440, not raw SemVer; SemVer's `X.Y.Z` form is a subset PEP 440 accepts, so a plain `1.2.3` is valid in both. Where they diverge is build metadata: SemVer §10 allows a `+build` suffix, but PEP 440 treats `+local` as a *local* version segment that package indexes strip — a version like `1.2.3+20260701` publishes to the index as `1.2.3`. The consequence for a Python project is that the `pyproject.toml` `version` field carries the publishable core (`1.2.3`), and any date or build suffix is a tag-only concern, not a field that goes to the index.

**CalVer, when timing matters more than compatibility.** Calendar Versioning leads with the date — `2026.4`, `26.7.1` — and suits projects that release on a cadence and make no consumer compatibility promise (operating systems, terminal apps, services with no external API). It carries timing clearly and fails to carry compatibility at all, so a consumer cannot bound an acceptable range the way SemVer's major version allows. Choose CalVer when the audience reads the date; choose SemVer when the audience bounds a range.

**Single source of truth.** The version lives in `pyproject.toml` and nowhere else; a tag, a release note, and a changelog entry are all derived from it. Maintaining a version in two places (a field and a tag that drifts) is the same defect as any duplicated truth — they diverge, and the divergence is discovered at release time under pressure.

**Publish is a policy choice.** `publish-release` does not assume one form of release; it picks among release notes, a PR to `main`, and a tagged release, according to what the project has decided its release policy is. A library tags and publishes; an internal service may merge a PR to `main` and stop; an early-stage project may ship only notes. The versioning knowledge fixes what a version *is*; the release policy fixes *how* a version ships.

## Content

### SemVer bump rules

| Change | Bump | Example |
|---|---|---|
| breaking (API contract change) | major | `1.2.3` → `2.0.0` |
| backward-compatible feature | minor | `1.2.3` → `1.3.0` |
| bug fix | patch | `1.2.3` → `1.2.4` |
| anything, while below 1.0.0 | minor may break | `0.2.0` → `0.3.0` (breaking allowed) |

### Scheme comparison

| Scheme | Form | Carries | Fits |
|---|---|---|---|
| SemVer | `MAJOR.MINOR.PATCH` | compatibility | libraries, packages with consumers |
| CalVer | `YYYY.MINOR.MICRO` | timing | cadence-released apps, services, OS-like tools |
| SemVer + local tag | `X.Y.Z` (field), `vX.Y.Z+date` (tag) | both, split across field and tag | projects that want both but must keep the index field clean |

### Tag and release forms

| Output | Form |
|---|---|
| git tag | `v{version}` (e.g. `v1.2.3`) |
| pyproject field | `1.2.3` (PEP 440 core; no `+local`) |
| release notes / changelog | `## [v1.2.3] - {date}` |

## Related

- [[software-craft/git-conventions]] — the commit and branch discipline a release rides on
- [[software-craft/code-review]] — the review that gates what gets released
