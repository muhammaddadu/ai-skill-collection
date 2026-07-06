---
name: finance-based-pricing-advisor
description: Evaluate pricing changes using ARPU, conversion, churn risk, NRR, and payback. Use when deciding whether a pricing move should ship.
intent: >-
  Evaluate the **financial impact** of pricing changes (price increases, new tiers, add-ons, discounts) using ARPU/ARPA analysis, conversion impact, churn risk, NRR effects, and CAC payback implications. Use this to make data-driven go/no-go decisions on proposed pricing changes with supporting math and risk assessment.
type: interactive
best_for:
  - "Evaluating price increases, discounts, or new packaging"
  - "Estimating churn and conversion risk before a pricing change"
  - "Making a go/no-go call on monetization changes"
scenarios:
  - "Should we raise prices 15% for new customers next quarter?"
  - "Evaluate a new premium tier for our SaaS product"
  - "Help me assess whether an annual discount will improve revenue"
---


## Purpose

Evaluate the **financial impact** of pricing changes (price increases, new tiers, add-ons, discounts) using ARPU/ARPA analysis, conversion impact, churn risk, NRR effects, and CAC payback implications. Use this to make data-driven go/no-go decisions on proposed pricing changes with supporting math and risk assessment.

**What this is:** Financial impact evaluation for pricing decisions you're already considering.

**What this is NOT:** Comprehensive pricing strategy design, value-based pricing frameworks, willingness-to-pay research, competitive positioning, psychological pricing, packaging architecture, or monetization model selection. For those topics, see the future `pricing-strategy-suite` skills.

This skill assumes you have a specific pricing change in mind and need to evaluate its financial viability.

## Outputs

**Artifact:** Go/no-go recommendation on a specific pricing change (implement / test first / modify / don't change) with revenue, churn, conversion, and CAC-payback math; optional sensitivity scenarios
**Format:** Markdown
**Location:** Delivered in conversation; saved to a file only if the user asks
**Audience:** PM / founder presenting the pricing decision to leadership or board

## Key Concepts

### The Pricing Impact Framework

A systematic approach to evaluate pricing changes financially:

1. **Revenue Impact** — How does this change ARPU/ARPA?
   - Direct revenue lift from price increase; revenue loss from reduced conversion or increased churn; net revenue impact

2. **Conversion Impact** — How does this affect trial-to-paid or sales conversion?
   - Higher prices may reduce conversion rate; better packaging may improve it; test assumptions

3. **Churn Risk** — Will existing customers leave due to price change?
   - Grandfathering strategy (protect existing customers); churn risk by segment (SMB vs. enterprise); churn elasticity

4. **Expansion Impact** — Does this create or block expansion opportunities?
   - New premium tier = upsell path; usage-based pricing = expansion as customers grow; add-ons = cross-sell

5. **CAC Payback Impact** — Does the pricing change affect unit economics?
   - Higher ARPU = faster payback; lower conversion = higher effective CAC; net effect on LTV:CAC

### Pricing Change Types

**Direct monetization changes:**
- Price increase (all customers or new customers only)
- New premium tier (create upsell path)
- Paid add-on (monetize previously free feature)
- Usage-based pricing (charge for consumption)

**Discount strategies:**
- Annual prepay discount (improve cash flow)
- Volume discounts (larger deals)
- Promotional pricing (temporary price reduction)

**Packaging changes:**
- Feature bundling (combine features into tiers)
- Unbundling (separate features into add-ons)
- Pricing metric change (seats → usage, or vice versa)

### Anti-Patterns (What This Is NOT)

- **Not value-based pricing:** This evaluates a proposed change, not "what should we charge?"
- **Not WTP research:** This analyzes impact, not "what will customers pay?"
- **Not competitive positioning:** This is financial analysis, not market positioning
- **Not packaging architecture:** This evaluates one change, not redesigning all tiers

### When to Use This Framework

**Use this when:**
- You have a specific pricing change to evaluate (e.g., "Should we raise prices 20%?")
- You need to quantify revenue, churn, and conversion trade-offs
- You're deciding between pricing change options (test A vs. B)
- You need to present pricing change impact to leadership or board

**Don't use this when:**
- You're designing pricing strategy from scratch (use value-based pricing frameworks)
- You haven't validated willingness-to-pay (do customer research first)
- You don't have baseline metrics (ARPU, churn, conversion rates)
- Change is too small to matter (<5% price change, <10% of customers affected)

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol: session heads-up + entry modes (Guided, Context dump, Best guess), one-question turns in plain language, progress labels, interruption/pause handling, and numbered quick-select options (include `Other (specify)` when useful). This file defines the domain-specific assessment content; if there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 4 adaptive questions**, offering **3-5 enumerated options** at decision points.

---

### Step 0: Gather Context

**Agent asks:**

"Let's evaluate the financial impact of your pricing change. Please provide:

**Current pricing:**
- Current ARPU or ARPA
- Current pricing tiers (if applicable)
- Current monthly churn rate
- Current trial-to-paid conversion rate (if relevant)

**Proposed pricing change:**
- What change are you considering? (price increase, new tier, add-on, etc.)
- New pricing (if known)
- Affected customer segment (all, new only, specific tier)

**Business context:**
- Total customers (or MRR/ARR)
- CAC (to assess payback impact)
- NRR (to assess expansion context)

You can provide estimates if you don't have exact numbers."

---

### Step 1: Identify Pricing Change Type

**Agent asks:**

"What type of pricing change are you considering?

1. **Price increase** — Raise prices for new customers, existing customers, or both
2. **New premium tier** — Add higher-priced tier with additional features
3. **Paid add-on** — Monetize a new or existing feature separately
4. **Usage-based pricing** — Charge for consumption (seats, API calls, storage, etc.)
5. **Discount strategy** — Annual prepay discount, volume pricing, or promotional pricing
6. **Packaging change** — Rebundle features, change pricing metric, or tier restructure

Choose a number, or describe your specific pricing change."

**Based on the selection, ask the matching follow-up question set — read `references/change-type-questions.md` for the six per-type question sets** (details, affected segment, adoption/cannibalization, trade-offs).

---

### Step 2: Assess Expected Impact

**Agent asks:**

"Now let's quantify the impact. Based on your pricing change, estimate:

**Revenue impact:**
- Current ARPU: $___
- Expected new ARPU: $___
- ARPU lift: ___%

**Conversion impact:**
- Current conversion rate: ___%
- Expected new conversion rate: ___%
- Conversion change: [increase / decrease / no change]

**Churn risk:**
- Current monthly churn: ___%
- Expected churn after change: ___%
- Churn risk: [low / medium / high]

**Expansion impact:**
- Does this create expansion opportunities? (new tier to upgrade to, usage growth)
- Expected NRR change: ___% → ___%

You can provide estimates. We'll model scenarios (conservative, base, optimistic)."

---

### Step 3: Evaluate Current State

**Agent asks:**

"To assess whether this pricing change makes sense, I need your current baseline:

**Current metrics:**
- MRR or ARR: $___
- Number of customers: ___
- ARPU/ARPA: $___
- Monthly churn rate: ___%
- NRR: ___%
- CAC: $___
- LTV: $___

**Growth context:**
- Current growth rate: ___% MoM or YoY
- Target growth rate: ___%

**Competitive context:**
- Are you priced below, at, or above market?
- Competitive pressure: (low, medium, high)"

---

### Step 4: Deliver Recommendations

**Agent synthesizes:** revenue impact (ARPU lift × customer base), conversion impact (new customers affected), churn impact (existing customers affected), net revenue impact, CAC payback impact, risk assessment.

**Pick the recommendation pattern, then read `references/recommendation-templates.md` for the full output template to fill in:**

- **Pattern 1: Implement Broadly** — net revenue impact clearly positive (>10% ARPU lift, <5% churn risk), minimal conversion impact, strong value justification → implementation plan (grandfathering, value comms, 30-60 day monitoring) + timeline + success criteria
- **Pattern 2: Test First (A/B Test)** — uncertain impact (wide conservative-to-optimistic range), moderate churn/conversion risk, base large enough to test → control/test cohort design, 60-90 day duration, tracked metrics, roll-out vs. kill decision criteria
- **Pattern 3: Modify Approach** — original proposal has significant risk and a better alternative exists → alternatives (smaller increase, grandfather + raise for new only, segment-based pricing) with a specific recommendation
- **Pattern 4: Don't Change Pricing** — net revenue impact negative or marginal, high churn risk without offsetting gains → what would need to change, alternative strategies (retention, expansion, CAC), when to revisit

---

### Step 5: Sensitivity Analysis (Optional)

**Agent offers:**

"Want to see what-if scenarios?

1. **Optimistic case** — Higher ARPU lift, lower churn
2. **Pessimistic case** — Lower ARPU lift, higher churn
3. **Breakeven analysis** — What churn rate makes this neutral?

Or ask any follow-up questions."

**Agent can provide:** scenario modeling, sensitivity tables (if churn is X%, revenue impact is Y), comparison to alternative pricing strategies.

---

## Examples

### Example 1: Price Increase (Good Case)

**Scenario:** 20% price increase for new customers only

**Current state:**
- ARPU: $100/month, Customers: 1,000, MRR: $100K
- Churn: 3%/month, New customers/month: 50

**Proposed change:** New customer pricing $120/month (+20%); existing grandfathered at $100

**Impact:** New customer ARPU $120 (+20%); churn risk low (existing protected); conversion impact minimal (<5% drop estimated)

**Recommendation:** Implement. Net revenue impact +$12K/year with low risk.

### Example 2: Price Increase (Risky)

**Scenario:** 30% price increase for all customers

**Current state:**
- ARPU: $50/month, Customers: 5,000, MRR: $250K
- Churn: 5%/month (already high)

**Proposed change:** All customers to $65/month (+30%)

**Impact:**
- ARPU lift: +30% = +$75K MRR
- Churn risk: High (5% → 8% estimated)
- Churn-driven loss: 3% × 5,000 × $65 = -$9.75K MRR/month
- Net: +$65K MRR but an accelerating churn problem

**Recommendation:** Don't change. Fix retention first (reduce 5% churn), then raise prices.

### Example 3: New Premium Tier

**Scenario:** Add $500/month premium tier

**Current state:** Top tier $200/month (500 customers), ARPA $200

**Proposed change:** New $500/month tier with advanced features; expected adoption 10% of current top tier (50 customers)

**Impact:**
- Upsell revenue: 50 × ($500 - $200) = +$15K MRR
- Cannibalization risk: Low (features justify premium)
- NRR impact: 105% → 110%

**Recommendation:** Implement. Creates expansion path, minimal cannibalization risk.

---

## Common Pitfalls

1. **Ignoring Churn Impact** — "Raise prices 30% and make $X more!" with no churn modeling → churn wipes out the gains. Fix: model conservative/base/optimistic churn scenarios and net them against the lift.
2. **Not Grandfathering Existing Customers** — raising prices for everyone effective immediately → churn spike from customers who feel betrayed. Fix: grandfather existing; raise for new customers only.
3. **Testing Without Statistical Power** — "We tested on 10 customers and it worked!" → results are noise. Fix: 100+ customers per cohort for 60-90 days.
4. **Pricing Changes Without Value Justification** — "We're raising prices because we need more revenue" → customers see price without value; churn. Fix: tie increases to value improvements (features, support, outcomes).
5. **Ignoring CAC Payback Impact** — "Higher ARPU is always better!" → if conversion drops 30%, effective CAC and payback explode. Fix: calculate payback impact; higher ARPU with lower conversion can make it worse.
6. **Annual Discounts That Hurt Margin** — 30% annual prepay discount → customers lock in low prices; LTV destroyed. Fix: cap annual discounts at 10-15%; balance cash flow against LTV.
7. **Copycat Pricing** — "Competitor raised prices, so should we" → their customers, value prop, and cost structure differ. Fix: use competitors as data points; decide from your own unit economics.
8. **Premature Optimization** — A/B testing 47 price points → analysis paralysis on 5% optimizations while missing 50% growth opportunities. Fix: big changes (tiers, packaging, add-ons) first; micro-optimize later.
9. **Forgetting Expansion Revenue** — maximizing ARPU at acquisition → high entry price blocks landing customers and expansion. Fix: consider land-and-expand — lower entry, higher expansion via upsells.
10. **No Communication Plan** — announcing a price rise with no customer comms → surprised customers churn; reputation damage. Fix: communicate 30-60 days ahead; emphasize value, not just price.

---

## References

### Related Skills
- `saas-revenue-growth-metrics` — ARPU, ARPA, churn, NRR metrics used in pricing analysis
- `saas-economics-efficiency-metrics` — CAC payback impact of pricing changes
- `finance-metrics-quickref` — Quick lookup for pricing-related formulas
- `feature-investment-advisor` — Evaluates whether to build features that enable pricing changes
- `business-health-diagnostic` — Broader business context for pricing decisions

### External Frameworks (Comprehensive Pricing Strategy)
These are OUTSIDE the scope of this skill but relevant for broader pricing work:

- **Value-Based Pricing** — Price based on value delivered, not cost
- **Van Westendorp Price Sensitivity** — WTP research methodology
- **Conjoint Analysis** — Feature-to-price trade-off research
- **Good-Better-Best Packaging** — Tier architecture design
- **Price Anchoring & Decoy Pricing** — Psychological pricing tactics
- **Patrick Campbell (ProfitWell):** Pricing research and benchmarks

### Future Skills (Comprehensive Pricing)
For topics NOT covered here, see future `pricing-strategy-suite`:
- `value-based-pricing-framework` — How to price based on value
- `willingness-to-pay-research` — WTP research methods
- `packaging-architecture-advisor` — Tier and bundle design
- `pricing-psychology-guide` — Anchoring, decoys, framing
- `monetization-model-advisor` — Seat-based vs. usage vs. outcome pricing

### Provenance
- Adapted from `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` (Decision Framework #3)
- Pricing scenarios from `research/finance/Finance for Product Managers.md`
