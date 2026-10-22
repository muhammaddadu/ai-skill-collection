# Service lead generation: delivery and outcome checks

Use for quote/enquiry funnels, live campaign replacements, or budget reallocations.
This is reusable guidance, not authority to change an account. Keep account IDs,
client data, budgets and release evidence in the project's handover.

## Choose the outcome before choosing the automation

- Separate page view, form start, valid quote, qualified lead, instructed matter,
  completed matter and collected fee. A button click is not the next business state.
- Audit actual primary/secondary actions and campaign goals. Do not infer primary
  status from the goal-category picker or assume all imported GA4 events are useful
  bidding signals. Avoid counting both browser and CRM copies of one event.
- For professional services, reconcile quoted professional fees, VAT, third-party
  outlays, retained supplements, refunds and delivery costs. Unknown breakdowns
  must not fall back to the customer total. A quoted net fee is still not revenue.
- Prefer cost per qualified/instructed matter and retained contribution once the
  CRM reconciliation is reliable. Until then, call quote CPA a provisional proxy.
- Define a minimal event contract: opaque quote/lead ID, stage and event time,
  allowed campaign/click attribution, service, referring location, actual property
  location when separately confirmed, value/currency/value basis and reconciliation
  status. Preserve consent; do not put personal details in URLs or GA event fields.
- Reconcile cohorts through their conversion lag. Visitor city, query city,
  referring-page city and property city are different dimensions. County results
  do not prove city profitability. Show counts and uncertainty for small samples.

## Match the complete journey

- Align search intent, ad, city/service page, CTA, quote page and hosted form.
  Use allowlisted intent/location values and a safe generic fallback.
- Carry approved intent, source-page/location and permitted attribution through
  the CTA and handoff. Referral context must not silently fill a property address.
- A personalised heading does not prove hosted-widget preselection. Inspect and
  test the widget contract; retain an editable choice and document supplier-owned
  work. Do not patch around it with hidden DOM manipulation or fake submissions.
- Reduce competing navigation, repeated price guides and unnecessary inputs on
  the quote path. Retain costs, help, identity/regulation, privacy and cookie choices.
- Test mobile, keyboard focus, labels, groups, validation/error announcements and
  recovery. Inspect the rendered result; a screenshot alone does not prove behavior.
- Confirm initial HTML H1/canonical/source links and actual asset bytes/content
  types after deployment. HTTP 200, successful build and client-side rendering can
  hide fallback HTML, missing assets and incorrect MIME metadata.
- Use generated regional imagery as illustration, not evidence of an actual local
  office, exact street or client property. Preserve approved branding. Verify rights,
  provenance, current platform rules and any applicable disclosure requirements.

## Replace campaigns without multiplying the budget

1. Confirm account identity, current serving status, approved total envelope and
   whether it means average daily budgets or a strict cash limit. Inventory shared
   budgets, experiments, schedules and already-spent amounts separately.
2. Build the replacement paused. A successful copy notification is not proof that
   ads, keywords, assets, negative lists or geography copied. Read back each.
3. Verify actual inclusion/exclusion locations and presence/interest setting,
   networks, goals, bidding, URL expansion, dates and schedules. Defaults can widen
   geography even when other campaign settings appear copied.
4. Read back keyword match types, duplicate coverage and negative-list membership.
   Preserve reviewed exclusions. Add new exact/phrase negatives from query evidence;
   do not blanket-exclude free quotes, online services or first-time buyers.
5. Check final URLs and every intended query parameter. Preview bulk imports for
   exact campaign/group scope, counts and errors; apply only reviewed changes.
   Imports must not create duplicate ads/keywords on a retry.
6. Confirm usable sitelinks/callouts/images and city-group associations. Do not
   attach disapproved assets or change account/shared assets as a scope workaround.
7. For replacement, pause superseded serving campaigns before enabling the
   replacement. For a native experiment, verify the actual traffic/budget-sharing
   semantics; do not assume a standalone copy shares its source's budget.
8. Read back final enabled statuses and combined budgets. Pausing a campaign does
   not erase its spend earlier that day. Average daily budgets are not strict daily
   cash caps; budget changes can retain the day's higher spending limit.
9. Save a screenshot and a compact before/after ledger with IDs, amounts, time,
   chosen rationale, rollback, and pending checks. A submitted action is not proof
   of activation. Keep repository/application deployment evidence separate.

## Decide what to retain, test or remove

- Retaining a lower quote-CPA campaign is a provisional choice, not proof of
  incremental instructions. Inspect brand capture, placement/query quality, lead
  duplication, actual instructions, fees and team capacity where data allows.
- Compare retaining the baseline, a smaller capped allocation, and pausing. Show
  the opportunity cost and uncertainty. Do not invent a profitable winner.
- Reallocate within the total envelope by reducing the donor first, then increasing
  the recipient. Do not multiply budgets across every drafted city or service.
- Avoid repeated bid/budget/creative changes during learning without a material
  failure. Record necessary changes and their start times. Pre/post comparisons
  spanning several changes are observational, not a causal A/B result.
- More automation is an option: test broader matching or value bidding when the
  outcome signals, query controls and sample support it. Neither manual/exact
  targeting nor AI expansion is a universal answer.
- Ad Strength and Quality Score diagnose different aspects of quality; neither
  proves profitability. If table/detail/editor ratings disagree, record the exact
  ad ID and both readings. Recheck once rather than creating duplicate versions or
  weakening message match merely to chase a badge. Eligibility, approval, learning
  and actual serving are also distinct states.

## Next review and evidence limits

Compare spend, valid/qualified quotes, mature instructions, retained fees, cost
per stage and lost reasons by service/city. Include brand/non-brand and channel
mix when available. Check failures promptly; assess commercial results after
sufficient lag and sample. A suggested review is not a scheduled automation.
Missing GA/CRM/field-performance data is unverified, not a passing score. Never
claim a complete audit or measured uplift from local tests or a launch alone.

## Primary references

Verified 22 October 2026; recheck for platform changes:
- [Google budget-change behavior](https://support.google.com/google-ads/answer/10487143)
- [Google Quality Score diagnostic](https://support.google.com/google-ads/answer/6167118)
- [Google consent modes](https://developers.google.com/tag-platform/security/concepts/consent-mode)
- [Google consent implementation](https://developers.google.com/tag-platform/security/guides/consent)
