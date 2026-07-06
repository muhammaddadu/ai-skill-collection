# User Story Splitting Template

Use this template to split a large story into smaller, independently deliverable user stories.

## Provenance
Adapted from `prompts/user-story-splitting-prompt-template.md` in the `https://github.com/deanpeters/product-manager-prompts` repo.

## Splitting Logic (Use in Order)
1. Workflow steps (thin end-to-end slices)
2. Operations (CRUD — "manage" signals Create/Read/Update/Delete)
3. Business rule variations
4. Data variations
5. Data entry methods (simple UI first, fancy UI later)
6. Acceptance criteria complexity (multiple When/Then pairs)
7. Major effort milestones ("implement one + add remaining")
8. Simple/complex (simplest core first, variations later)
9. External dependencies
10. DevOps steps
11. Defer performance ("make it work" before "make it fast")
12. Tiny Acts of Discovery (TADs) / break out a spike if none apply

## Output Template
```markdown
### Original Story
[Story written using `skills/user-story/template.md`]

### Suggested Splits
1. Split 1 using **[rule name]**:
   - [Left split story, using `skills/user-story/template.md`]
   - [Right split story, using `skills/user-story/template.md`]
2. Split 2 using **[rule name]**:
   - [Left split story]
   - [Right split story]
3. Split 3 using **[rule name]**:
   - [Left split story]
   - [Right split story]
```

## Notes
- Each split should deliver user value on its own.
- If no rule applies, propose TADs to de-risk and clarify before writing stories.
