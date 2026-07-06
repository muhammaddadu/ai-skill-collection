---
name: incident-postmortem
description: "Run a blameless postmortem: reconstruct the timeline, find contributing factors (never one root cause, never a person) and owned, dated action items. Use after an incident/outage/sev for a postmortem, incident review, 'what went wrong' or RCA. Do NOT use during an active incident (stabilize first; sentry-cli + runbooks) or for retro of normal work."
type: interactive
domain: 4-iteration
---

# Incident Postmortem

## Purpose
Turn a resolved incident into organizational learning: a reconstructed timeline,
a set of contributing factors (plural — systems fail through combinations, not
one root cause and never one person), and a short list of owned, dated action
items that make the next incident less likely, detected faster, or mitigated
faster. Runs as a facilitated team session or a solo async write-up, scaled to
severity. The output is written for the whole team and, above all, for the
future responder at 3am who hits something similar.

## Outputs
**Artifact:** blameless postmortem document
**Format:** markdown — fill in `references/postmortem-template.md`
**Location:** `docs/postmortems/YYYY-MM-DD-<slug>.md` in the team's repo.
**Append-only:** postmortems are never rewritten after publication. Corrections,
later discoveries, and follow-up outcomes go in the **Addenda** section with a
date. Rewriting history destroys the record of what was believed at the time —
which is exactly the data future responders need.
**Audience:** the whole team + future responders (write for someone who wasn't
there and is reading this during the *next* incident).

## Prerequisites
- The incident is **resolved or stable** — never run this mid-incident.
- Access to the evidence: alerting history, deploy log, incident chat channel,
  error tracker (see `../sentry-cli/` for pulling issues/events), dashboards.
- A facilitator, ideally **not** the primary responder (see Workflow step 1).

## Blameless guardrails (baked into every step)

These are not tone suggestions; they are rules the document and the session
must satisfy. Violating them produces a document people will lie to next time.

1. **State the framing out loud at the start:** *"Everyone acted reasonably
   given what they knew at the time. If a person could take the system down by
   acting reasonably, the system let them — the system is what we're here to
   fix."*
2. **No names in contributing factors.** Roles only: "the on-call engineer",
   "the deploying engineer", "the reviewer". Names may appear in the timeline
   as factual actors ("@sam paged @alex") but never in a factor, cause, or
   action item's rationale.
3. **Counterfactuals are banned.** "X should have checked the dashboard"
   rewrites the past and blames a person. Rewrite every "should have" as a
   statement about the system: "the deploy pipeline allowed a config change to
   ship without a canary" / "no alert existed on the queue depth that was the
   first visible symptom."
4. **Record what was known at each moment.** Hindsight makes every incident
   look obvious. The timeline captures what responders *could see* at each
   timestamp, not what we now know was happening. "At 14:32 the dashboard
   showed normal latency (the p99 panel was averaging over 1h)" is a finding;
   "latency was already degraded at 14:32" alone is hindsight.

Language swaps to apply while drafting and editing:

| Blame phrasing (reject) | System phrasing (use) |
|---|---|
| "Sam should have run the migration in staging first" | "The migration path had no staging step; production was the first environment to execute it" |
| "The on-call ignored the alert" | "The alert fired into a channel with ~40 alerts/day; it was indistinguishable from routine noise" |
| "Human error" | "The system accepted an input/action that could take it down" — then name what accepted it |
| "The reviewer missed the bug" | "Review had no signal for this class of change (no test, no lint, no checklist item)" |

## Workflow

### Step 1 — Preconditions
Confirm before anything else:
- **Incident is resolved or stable.** If it is still active, stop: stabilize
  first (runbooks, `../sentry-cli/` for live triage), postmortem later.
- **Pick a facilitator who is not the primary responder** where possible. The
  primary responder is the most valuable *witness*; making them run the session
  turns their testimony into self-defense. On a small team where this is
  impossible, name the conflict explicitly and lean harder on guardrails 2–3.
- **State the blameless framing** (guardrail 1) at the top of the session and
  in the document's Summary.
- Pick the severity path now (Step 5): full facilitated session for high-sev,
  short async write-up for low-sev and near-misses.

### Step 2 — Gather evidence BEFORE the session
Never reconstruct a timeline from memory in the room — memory is the least
reliable source and the most vulnerable to hindsight. Assemble first, from:

- **Alerts:** when did each alert fire, who was paged, when acknowledged.
- **Deploy log:** every deploy/config/flag change in the window (start hours
  *before* the first symptom — the trigger often shipped earlier).
- **Chat:** the incident channel/thread is the best record of what responders
  knew and tried, with timestamps. Export it before it scrolls away.
- **Error tracker:** use `../sentry-cli/` to pull the hard data —
  `sentry issue list --query "is:unresolved" --period 24h` to find the issues
  in the window, `sentry issue view <ID>` for first-seen/last-seen and event
  counts, `sentry event list <ID>` for individual events, `sentry release list`
  to line errors up against deploys. First-seen timestamps frequently prove
  the problem started well before anyone knew.

Normalize every timestamp to **UTC** — mixed timezones corrupt gap analysis.

**Quantify impact** before the session so it's fact, not debate: duration
(start → full resolution), users affected (count or %), requests failed,
revenue or SLA/error-budget impact, support tickets. "Bad outage" is not a
measurement; "43 minutes, ~12% of checkout traffic, ~$8k, SLA breached for two
customers" is.

### Step 3 — Run the session
Facilitate using the protocol in `workshop-facilitation` — one question per
turn, quick-select numbered options, progress labels (`Timeline Qx/n`,
`Factors Qx/5`), interruption-safe pacing, and an entry-mode choice up front.
Example opening:

> "Quick heads-up: this takes 30–60 minutes depending on severity. We'll walk
> the timeline, mark the detection and mitigation gaps, collect contributing
> factors, note what went well, and leave with at most 5 owned action items.
> First, the framing: everyone acted reasonably given what they knew — we're
> examining the system, not people. How do you want to start?
> 1. Guided (I ask one question at a time)
> 2. Context dump (paste the incident channel / notes; I'll ask only gaps)
> 3. Best guess (I draft from the evidence; you correct)"

The session phases, in order:

**3a. Walk the timeline chronologically.** Present the evidence-based draft
timeline; walk it start to finish, one entry at a time. Ask participants only
to *correct and fill gaps* ("what did you see at this point?"), not to explain
or justify. Capture what was known at each moment (guardrail 4). No jumping
ahead to causes — the timeline must be agreed before analysis.

**3b. Mark the two gaps.** From the agreed timeline, compute and record:
- **Detection gap:** when the problem *started* → when a human *knew*.
- **Mitigation gap:** when a human knew → when impact *ended*.

Example: errors began at 13:47 (Sentry first-seen), the page fired at 14:29,
rollback completed at 14:41 → detection gap **42 min**, mitigation gap
**12 min**. Responders were fast; the system was blind.

These two numbers direct the action items: a large detection gap means the
system was blind (alerting/observability work); a large mitigation gap means
responders were slow-armed (runbooks, rollback speed, access, escalation).

**3c. Contributing factors — "what made this possible?"** For each pivotal
timeline moment, ask **"what made this possible?"** repeatedly — this is
deliberately NOT five-whys: five-whys drills a single shaft to one "root
cause" and stops; this question fans *outward*, because real incidents need
several independent conditions to line up. Sweep each dimension explicitly:

- **Code:** what in the change or the existing system made this failure mode possible?
- **Process:** what in review/deploy/release practice let it through?
- **Tooling:** what did the pipeline, flags, or rollback machinery allow or lack?
- **Knowledge:** what wasn't known, documented, or shared that mattered?
- **Alerting:** why did the system stay silent (or noisy) as long as it did?

A healthy postmortem lists 3–7 factors across several dimensions. One factor
means you stopped early. Every factor must pass guardrails 2–3: roles not
names, system statements not "should have"s.

Example — "the bad deploy" incident above, fanned out:
- *code:* the config parser silently defaulted on an unknown key instead of failing
- *process:* config-only changes were exempt from the canary stage
- *tooling:* rollback required a full redeploy (12 min) rather than a config revert
- *knowledge:* only one engineer knew the queue-depth dashboard existed
- *alerting:* no alert on queue depth — the first user-visible symptom

Any one of these fixed would have prevented, shrunk, or surfaced the incident;
that is what "contributing factors" means.

**3d. What went WELL — keep it.** Ask explicitly: what limited the blast
radius? Which alert, runbook, habit, or fallback worked? These are load-bearing
practices; if they aren't named, the next reorg or refactor deletes them.

**3e. Action items.** Propose candidates from the factors and gaps, then apply
the rules in Step 4 as hard filters before anything enters the document.

### Step 4 — Action item rules (hard filters)
- **Every item has an owner (a person) and a due date.** "Team to improve
  monitoring" is a wish, not an action item.
- **Classify each as** `prevent` (this can't happen again), `detect-faster`
  (we'd know sooner), or `mitigate-faster` (impact ends sooner).
- **Maximum ~5 items.** More than five means none of them happen. Cut to the
  highest-leverage few; park the rest in the doc's Lessons if genuinely worth
  keeping.
- **If detection gap > mitigation gap, at least one item must be
  `detect-faster`.** Teams reflexively write prevention items; when the system
  was blind for longer than it was slow, blindness is the bigger bug.
- **File every item in the team's normal backlog** (Jira/Linear/GitHub issues)
  with a link back to the postmortem. The doc's table is a record, not a
  tracker — items that live only in the doc silently die.

### Step 5 — Severity-scaled depth
Match effort to severity — the biggest postmortem killer is a process so heavy
it only ever runs after catastrophes.

**High-sev (user-facing outage, SLA breach, data issue):** the full path —
Steps 1–4 with a facilitated synchronous session, all affected responders
invited, published within ~5 business days while memory is fresh.

**Low-sev / near-miss — the 30-minute async short path:**
1. One person (ideally not the primary responder; on a solo team, apply the
   guardrails extra strictly) pulls evidence per Step 2 — timebox 15 min.
2. Fill in `references/postmortem-template.md` directly: timeline, both gaps,
   2–3 contributing factors via "what made this possible?", one thing that
   went well, **1–2** action items max, owned and dated.
3. Post the draft to the team channel for async correction (24h window),
   then file it to `docs/postmortems/` and the action items to the backlog.

Never skip near-misses entirely — a near-miss is the same lesson as an outage
at zero cost, and it's the cheapest postmortem you'll ever run (see Pitfalls).

### Step 6 — Publish
- Write the document from `references/postmortem-template.md`, save to
  `docs/postmortems/YYYY-MM-DD-<slug>.md`, and share it with the whole team.
- From publication on the file is **append-only**: later corrections or
  follow-up outcomes are dated entries under **Addenda**, never edits to the
  original text.

## Pitfalls
- **Blame with polite wording:** the doc says "the engineer misconfigured the
  flag" instead of a name — still blame, just laundered through a role used as
  an accusation → people sanitize what they share next time and the evidence
  dries up → factors must describe what the *system* allowed ("the flag system
  accepted an invalid combination without validation"); if deleting the actor
  from the sentence breaks it, it's blame.
- **Root-cause singular fixation:** the session stops at the first satisfying
  cause ("the bad deploy") → the four other conditions that let a routine bad
  deploy become an outage stay in place and recombine next quarter → ask "what
  made this possible?" across all five dimensions until you have several
  factors; be suspicious of any postmortem with exactly one.
- **Action-item landfill:** 15 items leave the session, none with real owners
  → zero ship, and the next postmortem's action items are the last
  postmortem's action items → hard-cap at ~5, each owner+date, filed in the
  real backlog, reviewed like any other work.
- **Postmortem written by the person who feels guiltiest:** the responder
  closest to the trigger volunteers to write it as penance → the doc
  over-indexes on their "mistake" and under-reports systemic factors, and the
  framing is self-blame all the way down → facilitator/author should not be
  the primary responder; their account is testimony, not the analysis.
- **Skipping postmortems for near-misses:** "no customer impact, nothing to
  review" → the same factor combination fires again with worse luck, and this
  time it *is* an outage → near-misses are free lessons — run the 30-minute
  short path (Step 5) every time luck was a contributing factor to survival.

## Next steps
- **Action items → the team backlog** (Jira/Linear/GitHub issues) with links
  back to the postmortem; review them in normal planning, not a special ritual.
- **Recurring patterns across postmortems → structural fixes:** when the same
  factor shows up twice, escalate from action items to an architecture
  decision — record it with `adr` or design it with `tech-spec`.
- **Detection gaps → alerting improvements:** repeated `detect-faster` items
  point at missing SLOs and alert coverage — run `slo-design` (delivery domain)
  to define the SLIs, burn-rate alerts, and runbooks that close them.
