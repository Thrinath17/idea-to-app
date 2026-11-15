# Source data for the idea-to-app stack catalog.
# pricing: "free" = free / open source, "free-tier" = managed with a free plan, "paid" = paid or usage-based only
# rec: app archetypes this is the recommended default for:
#   pwa = personal / installable web app, saas = full-stack SaaS web app, content = content or marketing site,
#   mobile = native mobile app, ai = AI-powered app
CATEGORIES = [
  ("design", "Design and inspiration"), ("frontend", "Frontend framework"), ("ui", "UI kit and styling"),
  ("backend", "Backend and BaaS"), ("database", "Database"), ("orm", "ORM and data access"), ("auth", "Authentication"),
  ("hosting", "Hosting"), ("email", "Email"), ("storage", "File storage"), ("payments", "Payments"),
  ("analytics", "Analytics"), ("monitoring", "Monitoring"), ("cicd", "CI/CD"), ("ai", "AI and LLMs"),
  ("search", "Search"), ("push", "Push notifications"), ("cms", "CMS"), ("mobile", "Mobile"), ("testing", "Testing"),
]

O = []
def o(cat, name, url, pricing, note, repo=None, oss=False, rec=()):
    O.append(dict(cat=cat, name=name, url=url, pricing=pricing, note=note, repo=repo, oss=oss or bool(repo and pricing == "free"), rec=list(rec)))

# Design and inspiration
o("design", "Figma", "https://www.figma.com", "free-tier", "Industry-standard design tool. The Figma MCP is connected, so designs and variables can be read directly.", rec=("pwa","saas","content","mobile","ai"))
o("design", "Penpot", "https://penpot.app", "free", "Open-source Figma alternative; self-host or use the free cloud.", repo="penpot/penpot", oss=True)
o("design", "Subframe", "https://www.subframe.com", "free-tier", "Visual UI builder with an MCP for designing on a canvas from chat.")
o("design", "Mobbin", "https://mobbin.com", "free-tier", "Library of real app screens and flows for inspiration.")
o("design", "Dribbble", "https://dribbble.com", "free", "Visual inspiration from designers; good for themes and moods.")
o("design", "Storybook", "https://storybook.js.org", "free", "Workshop for building and documenting UI components (design library).", repo="storybookjs/storybook", oss=True, rec=("saas",))

# Frontend
o("frontend", "Plain HTML/CSS/JS", "https://developer.mozilla.org", "free", "No framework or build step. Fastest for small personal apps (this app).", rec=("pwa",))
o("frontend", "React", "https://react.dev", "free", "The most widely used UI library.", repo="facebook/react")
o("frontend", "Next.js", "https://nextjs.org", "free", "React framework with routing, server rendering and API routes.", repo="vercel/next.js", rec=("saas","ai"))
o("frontend", "Vue", "https://vuejs.org", "free", "Approachable component framework.", repo="vuejs/core")
o("frontend", "Nuxt", "https://nuxt.com", "free", "Full-stack framework for Vue.", repo="nuxt/nuxt")
o("frontend", "Svelte / SvelteKit", "https://svelte.dev", "free", "Compiler-based framework; small bundles, little boilerplate.", repo="sveltejs/svelte")
o("frontend", "Angular", "https://angular.dev", "free", "Batteries-included framework, common in enterprises.", repo="angular/angular")
o("frontend", "Astro", "https://astro.build", "free", "Content-first sites that ship little JavaScript.", repo="withastro/astro", rec=("content",))
o("frontend", "React Router (Remix)", "https://reactrouter.com", "free", "Full-stack React routing framework.", repo="remix-run/react-router")
o("frontend", "SolidJS", "https://www.solidjs.com", "free", "Fine-grained reactive UI library.", repo="solidjs/solid")
o("frontend", "Vite", "https://vite.dev", "free", "Fast dev server and bundler used under most modern frameworks.", repo="vitejs/vite")

# UI kit
o("ui", "Hand-written CSS + tokens", "https://developer.mozilla.org/docs/Web/CSS/Using_CSS_custom_properties", "free", "Your own design tokens and components (this app). Full control, no dependency.", rec=("pwa",))
o("ui", "Tailwind CSS", "https://tailwindcss.com", "free", "Utility-first CSS with a token-based config.", repo="tailwindlabs/tailwindcss", rec=("saas","content","ai"))
o("ui", "shadcn/ui", "https://ui.shadcn.com", "free", "Copy-in components built on Radix and Tailwind.", repo="shadcn-ui/ui", rec=("saas","ai"))
o("ui", "MUI (Material UI)", "https://mui.com", "free", "Large React component library following Material Design.", repo="mui/material-ui")
o("ui", "Radix UI Primitives", "https://www.radix-ui.com", "free", "Unstyled, accessible React primitives.", repo="radix-ui/primitives")
o("ui", "Mantine", "https://mantine.dev", "free", "Full-featured React component library.", repo="mantinedev/mantine")
o("ui", "Chakra UI", "https://chakra-ui.com", "free", "Accessible React components with style props.", repo="chakra-ui/chakra-ui")
o("ui", "daisyUI", "https://daisyui.com", "free", "Themeable component classes for Tailwind.", repo="saadeghi/daisyui")
o("ui", "Bootstrap", "https://getbootstrap.com", "free", "Classic CSS framework with components.", repo="twbs/bootstrap")
o("ui", "Ant Design", "https://ant.design", "free", "Enterprise-grade React UI library.", repo="ant-design/ant-design")

# Backend / BaaS
o("backend", "Firebase", "https://firebase.google.com", "free-tier", "Auth, Firestore, hosting, functions in one console. Spark plan free; Functions need Blaze (this app).", rec=("pwa",))
o("backend", "Supabase", "https://supabase.com", "free-tier", "Postgres, auth, storage, realtime and edge functions; open source.", repo="supabase/supabase", oss=True, rec=("saas","mobile","ai"))
o("backend", "Appwrite", "https://appwrite.io", "free-tier", "Open-source backend: auth, database, storage, functions.", repo="appwrite/appwrite", oss=True)
o("backend", "PocketBase", "https://pocketbase.io", "free", "Single-file backend with SQLite, auth and realtime; self-host.", repo="pocketbase/pocketbase")
o("backend", "Convex", "https://www.convex.dev", "free-tier", "Reactive TypeScript backend with a realtime database.", repo="get-convex/convex-backend", oss=True)
o("backend", "Express", "https://expressjs.com", "free", "Minimal Node.js web framework.", repo="expressjs/express")
o("backend", "Hono", "https://hono.dev", "free", "Small, fast web framework for edge runtimes and Node.", repo="honojs/hono")
o("backend", "Fastify", "https://fastify.dev", "free", "High-performance Node.js framework.", repo="fastify/fastify")
o("backend", "NestJS", "https://nestjs.com", "free", "Structured TypeScript server framework.", repo="nestjs/nest")
o("backend", "FastAPI", "https://fastapi.tiangolo.com", "free", "Modern Python API framework with type hints.", repo="fastapi/fastapi")
o("backend", "Django", "https://www.djangoproject.com", "free", "Batteries-included Python web framework.", repo="django/django")
o("backend", "Ruby on Rails", "https://rubyonrails.org", "free", "Convention-over-configuration full-stack framework.", repo="rails/rails")
o("backend", "Laravel", "https://laravel.com", "free", "Full-stack PHP framework.", repo="laravel/framework")

# Database
o("database", "Cloud Firestore", "https://firebase.google.com/docs/firestore", "free-tier", "Document database with realtime sync and offline cache (this app).", rec=("pwa",))
o("database", "PostgreSQL", "https://www.postgresql.org", "free", "The default relational database; extensions like pgvector.", repo="postgres/postgres", rec=("saas","ai"))
o("database", "Neon", "https://neon.tech", "free-tier", "Serverless Postgres with branching.", repo="neondatabase/neon", oss=True)
o("database", "SQLite", "https://sqlite.org", "free", "Embedded file database; great for small apps and edge.", repo="sqlite/sqlite")
o("database", "Turso (libSQL)", "https://turso.tech", "free-tier", "Hosted SQLite at the edge.", repo="tursodatabase/libsql", oss=True)
o("database", "MySQL", "https://www.mysql.com", "free", "Popular relational database.", repo="mysql/mysql-server")
o("database", "MongoDB", "https://www.mongodb.com", "free-tier", "Document database; Atlas has a free cluster.", repo="mongodb/mongo")
o("database", "Redis", "https://redis.io", "free-tier", "In-memory store for caching, queues and sessions.", repo="redis/redis")
o("database", "PlanetScale", "https://planetscale.com", "paid", "Managed MySQL (Vitess) and Postgres; no free plan.")

# ORM
o("orm", "Prisma", "https://www.prisma.io", "free", "Type-safe ORM with schema and migrations.", repo="prisma/prisma")
o("orm", "Drizzle ORM", "https://orm.drizzle.team", "free", "Lightweight, SQL-like TypeScript ORM.", repo="drizzle-team/drizzle-orm", rec=("saas","ai"))
o("orm", "TypeORM", "https://typeorm.io", "free", "Decorator-based ORM for TypeScript.", repo="typeorm/typeorm")
o("orm", "SQLAlchemy", "https://www.sqlalchemy.org", "free", "The standard Python ORM and SQL toolkit.", repo="sqlalchemy/sqlalchemy")

# Auth
o("auth", "Firebase Authentication", "https://firebase.google.com/docs/auth", "free-tier", "Google, Apple, email and phone sign-in (this app).", rec=("pwa",))
o("auth", "Supabase Auth", "https://supabase.com/auth", "free-tier", "Auth tied to Postgres row-level security.", oss=True, rec=("saas","mobile","ai"))
o("auth", "Better Auth", "https://www.better-auth.com", "free", "Framework-agnostic TypeScript auth library.", repo="better-auth/better-auth")
o("auth", "Auth.js", "https://authjs.dev", "free", "Auth for Next.js and other frameworks (formerly NextAuth).", repo="nextauthjs/next-auth")
o("auth", "Clerk", "https://clerk.com", "free-tier", "Drop-in auth UI and user management.")
o("auth", "Auth0", "https://auth0.com", "free-tier", "Enterprise identity platform by Okta.")
o("auth", "Keycloak", "https://www.keycloak.org", "free", "Self-hosted identity and access management.", repo="keycloak/keycloak")

# Hosting
o("hosting", "Firebase Hosting", "https://firebase.google.com/docs/hosting", "free-tier", "Static hosting on a global CDN with one-command deploys (this app).", rec=("pwa",))
o("hosting", "Vercel", "https://vercel.com", "free-tier", "Best fit for Next.js; free Hobby plan is for non-commercial use.", rec=("saas","ai"))
o("hosting", "Netlify", "https://www.netlify.com", "free-tier", "Static sites and serverless functions with previews.")
o("hosting", "Cloudflare Pages / Workers", "https://pages.cloudflare.com", "free-tier", "Edge hosting with generous free limits.", rec=("content",))
o("hosting", "GitHub Pages", "https://pages.github.com", "free", "Free static hosting from a repo; no server code.")
o("hosting", "Render", "https://render.com", "free-tier", "Web services, databases and cron; free services sleep when idle.")
o("hosting", "Railway", "https://railway.com", "paid", "Deploy apps and databases quickly; usage-based after a trial.")
o("hosting", "Fly.io", "https://fly.io", "paid", "Run containers close to users; pay as you go.")
o("hosting", "AWS Amplify", "https://aws.amazon.com/amplify", "free-tier", "Full-stack hosting on AWS.")
o("hosting", "Coolify", "https://coolify.io", "free", "Self-hosted Heroku/Vercel alternative on your own server.", repo="coollabsio/coolify")

# Email
o("email", "Resend", "https://resend.com", "free-tier", "Developer-friendly email API; pairs with React Email.", rec=("saas","ai"))
o("email", "React Email", "https://react.email", "free", "Build email templates with React components.", repo="resend/react-email")
o("email", "Amazon SES", "https://aws.amazon.com/ses", "paid", "Very cheap high-volume sending; more setup.")
o("email", "Postmark", "https://postmarkapp.com", "free-tier", "Fast transactional email; small free developer allowance.")
o("email", "Mailgun", "https://www.mailgun.com", "free-tier", "Email API with a small free plan.")
o("email", "Brevo", "https://www.brevo.com", "free-tier", "Transactional and marketing email with a daily free allowance.")
o("email", "SendGrid", "https://sendgrid.com", "paid", "Twilio email API; free trial, then paid.")
o("email", "Firebase Trigger Email", "https://firebase.google.com/products/extensions/firebase-firestore-send-email", "free", "Firebase extension that sends email via your SMTP provider.", rec=("pwa",))

# Storage
o("storage", "Supabase Storage", "https://supabase.com/storage", "free-tier", "S3-compatible storage with access rules.", rec=("saas","mobile","ai"))
o("storage", "Cloudflare R2", "https://www.cloudflare.com/developer-platform/r2/", "free-tier", "S3-compatible storage with no egress fees.")
o("storage", "AWS S3", "https://aws.amazon.com/s3", "paid", "The standard object storage; free tier for new accounts.")
o("storage", "Firebase Cloud Storage", "https://firebase.google.com/docs/storage", "paid", "File storage with Firebase rules; new buckets need the Blaze plan.", rec=("pwa",))
o("storage", "UploadThing", "https://uploadthing.com", "free-tier", "File uploads for TypeScript apps.", repo="pingdotgg/uploadthing", oss=True)
o("storage", "Cloudinary", "https://cloudinary.com", "free-tier", "Image and video storage with transformations.")
o("storage", "MinIO", "https://min.io", "free", "Self-hosted S3-compatible storage.", repo="minio/minio")

# Payments
o("payments", "Stripe", "https://stripe.com", "paid", "Payments, subscriptions and invoices; per-transaction fees.", rec=("saas","ai"))
o("payments", "Paddle", "https://www.paddle.com", "paid", "Merchant of record: handles global tax for you.")
o("payments", "Lemon Squeezy", "https://www.lemonsqueezy.com", "paid", "Merchant of record for digital products (owned by Stripe).")
o("payments", "RevenueCat", "https://www.revenuecat.com", "free-tier", "In-app subscriptions for iOS and Android.", rec=("mobile",))
o("payments", "PayPal", "https://developer.paypal.com", "paid", "Widely recognized checkout; per-transaction fees.")

# Analytics
o("analytics", "PostHog", "https://posthog.com", "free-tier", "Product analytics, session replay and feature flags; open source.", repo="PostHog/posthog", oss=True, rec=("saas","ai","mobile"))
o("analytics", "Plausible", "https://plausible.io", "paid", "Privacy-friendly analytics; free if self-hosted.", repo="plausible/analytics", oss=True, rec=("content",))
o("analytics", "Umami", "https://umami.is", "free", "Simple, privacy-focused analytics; self-host or cloud.", repo="umami-software/umami")
o("analytics", "Google Analytics", "https://marketingplatform.google.com/about/analytics/", "free", "Free, powerful, but heavy and needs cookie consent.")
o("analytics", "Firebase Analytics", "https://firebase.google.com/docs/analytics", "free", "Free event analytics for Firebase apps.", rec=("pwa",))
o("analytics", "Mixpanel", "https://mixpanel.com", "free-tier", "Event-based product analytics.")
o("analytics", "Vercel Analytics", "https://vercel.com/analytics", "free-tier", "Built-in page analytics for Vercel sites.")

# Monitoring
o("monitoring", "Sentry", "https://sentry.io", "free-tier", "Error tracking and performance monitoring.", repo="getsentry/sentry", oss=True, rec=("pwa","saas","mobile","ai"))
o("monitoring", "Better Stack", "https://betterstack.com", "free-tier", "Uptime checks, status pages and logs.")
o("monitoring", "UptimeRobot", "https://uptimerobot.com", "free-tier", "Simple uptime monitoring.", rec=("content",))
o("monitoring", "Grafana", "https://grafana.com", "free-tier", "Dashboards for metrics and logs; free cloud tier.", repo="grafana/grafana", oss=True)
o("monitoring", "LogRocket", "https://logrocket.com", "free-tier", "Session replay with error context.")
o("monitoring", "Datadog", "https://www.datadoghq.com", "paid", "Full observability platform for larger teams.")

# CI/CD
o("cicd", "GitHub Actions", "https://github.com/features/actions", "free-tier", "CI/CD in your GitHub repo; free minutes for private repos.", rec=("pwa","saas","content","mobile","ai"))
o("cicd", "Platform auto-deploys", "https://vercel.com/docs/deployments", "free-tier", "Vercel, Netlify and Cloudflare deploy on every push with previews.")
o("cicd", "GitLab CI/CD", "https://docs.gitlab.com/ci/", "free-tier", "Built-in CI for GitLab repos.")
o("cicd", "CircleCI", "https://circleci.com", "free-tier", "Hosted CI with a free plan.")
o("cicd", "EAS Build", "https://expo.dev/eas", "free-tier", "Cloud builds and store submission for Expo apps.", rec=("mobile",))

# AI
o("ai", "Claude API", "https://platform.claude.com", "paid", "Anthropic models (Opus, Sonnet, Haiku); pay per token.", rec=("ai",))
o("ai", "OpenAI API", "https://platform.openai.com", "paid", "GPT models; pay per token.")
o("ai", "Gemini API", "https://ai.google.dev", "free-tier", "Google models with a free tier.")
o("ai", "Vercel AI SDK", "https://ai-sdk.dev", "free", "TypeScript toolkit for streaming chat and tools across providers.", repo="vercel/ai", rec=("ai",))
o("ai", "LangChain", "https://www.langchain.com", "free", "Framework for chaining LLM calls, tools and retrieval.", repo="langchain-ai/langchain")
o("ai", "Ollama", "https://ollama.com", "free", "Run open models locally.", repo="ollama/ollama")
o("ai", "Firebase AI Logic", "https://firebase.google.com/docs/ai-logic", "free-tier", "Call Gemini from the client without your own server.")

# Search
o("search", "Postgres full-text search", "https://www.postgresql.org/docs/current/textsearch.html", "free", "Built into Postgres; enough for most apps.", rec=("saas",))
o("search", "Meilisearch", "https://www.meilisearch.com", "free-tier", "Fast, typo-tolerant search engine; open source.", repo="meilisearch/meilisearch", oss=True)
o("search", "Typesense", "https://typesense.org", "free-tier", "Open-source instant search.", repo="typesense/typesense", oss=True)
o("search", "Algolia", "https://www.algolia.com", "free-tier", "Hosted search with a free plan.", rec=("content",))
o("search", "Elasticsearch", "https://www.elastic.co/elasticsearch", "free-tier", "Powerful search and analytics engine.", repo="elastic/elasticsearch", oss=True)

# Push
o("push", "Firebase Cloud Messaging", "https://firebase.google.com/docs/cloud-messaging", "free", "Free push for web, Android and iOS.", rec=("pwa",))
o("push", "Web Push (VAPID)", "https://developer.mozilla.org/docs/Web/API/Push_API", "free", "Standard browser push with the web-push library.", repo="web-push-libs/web-push")
o("push", "OneSignal", "https://onesignal.com", "free-tier", "Push, in-app and email messaging.", rec=("saas",))
o("push", "Expo Notifications", "https://docs.expo.dev/push-notifications/overview/", "free", "Push for Expo/React Native apps.", rec=("mobile",))
o("push", "Novu", "https://novu.co", "free-tier", "Open-source notification infrastructure (email, push, in-app).", repo="novuhq/novu", oss=True)

# CMS
o("cms", "Sanity", "https://www.sanity.io", "free-tier", "Structured content with a customizable studio.", rec=("content",))
o("cms", "Payload", "https://payloadcms.com", "free", "Code-first headless CMS that lives in your Next.js app.", repo="payloadcms/payload")
o("cms", "Strapi", "https://strapi.io", "free", "Popular open-source headless CMS.", repo="strapi/strapi")
o("cms", "Directus", "https://directus.io", "free-tier", "Turns any SQL database into an API and admin app.", repo="directus/directus", oss=True)
o("cms", "Contentful", "https://www.contentful.com", "free-tier", "Enterprise headless CMS.")
o("cms", "Ghost", "https://ghost.org", "free", "Publishing platform for blogs and newsletters.", repo="TryGhost/Ghost")

# Mobile
o("mobile", "Installable PWA", "https://web.dev/learn/pwa/", "free", "Add to home screen; one codebase, no app store (this app).", rec=("pwa",))
o("mobile", "Expo (React Native)", "https://expo.dev", "free-tier", "Build iOS and Android apps in React; EAS for builds.", repo="expo/expo", oss=True, rec=("mobile",))
o("mobile", "React Native", "https://reactnative.dev", "free", "Native apps with React.", repo="facebook/react-native")
o("mobile", "Flutter", "https://flutter.dev", "free", "Google's cross-platform UI toolkit (Dart).", repo="flutter/flutter")
o("mobile", "Capacitor", "https://capacitorjs.com", "free", "Wrap a web app as a native iOS/Android app.", repo="ionic-team/capacitor")
o("mobile", "Tauri", "https://tauri.app", "free", "Small, secure desktop and mobile apps from web code.", repo="tauri-apps/tauri")
o("mobile", "SwiftUI (native iOS)", "https://developer.apple.com/xcode/swiftui/", "free", "Apple's native UI framework; best iOS experience.")

# Testing
o("testing", "Playwright", "https://playwright.dev", "free", "End-to-end browser testing across engines.", repo="microsoft/playwright", rec=("saas","ai","pwa"))
o("testing", "Vitest", "https://vitest.dev", "free", "Fast unit tests with Vite.", repo="vitest-dev/vitest", rec=("saas","ai"))
o("testing", "Jest", "https://jestjs.io", "free", "Long-standing JavaScript test runner.", repo="jestjs/jest")
o("testing", "Cypress", "https://www.cypress.io", "free-tier", "End-to-end testing with a visual runner.", repo="cypress-io/cypress", oss=True)
o("testing", "Testing Library", "https://testing-library.com", "free", "Test UI the way users use it.", repo="testing-library/react-testing-library")
o("testing", "Node test runner", "https://nodejs.org/api/test.html", "free", "Built into Node; no dependencies (this app).", rec=("pwa",))
