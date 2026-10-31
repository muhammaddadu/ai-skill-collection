---
name: uk-corporation-tax-reminders
description: Match UK HMRC Corporation Tax letters to existing books, first-year tax periods, payment status and deadlines. Use for reminders, unpaid-tax follow-up and preparing payment or CT600 next steps.
---

# UK Corporation Tax Reminders

## Output
Return an evidence-linked review and next actions for the company owner or adviser. Use chat for a question; save requested books, reports or status notes in the target workspace under its conventions. Keep all company identifiers, account balances, documents and dated decisions there.

## Workflow

Read the letter and inspect the workspace books and latest dated status notes before asking whether the company traded or made a profit. Extract company identity, exact period, issue/payment dates, whether an amount is stated, and period-specific payment reference. Keep UTRs and payment references in the user's private workspace; do not copy them into reusable instructions. A photograph alone does not authenticate a letter or banking details.

Check current official HMRC guidance for relevant deadlines, rates, filing routes and payment clearing times. Statutory first accounts may exceed twelve months while a CT accounting period cannot; inspect all periods and obligations, not just the short period on one reminder. Verify period boundaries in HMRC records when available. Calculate each payment deadline independently and handle weekends according to the payment method. Determine return deadlines separately from payment deadlines using first-return guidance and notices.

Trace the letter's period to the tax working, its taxable-profit bridge and associated-company/rate assumptions. Reconcile period charges to total provision. Time-apportion only where appropriate to the income and expense category and applicable rules; a saved allocation is an estimate until reviewed. Separate the actual liability calculation from cash reserves. Do not tell HMRC nothing is due simply because a reminder has no amount or no return has been filed.

Track payment evidence explicitly: owner confirmation, bank instruction, cleared debit and HMRC allocation are different facts. Record a new owner confirmation as a dated workspace note without overwriting historical records. Check whether a confirmation covers one period or all outstanding amounts; use clear session context or clarify only when consequential. If unpaid, identify overdue principal separately from upcoming amounts. Quote book figures as estimates until finalized; do not claim an HMRC balance or exact interest without verification.

For unpaid overdue tax, prioritize reconciling the computation, checking any HMRC balance/payment credits and obtaining the correct reference for that period. Explain how to make the authorized payment concrete; if the final computation is pending, assess and explain payment on account using current HMRC guidance without presenting it as settled liability. Where ability to pay is a stated problem, research HMRC payment arrangements. Do not calculate speculative penalties as confirmed debt. Avoid delaying action on an overdue amount merely because the return deadline is later.

Prepare a compact period/estimated-tax/deadline/status table and the next action. File CT600, full accounts and tax computation through a currently supported route when authorized; a Companies House draft does not discharge HMRC filing requirements. Payment does not file a return, and a filed return does not prove payment.

Never infer filing or payment authority from a request to explain a reminder, update guidance or confirm unpaid status. Do all permitted read-only checks and local preparation first. Before an authorized payment, verify official bank details, amount, company account and the exact period's reference; never fabricate a missing reference or reuse the letter's reference for another period. Retain payment/receipt evidence and confirm allocation only when observed.

For a multi-obligation calendar or the long-first-period filing-date exception, use `uk-tax-deadlines`. Do not assume two first CT periods have two different return deadlines: inspect the relevant period of account and HMRC notice-service rule.

A personal Self Assessment panel is not proof of Corporation Tax enrolment or balance. Confirm company identity and the correct service before using a nil-balance message. Verify recent payment/credit history before retrying. If direct browser control is unavailable, identify that specific access limitation; do not confuse a visible/open tab with a controllable authenticated session.
