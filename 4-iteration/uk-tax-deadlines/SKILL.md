---
name: uk-tax-deadlines
description: "Build an evidence-backed UK tax and company-filing calendar with payment clearing dates and verified submission status. Use for deadlines and overdue obligations across taxes; use uk-corporation-tax-reminders for a specific CT reminder."
metadata:
  type: workflow
  source_reviewed: 2026-10-31
---

# Uk Tax Deadlines

## Output
Return a concise obligation table for the owner/adviser: entity, tax/filing, exact period, statutory due date, payment-method action date, evidence of status and next action. Save it only when requested or required by the workspace workflow. A saved calendar is not a scheduled reminder or filed return.

## Establish dates and status
Use the user's timezone and date, original notices, current accounts and live authority records where accessible. Resolve conflicting dates explicitly. Do not accept “deadline tonight” without reading the notice, but continue useful preparation while resolving it. Identify the taxpayer and tax: a personal Self Assessment paper-return deadline is not a company CT deadline.

Keep payment, return submission, return acceptance, assessment and bank/authority receipt separate. Supersede stale saved-draft status with a public filing and acceptance acknowledgement when verified. No posted liability or an empty statement does not prove no tax is due, particularly before a return is filed. A submitted payment can take time to appear; inspect history/credits and receipts before retrying.

## Corporation Tax
A CT accounting period cannot exceed twelve months. First statutory accounts may span a longer period, requiring two returns and separate payment references/deadlines. Ordinary small-company payment is usually nine months and one day after each CT period end; assess instalment rules separately, including associated-company and short-period limits.

The CT return filing date uses the latest applicable rule, not automatically twelve months after each CT period. For a relevant accounts period no longer than eighteen months, twelve months after that accounts period ends may give both first returns the same filing date. Later notice-service dates can matter. Verify [CTM93030](https://www.gov.uk/hmrc-internal-manuals/company-taxation-manual/ctm93030) and the actual notices before declaring a filing overdue.

A weekend does not automatically extend the legal due date. Check [HMRC payment methods](https://www.gov.uk/pay-corporation-tax): Faster Payments, card acceptance date, Bacs and new/existing Direct Debit have different timing. Do not delay an overdue best-estimate payment merely until the return filing deadline. Interest and late-filing penalties are distinct; do not assert an assessed charge without evidence. Use `uk-corporation-tax-reminders` for the period-by-period payment preparation.

## Other obligations
For Companies House, distinguish first/subsequent accounts, company type, accounting-reference-date changes and filing acceptance. Check the company register and current [accounts guidance](https://www.gov.uk/annual-accounts) and [confirmation-statement guidance](https://www.gov.uk/file-your-confirmation-statement-with-companies-house); do not reuse historic fees, review dates or default deadline formulas for exceptional periods.

For VAT, read the authority's actual period/frequency and scheme before using the usual month-plus-seven-days rule. Use [VAT deadlines](https://www.gov.uk/vat-returns/deadlines) and `uk-vat-review` for scheme and return preparation. Do not equate VAT submission penalties with late-payment charges or claim points expire solely through a simple period of compliant filing.

For Self Assessment, distinguish paper and online filing, registration and balancing/payments-on-account obligations using [the current deadlines](https://www.gov.uk/self-assessment-tax-returns/deadlines). MTD for Income Tax applies to qualifying individuals under current rollout rules, not automatically to companies or VAT registrants. Use [the current MTD eligibility guidance](https://www.gov.uk/guidance/check-if-youre-eligible-for-making-tax-digital-for-income-tax), including thresholds, reference income years and exemptions, rather than a copied future rollout calendar.

For payroll, separate FPS/EPS submission, PAYE payment, benefit reporting and employer-NI obligations; [verify current payroll rules](https://www.gov.uk/running-payroll). Do not label a late-payment penalty table as an RTI submission penalty.

## Complete the urgent path
Prioritize an evidenced due/overdue obligation. Prepare the exact period, amount basis and reference, then identify only the missing information that prevents safe completion. Finish authorized reversible work before asking for final action-specific approval. Never guess a payment reference, duplicate an accepted filing, create a schedule without instruction, or claim a payment happened from an open browser tab.
