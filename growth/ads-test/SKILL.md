---
name: ads-test
description: "A/B test design for paid ads: hypothesis framework, statistical significance calculator, test duration and sample size estimators, setup guides for Meta, Google, and LinkedIn experiments. Use when user says A/B test, split test, experiment design, statistical significance, or sample size."
user-invokable: false
tested_date: 2026-05-17
tested_with: claude-code v2.x
---

# A/B Test Design & Experiment Planning

<!-- Created: 2026-04-13 | v1.5 -->
<!-- Source: OpenClaudia/openclaudia-skills (ab-test-setup concept) -->

## Service lead generation and live changes

For quote/enquiry funnels, CRM outcomes or campaign/budget changes, read
[`Service lead-generation delivery checks`](../ads/references/lead-generation-delivery.md).
Use the applicable checks; a bounded task does not require a new full audit.
Keep unknown evidence unverified and reuse the account context already provided.

## Process

1. Understand what the user wants to test (creative, audience, bidding, landing page)
2. Build structured hypothesis using the framework below
3. Calculate required sample size and estimated duration
4. Recommend platform-specific test setup
5. Define success criteria and measurement plan

## Hypothesis Framework

Every test must start with a structured hypothesis:

```
IF we [change/action]
THEN [metric] will [increase/decrease] by [estimated %]
BECAUSE [reasoning based on data or insight]

Example:
IF we replace polished product shots with UGC creator videos
THEN Meta CTR will increase by 25-40%
BECAUSE Andromeda prioritizes diverse creative formats and UGC consistently outperforms polished in 2025-2026 benchmarks
```

### Hypothesis Quality Checklist
- [ ] Single variable being tested (isolate the change)
- [ ] Specific metric defined (not "performance")
- [ ] Estimated effect size stated (needed for sample size calculation)
- [ ] Timeframe defined
- [ ] Success/failure criteria clear before launch

## Statistical Significance Calculator

```
Required Sample Size (per variant):

delta = p × relative_MDE
n ≈ (Z_alpha + Z_beta)^2 × 2 × p × (1-p) / delta^2

Where:
- Z_alpha = 1.96 (for 95% confidence)
- Z_beta = 0.84 (for 80% power)
- p = baseline conversion rate
- relative_MDE = relative improvement as a fraction (20% = 0.20)
- delta = absolute rate difference (5% baseline × 20% relative = 0.01)
- This is a planning approximation for two independent, equal-sized variants;
  use a suitable power calculation for the actual design, especially rare events.

Simplified lookup:
```

| Baseline CVR | 5% relative MDE | 10% relative MDE | 20% relative MDE | 30% relative MDE |
|-------------|-----------------|------------------|------------------|------------------|
| 1% | 620,928 | 155,232 | 38,808 | 17,248 |
| 2% | 307,328 | 76,832 | 19,208 | 8,537 |
| 5% | 119,168 | 29,792 | 7,448 | 3,311 |
| 10% | 56,448 | 14,112 | 3,528 | 1,568 |
| 20% | 25,088 | 6,272 | 1,568 | 697 |

*Approximate per-variant samples, 95% confidence and 80% power.*

## Test Duration Estimator

```
Duration = Required Sample Size / Daily Traffic per Variant

Minimum duration: 7 days (capture weekly patterns)
Plan for seasonality and conversion lag; 28 days is not a forced stopping rule.
If volume cannot support the sample, report the test as underpowered or redesign it.
Learning phase: Google 7-14 days, Meta 3-7 days, LinkedIn 7-14 days

Inputs needed:
- Daily impressions or clicks
- Number of variants (2 = A/B, 3+ = multivariate)
- Baseline conversion rate
- Minimum detectable effect desired
```

### Duration Quick Estimates

| Total daily clicks, split 50/50 | 2% CVR, 20% relative MDE | 5% CVR, 20% relative MDE | 10% CVR, 20% relative MDE |
|-------------------------------|---------------------------|---------------------------|----------------------------|
| 100 | 385 days | 149 days | 71 days |
| 500 | 77 days | 30 days | 15 days |
| 1,000 | 39 days | 15 days | 8 days |
| 5,000 | 8 days | 3 days* | 2 days* |

*Allow weekly coverage and outcome lag even when the traffic sample arrives sooner.*
For example, 5% baseline/20% relative MDE needs about 7,448 clicks per arm;
100 total clicks/day split equally takes about 149 days, not 75.

A bundle of new campaigns, landing changes and budget shifts is a rollout. A
before/after comparison cannot isolate the effect of any one change. Select
qualified/instructed outcomes where reconciled; otherwise label quote metrics
as provisional. Do not call an underpowered city sample a winner.

## Platform-Specific Test Setup

### Meta Experiments
- Use Ads Manager > Experiments tab (not manual ad set duplication)
- Automatic audience splitting ensures no overlap
- Supported test types: A/B (creative, audience, placement), Holdout, Brand Survey
- Meta's Incremental Attribution (April 2025) provides AI-powered holdout testing for measuring real causal impact
- Budget: split evenly across variants; minimum $100/day per variant recommended
- Duration: 7-14 days typical; Meta auto-determines winner at 95% confidence

### Google Experiments
- Campaign Experiments (custom experiments) or Ad Variations
- Create experiment from existing campaign > select experiment type
- Traffic split: 50/50 recommended for fastest results
- Supported: bidding strategy, ad copy, landing page, audience
- Metrics: choose primary metric (conversions, CPA, ROAS) before launch
- Duration: 14-30 days recommended; minimum 2 weeks for bidding tests

### LinkedIn A/B Testing
- Built into Campaign Manager for Sponsored Content
- Duplicate ad set with single variable change
- Target: same audience segment with automatic rotation
- Minimum budget: $50/day per variant
- Key metrics: CTR (>0.44% benchmark), CPL, Lead Form CVR (13% benchmark)
- Duration: 14-21 days (LinkedIn's smaller daily volumes require longer tests)

### TikTok Split Testing
- Available in TikTok Ads Manager > Create A/B Test
- Test types: targeting, bidding, creative
- Auto-splits audience to avoid contamination
- Minimum 7 days, recommended 14 days
- Budget: minimum $20/day per ad group
- Creative tests: isolate hook (first 2-3 seconds) as the primary variable
- TikTok's enhanced split testing supports modular test variables (targeting, creative, budget, placement) via Smart+ since 2025

## What to Test (Priority Order)

### High Impact (test first)
1. **Creative concept** (different messaging angles, not just color changes)
2. **Hook/first 3 seconds** (video opening on Meta, TikTok, YouTube)
3. **Offer structure** (pricing, discount type, free trial length)
4. **Landing page** (headline, CTA, form length)
5. **Bidding strategy** (tCPA vs tROAS vs Maximize Conversions)

### Medium Impact
6. **Audience targeting** (interest vs lookalike vs broad)
7. **Ad format** (static vs video vs carousel)
8. **CTA button** (Learn More vs Sign Up vs Shop Now)
9. **Campaign structure** (CBO vs ABO, consolidated vs segmented)

### Low Impact (test last)
10. **Ad scheduling** (time of day, day of week)
11. **Device targeting** (mobile vs desktop)
12. **Minor copy variations** (word substitutions without concept change)

## Common Testing Mistakes to Avoid

- Testing too many variables at once (no clear winner attribution)
- Ending tests too early (before statistical significance)
- Testing during atypical periods (holidays, launches, incidents)
- Comparing unequal time periods
- Not documenting learnings (build institutional knowledge)
- Testing small changes when big changes are needed (optimize vs innovate)
- Ignoring learning phase on automated platforms

## Output Format

```
## A/B Test Plan

### Hypothesis
IF [change]
THEN [metric] will [direction] by [amount]
BECAUSE [reasoning]

### Test Design
| Parameter | Value |
|-----------|-------|
| Platform | [platform] |
| Test Type | [A/B / Multivariate] |
| Variable | [what's being changed] |
| Control | [current state] |
| Variant | [proposed change] |
| Primary Metric | [KPI] |
| Traffic Split | [50/50 / other] |

### Sample Size & Duration
| Metric | Value |
|--------|-------|
| Baseline CVR | [X%] |
| MDE | [X%] |
| Required Sample | [N per variant] |
| Daily Traffic | [N clicks/day] |
| Est. Duration | [X days] |
| Min Duration | 7 days |

### Success Criteria
- Winner declared at 95% confidence
- [Primary metric] improvement of [X%]+ sustained over [Y] days
- No negative impact on [secondary metric]

### Setup Instructions
[Platform-specific step-by-step]
```
