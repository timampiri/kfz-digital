# KFZ Digital — Project Guide

Landing page redesign of kfzdigital.de offering car registration services. Two audiences: B2C consumers (find local registration + register online) and B2B dealerships (white-label platform). MVP: B2C, B2B, and partner landing pages, plus V2 directory pages (cities + zulassungsstellen). All HTML/CSS live in `redesign/design/` (git submodule).

---

## Project Layout

```
KFZ Digital/
├── CLAUDE.md                    ← this file (main project guide)
├── ACTION_ITEMS.md
├── redesign/
│   ├── DESIGN.md                ← design tokens — canonical reference
│   ├── content-b2b.md, figma.md, logo.md, moodboard.md, wireframe-b2c.md
│   ├── design/                  ← git SUBMODULE — active HTML + CSS
│   │   ├── CLAUDE.md            ← scoped guide for working inside the submodule
│   │   ├── b2c.html, b2b.html, partner.html
│   │   ├── cities.html, city.html
│   │   ├── zulassungsstellen.html, zulassungsstelle.html
│   │   ├── design-system.html
│   │   └── design-system.css    ← canonical stylesheet for all pages
│   └── archive/                 ← V1–V5 backups + dated snapshots
├── research/                    ← business + pricing research
├── transcript/                  ← call recordings (see transcript/CLAUDE.md)
└── venv/                        ← Python env for kennzeichen-transcribe-translate skill
```

`redesign/design/` is a **git submodule** — commits scope to its own remote. After committing inside the submodule, commit the updated submodule pointer in the parent repo.

---

## Tech Stack

Vanilla HTML/CSS/JS. No build step, no npm, no frameworks. All styles inline in `<style>` blocks; design tokens in `redesign/DESIGN.md` and synchronized across pages.

---

## Design System

All tokens defined in `redesign/DESIGN.md` — the single source of truth. Canonical CSS source is b2b.html `:root`. Read DESIGN.md before editing any page.

Token categories:
- **14 color tokens** (--ink, --accent coral, --paper warm off-white, etc.)
- **4 spacing/shape tokens** (--r-lg, --r-md, --r-sm, --max)
- **Typography** (Geist primary + headings, Geist Mono labels, Instrument Serif accents)
- **Utility classes** (.wrap, .mono, .serif, .eyebrow)

---

## File Reference

Map tasks to the files you need to read first:

| Task | Read First |
|------|-----------|
| Building/editing any HTML page | `redesign/DESIGN.md` |
| B2C copy, layout, hero | `redesign/wireframe-b2c.md` |
| B2B copy, tiers, features | `redesign/content-b2b.md` |
| Pricing, routing, business logic | `research/kfz_digital_b2c_research.md` |
| Logo, brand direction, moodboard | `redesign/logo.md`, `redesign/moodboard.md` |
| Figma components, structure | File ID: `FD0JCQoy6e9CJ99HEFbqrd` |

---

## Platform Context

For business model, target market, competitors, and team structure, see `research/platform-overview.md`. The current project focuses on Phase 1 customer acquisition through landing page redesign.

---

## Working Conventions

- **Language:** UK English throughout (all docs, copy, code). German is a later localization step.
- **Light mode only:** Launch mandatory light-mode only; dark mode not a launch requirement.
- **Mobile-aware desktop-first:** Responsive layouts with mobile viewport respect.
- **Transcript library:** See `transcript/CLAUDE.md` for index of all call recordings with topics and key themes. English `.md` files only.
- **Never use transcripts as build reference** — content already distilled into `research/` docs. Transcripts are raw material only.
- **Audio workflow:** Audio → `kennzeichen-transcribe-translate` skill → add entry to `transcript/CLAUDE.md`.

---

## Development Notes

- **Accessibility:** 4.5:1 contrast minimum; never rely on color alone; focus rings on all interactive elements
- **Performance:** Load assets inline when <5KB; no external CSS/JS for this project
- **Responsive:** Headings use `clamp()` for fluid scaling; test on mobile + desktop
- **Figma sync:** Regular sync with File ID `FD0JCQoy6e9CJ99HEFbqrd` to ensure visual consistency

---

## venv Dependency

`venv/` directory is a Python environment for the `kennzeichen-transcribe-translate` skill. Do not delete or move — used for future audio transcription workflows.
