---
name: uk-expense-review
description: "Classify UK business costs and assess their tax deduction, VAT recovery and period using supporting evidence. Use for expense claims and omitted-cost reviews; distinguish companies, sole traders and property businesses."
metadata:
  type: workflow
  source_reviewed: 2026-10-31
---

# Uk Expense Review

## Output
Produce a deduction decision or compact expense schedule for the owner/bookkeeper, in chat or the requested workspace file. Include source, entity, date/service period, gross/net/VAT, ledger treatment, tax treatment and open evidence. Preserve source rows and existing categories until a supported change is authorized.

## Review sequence
Identify the taxpayer and income source before applying rules: company, individual trade, employment or property business. Do not use a self-employed simplified-expenses rule as a company deduction. Establish who paid, for whose business, and whether the cost is already included in agent statements, a bank import, reimbursements or an existing accrual.

Assess business purpose and separable private use, specific disallowances, capital versus revenue, service timing and any statutory relief separately. Payment date alone does not establish the accrual period. A supplier's printed annual date range does not necessarily make a one-off service an annual prepayment; use the actual service evidence. Unsupported allocations remain explicit estimates.

Distinguish an operating repair from an improvement or acquisition-related capital cost. There is no universal low-value equipment threshold that makes a capital item revenue. Capitalization, depreciation and tax capital allowances are separate decisions; check asset qualification and dwelling-house restrictions before suggesting AIA/full expensing. A company property disposal gain may use allowable acquisition/disposal costs even where no current rental-profit deduction applies. Do not count a cost twice.

For personally paid company expenses, record the cost or asset and the reimbursement owed to the director. Subsequent principal repayment is not another expense. Distinguish an incorporation cost from recurring compliance/accountancy fees. Reconcile agent gross rent and fees rather than deducting fees again from a net remittance. Refundable tenant deposits and reserve transfers are not automatically income or deductible costs.

For mileage, homeworking, benefits, pensions, phones, entertaining and financing, inspect the relevant entity-specific conditions and effective-date primary guidance. Employee benefit exemptions, company deductibility and VAT recovery are different questions. Do not label entire categories always deductible, use nominal family payroll without work, or assume a flat allowance applies automatically.

For VAT, first establish registration, valid evidence, business use, taxable/exempt attribution and scheme. VAT on costs of an exempt residential letting is not automatically reclaimable. Recoverable VAT normally stays out of the income-tax/CT cost; irrecoverable VAT can form part of the expense or asset. Use `uk-vat-review` where partial exemption or a scheme requires more work.

## Completeness and communication
Search existing records before asking for documents. Alternative contemporaneous evidence may substantiate a cost even where a separate invoice is unavailable; distinguish evidence adequate for accounting from VAT-invoice requirements. An owner's completeness confirmation closes the omitted-cost request, without converting uncertain treatment into proven treatment.

Show a supported deduction, disallowance or unresolved estimate with its reason and period. Quantify the tax effect when helpful and distinguish that from the net cash cost. Do not create an expense simply to reduce a bill or write off a receivable merely because settlement evidence is incomplete.

Use current [company expense rules](https://www.gov.uk/corporation-tax-rates/corporation-tax-expenses), the [Property Income Manual](https://www.gov.uk/hmrc-internal-manuals/property-income-manual), [capital allowances](https://www.gov.uk/capital-allowances), and [employee expenses and benefits](https://www.gov.uk/expenses-and-benefits-a-to-z). Verify any numerical threshold from the relevant effective-date source rather than a copied table.
