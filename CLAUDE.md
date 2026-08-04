# Memory

## Me
Douglas Colvin (drcolvin@yahoo.com, drcolvin63@googlemail.com). Founder of P3MAI. Programme/Portfolio Director, 25+ years, AI infrastructure & enterprise transformation. Based Dubai/Abu Dhabi, UAE.

## People

| Who | Role |
|-----|------|
| **Douglas** | Douglas Colvin, founder of P3MAI (me) |

## Terms

| Term | Meaning |
|------|---------|
| **P3MAI** | Program, Project, and PMO Management in AI — Douglas's consultancy |
| PMO | Project/Programme Management Office |
| the site | The P3MAI 5-page website in this folder. **Live on Rise** at p3mai.com. |
| **apps front door** | **`apps.p3mai.com`** — one domain fronting ALL the apps via a Render reverse proxy (repo `../claude-code/apps-gateway/`). Every app is served at `apps.p3mai.com/<slug>`. This **replaced the old per-app subdomains** (no `prince2.p3mai.com`). Legacy `app.p3mai.com` now 301s to `/pmo`. See the auto-memory `project_apps_front_door`. |
| the app / PMO Service | Internal PMO tool at `../claude-code/pmo-service/` — Services page PMO card → "PMO Example" button. **Live at `apps.p3mai.com/pmo`** (`app.p3mai.com` redirects there). |
| Method Map | Config-driven method explorer at `../claude-code/method-map/`. **FOUR frameworks live**, each its own Render service from one codebase: **PRINCE2** `/prince2`, **MSP** `/msp`, **SAFe** `/safe`, **PMBOK** `/pmbok` (all under `apps.p3mai.com`). Services-page buttons: Project Management card has PRINCE2 + SAFe + PMBOK; Programme card has MSP. Env-aware in `script.js` (localhost → `apps.p3mai.com/<slug>`). |
| P3M3 Assessment | P3M3 PMO Maturity self-assessment at `../claude-code/p3m3-assessment/` — Services page PMO card → "P3M3 Maturity Assessment" button. **Live at `apps.p3mai.com/p3m3`.** |
| **portfolio strategy** | Cross-app commercial plan (market research, MoSCoW backlog, roadmap) lives at `../P3MAI-Portfolio/` — the layer above all the individual projects. |

## Projects

| Name | What |
|------|------|
| **P3MAI website** | 5-page static site (index, about, services, blog, contact) + calculator.html. Navy/gold brand, pyramid logo. Live work in this folder. |

→ Details: memory/projects/p3mai-website.md

## Preferences
- Concise, direct communication — minimal unnecessary explanation.
- No fabricated content on the real business site (no fake testimonials, addresses, or claims — everything grounded in the CV).
- Logo must remain original artwork (no copyright infringement).

---
*History: this site began as a fictional "Bright Path Coaching" build (see memory/projects/bright-path-coaching.md), fully rebranded to P3MAI in July 2026.*
