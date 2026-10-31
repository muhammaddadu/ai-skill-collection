---
name: uk-vat-review
description: "Review UK VAT registration, supply treatment, recovery and return reconciliations using current HMRC guidance. Use for VAT and MTD VAT questions; not a substitute for Corporation Tax or personal MTD Income Tax rules."
metadata:
  type: workflow
  source_reviewed: 2026-10-31
---

# Uk Vat Review

## Output
Produce a VAT decision or reconciled return working for the business owner/adviser, in chat or the requested workspace file. Identify registration/entity, return period, scheme, supply classifications, tax-point basis, input-tax evidence, source reconciliations and submission/payment status. Keep identifiers and transactions in the private target workspace.

## Establish scope
Check the business and jurisdiction, registration/effective date, accounting scheme, actual HMRC obligations, and whether the question concerns goods, services, land, imports or a cross-border supply. Do not assume ordinary accrual VAT from a bookkeeping label or that any business can reclaim VAT by registering.

For registration, distinguish rolling historic taxable turnover and the forward-looking next-thirty-days test. Zero-rated taxable turnover and exempt turnover are different. Non-established businesses can have different registration requirements. Verify thresholds and deadlines from [current registration guidance](https://www.gov.uk/vat-registration/when-to-register), not this skill's source vintage.

## Classify before calculating
Use the nature of the supply, tax point, place of supply and relevant relief conditions to establish rate/treatment. Zero-rated, exempt, outside scope and reverse-charge supplies have different recovery and reporting consequences. Do not use a broad product-category table as a ruling.

Residential rent is generally exempt, subject to the actual supply and exceptions. VAT charged by an agent is not automatically recoverable by a residential landlord, even when other activities are VAT registered. Review attribution, partial exemption and direct-cost treatment; irrecoverable VAT belongs in the relevant book cost/asset where appropriate. Read [VAT Notice 742](https://www.gov.uk/guidance/vat-on-land-and-property-notice-742) and [partial exemption](https://www.gov.uk/guidance/partial-exemption-vat-notice-706) when property or mixed supplies are involved.

For standard, cash, flat-rate or annual accounting, verify eligibility, entry/exit tests, tax points, capital-goods exceptions and actual payment obligations from [HMRC VAT schemes](https://www.gov.uk/vat-schemes). Do not assume schemes differ only in rate. Input tax needs qualifying business use and appropriate evidence; a bank debit alone does not establish recoverable VAT.

## Reconcile the return
Tie sales and purchases to the ledger, tax-control accounts, prior corrections and bank settlements. Keep gross/net/VAT distinct. Avoid duplicate invoice/payment imports, double counting reverse charges, or treating VAT payment as a second expense. Trace every return box to its own current instructions, especially Northern Ireland/EU goods rules, postponed import VAT and overseas-service reverse charges; historic labels for all EU acquisitions/supplies are insufficient.

Use [current return instructions](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012). Explain estimates, adjustments and unresolved differences. Nil is a real conclusion only after completeness and obligation checks.

## Filing and completion
Check MTD-compatible software, digital records and digital-link requirements, available exemptions, authorization and access. Installing these instructions does not install a connector or authorize account signup, financial-data upload or submission. Use existing authorized tools when available; prepare local workings if the connection is absent. MTD VAT and MTD Income Tax are separate regimes.

Use `uk-tax-deadlines` to verify actual filing/payment dates and current penalties. Do not copy historic VAT late-payment percentages or interest spreads. For an authorized filing, retain the validated return preview, submission identifier/acknowledgement and payment evidence separately; verify allocation before retrying. Never imply authority acceptance from a locally balanced nine-box worksheet.
