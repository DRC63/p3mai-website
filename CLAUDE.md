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
| **route to market** | The adopted commercial framework for the site and the apps — revenue stack, value-based pricing, productising, three-tier offers, delivery workflows. **Consult before deciding what to build, how to price it, or how to package it.** → `memory/approach/route-to-market.md` (source doc: `reference/`). |
| **the estimators** | `p3mai_services_cost_estimator.html` is the **primary** self-serve pricing calculator — the real P3MAI service catalogue (three towers, twelve products, POTI, licensing). Linked from the Services page ("Get an Instant Cost Estimate", between the pricing cards and the comparison table) with a return link back. `calculator.html` is the original simple web-project estimator, unlinked. `p3mai_cost_estimator.html` (earlier generic AI-services version) was deleted 2026-08-06 — Douglas called it a duplicate. **Pricing model documented in `memory/approach/pricing-model.md`.** |

## Projects

| Name | What |
|------|------|
| **P3MAI website** | 5-page static site (index, about, services, blog, contact) + three cost estimators. Navy/gold brand, pyramid logo. Live work in this folder. |

→ Details: memory/projects/p3mai-website.md

## Preferences
- Concise, direct communication — minimal unnecessary explanation.
- No fabricated content on the real business site (no fake testimonials, addresses, or claims — everything grounded in the CV).
- Logo must remain original artwork (no copyright infringement).
- **Wordmark is always two-tone: `P3M` in the primary colour, `AI` in gold.** Never flat.
  The pyramid SVGs are icon-only — the wordmark comes from HTML text beside them.
  → `memory/approach/brand-lockup.md` (includes the audit command).
- Prices in **both AED and GBP** (see the `aed-prices` skill).
- **Build and commercial decisions follow `memory/approach/route-to-market.md`** — value-based
  pricing, named-audience specificity, three-tier offers, validate small before investing.
- Branded documents: navy/gold cover with the pyramid banner, contents page with real page numbers,
  pyramid + P3MAI in every header and footer, "Page X of Y". Build script pattern kept in
  `reference/` (two-pass: render → read page numbers → rebuild contents).

---
*History: this site began as a fictional "Bright Path Coaching" build (see memory/projects/bright-path-coaching.md), fully rebranded to P3MAI in July 2026.*
