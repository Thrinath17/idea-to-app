# Idea to App

A Claude Code skill and playbook for taking a rough app idea to a deployed app with the least possible setup. Distilled from building the *steady.* workout tracker.

**For the person with the idea, it's six steps:** say the idea → shape it → pick a look → a few sign-ins → watch the MVP get built → ask for changes.

- **Playbook page (private):** https://claude.ai/artifact/2eXo5cK3zbWS2J2meS4UQz. Three tabs: Playbook, Stack catalog, steady. story.
- **Use it:** in any new, empty folder in Claude Code, say *"I have an app idea: …"*. In a project that has `.claude/app-plan.md`, just ask for features.

## What's in here

```text
idea-to-app/
├── skills/idea-to-app/              ← the skill (linked into ~/.claude/skills)
│   ├── SKILL.md                     ← modes: new project, feature rounds, review rounds
│   ├── references/
│   │   ├── phases.md                ← refine-the-idea and build details
│   │   ├── design.md                ← inspiration, themes, design system rules
│   │   ├── setup-recipes.md         ← per service: what you click vs what Claude automates
│   │   ├── ship.md                  ← ship checklist, CLAUDE.md template
│   │   ├── state-file.md            ← .claude/app-plan.md template
│   │   ├── catalog.json             ← 144 tools: pricing, open source, GitHub stars
│   │   ├── playbook_template.html   ← playbook page source
│   │   └── playbook.html            ← built page (template + catalog)
│   └── scripts/
│       ├── catalog_src.py           ← catalog data (edit this)
│       ├── fetch_stars.py           ← refresh GitHub stars → catalog.json
│       └── build_playbook.py        ← rebuild playbook.html
└── .claude-plugin/plugin.json       ← lets this folder be installed as a plugin later
```

## Common tasks

Refresh the catalog (stars and options):

```bash
python3 -I skills/idea-to-app/scripts/fetch_stars.py skills/idea-to-app/references/catalog.json
```

```bash
python3 -I skills/idea-to-app/scripts/build_playbook.py
```

Then ask Claude to republish the playbook artifact to its existing URL.

Install on another machine: clone this repo, then link the skill:

```bash
ln -s "$PWD/skills/idea-to-app" ~/.claude/skills/idea-to-app
```

## Worked example

steady. (`~/Documents/Codex/2026-11-12/referenced-chatgpt-conversation-this-is-an/outputs/workout-tracker`) runs on this process in feature-round mode. See its `.claude/app-plan.md`, `CLAUDE.md` and `docs/DESIGN.md`.
