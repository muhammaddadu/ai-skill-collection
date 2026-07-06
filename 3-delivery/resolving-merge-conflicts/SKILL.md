---
name: resolving-merge-conflicts
description: "Resolve an in-progress git merge or rebase conflict hunk by hunk: trace each side's original intent, preserve both where possible, verify with the project's checks, and finish the merge. Use when a merge/rebase stops on conflicts or files contain conflict markers. Do NOT use for branch strategy or general git history rewriting."
type: component
domain: 3-delivery
---

# Resolving Merge Conflicts

## Outputs

**Artifact:** a resolved merge — the completed merge/rebase commit(s) with every conflict resolved on intent (no invented behaviour) and the project's automated checks passing
**Format:** git commit(s) in the target repo
**Location:** the branch being merged/rebased
**Audience:** reviewers and the branch owner

## Workflow

1. **See the current state** of the merge/rebase. Check git history, and the conflicting files.

2. **Find the primary sources** for each conflict. Understand deeply why each change was made, and what the original intent was. Read the commit messages, check the PRs, check original issues/tickets.

3. **Resolve each hunk.** Preserve both intents where possible. Where incompatible, pick the one matching the merge's stated goal and note the trade-off. Do **not** invent new behaviour. Always resolve; never `--abort`.

4. Discover the project's **automated checks** and run them — typically typecheck, then tests, then format. Fix anything the merge broke.

5. **Finish the merge/rebase.** Stage everything and commit. If rebasing, continue the rebase process until all commits are rebased.
