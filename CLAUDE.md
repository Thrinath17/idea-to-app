# Idea to App (the harness itself)

This repo is the source of the `idea-to-app` skill and its playbook page. `~/.claude/skills/idea-to-app` is a symlink to `skills/idea-to-app`, so edits here apply in every project immediately.

## Rules for changes
- **Keep it simple for the reader.** For the user it's six steps (say the idea → shape it → pick a look → a few sign-ins → watch the MVP get built → ask for changes). Mechanics like the state file and modes stay behind the scenes in the playbook.
- **The skill's operating rules are fixed:** gates via AskUserQuestion with a recommended option; UX-first; deploy and commit only when the user says so; never test on real data; the user owns accounts and secrets. Don't loosen them.
- **Catalog:** edit `scripts/catalog_src.py`, then run `fetch_stars.py` and `build_playbook.py`. Only list relatively popular options. Pricing labels stay general (free / free tier / paid). Only show stars when the repo is the product.
- **Playbook page:** edit `references/playbook_template.html`, rebuild, check it at 375px and 1280px in the built-in browser (serve the built file locally), then republish to https://claude.ai/artifact/2eXo5cK3zbWS2J2meS4UQz by passing that URL as `url`.
- **Setup recipes:** verify CLI commands with `--help` before writing them down.
- Commit only when the user asks.
