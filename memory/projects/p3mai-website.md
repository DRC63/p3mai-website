# P3MAI Website

**Also called:** "the site", "my business website"
**Status:** Active — built, branded, and populated. Git repo pushed to GitHub; hosting/DNS deployment still pending.
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

## PMO Service app integration (2026-07-28)
The Services page's PMO card has an "Example" button linking to the PMO Service app
(separate project, `../claude-code/pmo-service/`), and the app's sidebar links back via a
"Back to Website" link. Both use runtime env-detection in JS (`window.location.hostname`)
rather than hardcoded URLs, so nothing needs manual editing between local dev
(`localhost:5173` / `localhost:4173`) and production (`app.p3mai.com` / `p3mai.com`).
Gotcha already hit once: `window.location.hostname` is an empty string for `file://` pages,
not `"localhost"` — the check must explicitly treat `protocol === 'file:'` as local too, or
opening the raw HTML file breaks the link.

Local dev requires the site to be served over HTTP, not opened as a raw `file://` path —
browsers block navigation from `http://` to `file://` (and the reverse is unreliable too),
which breaks the cross-links. A `business-website` `preview_start` config
(`python -m http.server 4173`) was added to the working-directory-level
`.claude/launch.json` for this reason.

The PMO app has no authentication (single-user tool, Douglas's deliberate choice to deploy
it fully open on `app.p3mai.com` rather than add a login first) — worth revisiting if it
ever holds real working data instead of demo content. **Update 2026-07-28: it's live**, at
`https://pmo-service.onrender.com`, deployed via Dockerfile with auto-seed on boot (see the
app's own project notes for the full story). `app.p3mai.com` DNS record still pending.

## Method Map app integration (2026-08-01)
The Services page's **Project Management** card has a "PRINCE2 Method Map" button linking to
the Method Map app (separate project, `../claude-code/method-map/` — a PRINCE2 interdependency
network + lifecycle explorer). Uses the **same env-aware pattern as the PMO link**: the
services.html href is `http://localhost:5175` (local dev), and `script.js` swaps it to the
live app in production. Prod target is currently `https://method-map.onrender.com` — **switch
to `https://prince2.p3mai.com` once that custom domain's DNS CNAME resolves** (the app is set
up for prince2.p3mai.com in Render; DNS pending). The `script.js` selector already matches all
three hosts (`localhost:5175` / `method-map.onrender.com` / `prince2.p3mai.com`), so only the
swap-target string in the JS needs changing.

**Gotcha:** the `localhost:5173` (PMO) and `localhost:5175` (Method Map) hrefs in
services.html are NOT bugs — they're the dev defaults that `script.js` rewrites to the live
URLs in production. Do NOT "fix" them to hardcoded production URLs; that breaks local dev.

## Version control
Git repo initialized 2026-07-28, pushed to `https://github.com/DRC63/p3mai-website` (private).
Local commit identity is set per-repo (Douglas Colvin / drcolvin@yahoo.com), not global.
`.gitignore` excludes Office lock files (`~$*`) and OS junk.

## Hosting: Rise, not Netlify (corrected 2026-07-28)
The domain's actual host is **Rise** (UK shared cPanel/FTP hosting) — "Deploy to Netlify"
below was the original plan before Douglas clarified this; Netlify was never actually set up
and isn't the real plan. Rise has no "Setup Python App" feature (confirmed), so only this
static site can be deployed there — the PMO app lives on Render instead (see above).

Douglas has been deploying by manually dropping the **entire** `business-website/` folder
into Rise's `public_html` via FTP/File Manager, which also uploads files that should never
be public. Only these should go to `public_html`:
```
index.html, about.html, services.html, blog.html, contact.html, calculator.html
style.css, script.js, favicon.svg
logo-triangle-navy.svg, logo-triangle-white.svg, logo-triangle-icon.svg,
  logo-triangle-icon.png, logo-triangle-white.png
douglas.jpg
blog-thumb-agentic.jpg, blog-thumb-pmo.jpg, blog-thumb-scale.jpg
```
Never upload: the CV and working `.docx` files, `CLAUDE.md`/`TASKS.md`/`memory/`/`.git/`
(internal notes + git history), the internal screenshot JPEGs (`Douglas Colvin.JPG`,
`Overview.jpeg`, `Progress.jpeg`, `Risks.JPG`, `Status Report *.JPG`, `Tasks A.jpeg`,
`Tracker.jpeg`), or the superseded logo/photo files listed under Conventions above. None of
this is enforced by Rise (no directory-listing protection needed to exploit it — a guessed
or discovered filename is enough), so it's a real exposure, not just clutter. Flagged to
Douglas 2026-07-28; unconfirmed whether he's cleaned up what's already been uploaded.

## Next Up
- Clean up / redo the Rise `public_html` upload using the file list above
- Add DNS CNAME `app` → Render's target for `app.p3mai.com` in Rise's DNS panel
