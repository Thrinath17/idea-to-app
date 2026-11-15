---
name: idea-to-app
description: The user's app-building process, from idea to live app and every round after. Use when the user describes a new app idea ("I have an app idea", "build me an app", "let's make an app for…"), and also in any project that has .claude/app-plan.md whenever they ask for a feature, change, fix, design tweak or deploy ("add X", "users should be able to…", "change Y"), or ask for a review or health check. Also use to refresh the stack catalog or open the idea-to-app playbook.
---

# Idea to App

One entry point for the whole life of an app. The user only thinks about **what** the app should do. The setup happens once, early and mostly automatically, and every later round is about features. It was distilled from building the user's *steady.* workout tracker. The human-readable version is `references/playbook.html` (published at https://claude.ai/artifact/2eXo5cK3zbWS2J2meS4UQz).

## Step 0: pick the mode from the state file

Look for `.claude/app-plan.md` at the project root (template: `references/state-file.md`).

| State | Mode |
|---|---|
| No file, and the user describes an idea | **New project**. Create the file in the first turn. |
| `status: refining`, `designing`, `stack`, `setup` or `mvp` | **New project**: resume at that stage. |
| `status: feature-rounds` and a feature, change or fix request | **Feature round** |
| `status: feature-rounds` and "review", "health check" or "what's missing" | **Review round** |

Read the whole state file before doing anything; it's the memory across sessions. **Update it at the end of every turn**: stage, decisions (with the reason), backlog, and setup checklist ticks. Never ask the user something the file already answers.

## Operating rules (every mode)

1. **Gates:** decisions go through `AskUserQuestion` with a recommended option first, marked "(Recommended)". Don't pass a gate without an answer.
2. **Think as a UX designer first:** check `docs/DESIGN.md`, then ask about every design decision it doesn't settle.
3. **Show, don't describe:** use visual previews for themes, logos and flows. Publish briefs, setup plans and reviews as artifacts.
4. **Deploy and commit only when the user says so.** Never loosen this rule in project files.
5. **Never test on real data:** use emulators or fakes. For real data: read, back up to git-ignored `private/`, change, read back.
6. **The user owns accounts and secrets:** Claude never creates accounts, enters passwords or handles API keys. The user signs in and pastes secrets into a terminal or secret store. Claude does everything else through CLIs once the user is signed in.
7. **Keep setup light:** only ask for accounts the next milestone needs. Everything else waits in "Later" until a feature needs it.
8. Keep the task list current and wrap up each turn: what's done, what's not verified, and the next decision.

## Mode A · New project

Five stages. Each can take as many prompts as it needs. To the user it's simply: say the idea → refine it → pick a look → a few sign-ins → watch the MVP get built → ask for changes.

**A1 · Refine the idea (PM)** — `references/phases.md` § Think
- Turn 1: a short product brief artifact (problem, users, MVP vs later, flows as mermaid diagrams including onboarding, data model and data rules, risks, name ideas), plus at most four questions that change scope.
- Later turns: refine the brief from the user's answers. Keep a "what changed" line at the top of the brief.
- Move on only when the user says the idea is ready. **Gate:** confirm MVP scope and name. Set `status: designing`.

**A2 · Design (UX)** — `references/design.md`
- Real inspiration first: the user's Figma files via the Figma MCP, Subframe if connected, apps and sites they like. Then 2–3 distinct theme previews and logo concepts. **Gate:** pick one.
- The design system is built in A4 (foundation), not here. Here we only decide. Set `status: stack`.

**A3 · Stack and setup plan** — `references/catalog.json` + `references/setup-recipes.md`
- Choose the closest app type (`pwa`, `saas`, `content`, `mobile`, `ai`). Recommend one option per needed category with alternatives, each marked free, free tier or paid. **Gate:** confirm or swap.
- Then produce the **setup plan** (an artifact and the checklist section in the state file) from the recipes, grouped as:
  - **You, in a browser.** Only what needs a human: sign-ins, billing, consent screens, secrets. Each step has a time estimate, why it's needed, the cost, and exact clicks.
  - **Claude, automatically.** Everything a CLI can do after sign-in.
  - **Later.** Steps tied to features that aren't next, or to launch (custom domain, app stores).
  Keep the tone calm and short: "About 10 minutes in total. You'll sign in twice and click one toggle."
- Set `status: setup`.

**A4 · Foundation sprint (one session)**
- Walk the "You" steps one at a time. After each, verify it yourself (e.g. `firebase login:list`, `gh auth status`, `vercel whoami`) and tick it in the state file.
- Then automate: repo and `CLAUDE.md` (template in `references/ship.md`), the design system (tokens, components, empty states, dialogs, DESIGN.md, design library, rule tests), cloud resources, security rules, emulator-based tests, and a deployed skeleton with sign-in working. Deploy only on "deploy".
- Seed the backlog with the approved MVP features in build order. Set `status: mvp`.

**A5 · Build the MVP (automatic)**
- Don't wait for the user to re-request features they already approved in A1. Build the MVP backlog one slice at a time, in a sensible order (the core loop first).
- For each slice: build it, run the tests, check it at 375px and 1280px, then show the user a short summary with a screenshot or link. Ask only the design questions this slice raises and DESIGN.md doesn't settle. Tick it in the state file and continue to the next.
- If the user redirects mid-way ("skip photos", "change the order"), update the backlog and carry on.
- When the MVP is done, offer to deploy (deploy only on "deploy"). Set `status: feature-rounds` and tell the user: "Your MVP is ready. From now on, just tell me what to change or add."

## Mode B · Feature round (most of the time)

For each request ("add X", "change Y", a bug):
1. **Mini brief:** restate the feature in 2–4 lines: who, what, acceptance criteria, data changes. Check it against the decisions and data rules in the state file. If it conflicts, say so.
2. **Design questions:** only the ones this feature raises and DESIGN.md doesn't settle. Ask them all in one `AskUserQuestion` call.
3. **Just-in-time setup:** if the feature needs a new service (email, payments, AI), pull its recipe from `setup-recipes.md`, show the few "You" steps, verify them, and automate the rest.
4. **Build:** follow `CLAUDE.md` and DESIGN.md. Write tests, including design-rule tests. Check at 375px and 1280px, light and dark. Use emulators for data.
5. **Ship:** deploy only on "deploy", then verify the live site.
6. **Update the state file:** move the backlog item to Done, log decisions, and add any follow-ups you noticed.

Several small requests in one message make one round. A request that changes the product's direction goes back to a short A1-style brief first.

## Mode C · Review round

Publish a product and UX review artifact: feature inventory, onboarding flow (current vs proposed), inconsistencies with severity, and a design, accessibility (WCAG) and localization review, ending with a prioritized order of work. Add the findings to the backlog with IDs. **Gate:** the user picks what to act on; those become feature rounds.

## Maintenance

- **Refresh the catalog:** edit `scripts/catalog_src.py`, run `python3 -I scripts/fetch_stars.py references/catalog.json`, then `python3 -I scripts/build_playbook.py`, and republish the playbook artifact (pass its URL as `url`).
- **Setup recipes:** when a vendor's flow changes, update `references/setup-recipes.md`. Verify CLI commands with `--help` before running them.
- **Worked example:** the steady. project at `~/Documents/Codex/2026-11-12/referenced-chatgpt-conversation-this-is-an/outputs/workout-tracker`. See its `.claude/app-plan.md`, `CLAUDE.md`, `docs/DESIGN.md` and the design-rule tests.
