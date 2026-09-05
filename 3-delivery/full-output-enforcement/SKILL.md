---
name: full-output-enforcement
description: "Deliver complete files or exhaustive enumerations when the user explicitly requests unabridged output. Use to prevent omission placeholders in full-output tasks; ordinary repository edits and concise explanations do not require this workflow."
---

# Full-Output Enforcement

## Baseline

Apply this workflow when the user asks for complete files or exhaustive output. Deliver every requested item. For repository edits, complete the files on disk and link to them; repeating their contents in chat is necessary only when requested.

## Banned Output Patterns

Do not substitute the following patterns for work the user requested. Literal syntax, examples, and TODOs that are themselves part of the requested artifact are allowed:

**In code blocks:** `// ...`, `// rest of code`, `// implement here`, `// TODO`, `/* ... */`, `// similar to above`, `// continue pattern`, `// add more as needed`, bare `...` standing in for omitted code

**In prose:** "Let me know if you want me to continue", "I can provide more details if needed", "for brevity", "the rest follows the same pattern", "similarly for the remaining", "and so on" (when replacing actual content), "I'll leave that as an exercise"

**Structural shortcuts:** Outputting a skeleton when the request was for a full implementation. Showing the first and last section while skipping the middle. Replacing repeated logic with one example and a description. Describing what code should do instead of writing it.

## Execution Process

1. **Scope** — Read the full request. Track the deliverables expected (files, functions, sections, answers), updating that inventory when the user changes scope.
2. **Build** — Generate every deliverable completely. No partial drafts, no "you can extend this later."
3. **Cross-check** — Before output, re-read the original request. Compare your deliverable count against the scope count. If anything is missing, add it before responding.

## Handling Long Outputs

Prefer complete workspace artifacts for large outputs when the environment supports files. Continue working across context compaction without requiring the user to restart the task. If a chat-only response cannot contain the requested artifact:

- Do not compress remaining sections to squeeze them in.
- Do not skip ahead to a conclusion.
- Write at full quality up to a clean breakpoint (end of a function, end of a file, end of a section).
- End with:

```
[PAUSED — X of Y complete. Send "continue" to resume from: next section name]
```

On "continue", pick up exactly where you stopped. No recap, no repetition.

## Quick Check

Before finalizing any response, verify:
- No omission placeholders replace requested work
- Every item the user requested is present and finished
- Code blocks contain actual runnable code, not descriptions of what code would do
- Concise reporting does not omit any requested artifact
