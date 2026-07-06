---
name: web-design-guidelines
description: "Audit UI code against Web Interface Guidelines compliance rules — ARIA, focus, touch targets, keyboard nav, reduced motion, semantic HTML. Use when asked to review UI, check accessibility, or audit design/UX. Do NOT use for aesthetics or building UI (`cleanui`) or palette/font lookup (`ui-design-system-search`)."
type: component
domain: 3-delivery
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

> **Network dependency:** this skill fetches the latest guidelines from a remote
> URL (below) at review time — it needs outbound network access. If the fetch
> fails, say so and stop; do not audit against remembered rules.

## Outputs

**Artifact:** UI compliance audit — accessibility/UX findings for the reviewed files
**Format:** terse `file:line` findings, as specified by the fetched guidelines
**Location:** the conversation (or the review/PR comment it feeds)
**Audience:** developers and reviewers of the audited UI code

## How It Works

1. Fetch the latest guidelines from the source URL below
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the fetched guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Fetch fresh guidelines before each review:

```
https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md
```

Use WebFetch to retrieve the latest rules. The fetched content contains all the rules and output format instructions.

## Usage

When a user provides a file or pattern argument:
1. Fetch guidelines from the source URL above
2. Read the specified files
3. Apply all rules from the fetched guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
