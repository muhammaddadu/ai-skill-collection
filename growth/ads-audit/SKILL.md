---
name: ads-audit
description: "Audit active paid-advertising accounts across platforms, with evidence-backed health scores and a prioritized action plan. Use for multi-platform account-health audits; use a platform-specific `ads-*` skill for one channel."
user-invokable: false
tested_date: 2026-05-17
tested_with: claude-code v2.x
---

# Full Multi-Platform Ads Audit

This audit operates under the **10-Principle Thinking Framework** (see
`../ads/references/thinking-framework.md`). OBSERVE (External + Internal)
dominates data collection, THINK + CONNECT (Lateral) dominate analysis,
CONNECT (System) + ACCEPT dominate synthesis and prioritization. If the
audit feels mechanical, you are skipping a principle.

## Process

1. **Collect account data**: request exports, screenshots, or API access
2. **Validate**: confirm at least one platform's data is available before proceeding
3. **Detect business type**: analyze account signals per ads orchestrator
4. **Identify active platforms**: determine which platforms are in use and load each corresponding platform skill, including `ads-apple`, `ads-amazon`, and `ads-youtube` when applicable. Count overlapping Google/YouTube spend once.
5. **Run audit roles** (delegate only when available and authorized; otherwise run inline sequentially):
   - `audit-google`: Conversion tracking, wasted spend, structure, keywords, ads, settings (80 checks; G01-G61 + 19 hyphenated v1.5+ IDs incl. AI Max)
   - `audit-meta`: Pixel/CAPI health, creative fatigue, structure, audience (50 checks; M01-M40 + 10 hyphenated v1.5+ IDs incl. Andromeda)
   - `audit-creative`: LinkedIn, TikTok, Microsoft creative checks + cross-platform synthesis
   - `audit-tracking`: LinkedIn, TikTok, Microsoft tracking + cross-platform tracking health
   - `audit-budget`: LinkedIn, TikTok, Microsoft budget/bidding + cross-platform allocation
   - `audit-compliance`: All-platform compliance, settings, performance benchmarks
6. **Validate**: verify each role returned valid scores with required fields before aggregating
7. **Score**: calculate per-platform and aggregate Ads Health Score (0-100)
8. **Report**: generate prioritized action plan with Quick Wins

## Data Collection

Ask the user for available data. Accept any combination:
- Google Ads: account export, Change History, Search Terms Report
- Meta Ads: Ads Manager export, Events Manager screenshot, EMQ scores
- LinkedIn Ads: Campaign Manager export, Insight Tag status
- TikTok Ads: Ads Manager export, Pixel/Events API status
- Microsoft Ads: account export, UET tag status, import validation results

If no exports available, audit from screenshots or manual data entry.

## Scoring

Read `../ads/references/scoring-system.md` for the canonical algorithm, category
weights, grades, severity definitions, and Quick Wins criteria. Do not maintain
a second copy here. Use the platform skill for checks not covered by the shared
catalog and disclose any unresolved scoring conflict.

Report missing evidence as unverified, not as a pass. Publish the assessed spend
and check coverage alongside scores; do not imply that unassessed accounts were
audited. If budget shares are unknown, report platform scores without inventing
a spend-weighted aggregate.

## Output Files

- `ADS-AUDIT-REPORT.md`: Comprehensive multi-platform findings
- `ADS-ACTION-PLAN.md`: Prioritized recommendations (Critical > High > Medium > Low)
- `ADS-QUICK-WINS.md`: Items fixable in <15 minutes with high impact

## Report Structure

### Executive Summary
- Aggregate Ads Health Score (0-100) with grade
- Per-platform scores
- Business type detected
- Active platforms identified
- Top 5 critical issues across all platforms
- Top 5 quick wins across all platforms

### Per-Platform Sections
Each platform section includes:
- Platform Health Score with grade
- Category breakdown with pass/warning/fail per check
- Platform-specific Quick Wins
- Detailed findings with remediation steps

### Cross-Platform Analysis
- Budget allocation assessment (actual vs recommended)
- Tracking consistency (are all platforms tracking the same events?)
- Creative consistency (is messaging aligned across platforms?)
- Attribution overlap (are platforms double-counting conversions?)

### Strategic Recommendations
- Platform prioritization based on business type
- Budget reallocation recommendations
- Scaling opportunities (platforms/campaigns ready to scale)
- Kill list (campaigns/ad groups to pause immediately)
