# Ship checklist and templates

## Before the first deploy
- [ ] The user created the accounts (hosting, backend, email…). Claude never creates accounts or handles passwords.
- [ ] Public config in the client (e.g. the Firebase web config) and secrets only in server secret stores (`firebase functions:secrets:set`, Vercel env vars). The user types the secrets.
- [ ] Security rules deny by default and allow each user only their own data. Test that an unauthenticated read is refused.
- [ ] Auth: authorized domains include the production domain. For Firebase on Hosting, set `authDomain` to `<project>.web.app` and add `https://<project>.web.app/__/auth/handler` to the OAuth client's redirect URIs (Google Cloud console → APIs & Services → Credentials).
- [ ] Paid APIs: an allowlist of who may call them, low instance limits, and a provider spend limit plus a budget alert.
- [ ] Caching: HTML and app code `no-cache`, the service worker `no-store`, versioned asset URLs, a network-first service worker that leaves `/__/` paths alone.
- [ ] Tests pass; emulator mode is off in the committed config (add a test for it).

## Deploy (only on "deploy")
- Run the deploy command, then verify the live site: key URLs return 200, the new version's assets load, there are no console errors, and the main flow works.
- Tell the user what you couldn't verify (e.g. signed-in state, real devices).

## After launch
- Install on a phone (iOS Safari: Share → Add to Home Screen; Android Chrome: Install app). If an update doesn't show, close the app fully and reopen it.
- Backups: an export in the app, plus an occasional server-side backup before any data fix.
- Monitoring: error tracking (Sentry free tier) and uptime checks if the app has a backend.

## Data fixes on production
1. Read and summarize what's there.
2. Ask what should change.
3. Back up the full data to `private/<name>-backup-<date>.json` (git-ignored).
4. Change it.
5. Read back and show the result.

## CLAUDE.md template

```markdown
# <app name>

<one-line description>. Stack: <frontend>, <backend>, <hosting>. Live at <url>.

## Rules for every change
- Think as a UX designer first: check docs/DESIGN.md, then ask the user about design decisions it doesn't settle, with a recommended option.
- Design: follow docs/DESIGN.md; tokens and existing components only; no inline styles.
- Check phone (375px) and desktop (~1280px), light and dark.
- Tests: <commands>. Add a test for new behavior.
- Version bump: <how assets and caches are versioned>.
- Deploy: <command>. Commit and deploy only when the user asks.

## Data
- <where data lives, the collections, the data rules (uniqueness, IDs), how to add fields so they sync>
- Never rename stored fields; old data must keep working.
- Personal data never goes in the repo (private/ is git-ignored).
```
