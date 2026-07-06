---
name: business-health-diagnostic
description: Diagnose SaaS business health across growth, retention, efficiency, and capital. Use when preparing a business review or prioritizing urgent fixes.
intent: >-
  Diagnose overall SaaS business health by analyzing growth, retention, unit economics, and capital efficiency metrics together. Use this to identify problems early, prioritize actions by urgency, and deliver a comprehensive health scorecard for board meetings, quarterly reviews, or fundraising preparation.
type: interactive
theme: finance-metrics
best_for:
  - "Getting a complete read on your SaaS business health across all dimensions"
  - "Identifying which metrics are red flags vs. leading indicators"
  - "Preparing for a board meeting or investor review"
scenarios:
  - "Our growth is strong but we're burning cash fast — I need to understand our unit economics before the board meeting"
  - "I'm preparing for a Series A board meeting and need to assess our business health across growth, retention, and efficiency"
estimated_time: "20-30 min"
---


## Purpose

Diagnose overall SaaS business health by analyzing growth, retention, unit economics, and capital efficiency metrics together. Use this to identify problems early, prioritize actions by urgency, and deliver a comprehensive health scorecard for board meetings, quarterly reviews, or fundraising preparation.

This is not a single-metric check—it's a holistic diagnostic that connects revenue, retention, economics, and efficiency to reveal systemic issues and opportunities.

## Outputs

**Artifact:** Business health scorecard (overall + per-dimension scores), red-flag list, and prioritized action plan with stage-appropriate benchmarks
**Format:** Markdown (tables + recommendations)
**Location:** Delivered in conversation; saved to a file only if the user asks
**Audience:** Founder / PM / exec preparing a board meeting, QBR, or fundraise

## Key Concepts

### The Business Health Framework

A SaaS business is healthy when four dimensions work together:

1. **Growth & Retention** — Are you growing and keeping customers?
   - Revenue growth rate, NRR (Net Revenue Retention), churn rate, Quick Ratio

2. **Unit Economics** — Is the business model profitable at the customer level?
   - CAC, LTV, LTV:CAC ratio, payback period, gross margin

3. **Capital Efficiency** — Are you using cash efficiently?
   - Burn rate, runway, Rule of 40, Magic Number

4. **Strategic Position** — Are you positioned for sustainable success?
   - Market positioning (below/at/above market pricing), competitive moat (network effects, data, brand), revenue concentration risk, operating leverage

### Stage-Specific Benchmarks

**Early Stage (Pre-$10M ARR):**
- Focus: Product-market fit, unit economics
- Growth: >50% YoY · LTV:CAC: >3:1 · Gross Margin: >70% · Runway: >12 months
- Acceptable: Negative margins, high burn (if unit economics work)

**Growth Stage ($10M-$50M ARR):**
- Focus: Scaling efficiently
- Growth: >40% YoY · NRR: >100% · Rule of 40: >40 · Magic Number: >0.75
- Acceptable: Moderate burn if growth is strong

**Scale Stage ($50M+ ARR):**
- Focus: Profitability, efficiency
- Growth: >25% YoY · NRR: >110% · Rule of 40: >40 · Profit Margin: >10%
- Required: Positive or near-positive cash flow

### Red Flag Categories

**Critical (Fix immediately):**
- Runway <6 months
- LTV:CAC <1.5:1
- Churn accelerating cohort-over-cohort
- NRR <90%
- Magic Number <0.3

**High Priority (Fix within quarter):**
- Rule of 40 <25
- Payback >24 months
- Quick Ratio <2
- Gross margin <60%
- Revenue concentration >50% in top 10 customers

**Medium Priority (Address within 6 months):**
- NRR 90-100% (flat, not growing)
- Magic Number 0.3-0.5
- Operating leverage negative
- Churn rate stable but high (>5% monthly)

### Anti-Patterns (What This Is NOT)

- **Not a single metric:** "Revenue is growing 50%, we're great!" (ignoring burn, churn, unit economics)
- **Not stage-agnostic:** Early-stage burn is acceptable; scale-stage burn is a problem
- **Not static:** Health is directional—are metrics improving or degrading?
- **Not just numbers:** Context matters (competitive pressure, market changes, team capacity)

### When to Use This Framework

**Use this when:**
- Preparing for board meetings or investor updates
- Quarterly business reviews (QBR)
- Fundraising preparation (know your numbers)
- Annual planning (identify improvement areas)
- You suspect problems but can't pinpoint them
- New PM/exec joining and needs health assessment

**Don't use this when:**
- You're pre-revenue (focus on product-market fit first)
- You're in pure research mode (not enough data)
- You need tactical guidance (use specific skills: feature, channel, pricing)

### Facilitation Source of Truth

Use `workshop-facilitation` as the default interaction protocol: session heads-up + entry modes (Guided, Context dump, Best guess), one-question turns in plain language, progress labels, interruption/pause handling, and numbered quick-select options (include `Other (specify)` when useful). This file defines the domain-specific assessment content; if there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 4 adaptive questions**, then delivers a comprehensive diagnostic with prioritized recommendations.

---

### Step 0: Gather Context

**Agent asks:**

"Let's diagnose your business health. I'll need metrics across four dimensions: growth, retention, unit economics, and capital efficiency.

**Company context:**
- Stage: (Pre-$10M ARR, $10M-$50M ARR, $50M+ ARR)
- Business model: (PLG, sales-led, hybrid)
- Target market: (SMB, mid-market, enterprise, mixed)

**Why this matters:** Benchmarks vary by stage. Early-stage optimizes for growth; scale-stage optimizes for efficiency.

Please provide the following metrics. Use 'unknown' if you don't have a metric."

---

### Step 1: Growth & Retention Metrics

**Agent asks:**

"**Growth & Retention:**

1. **Revenue:**
   - Current MRR or ARR: $___
   - Revenue growth rate: ___% (MoM or YoY)

2. **Retention:**
   - Monthly churn rate: ___%
   - NRR (Net Revenue Retention): ___%
   - Quick Ratio: ___ (or I can calculate it)

3. **Expansion:**
   - Expansion revenue as % of total MRR: ___%

4. **Cohort trends:**
   - Are recent cohorts retaining better or worse than older cohorts?
     1. Better (improving)
     2. Same (stable)
     3. Worse (degrading)
     4. Unknown"

**Based on answers, agent evaluates:**
- ✅ **Healthy growth:** Growth >40% YoY (growth stage) or >25% (scale stage)
- ✅ **Healthy retention:** NRR >100%, churn <5% monthly, Quick Ratio >2
- 🚨 **Growth problems:** Growth <20% YoY
- 🚨 **Retention problems:** NRR <100%, churn >5%, cohort degradation

---

### Step 2: Unit Economics Metrics

**Agent asks:**

"**Unit Economics:**

1. **Acquisition:**
   - CAC (Customer Acquisition Cost): $___
   - Blended or by channel? (If by channel, what's your best channel CAC?)

2. **Value:**
   - LTV (Lifetime Value): $___
   - LTV:CAC ratio: ___ (or I can calculate it)
   - Payback period: ___ months (or I can calculate it)

3. **Margins:**
   - Gross margin: ___%
   - Contribution margin (if known): ___%

4. **Trends:**
   - Is CAC increasing, stable, or decreasing over time?
     1. Decreasing (improving efficiency)
     2. Stable
     3. Increasing (diminishing returns)
     4. Unknown"

**Based on answers, agent evaluates:**
- ✅ **Healthy economics:** LTV:CAC >3:1, payback <12 months, gross margin >70%
- ⚠️ **Marginal economics:** LTV:CAC 2-3:1, payback 12-18 months
- 🚨 **Poor economics:** LTV:CAC <2:1, payback >24 months, gross margin <60%

---

### Step 3: Capital Efficiency Metrics

**Agent asks:**

"**Capital Efficiency:**

1. **Cash:**
   - Cash balance: $___
   - Monthly net burn rate: $___
   - Runway: ___ months (or I can calculate it)

2. **Efficiency ratios:**
   - Rule of 40: ___ (Growth % + Profit Margin %) (or I can calculate it)
   - Magic Number: ___ (S&M efficiency) (or I can calculate it)

3. **Operating expenses:**
   - S&M as % of revenue: ___%
   - R&D as % of revenue: ___%
   - Is OpEx growing faster than revenue?
     1. No (positive operating leverage)
     2. Yes (negative operating leverage)
     3. Unknown

4. **Profitability:**
   - Profit margin: ___%
   - Path to profitability: (already profitable, 6-12 months, 12-24 months, >24 months, unknown)"

**Based on answers, agent evaluates:**
- ✅ **Healthy efficiency:** Rule of 40 >40, magic number >0.75, runway >12 months
- ⚠️ **Acceptable efficiency:** Rule of 40 25-40, magic number 0.5-0.75, runway 6-12 months
- 🚨 **Poor efficiency:** Rule of 40 <25, magic number <0.5, runway <6 months

---

### Step 4: Deliver Comprehensive Diagnostic

**Agent synthesizes all metrics and delivers:**

1. **Overall Health Score** — Healthy / Moderate / Concerning / Critical
2. **Dimension Scores** — Growth, Retention, Economics, Efficiency
3. **Red Flags** — Critical, High Priority, Medium Priority
4. **Prioritized Recommendations** — Top 3-5 actions with expected impact
5. **Stage-Appropriate Benchmarks** — How you compare to peers

**Pick the output pattern by overall health, then read `references/diagnostic-output-templates.md` for the full output template to fill in:**

- **Pattern 1: Healthy** — all dimensions meet stage benchmarks, no critical red flags, improving trends → scorecard + key strengths + optimization opportunities + next-quarter actions + monitoring cadence + benchmark table
- **Pattern 2: Moderate (Fixable Issues)** — 1-2 dimensions have problems, medium-priority red flags, solvable with focus → scorecard + red flags + root cause analysis + prioritized 30-day/quarter action plan + 90-day success targets + "what not to do"
- **Pattern 3: Concerning (Urgent Action Required)** — multiple critical red flags, 2+ dimensions problematic → scorecard + critical red flags with timelines + 90-day survival plan (triage → stop the bleeding → stabilize) + day-90 success criteria + avoid list
- **Pattern 4: Critical (Existential Crisis)** — runway <3 months OR multiple critical failures (LTV:CAC <1:1, massive churn, no path to profitability) → Pattern 3 structure with urgent tone, shorter timelines, drastic measures (emergency board meeting, fundraise or cut burn 50%+ this week)

---

## Examples

### Example 1: Healthy Growth-Stage SaaS

**Metrics:**
- ARR: $20M, Growth: 60% YoY
- NRR: 115%, Churn: 2.5%
- LTV:CAC: 4:1, Payback: 10 months
- Rule of 40: 50, Runway: 18 months

**Diagnosis:** Healthy. Scale aggressively.

### Example 2: Moderate Health (Retention Issue)

**Metrics:**
- ARR: $15M, Growth: 40% YoY
- NRR: 95%, Churn: 5%
- LTV:CAC: 3.5:1, Payback: 12 months
- Rule of 40: 38, Runway: 12 months

**Diagnosis:** Moderate. Fix retention before scaling further.

### Example 3: Concerning (Multiple Issues)

**Metrics:**
- ARR: $8M, Growth: 25% YoY (slowing)
- NRR: 88%, Churn: 7% (increasing)
- LTV:CAC: 1.8:1, Payback: 20 months
- Rule of 40: 15, Runway: 8 months

**Diagnosis:** Concerning. Urgent action on retention and unit economics required.

---

## Common Pitfalls

1. **Celebrating Single Metrics** — "Revenue growing 50%!" while ignoring burn, churn, unit economics → scaling a broken model. Fix: look at all four dimensions together.
2. **Ignoring Stage-Specific Benchmarks** — "We're not profitable yet, is that bad?" at early stage → misplaced worry. Fix: early stage optimizes for growth and unit economics, not profitability; use stage-appropriate benchmarks.
3. **Focusing on Lagging Indicators Only** — "Churn is 5%, let's watch it" → by the time churn/NRR show problems, it's late. Fix: track leading indicators (usage, engagement, onboarding completion).
4. **Not Acting on Red Flags** — "NRR <100% for 3 quarters, we'll fix it eventually" → problems compound into crisis. Fix: set clear timelines; if a metric doesn't improve in X time, escalate.
5. **Trying to Fix Everything at Once** — improving growth, retention, CAC, and efficiency simultaneously → resources spread thin, nothing improves. Fix: prioritize top 1-3 issues; fix sequentially.

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — Detailed growth and retention metrics
- `saas-economics-efficiency-metrics` — Detailed unit economics and capital efficiency
- `finance-metrics-quickref` — Fast lookup for all metrics and benchmarks
- `feature-investment-advisor` — Uses health diagnostic to inform feature priorities
- `acquisition-channel-advisor` — Uses health diagnostic to inform channel priorities
- `finance-based-pricing-advisor` — Uses health diagnostic to inform pricing decisions

### External Frameworks
- **Bessemer Venture Partners:** "SaaS Metrics 2.0" — Comprehensive benchmarks
- **David Skok:** "SaaS Metrics" — Unit economics benchmarks
- **OpenView Partners:** SaaS benchmarking reports
- **Battery Ventures:** "State of SaaS" annual report

### Provenance
- Adapted from `research/finance/Finance_QuickRef.md` (Red flags table)
- Decision frameworks from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md`
- Benchmarks from `research/finance/Finance for Product Managers.md`
