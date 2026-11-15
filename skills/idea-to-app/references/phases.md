# Phase details

## Think

Ask at most four clarifying questions in one `AskUserQuestion` call, and only where the answer changes scope: who it's for, which devices, single-user or multi-user, and must-have integrations. Infer the rest and state your assumptions.

The product brief artifact has these sections:
1. **One-liner** and **target users** (primary and secondary).
2. **Jobs to be done**: 3–5 statements ("When I…, I want to…, so I can…").
3. **MVP features** (must-have) vs **later**. Every MVP feature names the flow it belongs to.
4. **User flows** as mermaid `flowchart TD` diagrams: first-run onboarding, the core loop (the thing people do daily), and settings or data management.
5. **Data model**: entities, fields, relationships. **Data rules**: uniqueness (e.g. one session per day), IDs (stable client-generated UUIDs for offline sync), deletion and backup, what's private.
6. **Success measures** (e.g. a week of logging without friction) and **risks** (privacy, costs, platform limits like iOS PWA storage).
7. **Name candidates** (2–3).

Pitfalls from steady.:
- **Don't ship one person's personal defaults to everyone.** Plan templates and onboarding instead.
- **Define states once.** steady. ended up with three meanings of "done" across the week view, adherence and streak. Write one definition per term in the brief.
- **Plan first-run onboarding in the MVP,** not as an afterthought.

## Build

**Project skeleton**
- `public/` (or the framework's equivalent), `tests/`, `docs/DESIGN.md`, `CLAUDE.md`, `.gitignore` including `private/`, `.env*` and secret files.
- Run `git init` before the first change.

**Slices:** each slice is usable end to end (UI, data, sync) and small enough to review in one sitting. Suggested order:
1. App shell, design system and empty states.
2. Core create/edit/delete flow with local persistence.
3. Sign-in and sync, tested with emulators and two separate browser origins as two devices.
4. Secondary features.
5. Settings, backup and export.
6. Onboarding.

**Testing**
- Unit tests for logic: dates, streaks, merges.
- Design-rule tests: no raw colors, font sizes or radii outside the token block; spacing only from the scale; no inline styles; dialogs labelled.
- Optional end-to-end tests (Playwright) for the core loop.

**Verification:** use the built-in browser at mobile (375×812), tablet and desktop presets, in light and dark. Check for horizontal scroll and console errors.

**Data safety:** never point local testing at production. Use the emulators (`firebase emulators:start --project demo-…`), or a separate dev project.

**Feature switches:** a constant like `FEATURE_ENABLED = false`, plus hidden markup, until the backend is deployed and the design is approved.

**Versioning:** bump `?v=` on changed assets and the service worker `CACHE_NAME`. Serve HTML with `Cache-Control: no-cache`, and use a network-first service worker.
