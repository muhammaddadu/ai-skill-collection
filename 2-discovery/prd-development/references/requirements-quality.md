# Requirements quality before handoff

Apply proportionately: a small change may need a few acceptance criteria, not a
new document. Keep the project's existing identifiers and terminology.

## Clarify consequential ambiguity

Scan the proposed scope for unclear actors/permissions, state transitions,
failure and recovery paths, external dependencies, accessibility, data handling,
and measurable quality constraints. Do not turn every category into a question.

First use supplied evidence and decisions. Rank remaining unknowns by impact and
uncertainty; ask the highest-impact unanswered question first, with a recommendation
and its trade-off where useful. Follow `workshop-facilitation` for guided pacing.
Do not force short answers when nuance matters. Stop questioning once the remaining
unknowns would not materially change scope, safety, implementation, or validation.

Record each answer in the affected requirement and remove contradictory wording;
a clarification appendix alone must not leave two competing sources of truth.
Keep unresolved assumptions visible with owner and resolution point. A requested
single-shot draft can proceed with labelled assumptions, but must not present
unapproved high-impact choices as settled decisions.

## Check the requirements, not the implementation

- Give buildable requirements stable IDs (or reuse existing section/story IDs).
  State actor, observable behavior, relevant conditions, and acceptance evidence.
- Replace vague terms such as "fast" or "secure" with an agreed criterion and
  measurement context. Never invent a threshold merely to complete a template.
- Cover relevant negative, empty, permission-denied, and recovery paths; identify
  omissions explicitly instead of silently expanding scope.
- Separate product behavior and quality requirements from business outcomes.
  "Invitation expires after the agreed interval" is buildable; "increase adoption"
  requires post-release measurement, not a code-completion checkbox.
- Check completeness, clarity, consistency, and testability. "Is expiry behavior
  specified for pending invitations?" is a requirements-quality check; "does this
  test pass?" belongs to implementation verification through `test-strategy`.

At handoff, retain requirement/acceptance IDs so `tech-spec` and `pi-planning` can
link design decisions and tasks back to intent. For a review spanning several
documents, use `critical-review`'s cross-artifact consistency reference instead of
maintaining another checklist here.
