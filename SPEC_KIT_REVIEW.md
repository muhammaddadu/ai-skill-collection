# Spec Kit workflow review

Reviewed 2026-09-10 at upstream commit
[`03a79d14ec785626db1dc300444f5b9154606e82`](https://github.com/github/spec-kit/tree/03a79d14ec785626db1dc300444f5b9154606e82).
Scope: workflow instructions and selected templates, compared with this collection;
not a security audit or runtime test of the Specify CLI or its extensions.

## Decision

Adopt the connections between specification, design, task planning, and evidence
inside existing skills. Do not add a parallel Spec Kit skill family. The additions
are condensed adaptations with collection-specific authorization and evidence rules.

| Upstream source (under `templates/` at the reviewed commit) | Existing skill enhanced | Adaptation |
|---|---|---|
| `commands/clarify.md`, `commands/checklist.md` | `prd-development` | Consequential questions, integrated answers, requirements-quality checks distinct from software tests |
| `plan-template.md` | `tech-spec` | Existing governing decisions checked before and after design; research rationale and requirement-to-design mapping |
| `commands/tasks.md` | `pi-planning` | Stable task references, independently demonstrable story slices, explicit prerequisites and safe parallel boundaries |
| `commands/analyze.md` | `critical-review` | Read-only cross-artifact consistency and planned-coverage review |
| `commands/converge.md` | `release-readiness` | Candidate-to-intent reconciliation with evidence states and deduplicated remediation tasks |

Conditional detail lives in three routed references; existing skill names,
manifests, document layouts, and installation paths are unchanged. Each stage owns
its check; other stages route to it rather than repeat the full procedure.

## Deliberately not imported

- CLI/bootstrap, numbered feature branches, fixed `.specify` directories, or
  command placeholders: these would add runtime assumptions and competing structure.
- Extension hooks or automatic downstream execution: reviewed documents must not
  grant new authority to run commands, spawn agents, write tickets, or deploy.
- A second project constitution: use applicable repository conventions and ADRs.
- Rigid answer-length/question quotas: retain focused human feedback without
  rejecting nuanced answers or asking questions already answered.
- Treating tests as absent unless explicitly requested: retain risk-based
  `test-strategy` and project requirements; TDD is a separate method choice.
- Unconditional append-only remediation: reuse an unresolved task for the same gap
  and preserve history; leave task files unchanged when nothing needs changing.
- Treating code inspection as full conformance: distinguish verified, unverified,
  partial, missing, contradictory, and unknown; business outcomes need live measures.

## Review cases

Manual instruction walkthroughs, not model-execution benchmarks:

| Case | Required behavior |
|---|---|
| PRD says "fast" without an agreed target | Flag consequential ambiguity; do not invent a number |
| Spec says admin-only, plan allows every member | Report the conflicting sources; no silent scope rewrite |
| Two independent-looking tasks change the same file | Require shared-edit ownership/sequencing before marking parallel |
| Completed task has code but no execution evidence | Report implemented but unverified, not verified or missing |
| Adoption KPI has no code task | Keep it in post-release measurement, outside buildable task coverage |
| Second reconciliation sees the same unresolved gap | Reuse its task when authorized, not append a duplicate |
| User requested review only | Report findings without changing artifacts or deploying |
| Small patch has no PRD | Review agreed change scope without inventing a document pipeline |

Structural validation uses the repository linter and symlink installation checks.
Legacy frontmatter is intentionally unchanged; this change does not claim a full
current-schema migration of the collection.

## Upstream license notice

MIT License

Copyright GitHub, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
