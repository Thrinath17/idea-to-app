# State file: `.claude/app-plan.md`

This is the app's memory across sessions. Create it in the first turn of a new project and update it at the end of every turn. Keep it short and factual; details belong in the docs it links to.

```markdown
---
app: <name>
status: refining | designing | stack | setup | mvp | feature-rounds
app_type: pwa | saas | content | mobile | ai
live_url: <url or none>
updated: <YYYY-MM-DD>
---

# <name>

<one-line description>

## Brief
- Users: …
- Core loop: …
- Links: product brief <artifact url>, design library <path>, review <artifact url>

## Stack
| Category | Choice | Why | Cost |
|---|---|---|---|
| Frontend | … | … | free |

## Data rules
- <e.g. one session per day; IDs are client UUIDs; settings sync as one document>

## Decisions
- <YYYY-MM-DD> <decision>. Why: <reason>.

## Setup checklist
### You (browser)
- [x] <step> — <time>
### Claude (automated)
- [x] <step>
### Later (when needed)
- [ ] <step> — needed for <feature>

## Backlog
### Next
- [ ] <feature or fix> (<source, e.g. review P2>)
### Later
- [ ] …
### Done
- [x] <YYYY-MM-DD> <feature>
```

Rules:
- Every decision gets a date and a reason, so later rounds don't reopen it by accident.
- Backlog items from reviews keep their review IDs (P1, U3, A1, L2…).
- Tick setup steps only after verifying them (CLI status, a successful call, a deployed URL).
