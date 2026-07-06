---
name: product-brief
description: "Turn raw intake — a request, idea, or stakeholder ask — into the Product Brief that earns Sign-Off 1: intent framed, constraints and success criteria captured, priority argued. Use when a new ask arrives and Discovery must not start without a brief. Do NOT use for full requirements (prd-development) or problem framing alone (problem-statement)."
type: component
domain: 1-exploration
---

# product-brief — Intake to Sign-Off 1

## Purpose

Turn raw intake — a feature request, a half-formed idea, an executive ask, a
support-ticket pattern — into a **Product Brief**: the short document that
frames the intent behind the ask, records the constraints and success criteria
the stakeholders actually hold, declares what is out of scope, and argues why
this deserves attention now. The brief is the blueprint's entry artifact for
the whole product process: it is what **Sign-Off 1** approves, and **no
Discovery work starts without it**. A signed-off brief means the humans who
own the direction have agreed on *what we're trying to achieve and why it's
worth a team's time* — before anyone writes a PRD, runs an interview, or
sketches a solution.

A brief is one to two pages. Its job is alignment, not specification: enough
clarity that the Discovery team knows what success looks like, not so much
detail that Discovery's questions are pre-answered.

Where it sits among adjacent artifacts: a `problem-statement` frames one
user problem and can feed the brief's intent section; the brief adds
stakeholders, constraints, success criteria, scope, and priority, and is what
Sign-Off 1 approves; the PRD (`prd-development`) comes *after* the gate and
specifies the solution. One initiative, in that order.

## Outputs

**Artifact:** Product Brief
**Format:** markdown (from `references/product-brief-template.md`)
**Location:** `docs/product/briefs/<slug>.md` in the target repo — `<slug>` is
a short kebab-case name for the initiative
**Audience:** the signing stakeholders (Sign-Off 1) and the Discovery team
that inherits the brief

## Prerequisites

- A concrete piece of intake: the request, idea, or ask, in whatever raw form
  it arrived (Slack message, meeting note, ticket, hallway sentence). If there
  is no identifiable ask yet — only a vague sense that "something is wrong in
  area X" — frame the problem first with `problem-statement`, then return here.
- Access to the requesting stakeholders. The brief records *their* intent,
  constraints, and success criteria; it cannot be written about them in
  absentia.

## Workflow

### 1. Capture the intake verbatim

Copy `references/product-brief-template.md` to
`docs/product/briefs/<slug>.md` and paste the original ask into the intake
section **word for word** — the Slack message, the ticket text, the quote from
the meeting. Note who said it, when, and through what channel.

Do not paraphrase at this stage. Paraphrasing is where interpretation sneaks
in; the verbatim record is what lets everyone later check whether the framed
intent is faithful to what was actually asked. It is also the receipt that
makes the requester feel heard.

### 2. Identify the intent behind the ask

Most intake arrives solution-shaped: "we need a dashboard", "add an export
button", "can we integrate with X". The brief's first real work is separating
the **intent** (the outcome the requester wants in the world) from the
**proposal** (the mechanism they reached for). Ask the requester: *"If this
existed tomorrow, what would be different? What are you able to do that you
can't today?"* Keep asking until the answer is an outcome, not a feature.

Route to sibling skills when the digging stalls:

- The underlying **problem is fuzzy** — you can't say who is blocked or why it
  matters: run `problem-statement` and link the result from the brief.
- The **user need is unclear** — you know what was asked for but not what job
  the user is hiring it for: run `jobs-to-be-done` and fold the findings in.

Write the intent as one or two sentences in the brief: *what* we want to be
true, and *why now* — what changed (a deadline, a competitor, a threshold
crossed, a strategic bet) that makes this the moment.

### 3. Gather stakeholder intent, constraints, and success criteria

This is the blueprint's first callout, and it is a rule of *who supplies
what*: **stakeholders provide the intent, the constraints, and the success
criteria — you elicit and record them, you do not invent them.** A brief whose
constraints and success criteria came from the author's imagination will pass
its own sign-off and then collapse in Discovery when the real ones surface.

Sit down with each requesting stakeholder (identify them all first — use
`stakeholder-identification` if the map is unclear) and capture:

- **Intent as they state it** — in their words, per stakeholder. Divergent
  intents between stakeholders are a finding, not a formatting problem; record
  the divergence and get it resolved before sign-off, not after.
- **Constraints**, split explicitly into:
  - **Hard** — violating these kills the initiative: regulatory deadlines,
    budget ceilings, platform mandates, contractual commitments.
  - **Soft** — preferences with owners: "we'd rather not touch the billing
    system", "marketing wants this before the conference". Name who holds
    each and what relaxing it would cost.
- **Success criteria** — measurable statements of what "worked" means, each
  with a metric, a target, and a time horizon. Push every vague criterion
  ("users love it", "the process is faster") until it has a number and a
  date, or is honestly recorded as a hypothesis Discovery must firm up.

Also record the **users affected** — who experiences the change, whether they
are the same people as the requesters (they usually aren't), and roughly how
many.

### 4. Declare what is out of scope

Write down the adjacent things this initiative deliberately does **not**
cover — the neighboring feature everyone will assume is included, the second
user segment, the migration of the legacy path. Every out-of-scope line
prevents a future argument. If a stakeholder objects to an exclusion, that
objection surfaces *now*, at the cost of a conversation, instead of mid-build
at the cost of a re-plan. An empty out-of-scope section is a warning sign:
it usually means scope hasn't been thought about, not that scope is total.

### 5. Argue the priority

The brief must say why this deserves a slot **ahead of the alternatives** —
not just that it is worthwhile. "It's valuable" is true of everything in the
backlog. State the cost of delay, what it displaces, and why now beats next
quarter. Ground the argument in the success criteria from step 3.

If priority is **contested** — stakeholders disagree, or you're arguing
against another initiative competing for the same slot — route to
`prioritization-advisor` to pick a scoring framework and run it, then record
the outcome (scores, framework used, who agreed) in the brief's priority
section. A one-line "P1" with no rationale is not an argument; it's a demand.

### 6. Run the Sign-Off 1 checklist

Before requesting sign-off, verify the brief against the gate's four
questions:

- [ ] **Intent clear?** Can a reader who wasn't in the room say what outcome
  is wanted and why now — without asking anyone?
- [ ] **Constraints explicit?** Hard and soft separated, each soft constraint
  owned by a named stakeholder?
- [ ] **Success measurable?** Every criterion has a metric, target, and
  horizon — or is flagged as a hypothesis for Discovery?
- [ ] **Priority agreed?** The rationale is written down, and contested calls
  were resolved (not deferred) — with the framework and outcome recorded?

Any unchecked box means the brief is not ready; fix it rather than arguing it
through the gate. Then present the brief to the stakeholders who own the
direction and record the sign-off in the brief itself: who approved, when,
and any conditions attached. A brief without a recorded sign-off has not
passed Sign-Off 1 — verbal agreement in a meeting evaporates; the record
doesn't.

### 7. Hand off to Discovery

On sign-off, the brief becomes Discovery's charter. Hand it to the team
entering PRD Forming (`prd-development`) and the wider discovery cycle
(`discovery-process`). The brief is now **frozen as the record of what was
agreed**: if Discovery's findings change the intent, constraints, or success
criteria materially, that's a revision that goes back through the
stakeholders — amend the brief and re-record sign-off, don't silently drift.

## Pitfalls

- **Solution-shaped intake accepted as intent:** the brief's intent section
  says "build a dashboard" because that's what the stakeholder asked for → the
  team delivers the dashboard, the underlying need goes unmet, and the real
  ask returns in next quarter's intake wearing a different feature → always
  run step 2's outcome questioning; if the ask can't be restated as "what
  would be different", it isn't intent yet — use `problem-statement` to dig.
- **Unmeasurable success criteria:** criteria like "improve the experience"
  or "make onboarding smoother" pass sign-off because nobody wants to be the
  pedant → Sign-Off 1 approves a feeling; months later nobody can say whether
  the initiative worked, so it can neither be declared done nor killed → push
  every criterion to metric + target + horizon in step 3, or record it
  explicitly as a Discovery hypothesis — never as a criterion.
- **Sign-off skipped "because it's small":** the ask looks like a week of
  work, so the team starts Discovery (or worse, delivery) on a nod → small
  asks grow, and when this one does there is no agreed intent or scope to
  appeal to — the gate existed precisely for the moment it was skipped → the
  gate is unconditional; for genuinely small asks the brief can be half a
  page, but a signed-off half-page is still required.
- **Brief that's secretly a PRD:** the brief specifies user flows, screens,
  data models, and edge cases → Discovery is pre-empted — the team inherits
  conclusions instead of questions, and PRD Forming becomes a formality that
  rubber-stamps whatever the brief author assumed → keep the brief at intent
  altitude (outcomes, constraints, success, scope boundary); when you catch
  yourself writing "the user taps…", cut it — that sentence belongs to
  `prd-development`.

## Next steps

- `prd-development` — PRD Forming begins from the signed-off brief; the
  brief's intent and success criteria seed the PRD's problem and goals.
- `discovery-process` — the full discovery cycle (framing → interviews →
  synthesis → experiments) that validates the brief's assumptions and turns
  its hypotheses into evidence.
