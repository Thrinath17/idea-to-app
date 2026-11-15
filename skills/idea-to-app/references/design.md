# Design phase

## 1. Inspiration (before proposing anything)

Use real sources, in this order of preference:
- **The user's own references:** Figma files (Figma MCP: `create_session` with the file key first, then `get_design_context`, `get_screenshot`, `get_variable_defs`), or links to sites and apps they like (open them in the built-in browser and note palette, type, density and patterns).
- **Subframe MCP** (if connected), for canvas-based UI exploration.
- **Category references:** look at 3–5 well-regarded apps in the same category (e.g. Mobbin or Dribbble through the browser), and note *patterns*, not pixels. Never copy a specific product's look or brand.
- The brightdata `design-mirror` skill can extract a site's visual style, but only use it for a site the user names as inspiration, and adapt rather than clone it.

## 2. Theme directions

Offer 2–3 directions that differ meaningfully: palette, type pairing, density, corner style, illustration or icon style, tone of voice. Each preview shows:
- a palette (light and dark), with the accent used for text and for fills;
- a type pairing with a sample heading, body and label;
- the app's key screen at phone width;
- one sentence explaining why it fits *this* subject.

Avoid the AI-default looks unless the user asks for them: warm cream with a serif and terracotta; near-black with one neon pop; purple-to-blue gradient heroes; emoji section markers; everything centered; the same rounded card everywhere.

**Logo:** 2–3 concepts at app-icon size, shown next to the wordmark. The app icon is full-bleed (the platform rounds the corners), with content in the central 80% so it works as a maskable icon.

## 3. Design system (after the user picks)

Write the tokens first, in one marked block (`/* @tokens-start */ … /* @tokens-end */`), defined for both themes:
- **Color:** bg, surface, surface-sunken, border, text, text-muted, accent (fill), accent-strong (hover), accent-text (accent used as text, contrast-checked), accent-soft (tint), on-accent, success, warning, danger, overlay, chart colors.
- **Spacing:** a 4px scale (4, 8, 12, 16, 20, 24, 32, 40).
- **Radius:** sm 8, md 12, lg 16, pill.
- **Type:** at least 11px; inputs at 16px (stops iOS zoom); weights 400/500/600/700.
- **Controls:** 44px inputs and dialog buttons, 36px secondary, 32px small.

**Components (styled once):** primary / secondary / text / destructive buttons; fields; segmented choice; rating scale; card; collapsible card with a chevron; section head; tag; empty state; dialog (head, hint, fields, actions; bottom sheet on phones; destructive action left on desktop and below the others on phones).

**Rules (put them in DESIGN.md):**
- One meaning per icon: the chevron expands, and + always comes with a label. Never put two icons side by side.
- Show a control only when it can do something; empty states offer the next step.
- Don't repeat information on one screen.
- Destructive actions say what will be lost and ask first.
- Fixed breakpoints (1100, 850, 700, 600, 510, 380); no horizontal scroll at 375px.
- Sentence case; buttons say what they do; hints are one sentence.
- Accessibility: labels on every input; `role="dialog"` with `aria-modal` and `aria-labelledby`; focus moved into dialogs and returned afterwards; never color alone for state; respect reduced motion.

**Enforce in tests:** colors, font sizes and radii only from tokens; spacing only from the scale (raw 0/1px/2px allowed); no inline styles; dialogs labelled; the design library covers every component.

**Design library page:** one HTML page that loads the real stylesheet and shows the logo, color tokens (with a theme toggle), the type scale, spacing and radius, buttons, fields, cards, the app's domain components, empty states and a dialog. Make it reachable but unlinked (e.g. `/design-library.html`).
