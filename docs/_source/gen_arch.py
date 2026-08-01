"""Generate 01_Architecture_and_Design.docx for the P3MAI website."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "01_Architecture_and_Design.docx")
ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
VER, DATE = "v1.0", "1 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL", VER)
ds.title_page(doc, "DOC-01", "Architecture & Design", "Structure & design of the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL")
ds.doc_control(doc, [[VER, "2026-08-01", "Douglas Colvin", "Initial issue"]])
ds.add_toc(doc)

ds.heading(doc, "1.  Executive summary", 1)
ds.para(doc, "The **P3MAI website** is the public business site for P3MAI (Douglas Colvin's programme, "
        "project and PMO consultancy). It is a **hand-built static site** — five pages plus a standalone "
        "cost estimator — with no framework and no build step: plain HTML5, CSS3 and vanilla JavaScript. "
        "It carries the P3MAI brand (navy/gold, Poppins, a pyramid logo) and links out to the two P3MAI "
        "web apps. It is hosted on **Rise** and served at **p3mai.com**.")

ds.heading(doc, "2.  Introduction", 1)
ds.heading(doc, "2.1  Purpose & scope", 2)
ds.para(doc, "The design and structure reference for the website. Visitor-facing guidance is in "
        "**DOC-02**; maintenance and publishing in **DOC-03**.")
ds.heading(doc, "2.2  Audience", 2)
ds.para(doc, "Whoever maintains the site — comfortable editing HTML/CSS, no framework knowledge needed.")

ds.heading(doc, "3.  Site overview", 1)
ds.para(doc, "Five linked pages, a shared header/footer, and a standalone estimator:")
ds.figure(doc, os.path.join(ASSETS, "web_sitemap.png"), "Figure 1 — Site map.")
ds.table(doc, ["Page", "Purpose"], [
    ["index.html", "Home — hero, feature cards, CV-sourced track record, call to action"],
    ["about.html", "Bio and career timeline (from the CV), certifications, values"],
    ["services.html", "Programme / Project / PMO cards; links to the PMO app and Method Map; comparison table"],
    ["blog.html", "AI / project-management posts"],
    ["contact.html", "Validated contact form, contact details, map"],
    ["calculator.html", "Project Cost Estimator — a standalone interactive tool"],
], col_widths=[3.2, 12.3])
ds.para(doc, "An auxiliary `dashboard.html` productivity/notes page also exists outside the main "
        "navigation.")

ds.heading(doc, "4.  Technology", 1)
ds.table(doc, ["Aspect", "Choice"], [
    ["Markup", "Hand-written HTML5, one file per page"],
    ["Styling", "A single CSS design system (style.css)"],
    ["Behaviour", "Vanilla JavaScript (script.js) — no framework, no build"],
    ["Fonts", "Poppins (brand), system fallbacks"],
    ["Assets", "SVG logo set, optimised JP/PNG imagery"],
    ["Hosting", "Rise (UK shared cPanel/FTP)"],
], col_widths=[3.2, 12.3])
ds.callout(doc, "note", "No build step by design",
           ["The site is deliberately static and dependency-free — nothing to compile, nothing to break. "
            "Edit an HTML/CSS/JS file, preview, and publish."])

ds.heading(doc, "5.  Design system", 1)
ds.table(doc, ["Element", "Value"], [
    ["Primary colour", "Navy #0B2545 (with dark #071830)"],
    ["Accent", "Gold #C9A227"],
    ["Background", "Light grey #F6F7F9"],
    ["Font", "Poppins"],
    ["Logo", "Original plan-view pyramid mark + wordmark (navy on light, white on dark)"],
], col_widths=[3.6, 11.9])
ds.para(doc, "`style.css` holds the shared design system — layout, typography, buttons, cards, the "
        "sticky navigation and responsive breakpoints. The **header and footer markup is byte-identical "
        "across every page** (except the active nav item) so the site reads as one piece.")

ds.heading(doc, "6.  Front-end behaviour", 1)
ds.para(doc, "`script.js` provides the interactions, all progressive enhancements over the static markup:")
ds.bullet(doc, "**Env-aware app links** — rewrites the PMO and Method Map links to the live domains in "
          "production, leaving them at localhost in dev (see §7);")
ds.bullet(doc, "**Page-transition overlay** — a soft fade between internal pages;")
ds.bullet(doc, "**Responsive navigation** — a hamburger menu on small screens;")
ds.bullet(doc, "**Reveal-on-scroll** animations for sections;")
ds.bullet(doc, "**Contact-form validation** — client-side checks before submit;")
ds.bullet(doc, "**Smooth scrolling** for in-page anchor links.")

ds.heading(doc, "7.  Integrations", 1)
ds.para(doc, "The Services page links to the two P3MAI apps, both of which link back to the site:")
ds.table(doc, ["Link", "Dev", "Production"], [
    ["PMO Service ('Example')", "localhost:5173", "app.p3mai.com"],
    ["PRINCE2 Method Map", "localhost:5175", "method-map.onrender.com (→ prince2.p3mai.com)"],
], col_widths=[4.4, 3.6, 7.5])
ds.callout(doc, "pitfall", "Env-aware links — do not hardcode",
           ["The localhost hrefs in services.html are intentional dev defaults; `script.js` rewrites them "
            "to the live URLs in production. Replacing them with hardcoded URLs breaks local development."])
ds.para(doc, "The cost estimator directs enquiries to **hello@P3MAI.com**.")

ds.heading(doc, "8.  Hosting & deployment", 1)
ds.figure(doc, os.path.join(ASSETS, "web_hosting.png"),
          "Figure 2 — Hosting: publish selected files by FTP into Rise's public_html.")
ds.para(doc, "The site is hosted on **Rise** (UK shared cPanel/FTP hosting). Publishing means uploading "
        "the approved static files into `public_html`. The two apps live on Render under subdomains "
        "(app.p3mai.com, prince2.p3mai.com). Full publishing steps are in **DOC-03**.")
ds.callout(doc, "pitfall", "Publish only the approved files",
           ["Do not upload the entire project folder — it contains source assets, documents and memory "
            "that must never be public. See the Operation Manual for the exact allow-list."])

ds.heading(doc, "9.  Design decisions", 1)
ds.table(doc, ["Decision", "Rationale"], [
    ["Static, no framework/build", "Fast, robust, trivially hostable on shared hosting."],
    ["Byte-identical header/footer", "One consistent shell; verify with a diff after edits."],
    ["Env-aware links in JS", "Cross-links work in both dev and prod with no manual editing."],
    ["Original artwork only", "Brand integrity; no copyright risk."],
    ["No fabricated content", "Everything is grounded in the real CV — no fake testimonials or claims."],
], col_widths=[4.6, 10.9])

ds.heading(doc, "10.  Non-functional considerations", 1)
ds.bullet(doc, "**Performance** — static files, minimal JS; fast to load.")
ds.bullet(doc, "**Responsiveness** — mobile-first layout with a hamburger menu.")
ds.bullet(doc, "**SEO** — per-page titles and meta descriptions.")
ds.bullet(doc, "**Maintainability** — one file per page, one shared stylesheet and script.")

ds.heading(doc, "11.  Roadmap", 1)
ds.bullet(doc, "Switch the Method Map link to the branded prince2.p3mai.com once DNS resolves.")
ds.bullet(doc, "Further blog content; optional analytics.")

ds.heading(doc, "Appendix A — Files", 1)
ds.code_block(doc,
              "business-website/\n"
              "  index / about / services / blog / contact .html   the five pages\n"
              "  calculator.html      standalone cost estimator\n"
              "  style.css            shared design system\n"
              "  script.js            shared interactions (env-aware links, etc.)\n"
              "  logo/favicon SVGs, imagery\n"
              "  docs/                this documentation set")

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
