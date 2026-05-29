# KFZ Digital — redesign/design (active HTML + CSS)

This directory holds the active landing pages and the single canonical stylesheet. For the full project guide (tech stack, design system, conventions), see [`../../CLAUDE.md`](../../CLAUDE.md).

---

## What lives here

**Pages (8 HTML files):**
- `b2c.html`, `b2b.html`, `partner.html` — primary landing pages
- `cities.html`, `city.html` — V2 city directory + detail
- `zulassungsstellen.html`, `zulassungsstelle.html` — V2 offices directory + detail
- `design-system.html` — component reference page

**Styles:**
- `design-system.css` — canonical stylesheet for all pages. All design tokens defined in `:root`.

---

## Git submodule

This directory is a **git submodule** with its own `.git/`. Commits made here go to the submodule's own remote, not the parent repo. To track a change in the parent repo, commit inside the submodule first, then commit the updated submodule pointer in the parent.

---

## Before editing

1. Read [`../DESIGN.md`](../DESIGN.md) — design tokens (colors, spacing, typography) and component specs. Reuse tokens; do not invent new values.
2. Match the existing class naming and structure in `design-system.css`.
3. UK English in copy; bilingual `data-en` / `data-de` attributes where the page is bilingual.
