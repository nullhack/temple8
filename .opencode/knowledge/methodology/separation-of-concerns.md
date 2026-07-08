---
domain: methodology
tags: [separation-of-concerns, drift, flowr, single-source-of-truth]
last-updated: 2026-07-01
---

# Separation of Concerns

## Key Takeaways

- Four artifact kinds, one question each: the flow answers **where** (routing), an agent answers **who** (identity), a skill answers **how** (procedure), knowledge answers **what and why** (reference).
- Each fact lives in exactly one canonical location; any copy becomes a second source that drifts, and the stale copy usually wins attention at runtime.
- The flow YAML is the spine — it binds a state to its dispatched agent, procedure, artifacts, branch, gate, and exits; the other three files carry none of those.
- The orchestrator routes; agents, skills, and knowledge are loaded on demand, never the whole layer at once.
- A state's `description` orients — one or two lines on what the state is for; the step-by-step procedure, criteria lists, and technique live in the skill. When a `description` and a skill disagree on procedure, the skill wins.
- An escalation handoff rides a per-session journal: the discovering state appends its finding, the receiver reads it on re-entry, and the re-dispatch prompt carries it live. The tests and cassettes stay the spec; the journal is only the safety net against lost context mid-escalation.

## Concepts

**Four concerns, four homes.** The methodology layer has four artifact kinds, and each answers one question. The flow says where (states, transitions, dispatch, artifacts, gates). An agent file says who (the role, what it alone decides). A skill file says how (the step-by-step method). A knowledge file says what and why (definitions, criteria, reasoning). Mixing two concerns in one file splits one question across two load points and the model cannot tell which answer is authoritative.

**One fact, one location.** A fact copied out of its canonical home into another file is a second source. The day the two disagree, the older copy — already in context, already trusted — usually wins, and the agent improvises against a stale contract. Each piece of information lives in exactly one place and every consumer links to it rather than restating it. See [[methodology/agent-files]], [[methodology/skill-files]], [[methodology/knowledge-files]] for what is unique to each.

**The flow is the spine.** A state's `dispatch_to` binds it to an agent; its `skills` bind it to procedure; its `input artifacts` / `output artifacts` bind it to what is read and written; its `git branch` binds it to where commits land; its `conditions` bind it to its gate; its `next` binds it to its exits. The agent, skill, and knowledge files carry none of these — they would only duplicate the flow and drift.

**Route, then load on demand.** The orchestrator reads the flow and routes; it does not do the work. Agents, skills, and knowledge enter context only when a state dispatches them, so the layer is never loaded wholesale. This keeps each session's budget spent on the work, not on the methodology.

**Description orients; procedure lives in the skill.** A state's free-form `description` states what the state is for and the decision it gates — it does not embed the how. Step sequences, criteria catalogues, and technique belong in the skill (the canonical procedure home) and the knowledge it cites. A `description` that duplicates the procedure builds a second source that drifts; the day they disagree, the skill is authoritative and the description is stale.

## Content

### Who owns what

| Question | Owner | Artifact |
|---|---|---|
| Where (routing, transitions, artifacts, gates) | the flow | `.flowr/flows/*.yaml` |
| Who (identity, sole decisions) | the agent | `.opencode/agents/{role}.md` |
| How (step-by-step procedure) | the skill | `.opencode/skills/{skill}/SKILL.md` |
| What and why (reference, criteria) | knowledge | `.opencode/knowledge/{domain}/{concept}.md` |

### Drift mechanics

A duplication drifts in three steps: (1) a fact is copied from its home into a second file; (2) the home changes; (3) the copy does not. At runtime the copy is already in context and is trusted, so the agent acts on the stale fact. The cure is structural, not disciplinary — never copy in the first place; link.

### What the flow owns

Do not duplicate any of these outside the flow YAML.

| Flow attr | Binds |
|---|---|
| `dispatch_to` | the agent (who) |
| `skills` | the procedure (how) |
| `input artifacts` / `output artifacts` | what is read / written |
| `git branch` | where commits land |
| `conditions` | the gate evidence |
| `next` | the exits |

`description` is deliberately absent from this table: it is lean orientation (what the state is for), not a structural binding, and must not carry the step-by-step procedure — that is the skill's content. See [[methodology/skill-files]].

### Evidence vs enforcement

A gate `conditions` key (e.g. `stubtest-clean=true`) is EVIDENCE the dispatched agent asserts; flowr does not execute the check. The enforcement backstop is CI, which runs `ruff` (with `PYI`), `pyright`, `mypy.stubtest`, and `pytest` on every push and fails the build on any drift or violation — verifying what the agent asserted. The flow's job is to name the gate and collect honest evidence; CI's job is to prove it.

### Escalation handoffs

When a state exits on `reveals-gap` / `needs-capture` / `needs-elicitation`, its finding must reach the phase it re-enters. The finding rides two carriers: the discovering state **appends** it to `.cache/<session_id>/journal.md` (its `output artifacts`), and the re-dispatch prompt carries it verbatim. The receiving state **reads** `journal.md` on entry (its `input artifacts`) and re-derives the detail from the artifacts — the tests, source stubs, and cassettes that *are* the spec. The journal is a transient per-session safety net against context lost mid-escalation (e.g. a compress between the discovering state and re-entry); it is not a second spec and never duplicates what the tests express. One stable file absorbs every escalation — present and future — so new edges never spawn new artifact types.

### Rework trigger sources

The `@pytest.mark.pending` backlog is fed by two distinct trigger sources, read at `author-test-stubs` and `write-test-py`:

- **Build escalation** — a contract gap discovered mid-build is appended to `.cache/<session_id>/journal.md` (the carrier above) and re-enters plan as rework on the named contract.
- **Discovery flag** — a finding in `.cache/<session_id>/interview-notes.md` that implies *modifying* an existing block (flagged `rework — modifies existing <block>` at `interview-building-blocks`) re-enters plan as rework on that block's contracts.

Both surface as `@pytest.mark.pending` so `select-build-target` pulls them from the queue. The journal carries build-phase escalations; the interview notes carry requirements-level modification flags — two carriers, one backlog, no third artifact type. A discovery finding that adds a *new* block is new work, not rework, and authors a fresh stub without the pending marker.

### Loading model

The orchestrator reads the flow once per state and dispatches; it does not load the methodology layer up front. An agent loads when its role is dispatched; a skill loads when the state's `skills` names it; knowledge loads when a wikilink resolves. No session pays for the whole layer.

## Related

- [[methodology/agent-files]]
- [[methodology/skill-files]]
- [[methodology/knowledge-files]]
