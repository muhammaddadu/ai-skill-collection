---
name: uk-property-company-books
description: Reconcile UK property-company bank, letting-agent and acquisition evidence into year-end books, rental accruals and director-loan schedules. Use for bookkeeping or accounts preparation, not personal landlord tax.
---

# UK Property Company Books

## Output
Return an evidence-linked review and next actions for the company owner or adviser. Use chat for a question; save requested books, reports or status notes in the target workspace under its conventions. Keep all company identifiers, account balances, documents and dated decisions there.

## Workflow

Start from the current workbook, latest dated review notes and evidence inventory in the workspace. Read its AGENTS.md and RULES.md if present. Search existing evidence before asking the owner to repeat previous confirmations. Discover the actual folder path if the displayed cwd is missing; whitespace may be significant.

Use the available spreadsheet skill when inspecting or changing workbook artifacts. Keep analysis read-only unless edits are requested. Before substantive edits preserve the original and inspect builders before running them; old scripts can overwrite newer work.

Reconcile bank opening balance + movements = closing balance at the actual year-end. Separate gross rent, agent fees, VAT on fees, repairs, deposits and remittances. Reconcile missing monthly detail against annual/quarterly agent controls without adding the controls as extra transactions. Do not infer zero income from missing bank receipts.

Allocate income and expenditure by the supported service/rental period. Record debtors, prepaid expenses, creditors and deferred rent explicitly. Subsequent-year tenancy documents do not prove the earlier year's terms. Separate personal pre-incorporation activity from company activity and establish the effective beneficial takeover date from evidence and director explanations.

Trace purchase price and acquisition costs to supporting records. Distinguish capital costs from operating expenses, property ownership from market value, and personally funded company costs from company cash. Reconcile director-loan advances, reimbursable costs, interest and actual repayments; a credit loan repayment does not itself reduce rental profit. Unpaid share subscriptions are not bank cash. Preserve discrepancies with public incorporation records until reconciled.

For FRS 105 property accounts, assess cost, depreciation, impairment, useful life and residual value under current applicable guidance. Label judgement-based assumptions; do not invent a land split, valuation or supported life. Build a separate tax bridge for depreciation and other disallowed costs rather than applying a rate directly to accounting profit.

Deliver reconciled balances with clear evidence and estimate status, a short list of material unresolved amounts, and the next useful action. Separate historical cash, current cash, forecast tax reserves, computed tax and available loan-repayment capacity. Never imply that prepared books establish statutory approval, filing or payment. Keep company-specific amounts in the workspace records, not this reusable skill.

For deduction or capital/revenue decisions use `uk-expense-review`; for company-level tax and extraction planning use `uk-accounting`. A completeness confirmation closes requests for omitted expenses without settling existing estimates or authorizing extra deductions.
