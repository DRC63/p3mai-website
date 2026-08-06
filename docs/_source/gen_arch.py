"""Generate 01_Architecture_and_Design.docx for the P3MAI website."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "01_Architecture_and_Design.docx")
ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
VER, DATE = "v2.0", "6 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL", VER)
ds.title_page(doc, "DOC-01", "Architecture & Design", "Structure & design of the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL")
ds.doc_control(doc, [
    ["v1.0", "2026-08-01", "Douglas Colvin", "Initial issue"],
    [VER, "2026-08-06", "Douglas Colvin",
     "Copy overhaul + service pages + articles + services estimator + contact mail pipeline + "
     "apps front door; site is 12 pages + one PHP endpoint"],
])
ds.add_toc(doc)

ds.heading(doc, "1.  Executive summary", 1)
ds.para(doc, "The **P3MAI website** is the public business site for P3MAI (Douglas Colvin's program, "
        "project and PMO consultancy). It is a **hand-built site with no framework and no build step** — "
        "twelve HTML pages, two standalone estimators, one shared stylesheet and script, and exactly one "
        "piece of server-side code: `contact.php`, which emails enquiries to the domain mailbox. It "
        "carries the P3MAI brand (navy/gold, Poppins, pyramid logo, two-tone P3M+AI wordmark), presents a "
        "Board-level positioning (“AI-Enabled · Sovereign · Safe · Proven”), and links to six live "
        "P3MAI web apps through the **apps.p3mai.com front door**. Hosted on **Rise** at **p3mai.com**.")

ds.heading(doc, "2.  Introduction", 1)
ds.heading(doc, "2.1  Purpose & scope", 2)
ds.para(doc, "The design and structure reference for the website. Visitor-facing guidance is in "
        "**DOC-02**; maintenance and publishing in **DOC-03**.")
ds.heading(doc, "2.2  Audience", 2)
ds.para(doc, "Whoever maintains the site — comfortable editing HTML/CSS/JS and one small PHP file.")

ds.heading(doc, "3.  Site overview", 1)
ds.para(doc, "Twelve linked pages plus two standalone estimators, all sharing one header/footer shell:")
ds.figure(doc, os.path.join(ASSETS, "web_sitemap.png"), "Figure 1 — Site map.")
ds.table(doc, ["Page", "Purpose"], [
    ["index.html", "Home — problem-led hero + capability strap, named-client strip, story section, "
     "track record, engagement ladder, dual CTA"],
    ["about.html", "Breadth-first bio, six-milestone career timeline, sovereign-and-safe credentials, "
     "certifications"],
    ["services.html", "Three service cards (who-for lines, Service Details links, six app buttons), "
     "estimator CTA, comparison table"],
    ["program-management.html", "Service detail: triggers, method, Core42 supercomputers case study, ladder"],
    ["project-management.html", "Service detail: triggers, method, ENBD fraud case study, ladder"],
    ["pmo-services.html", "Service detail: triggers, method, Core42 Responsible-AI-PMO + Emirates/dnata "
     "case studies, ladder"],
    ["blog.html", "Four posts, each linking to a full article page"],
    ["building-web-apps-with-claude.html", "Article: the site/apps built with Claude — the case study"],
    ["ai-programs-need-a-pmo.html", "Article: day-one governance for AI programs"],
    ["scaling-ai-infrastructure.html", "Article: TOP500-scale delivery discipline"],
    ["agentic-ai-in-the-pmo.html", "Article: agents do assembly, humans do judgment"],
    ["contact.html", "Validated form (posts to contact.php), details, map"],
    ["p3mai_services_cost_estimator.html", "THE services estimator — towers, 12 products, POTI, tiers, "
     "licence scale; quote button carries the basket to the contact form"],
    ["calculator.html", "Legacy standalone web-project estimator (unlinked)"],
], col_widths=[5.2, 10.3])

ds.heading(doc, "4.  Technology", 1)
ds.table(doc, ["Aspect", "Choice"], [
    ["Markup", "Hand-written HTML5, one file per page"],
    ["Styling", "A single CSS design system (style.css, versioned ?v=N)"],
    ["Behaviour", "Vanilla JavaScript (script.js, versioned ?v=N) — no framework, no build"],
    ["Server-side", "contact.php only — the mail handler (PHP 8 on Rise)"],
    ["Fonts", "Poppins (brand), system fallbacks"],
    ["Assets", "SVG logo set, 3D tile icons, blog thumbnails"],
    ["Hosting", "Rise (UK shared cPanel/FTP) behind StackCDN"],
], col_widths=[3.2, 12.3])
ds.callout(doc, "note", "Almost no build step — by design",
           ["Static pages plus one PHP endpoint. Edit, preview, publish. The only compiled artefacts "
            "anywhere are these documents."])

ds.heading(doc, "5.  Design system & brand", 1)
ds.table(doc, ["Element", "Value"], [
    ["Primary colour", "Navy #0B2545 (with dark #071830)"],
    ["Accent", "Gold #C9A227"],
    ["Background", "Light grey #F6F7F9"],
    ["Font", "Poppins"],
    ["Logo", "Original plan-view pyramid mark; wordmark is HTML text"],
    ["Wordmark rule", "Always two-tone: 'P3M' in primary, 'AI' in gold — never flat"],
], col_widths=[3.6, 11.9])
ds.para(doc, "`style.css` holds the shared design system, including the copy-overhaul components: hero "
        "eyebrow strap, ghost buttons, client strip, story section, engagement-ladder cards, case-study "
        "blocks, trigger lists, article typography and the takeaways box. The **header and footer markup "
        "is byte-identical across every page** (except the active nav item).")

ds.heading(doc, "6.  Front-end behaviour", 1)
ds.para(doc, "`script.js` provides the interactions, all progressive enhancements over the static markup:")
ds.bullet(doc, "**Env-aware app links** — six Services-page buttons carry localhost dev defaults; "
          "script.js swaps them to the live apps.p3mai.com URLs in production (see §7);")
ds.bullet(doc, "**Contact-form context prefill** — Get in Touch buttons pass ?interest=<service>, the "
          "estimator passes its itemised basket as ?details=; both land in the Message field, never "
          "overwriting typed text;")
ds.bullet(doc, "**Real form submission** — fetch POST to contact.php with a locked Sending… state, a "
          "genuine success message, and a graceful direct-email fallback on failure;")
ds.bullet(doc, "**Page-transition overlay, responsive hamburger nav, reveal-on-scroll, client-side "
          "validation, smooth scrolling.**")

ds.heading(doc, "7.  Integrations", 1)
ds.para(doc, "All six P3MAI apps are served behind one front door — **apps.p3mai.com**, a Render reverse "
        "proxy — and every app links back to the site:")
ds.table(doc, ["Services-page button", "Dev default", "Production"], [
    ["PMO Example", "localhost:5173", "apps.p3mai.com/pmo"],
    ["P3M3 Maturity Assessment", "localhost:5174", "apps.p3mai.com/p3m3"],
    ["PRINCE2 Method Map", "localhost:5175", "apps.p3mai.com/prince2"],
    ["MSP Method Map", "localhost:5176", "apps.p3mai.com/msp"],
    ["SAFe Method Map", "localhost:5177", "apps.p3mai.com/safe"],
    ["PMBOK Method Map", "localhost:5178", "apps.p3mai.com/pmbok"],
], col_widths=[4.6, 3.4, 7.5])
ds.callout(doc, "pitfall", "Env-aware links — do not hardcode",
           ["The localhost hrefs in services.html are intentional dev defaults; `script.js` rewrites "
            "them in production. To change a target, edit the swap value in script.js, not the HTML."])
ds.para(doc, "The **contact pipeline** is the site's one integration with the outside world: "
        "contact.php validates, drops honeypot-caught bots, guards against header injection, and mails "
        "the enquiry to **drcolvin@p3mai.com** (From: noreply@p3mai.com for SPF; Reply-To: the visitor).")

ds.heading(doc, "8.  Hosting & deployment", 1)
ds.figure(doc, os.path.join(ASSETS, "web_hosting.png"),
          "Figure 2 — Hosting: Rise + StackCDN for the site; Render front door for the apps; "
          "contact.php mails the domain inbox.")
ds.para(doc, "The site is hosted on **Rise** (UK shared cPanel/FTP) behind **StackCDN**, which caches "
        "static assets by exact URL — hence the `?v=N` version strings on style.css and script.js. "
        "Publishing means uploading the approved files into `public_html`. Full steps, the allow-list "
        "and the CDN discipline are in **DOC-03**.")
ds.callout(doc, "pitfall", "Publish only the approved files",
           ["Never upload the whole project folder — it contains source assets, documents and memory "
            "that must never be public. DOC-03 carries the exact allow-list."])

ds.heading(doc, "9.  Design decisions", 1)
ds.table(doc, ["Decision", "Rationale"], [
    ["Static + one PHP endpoint", "Fast, robust, trivially hostable; email needs exactly one server-side file."],
    ["Byte-identical header/footer", "One consistent shell; verified with a diff after edits."],
    ["Env-aware links in JS", "Cross-links work in dev and prod with no manual editing."],
    ["Context-carrying CTAs", "Every enquiry arrives naming the service (or the estimator basket) it came from."],
    ["Asset version strings (?v=N)", "StackCDN caches by exact URL; bumping the string is the only reliable purge."],
    ["Original artwork only", "Brand integrity; no copyright risk."],
    ["No fabricated content", "Everything grounded in the real CV; testimonials section stays dormant until real quotes exist."],
], col_widths=[4.6, 10.9])

ds.heading(doc, "10.  Non-functional considerations", 1)
ds.bullet(doc, "**Performance** — static files behind a CDN; minimal JS.")
ds.bullet(doc, "**Responsiveness** — mobile-first layout with a hamburger menu.")
ds.bullet(doc, "**SEO** — per-page titles/meta descriptions; four full articles as the content layer.")
ds.bullet(doc, "**Security** — contact.php validates, caps lengths, strips CR/LF from headers, honeypots bots.")
ds.bullet(doc, "**Maintainability** — one file per page, one stylesheet, one script, one PHP file.")

ds.heading(doc, "11.  Roadmap", 1)
ds.bullet(doc, "Activate the dormant testimonials section once real attributed quotes exist (MKT-08).")
ds.bullet(doc, "Pivot the primary CTA to the free delivery health check after testimonials (MKT-09).")
ds.bullet(doc, "Analytics + email capture (MKT-01/02) — the funnel currently runs unmeasured.")

ds.heading(doc, "Appendix A — Files", 1)
ds.code_block(doc,
              "business-website/\n"
              "  index / about / services / blog / contact .html      core pages\n"
              "  program-management / project-management /\n"
              "    pmo-services .html                                 service detail pages\n"
              "  building-web-apps-with-claude / ai-programs-need-a-pmo /\n"
              "    scaling-ai-infrastructure / agentic-ai-in-the-pmo .html   articles\n"
              "  p3mai_services_cost_estimator.html                   THE services estimator\n"
              "  calculator.html                                      legacy estimator (unlinked)\n"
              "  contact.php                                          mail handler (the only PHP)\n"
              "  style.css / script.js                                design system + behaviour (?v=N)\n"
              "  logo/favicon SVGs, tile icons, blog thumbs, imagery\n"
              "  docs/                                                this documentation set")

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
