# Reconcile implementation with agreed intent

Review the release candidate, not merely completed task checkboxes. Record its
commit/version, the agreed requirement/design versions, and the review boundary.
Use existing traceability from `tech-spec` / `pi-planning`; for contradictions
between the documents themselves use `critical-review`.

For each in-scope buildable requirement and acceptance criterion, inspect the
relevant implementation and available test/runtime evidence. Start with paths and
contracts named by the plan, then follow affected dependencies as needed. Avoid
an unbounded repository audit. Business KPIs need operating measurements and must
not be declared achieved through source inspection.

| Requirement / AC | Implementation evidence | Verification evidence | Status | Gap / next action |
|---|---|---|---|---|

Use **verified**, **implemented but unverified**, **partial**, **missing**,
**contradicts intent**, or **blocked / unknown**. Source that appears correct is
not runtime proof; unavailable environments are not proof of missing code. Note
unrequested behavior separately and check whether it supports an agreed constraint
before treating it as scope creep. Keep local test, deployed, and live evidence
distinct. Missing required release evidence remains a failed readiness check.

For each gap, recommend the smallest action tied to its source requirement and
verification. A review-only request stops at the report. If remediation planning
is authorized, update/reuse an existing unresolved task for the same gap before
adding one; preserve IDs, completed history, and unrelated work. New tasks identify
the requirement, defect/evidence gap, dependencies, and completion check.

After authorized fixes, rerun affected checks and reconcile again. Stop when the
in-scope evidence supports the agreed criteria, or report the specific unresolved
decision/access dependency. Do not loop on unchanged blockers, weaken requirements
to obtain a pass, or claim complete coverage beyond what was inspected. A no-gap
run needs no task-file mutation. This review does not authorize deployment.
