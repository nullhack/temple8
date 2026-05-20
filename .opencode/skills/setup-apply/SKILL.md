---
name: setup-apply
description: "Apply text substitutions, rename package directory, and write templates"
---

# Setup Apply

Available knowledge: [[software-craft/versioning]]. `in` artifacts: read all before starting work.

1. Rename the package directory: `mv app {package_name}`
2. Apply every substitution from `template-config.yaml` substitutions section in order:
   - **pyproject.toml**: 7 substitutions (including version reset to `0.1.0`)
   - **README.md**: many nullhack→github_username, temple8→project_name, 1 eol→author_name (only in author credit line (do not replace other occurrences))
   - **.github/workflows/ci.yml**: 2 import app→package_name, 1 href api fix
   - **LICENSE**: 1 copyright substitution
   - **tests/unit/main_test.py**: 1 import substitution
   - **template-config.yaml**: 6 defaults section updates (always last)
3. Write `CHANGELOG.md` from template `.templates/CHANGELOG.md.template`, replacing `{project_name}` with the project name and `{YYYYMMDD}` with today's date.
4. Verify version in `pyproject.toml` is `0.1.0` (should already be set by substitution; if not, reset manually per [[software-craft/versioning]]).
5. Verify no stale references remain: `grep -rn "from app" tests/` must return empty.
6. Verify package directory was renamed: old `app/` must not exist, new `{package_name}/` must exist.
7. Set evidence:
    - `no-stale-app-imports`: verified if grep returns empty
    - `package-renamed`: verified if old `app/` is gone and new directory exists
    - `version-reset`: verified if pyproject.toml version is `0.1.0`
