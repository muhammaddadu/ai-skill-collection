---
name: ads-math
description: "PPC financial calculator: CPA, ROAS, CPL, break-even, impression share opportunity sizing, budget forecasting, LTV:CAC, MER. No API access needed — works with pasted export data. Use when user says PPC math, break-even, ROAS calculator, budget forecast, impression share, LTV CAC, or MER."
user-invokable: false
tested_date: 2026-05-17
tested_with: claude-code v2.x
---

# PPC Financial Calculator & Modeling

<!-- Created: 2026-04-13 | v1.5 -->
<!-- Source: itallstartedwithaidea/google-ads-skills (PPC math concept) -->

## Service lead generation and live changes

For quote/enquiry funnels, CRM outcomes or campaign/budget changes, read
[`Service lead-generation delivery checks`](../ads/references/lead-generation-delivery.md).
Use the applicable checks; a bounded task does not require a new full audit.
Keep unknown evidence unverified and reuse the account context already provided.

## Process

1. Ask the user what calculation they need (or detect from context)
2. Collect required inputs (from pasted data, exports, or verbal description)
3. Perform calculations with clear formulas shown
4. Present results with interpretation and recommendations
5. Flag any concerning metrics or benchmarks

## Calculators

### 1. CPA Calculator

```
CPA = Total Spend / Total Conversions

Inputs needed:
- Total ad spend (period)
- Total conversions (same period)

Output:
- CPA with period context
- CPA trend (if historical data provided)
- Comparison to industry benchmark (from benchmarks.md)
```

### 2. ROAS Calculator

```
ROAS = Revenue from Ads / Ad Spend
ROAS% = Revenue / Spend × 100
Revenue-minus-media return% = (Revenue - Spend) / Spend × 100
Profit ROI% = (Attributable contribution before acquisition - Acquisition cost) / Acquisition cost × 100

Inputs needed:
- Total ad spend
- Total revenue attributed to ads

Output:
- ROAS as ratio (e.g., 3.5x) and percentage (350%); revenue-minus-media
  return would be 250%, which is not profit ROI without delivery/other costs
- Break-even ROAS (based on margins if provided)
- Comparison to platform benchmarks
```

### 3. Break-Even Analysis

```
Break-Even CPA = Average Order Value × Profit Margin
Break-Even ROAS = 1 / Profit Margin

Inputs needed:
- Average order value (AOV) OR average deal value
- Profit margin (gross margin %)
- Current CPA or ROAS

Output:
- Maximum profitable CPA
- Minimum profitable ROAS
- Current headroom (how far above/below break-even)
- Recommendation: scale, maintain, or cut
```

### 4. Impression Share Opportunity

```
Impression Share Lost (Budget) = opportunity from budget increase
Impression Share Lost (Rank) = opportunity from bid/quality improvement

Revenue Opportunity = Current Revenue × (1 / Current IS - 1)

Inputs needed:
- Current impression share %
- IS lost to budget %
- IS lost to rank %
- Current spend and conversions

Output:
- Estimated additional conversions from full IS
- Budget needed for full IS (estimated)
- Priority: budget increase vs quality improvement
```

### 5. Budget Forecasting

```
Projected Spend = Daily Budget × Days in Period
Projected Conversions = Projected Spend / Historical CPA
Projected Revenue = Projected Conversions × AOV

Scaling scenarios:
- Conservative: +20% budget → estimated impact
- Moderate: +50% budget → estimated impact
- Aggressive: +100% budget → estimated impact (with diminishing returns caveat)

Inputs needed:
- Current daily budget
- Historical CPA (last 30 days)
- Forecast period
- AOV (if revenue projection needed)

Output:
- 3 scenarios with spend, conversions, revenue projections
- Diminishing returns warning for aggressive scaling
- State assumptions, approved envelope and platform-specific budget behavior;
  a 20% planning step is not a universal technical limit
```

### 6. LTV:CAC Ratio

```
CAC = Total Marketing Spend / New Customers Acquired
LTV = Average Revenue per Customer × Average Customer Lifespan
LTV:CAC Ratio = LTV / CAC

Inputs needed:
- Total marketing spend (all channels)
- New customers acquired
- Average revenue per customer (monthly or annual)
- Average customer lifespan (months)
- Optional: gross margin for unit economics

Output:
- LTV:CAC ratio with interpretation:
  - <1:1 = losing money on every customer
  - 1:1-2:1 = break-even to marginal
  - 3:1 = healthy (SaaS benchmark)
  - 5:1+ = may be under-investing in growth
- Payback period: months to recover CAC
- Recommendation based on ratio
```

### 7. MER (Marketing Efficiency Ratio)

```
MER = Total Revenue / Total Marketing Spend

Inputs needed:
- Total business revenue (period)
- Total marketing spend across ALL channels (same period)

Output:
- MER ratio (e.g., 5.0x)
- Interpretation:
  - E-commerce: 3-5x typical, 8x+ excellent
  - SaaS: 5-10x typical (higher margins)
  - Local service: 3-8x typical
- Comparison to business-type benchmark
- Note: MER captures blended efficiency including organic, brand, and retention
```

### Lead-generation economics

```
Cost per quote = Ad spend / Valid quotes
Cost per instructed matter = Ad spend / Actual instructed matters
All-in acquisition cost per matter = (Ad spend + Agency fees + Other acquisition costs) / Actual instructed matters
Expected contribution per quote before acquisition = P(instruction) × Expected contribution per instruction - Per-quote handling cost
```

Use mature, reconciled cohorts and the same date/attribution basis. Zero outcomes
make the unit cost undefined, not zero. Expected contribution per instruction
should allow for completion/abort rates, retained fees excluding VAT/outlays,
delivery costs and refunds. Quoted fees and deposits are not earned revenue.
Unknown value breakdowns must not become customer-total ROAS or an invented
instruction rate. Conditional scenarios are not forecasts or causal evidence.

### Incrementality & Advanced Measurement

For advanced accounts evaluating cross-channel contribution:
- **Meta Incremental Attribution** (launched April 2025): AI-powered holdout testing measuring real causal impact. Evaluate if budget exceeds $5K/month.
- **Google Meridian** (2025): Open-source Marketing Mix Model for incrementality measurement across channels.
- These tools complement PPC math calculations by measuring what would NOT have happened without the ad spend.

For large accounts detecting small effects (5% MDE), multiply the 10% MDE sample by ~4x.

## Quick Formulas Reference

| Metric | Formula |
|--------|---------|
| CPA | Spend / Conversions |
| ROAS | Revenue / Spend |
| CTR | Clicks / Impressions × 100 |
| CVR | Conversions / Clicks × 100 |
| CPC | Spend / Clicks |
| CPM | (Spend / Impressions) × 1,000 |
| CPL | Spend / Leads |
| Break-Even CPA | AOV × Margin% |
| Break-Even ROAS | 1 / Margin% |
| LTV | ARPU × Avg Lifespan |
| CAC | Total Marketing / New Customers |
| MER | Total Revenue / Total Marketing |
| Impression Share Opp | Revenue × (1/IS - 1) |

## Output Format

```
## PPC Financial Analysis

### [Calculator Name]

**Inputs:**
- [Listed inputs with values]

**Results:**
| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| [Metric] | [Value] | [Benchmark] | PASS/WARNING/FAIL |

**Interpretation:**
[1-2 sentence analysis]

**Recommendation:**
[Actionable next step]
```

## Data to Request

If the user doesn't provide enough data, ask for:
- Platform and campaign type
- Time period for analysis
- Spend and conversion data
- Revenue data (if ROAS/break-even needed)
- Margin data (if break-even/LTV needed)
- Business type (for benchmark comparison)
