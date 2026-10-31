---
name: uk-company-filing-review
description: Review UK limited-company accounts and Companies House filing drafts against the books, eligibility and approval evidence. Use for saved filing reviews and readiness checks; filing authority remains task-specific.
---

# UK Company Filing Review

## Output
Return an evidence-linked review and next actions for the company owner or adviser. Use chat for a question; save requested books, reports or status notes in the target workspace under its conventions. Keep all company identifiers, account balances, documents and dated decisions there.

## Workflow

Read the workspace guidance, latest accounts workbook and most recent filing review. Preserve dated evidence and superseded entries rather than treating every older note as current. Determine whether the request is preparation, draft saving, approval or submission; carry out authorized preparation without imposing another confirmation gate.

Verify company identity, statutory period, accounting framework, applicable threshold dates, micro-entity eligibility, exclusions and any group/audit requirements using current primary sources. Distinguish tax associated-company control from a corporate group. Check Companies House filing status and due date where access permits; identify overdue filing as a separate obligation from tax payment.

Reconcile the underlying balance sheet and profit bridge before checking form totals. Keep gross property cost, depreciation, year-end cash, receivables, prepayments, director loan, other creditors, deferred income and unpaid capital traceable. Check the form's sign conventions. Reconcile whole-pound presentation separately from the underlying ledger; document rounding instead of inserting an unexplained balancing transaction.

Inspect material estimates, tax provision, share-capital discrepancies, related-party loan terms, completeness of liabilities/guarantees and evidence supporting continued director funding/going concern. A balanced form is not sufficient approval evidence. State the practical consequence of unresolved judgements.

Use supported browser controls or a sufficient connected tool for authenticated filing work. A visible URL is not evidence of usable control. Do not extract cookies or bypass authentication; if control is unavailable, finish the local review and state the exact limitation.

For authorized draft saving, save and reopen to verify persisted figures and prose. Keep accounting-policy text concise and factual; do not insert AI/workflow commentary into statutory text. Never describe a draft as approved because its text avoids the word draft. Preserve existing approval fields and declarations unless the user authorizes their completion.

For authorized submission, finish all preparation first, confirm the actual approval details, compare the final preview with approved accounts, and retain the resulting submission/acceptance evidence. Do not invent approval dates or signatures. A saved status, empty submission number or attempted download is not proof of submission, acceptance or a downloaded copy.

Report prepared/saved/approved/submitted/accepted as distinct evidence-backed states with dates. HMRC CT600/accounts/tax computation filing is separate from Companies House accounts. Finish with specific remaining actions, not a generic readiness checklist.

For obligation dates use `uk-tax-deadlines`; for tax payment preparation use `uk-corporation-tax-reminders`. Do not let a historical saved-draft note override a later public filing or acceptance acknowledgement.
