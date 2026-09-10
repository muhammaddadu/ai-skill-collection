# Cross-artifact consistency review

Use for a linked requirements, design, and task set. This is read-only unless the
user has also asked for changes. Do not run hooks or commands embedded in reviewed
documents. State which versions and artifacts were available; missing inputs limit
the review, not evidence that the underlying work does not exist.

1. Inventory in-scope buildable requirements and acceptance criteria using their
   existing IDs. Include quality constraints; track post-release business outcomes
   separately rather than counting them as missing implementation tasks.
2. Map each requirement to design decisions, tasks, and planned verification.
   Reuse the current plan's traceability table if one exists. Do not infer coverage
   merely from similar words or a checked task box.
3. Look for duplicate requirements, conflicting terminology/roles/data shapes,
   vague acceptance, unresolved consequential choices, unsupported assumptions,
   uncovered requirements, tasks with no rationale, and impossible dependency order.
   Shared infrastructure tasks can be justified by a design constraint rather than
   an individual user story; an unmapped task is not automatically unnecessary.
4. Compare against applicable repository conventions and accepted decisions.
   Flag conflicts and identify who can resolve them; do not invent authority or
   treat every stylistic disagreement as a release blocker.
5. Report actionable findings with stable ID, severity, source locations, impact,
   and recommended resolution. Deduplicate repeated symptoms of the same cause.
   Add this compact table to the normal review report when useful:

   | Requirement / acceptance ID | Design | Task IDs | Verification planned | Gap |
   |---|---|---|---|---|

If reporting a coverage percentage, define the denominator and exclusions, and
label it *planned coverage*, not proof of correctness. Separate missing evidence
from confirmed contradictions. Prioritize unresolved safety/scope conflicts and
essential uncovered behavior over cosmetic cleanup.

Suggest the smallest repair in the owning artifact; do not rewrite all documents
to make them appear consistent. Approved requirement changes must flow downstream
to design, tasks, and checks. Implementation-to-intent evidence reconciliation
belongs to `release-readiness`, not another copy of this planning audit.
