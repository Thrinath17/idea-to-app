# Setup recipes

Use these to build the setup plan (stage A3) and the just-in-time setup in feature rounds. Each recipe has five parts:
- **When:** now (foundation), at launch, or when a specific feature needs it.
- **You:** browser steps that need a human (sign-in, billing, consent, secrets), with time estimates.
- **Claude:** what's automated after sign-in.
- **Verify:** how Claude confirms the step worked.
- **Cost.**

How to write the plan for the user:
- **Total time first.**
- **Group by milestone.**
- **One line per step.** Exact screen and button names in bold.
- **Never more than about 6 "You" steps for the foundation.** Defer the rest.

Example opener: "About 10 minutes. You'll sign in to two services and flip one switch. I'll do the rest."

CLI commands change. Run `<cli> <command> --help` before relying on flags, and adapt.

**Always first (2 minutes)**
- **Node.js:** check `node -v`. If it's missing, the user installs the LTS version from nodejs.org (or with Homebrew on a Mac).
- **Git and GitHub:** the user runs `gh auth login` and picks GitHub.com → HTTPS → browser. Claude runs `git init`, then `gh repo create <name> --private --source=. --push` only when the user asks to push. Verify with `gh auth status`.

---

## Firebase (auth, Firestore, hosting): the steady. path
**When:** now · **Cost:** free on the Spark plan; Functions and new Storage buckets need Blaze (pay as you go).

**You**
1. Install the CLI if needed (Claude can run `npm i -g firebase-tools`). Then run **`firebase login`** in a terminal tab and sign in with Google. About 1 min.
2. In the Firebase console, open the new project, then **Authentication → Get started → Sign-in method → Google → Enable**, and pick a support email. About 1 min. (No CLI for this.)
3. Hosted sign-in on Safari/iOS: Google Cloud console → **APIs & Services → Credentials → Web client (auto created by Google Service) → Authorized redirect URIs → add `https://<project-id>.web.app/__/auth/handler`**. About 2 min.

**Claude**
- `firebase projects:create <project-id> --display-name "<Name>"`
- `firebase apps:create WEB "<Name>" --project <project-id>`, then `firebase apps:sdkconfig WEB <appId> --project <project-id>`. Write the config into the app, with `authDomain` set to `<project-id>.web.app`.
- `firebase firestore:databases:create "(default)" --location=<nam5|eur3|…> --project <project-id>`. Ask the user for the region only if it matters (data residency).
- `firebase.json` (hosting with no-cache headers, rules), `.firebaserc`, `firestore.rules` (per-user), then `firebase deploy --only hosting,firestore:rules` **when the user says deploy**.
- Emulators for tests: `firebase emulators:start --only auth,firestore --project demo-<name>`.

**Verify**
- `firebase login:list` shows the account.
- `firebase projects:list` includes the project.
- An unauthenticated REST read is refused.
- The live URL returns 200.

**Later: Cloud Functions (e.g. AI features)**
- **You:**
  - In the console, click **Spark → Upgrade → Blaze**, and link billing. About 3 min.
  - In Google Cloud → **Billing → Budgets & alerts**, set a $1 budget.
- **Claude:** `functions/` code, `firebase deploy --only functions` on "deploy".

---

## Supabase (Postgres, auth, storage)
**When:** now · **Cost:** free tier (small projects; inactive projects pause after about a week).

**You**
1. Sign up at supabase.com, then **New project**. Choose the name and region, and let the dashboard generate the database password. Keep it in a password manager; Claude doesn't need it. About 2 min.
2. Run **`supabase login`** (opens the browser). About 1 min.
3. For Google sign-in: in Google Cloud → **APIs & Services → Credentials → Create OAuth client ID (Web)**, add the Supabase callback URL shown in **Authentication → Providers → Google**, then paste the client ID and secret into that Supabase screen. About 5 min.

**Claude:** `supabase init`, `supabase link --project-ref <ref>`, migrations in `supabase/migrations`, row-level security policies, `supabase db push`, and local dev with `supabase start` (needs Docker).

**Verify:** `supabase projects list`; a query as anon is refused by RLS.

---

## Vercel (hosting for Next.js and friends)
**When:** now · **Cost:** free Hobby plan (non-commercial); Pro for commercial use.

**You:** run **`vercel login`** (Claude can install the CLI with `npm i -g vercel`). About 1 min.

**Claude:** `vercel link`, then `vercel deploy` for previews and `vercel deploy --prod` on "deploy". For secrets, the user runs `vercel env add <NAME>` and pastes the value.

**Verify:** `vercel whoami`; the deployment URL returns 200.

## Netlify
**You:** `netlify login` · **Claude:** `netlify init`, `netlify deploy --prod` on "deploy" · **Cost:** free tier.

## Cloudflare Pages / Workers
**You:** `npx wrangler login` · **Claude:** `wrangler pages project create`, `wrangler pages deploy <dir>` on "deploy" · **Cost:** free tier.

## GitHub Pages
**You:** nothing beyond `gh auth login`. · **Claude:** a GitHub Actions workflow for Pages, plus enabling Pages via `gh api`. · **Cost:** free (public repos, or private on paid plans).

---

## Resend (email)
**When:** when a feature sends email · **Cost:** free tier.
**You:**
1. Sign up.
2. Under **Domains → Add domain**, add the DNS records it shows at your domain registrar. About 10 min, plus DNS wait. You can skip this for testing and send only to yourself.
3. Under **API Keys → Create**, put the key into the secret store yourself (`vercel env add RESEND_API_KEY` or `firebase functions:secrets:set RESEND_API_KEY`).

**Claude:** the email templates (React Email), the server-side send function, and a test send to the user's own address.

## Stripe (payments)
**When:** when a feature takes payments · **Cost:** per-transaction fees.
**You:**
1. Create an account (test mode needs no business details yet).
2. Run `stripe login`.
3. Store the secret key yourself.

Going live later needs business verification in the dashboard.

**Claude:** products and prices in test mode via CLI, the checkout and webhook code, and `stripe listen --forward-to` for local webhooks.

## Claude API (AI features)
**When:** when an AI feature is built · **Cost:** pay per token; set a spend limit.
**You:** at platform.claude.com, add credits under **Billing**, set a monthly limit, then **API Keys → Create** and store the key as a server secret yourself.
**Claude:** server-side calls only, with an allowlist of who may call them and a low instance limit.

## Sentry (errors)
**When:** at launch · **Cost:** free tier.
**You:** sign up and create a project. · **Claude:** `npx @sentry/wizard@latest -i <platform>` (the user may need to approve sign-in in the browser); the DSN is public.

## PostHog (analytics)
**When:** at launch, if wanted · **Cost:** free tier.
**You:** sign up and create a project. · **Claude:** add the snippet with the public project key; cookieless or consent mode as required.

## Expo / EAS (native mobile)
**When:** now, for mobile apps · **Cost:** free tier for builds. Store release needs an **Apple Developer Program** membership (paid yearly) and a **Google Play** developer account (one-time fee). Only needed at launch.
**You:** `npx expo login` (or `eas login`). At launch, enroll in the store programs. · **Claude:** `npx create-expo-app`, `eas build:configure`, `eas build`, `eas submit` on "deploy".

## Custom domain
**When:** at launch, optional · **Cost:** a domain costs a yearly fee.
**You:** buy the domain at any registrar. · **Claude:** add it in the host (`firebase hosting` console step or `vercel domains add`) and show the exact DNS records for the user to enter. SSL is automatic.

---

## Setup plan example (steady., written the way the user should see it)

> **About 10 minutes. You'll sign in twice and flip one switch. I'll do the rest.**
>
> **You**
> 1. Run `firebase login` in the terminal tab I open and sign in with Google (1 min).
> 2. Firebase console → **Authentication → Get started → Google → Enable** (1 min).
> 3. Google Cloud → **Credentials → Web client → add redirect URI** (I'll give you the exact URL) (2 min).
>
> **I'll do**
> - Create the project, web app, database and security rules.
> - Build the design system and app skeleton.
> - Run the tests and deploy when you say so.
>
> **Later, only when you want them**
> - The chat assistant: Blaze plan + Anthropic API key.
> - A custom domain.
