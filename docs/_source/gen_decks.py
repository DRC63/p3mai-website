"""Generate the three PowerPoint summary decks for the P3MAI website docs."""
import os
from deckstyle import Deck, RED

DOCS = os.path.join(os.path.dirname(__file__), "..")
A = lambda n: os.path.join(DOCS, "assets", n)

# 01 Architecture
d = Deck("DOC-01", "OFFICIAL")
d.title_slide("Architecture & Design", "Structure & design of the P3MAI website — summary (v2.0)")
d.bullets("What it is", [
    "Public business site for P3MAI — Board-level positioning.",
    "12 pages + 2 estimators + ONE PHP endpoint (contact.php).",
    "Hand-built HTML/CSS/JS — no framework, no build step.",
], lead="“AI-Enabled · Sovereign · Safe · Proven.”")
d.image("Site map", A("web_sitemap.png"),
        lead="Services opens 3 detail pages, the estimator and 6 live apps; Blog opens 4 full articles.")
d.table("Technology", ["Aspect", "Choice"], [
    ["Markup / style", "HTML5 · one CSS design system (?v=N versioned)"],
    ["Behaviour", "Vanilla JS (script.js ?v=N) — env-aware links, context CTAs"],
    ["Server-side", "contact.php only — the mail handler"],
    ["Brand", "Navy #0B2545 · gold #C9A227 · Poppins · two-tone P3M+AI wordmark"],
    ["Hosting", "Rise (UK cPanel/FTP) behind StackCDN"],
], col_widths=[3.2, 8.9])
d.bullets("Front-end behaviour (script.js)", [
    "Env-aware app links — six buttons swap to apps.p3mai.com/<slug> in prod.",
    "Context CTAs: ?interest= (service) and ?details= (estimator basket) prefill the contact form.",
    "Real form submission via fetch → contact.php → drcolvin@p3mai.com.",
    "Page transitions, hamburger nav, reveal-on-scroll, validation.",
])
d.image("Hosting & publishing", A("web_hosting.png"),
        lead="Rise + StackCDN for the site; Render front door for the apps; PHP mail pipeline.")
d.table("Key design decisions", ["Decision", "Why"], [
    ["Static + one PHP endpoint", "Fast, robust; email needs exactly one server file"],
    ["Byte-identical header/footer", "One consistent shell"],
    ["Context-carrying CTAs", "Every enquiry arrives naming its origin"],
    ["?v=N asset versioning", "StackCDN caches by exact URL"],
    ["No fabricated content", "Grounded in the real CV; testimonials dormant until real"],
], col_widths=[5.0, 7.1])
d.bullets("Roadmap", [
    "Activate testimonials when real quotes land (MKT-08) → CTA pivot (MKT-09).",
    "Analytics + email capture (MKT-01/02) — the funnel runs unmeasured today.",
])
d.save(os.path.join(DOCS, "01_Architecture_and_Design_Summary.pptx"))

# 02 User
d = Deck("DOC-02", "OFFICIAL")
d.title_slide("User Manual", "A guide to the P3MAI website — summary (v2.0)")
d.image("Site map", A("web_sitemap.png"),
        lead="5 main areas → 3 service pages, 4 articles, the estimator, 6 live apps.")
d.bullets("The pages", [
    "Home — problem-led hero, named clients, story, track record, the 3-step ladder.",
    "About — nine industries, six-milestone timeline, sovereign-and-safe credentials.",
    "Services — 3 cards with who-it's-for, Service Details pages, 6 app buttons.",
    "Blog — 4 posts, each with a full Read-more article.",
    "Contact — the form knows where you came from; enquiries email P3MAI directly.",
])
d.bullets("Services Cost Estimator", [
    "Pick a service line, products, POTI dimensions, tier, licence, days, maintenance.",
    "Live totals in AED / GBP / USD in the summary rail.",
    "Get a Detailed Quote → contact form with your full basket pre-written.",
    "Nothing stored until you choose to send.",
], lead="P3MAI's real catalogue, priced interactively.")
d.bullets("The six apps (all free to explore)", [
    "PMO Example + P3M3 Maturity Assessment (PMO card).",
    "PRINCE2 / SAFe / PMBOK Method Maps (Project card).",
    "MSP Method Map (Program card).",
    "All at apps.p3mai.com/<slug>; each links back to the site.",
])
d.bullets("Good to know", [
    "Start Where It Suits You: free tools → products → talk to Douglas.",
    "Estimates are indicative — final pricing follows a scoping conversation.",
    "Fully responsive; consistent navy/gold shell throughout.",
])
d.save(os.path.join(DOCS, "02_User_Manual_Summary.pptx"))

# 03 Ops
d = Deck("DOC-03", "OFFICIAL-SENSITIVE")
d.title_slide("Operation Manual", "Maintaining & publishing the P3MAI website — summary (v2.0)")
d.table("System at a glance", ["Item", "Value"], [
    ["Repository", "github.com/DRC63/p3mai-website (private)"],
    ["Hosting", "Rise (UK cPanel/FTP) behind StackCDN"],
    ["Live URL / mailbox", "p3mai.com · drcolvin@p3mai.com (via contact.php)"],
    ["Local preview", "python -m http.server 4173 (or start-local.bat)"],
    ["Asset versions (this issue)", "style.css?v=7 · script.js?v=8"],
], col_widths=[3.6, 8.5])
d.bullets("The CDN cache discipline", [
    ("Any CSS/JS change ⇒ bump its ?v=N in EVERY page and re-upload together.", RED),
    ("NEVER probe the next ?v=N before the file is deployed — it poisons the cache.", RED),
    "Verify origin with a throwaway query first; pre-warm the real URL after deploy.",
    "HIT + old last-modified = stale cache; fresh mtime + old content = wrong zip.",
])
d.bullets("The contact-mail pipeline", [
    "contact.html → contact.php → drcolvin@p3mai.com (Reply-To = visitor).",
    "Honeypot drops bots silently; header-injection guard; length caps.",
    "PHP doesn't run locally — the form only fully works on Rise.",
    "After any form change: curl test + confirm the email actually arrives.",
])
d.bullets("Publishing to Rise", [
    ("Upload ONLY the allow-list into public_html — never the whole folder.", RED),
    "Allow-list: 14 HTML pages + contact.php + CSS/JS + favicon + 2 logos + 12 images.",
    "Zip hygiene: distinct names per release, fingerprint check, delete after extract.",
])
d.table("DNS & domains", ["Host", "Points to"], [
    ["p3mai.com", "Rise (this site)"],
    ["apps.p3mai.com", "Render front door — all six apps at /<slug>"],
    ["app.p3mai.com", "Legacy 301 → apps.p3mai.com/pmo"],
], col_widths=[4.0, 8.1])
d.bullets("Troubleshooting quick hits", [
    "CSS/JS change invisible live → cache: bump ?v=N + pre-warm.",
    "Fresh upload, old content → wrong zip extracted: check the fingerprint.",
    "No enquiry emails → run the curl mail test; check spam + Rise mail logs.",
    "Cross-links broken locally → serve over http://, never file://.",
])
d.bullets("Publish an update (runbook)", [
    "Edit → preview :4173 → verify (shell diff, braces/tags, node --check) →",
    "bump ?v=N if CSS/JS changed → commit & push → upload allow-list files →",
    "verify live + pre-warm → mail-test if the form was touched.",
])
d.save(os.path.join(DOCS, "03_Operation_Manual_Summary.pptx"))
print("done — website decks")
