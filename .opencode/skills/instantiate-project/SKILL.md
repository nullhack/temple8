---
name: instantiate-project
description: "Create a new project instance from the temple8 template via copier, verify it, and initialise the first flowr session."
---

# Instantiate Project

1. Confirm the destination directory does not exist or is empty; IF `copier copy` would clobber existing work THEN stop and ask the user where to create the project.
2. Run `copier copy gh:nullhack/temple8 <destination>` (or the local template path if offline). Answer the questionnaire: `project_name`, `package_name` (defaults from `project_name`), `description`, `repo_url`, `version`, `author_name`, `author_email`, `keep_design`, `keep_research`, `reset_git`.
3. `cd` into the new project and verify the skeleton: `<package>/__init__.py` exists; `tests/{integration,e2e,cassettes,fixtures}/` and `tests/conftest.py` exist; `pyproject.toml` and `README.md` are rendered (no `{{ }}` placeholders remain); `.opencode/`, `.flowr/`, `.templates/`, `AGENTS.md`, `.github/` are present and unchanged.
4. Run `uv sync --extra dev` to materialise the venv.
5. Verify the gates load: `bash -c 'for f in .flowr/flows/*.yaml; do uv run python -m flowr validate "$f"; done'` — all six must report `{valid: true}`; `uv run ruff check .` must pass; `uv run pytest --collect-only -q` must collect zero tests cleanly.
6. Initialise the first session: `uv run python -m flowr session init pipeline-flow --name default`; confirm it lands at `discovery-flow/interview-general`.
7. Report the instance ready: destination path, the rendered identity, and the first flowr command (`uv run python -m flowr check --session default`) to begin driving.
