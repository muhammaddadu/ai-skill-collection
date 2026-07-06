# Walkthrough: one feature, the full cycle

A worked example of the blueprint end to end — which skill fires at each step,
what it produces, and what gates the next step. The feature: **"Add dark mode
to the customer app"** (an Expo/React Native app). `BLUEPRINT.md` is the map;
this is the map driven once.

Legend: ▸ = skill invoked · ✋ = human gate · ↩ = conditional path

---

## Phase 1 — Exploration (human)

> Frame the problem before touching AI.

| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 1. Intake arrives | ▸ `product-brief` | A stakeholder asks for dark mode. Captured verbatim; the ask is solution-shaped, so intent is extracted: *night-time users report eye strain and churn on evening sessions* | `docs/product/briefs/customer-app-dark-mode.md` |
| 2. Problem check | ▸ `problem-statement` (routed from product-brief) | Who is blocked, doing what, why it matters: "Evening commuters using the app in low light…" | Problem statement, folded into the brief |
| 3. Stakeholder inputs | *(inside product-brief)* | Stakeholders provide intent, constraints (must match brand palette; ship this quarter), success criteria (evening-session retention +5%, support tickets on brightness −50%) | Brief sections filled |
| 4. Priority contested? | ↩ ▸ `prioritization-advisor` | Two teams want the next slot — RICE comparison settles it | Priority rationale in the brief |

**✋ Sign-Off 1** — the brief's four checks pass (intent clear, constraints
explicit, success measurable, priority agreed). Stakeholders sign. Discovery may begin.

*Skills that could have fired instead, and when:* `jobs-to-be-done` (user need
unclear), `opportunity-solution-tree` (many competing solutions), `tam-sam-som-calculator` /
`positioning-statement` (new product rather than a feature), `company-intel` →
`company-research` (competitive pressure driving the ask).

---

## Phase 2 — Discovery (humans + AI)

> Humans bring taste. AI explores the space.

### PRD Forming
| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 5. PRD starts | ▸ `prd-development` | Problem, users, assumptions, risks; stakeholders consulted on **problem alignment** | PRD (Forming) |
| 6. User evidence | ▸ `discovery-interview-prep` → sessions | Five evening-usage interviews planned and run; `proto-persona` sharpens "the commuter" | Interview plan + synthesis into the PRD |
| 7. Design starts | ▸ `design-signal` (30%) | Conceptual flows for theme switching; UX risks named (contrast on promo imagery, system-vs-manual toggle) | Design Signal 30 report |

### PRD Storming
| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 8. Feasibility question | ▸ `eng-feasibility-spike` | One falsifiable question: *can the existing styling layer theme dynamically without a full restyle?* 2-day time-box; throwaway POC on the settings screen | Spike report: **feasible-with-cost** — 3 legacy screens need restyling |
| 9. Solution shaping | ▸ `prd-development` (Storming) + ▸ `design-signal` (still 30→60 work) | Solution options land in the PRD with the spike's evidence | PRD (Storming) |
| 10. Cheap validation | ↩ ▸ `pol-probe-advisor` → `pol-probe` | Optional: a fake-door "dark mode coming" toggle measures actual demand before committing | Probe result feeds the PRD |

### PRD Norming
| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 11. Usability proof | ▸ `design-signal` (60%) | Prototype tested with 6 users; contrast issues fixed; evidence table honest ("a 60 with weak evidence is a 30") | Design Signal 60 report |
| 12. Architecture recorded | ▸ `adr` | ACR-0007: "Theme tokens via context provider, not per-screen styles" — options, losers, consequences | `docs/adr/0007-theme-tokens.md` |
| 13. API impact? | ↩ ▸ `api-design` | Only if the backend stores a theme preference — here: one field on the profile endpoint, checked against A20 (no breaking change) | Contract note in the tech spec |
| 14. Engineering design | ▸ `tech-spec` | The PRD's "how": chosen design, data impact, test approach, rollout sketch | `docs/specs/dark-mode.md` |
| 15. Business rules | ▸ `prd-development` (Norming) | Stakeholders validate business rules (default theme, brand palette) — **not** the user journey | PRD (Normed) |

**✋ Sign-Off 2** — stakeholders validate scope, sequencing, outcomes — not
solution details. PRD is ready for commitment.

---

## Phase 3 — Delivery (AI codes; humans consult, review, ship)

| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 16. Increment planned | ▸ `pi-planning` | Readiness gate: Design Signal 90 ✓ (`design-signal`), tech spec current ✓, spike resolved ✓. MVP cut-line: manual toggle ships, system-sync follows. PRD → **Commitment-Ready** | PI plan + tickets |
| 17. Stories cut | ▸ `epic-breakdown-advisor` → `user-story` | Epic split (patterns from `user-story-splitting`); each story carries Gherkin criteria | Tickets with acceptance criteria |
| 18. Test plan | ▸ `test-strategy` | Criteria → pyramid: theme-token logic unit-tested, one E2E on toggle persistence; merge-gate vs release-gate done-bar | Test plan in the spec |
| 19. Agent execution? | ↩ ▸ `ralph` | If an autonomous agent runs the build: PRD → `prd.json` | prd.json |
| 20. Code, test-first | ▸ `tdd` + ▸ `cleanui` + ▸ `react-native-skills` | Red-green loop per story; UI follows the aesthetic direction + platform rules; RN perf rules on the theme switch (no re-render storms) | Implementation |
| 21. Something breaks | ↩ ▸ `diagnosing-bugs` | Flaky theme flash on cold start: repro loop → root cause (async storage read after first paint) → fix at source + regression test | Diagnosis + fix |
| 22. Conflict on merge | ↩ ▸ `resolving-merge-conflicts` | Long-lived branch meets a navigation refactor | Clean merge, checks green |
| 23. A11y audit | ▸ `web-design-guidelines` | Contrast ratios, focus states, reduced-motion on the theme transition | Audit findings fixed |
| 24. Rollout plan | ▸ `progressive-delivery` | Flag `rel_dark_mode` (owner + TTL set at creation), dark deploy, dogfood cohort, ramp 1→5→25→50→100% with abort criteria, kill switch | `docs/specs/rollouts/dark-mode.md` |
| 25. Go/no-go | ▸ `release-readiness` | Scored review: quality gates, rollback, observability (dashboards BEFORE launch), comms; hard gates checked | RELEASE-READINESS.md — **GO** |
| 26. Ship + ramp | *(execution)* + ↩ ▸ `expo-deployment` | Store build via EAS; ramp runs; PRD → **Live** | Released app |
| 27. Cleanup | ▸ `progressive-delivery` (step 5) | At 100% + soak: old light-only path deleted, flag deleted — the new thing is the main thing | Cleanup checklist merged |

*Also on call in this phase:* `postgres-best-practices` (if the preference
lands in a slow query), `api-design` review mode (contract drift),
`mcp-builder` / `nestjs-best-practices` / `react-best-practices` (stack-dependent),
`agent-docs` (if the repo's agent conventions need scaffolding first).

---

## Phase 4 — Learn & Iterate

| Step | Skill | What happens | Artifact |
|---|---|---|---|
| 28. Checkpoint | ▸ `learn-iterate` | At the date booked in step 25: evening retention +6% ✓, brightness tickets −38% ✗ (trending); insight: users can't find the toggle | Iteration review; PRD → **Updated** |
| 29. Decision | *(inside learn-iterate)* | **Iterate**: surface the toggle in onboarding — a new mini-cycle via `prd-development`; system-sync (below the cut-line) gets its named release | Adjustments with owners |
| 30. Incident during ramp? | ↩ ▸ `incident-postmortem` | The step-21 kill-switch event (if one fired) gets a blameless postmortem — separate from product learning | `docs/postmortems/…` |
| 31. Business lens | ↩ ▸ `saas-revenue-growth-metrics` / `business-health-diagnostic` | Quarterly: did retention movement show up in revenue? | Metrics readout |
| 32. Loop closes | → `product-brief` | The onboarding insight becomes next cycle's intake | New brief |

*(If the feature had missed and stayed missed: `eol-message` to retire it well.)*

---

## The cycle in one line each

1. **Exploration** — `product-brief` (+ `problem-statement`, `prioritization-advisor`) → ✋ Sign-Off 1
2. **Discovery** — `prd-development` × (`design-signal` 30/60 ∥ `eng-feasibility-spike` → `adr` → `tech-spec` (+ `api-design`)) → ✋ Sign-Off 2
3. **Delivery** — `pi-planning` → stories (`epic-breakdown-advisor`, `user-story`) → `test-strategy` → build (`tdd`, `cleanui`, stack skills) → `web-design-guidelines` → `progressive-delivery` → `release-readiness` → ship → flag cleanup
4. **Iterate** — `learn-iterate` → decisions → back to `product-brief`

Skipping a step doesn't save time — it just pushes the rework later.
