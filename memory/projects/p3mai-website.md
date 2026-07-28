# P3MAI Website

**Also called:** "the site", "my business website"
**Status:** Active — built, branded, and populated; deployment pending.
**Supersedes:** Bright Path Coaching (same codebase, fully rebranded July 2026).

## What It Is
Business website for P3MAI — Program, Project, and PMO Management in AI. Douglas Colvin's consultancy. 5-page static site plus a standalone cost calculator, all in this folder.

## Brand
- **Tagline:** "AI Program and Project Management Delivered at Scale"
- **Colors:** Navy `#0B2545` (primary), dark navy `#071830`, gold `#C9A227` (accent), light gray `#F6F7F9` (background)
- **Font:** Poppins
- **Logo:** Original plan-view pyramid mark (3 gold facets — 2 lit, 1 shaded, peak offset upper-left) + "P3MAI" wordmark. Files: `logo-triangle-navy.svg` (header, light bg), `logo-triangle-white.svg` (footer, dark bg), `logo-triangle-icon.svg`, `favicon.svg`. Both header and footer logos render at 40px height. Must remain original artwork — no copyright infringement.

## Pages & Files
| File | Content |
|------|---------|
| index.html | Hero, 3 feature cards, track-record stats (CV-sourced, not testimonials), CTA |
| about.html | Bio from CV, photo (douglas.jpg), career timeline 1999–2025, values, certifications |
| services.html | Program Mgmt / Project Mgmt / PMO cards + comparison table |
| blog.html | 3 AI/PM posts, author widget with photo, categories |
| contact.html | Validated form, both emails/phones, Google Map (DIFC Dubai), hours |
| calculator.html | Standalone project cost estimator (self-contained HTML/CSS/JS, real-time totals) |
| style.css / script.js | Shared design system + interactions (sticky nav, hamburger, reveal animations, page transitions, form validation) |
| douglas.jpg | Headshot — Adobe-processed (auto-tone + background removed onto `#F6F7F9`), used on About + blog sidebar |

## Business Details (real — do not fabricate beyond these)
- Emails: drcolvin@yahoo.com, drcolvin63@googlemail.com
- Mobiles: +971 5 85 383 932, +44 7990 520 094
- Location: Dubai / Abu Dhabi, UAE (no street address on site by design)
- LinkedIn: linkedin.com/in/douglascolvin
- Hours: Mon–Fri 9 AM–6 PM GST, weekends by appointment
- Calculator quote email: hello@P3MAI.com

## Key Facts Used on Site (from CV)
- 25+ years programme/portfolio leadership; budgets up to $1B; 100+ matrix-managed staff
- Two TOP500-ranked AI supercomputers delivered (#20 and #25 globally) at Core42/G42
- Career: Vodafone 1999 → RBS AD Transformation £28m 2017 → Core42/G42 Responsible AI PMO 2023 → supercomputers 2024–25
- Certifications: APM, PRINCE2, MSP, SAFe Scrum Master, Lean Six Sigma Green Belt

## Conventions
- Header/footer markup byte-identical across all 5 pages (except nav `.active` class) — verify with diff after edits
- Standard verification after changes: CSS brace balance, HTML tag balance, `node --check` on JS
- Old unused files still in folder: logo-icon.svg, logo-navy.svg, logo-white.svg (superseded logo concept), me.jpg (original photo), image0–4.jpeg

## Next Up
- Deploy to Netlify (first-time deploy — Douglas wants a step-by-step walkthrough)
