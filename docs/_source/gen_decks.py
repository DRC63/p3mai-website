"""Generate the three PowerPoint summary decks for the P3MAI website docs."""
import os
from deckstyle import Deck, RED

DOCS = os.path.join(os.path.dirname(__file__), "..")
A = lambda n: os.path.join(DOCS, "assets", n)

# 01 Architecture
d = Deck("DOC-01", "OFFICIAL")
d.title_slide("Architecture & Design", "Structure & design of the P3MAI website — summary")
d.bullets("What it is", [
    "Public business site for P3MAI.",
    "Five pages + a standalone Project Cost Estimator.",
    "Hand-built static site — HTML/CSS/JS, no framework, no build.",
], lead="Simple, fast, robust.")
d.image("Site map", A("web_sitemap.png"),
        lead="Home links five pages; Services links the two P3MAI apps.")
d.table("Technology", ["Aspect", "Choice"], [
    ["Markup / style", "HTML5 · one CSS design system"],
    ["Behaviour", "Vanilla JS (script.js) — no framework/build"],
    ["Brand", "Navy #0B2545 · gold #C9A227 · Poppins · pyramid logo"],
    ["Hosting", "Rise (UK shared cPanel/FTP)"],
], col_widths=[3.2, 8.9])
d.bullets("Front-end behaviour (script.js)", [
    "Env-aware app links (localhost in dev, live domain in prod).",
    "Page-transition overlay; responsive hamburger nav.",
    "Reveal-on-scroll; contact-form validation; smooth scroll.",
])
d.image("Hosting & publishing", A("web_hosting.png"),
        lead="Publish approved files by FTP into Rise public_html.")
d.bullets("Integrations", [
    "Services page → PMO Service (Example) and PRINCE2 Method Map.",
    "Both env-aware; both link back to the site.",
    "Cost estimator directs enquiries to hello@P3MAI.com.",
])
d.table("Key design decisions", ["Decision", "Why"], [
    ["Static, no framework/build", "Fast, robust, trivially hostable"],
    ["Byte-identical header/footer", "One consistent shell"],
    ["Env-aware links in JS", "Cross-links work in dev and prod"],
    ["No fabricated content", "Everything grounded in the real CV"],
], col_widths=[5.0, 7.1])
d.bullets("Roadmap", [
    "Switch the Method Map link to prince2.p3mai.com once DNS resolves.",
    "More blog content; optional analytics.",
])
d.save(os.path.join(DOCS, "01_Architecture_and_Design_Summary.pptx"))

# 02 User
d = Deck("DOC-02", "OFFICIAL")
d.title_slide("User Manual", "A guide to the P3MAI website — summary")
d.image("Site map", A("web_sitemap.png"), lead="Five pages + a standalone estimator.")
d.bullets("The pages", [
    "Home — intro, track record, call to action.",
    "About — bio, career timeline, certifications.",
    "Services — Program / Project / PMO cards + comparison.",
    "Blog — AI / PM articles.",
    "Contact — validated form, details, map.",
])
d.bullets("Services page — the two apps", [
    "Project Management card → PRINCE2 Method Map.",
    "PMO card → Example → the PMO Service app.",
    "Each app links back to the website.",
])
d.bullets("Project Cost Estimator", [
    "A standalone interactive calculator.",
    "Pick options → instant estimate in real time.",
    "Nothing stored; points you to hello@P3MAI.com.",
], lead="A quick, private guide to likely project cost.")
d.bullets("Good to know", [
    "Fully responsive — works on mobile with a hamburger menu.",
    "The estimate is indicative — contact P3MAI for a tailored quote.",
    "Consistent navy/gold header & footer throughout.",
])
d.save(os.path.join(DOCS, "02_User_Manual_Summary.pptx"))

# 03 Ops
d = Deck("DOC-03", "OFFICIAL-SENSITIVE")
d.title_slide("Operation Manual", "Maintaining & publishing the P3MAI website — summary")
d.table("System at a glance", ["Item", "Value"], [
    ["Repository", "github.com/DRC63/p3mai-website (private)"],
    ["Hosting", "Rise (UK shared cPanel/FTP)"],
    ["Live URL", "p3mai.com"],
    ["Local preview", "python -m http.server 4173"],
], col_widths=[3.2, 8.9])
d.bullets("Editing content", [
    "One HTML file per page; shared style.css and script.js.",
    "Keep the header/footer byte-identical across pages (diff after edits).",
    "Verify: CSS braces, HTML tags, node --check script.js.",
])
d.bullets("Env-aware app links — the rule", [
    ("Localhost hrefs in services.html are intentional dev defaults.", RED),
    "script.js rewrites them to live URLs in production.",
    "To change a target, edit the swap value in script.js — NOT the HTML.",
    "Switch Method Map to prince2.p3mai.com once DNS resolves.",
])
d.bullets("Publishing to Rise", [
    ("Upload ONLY the approved files into public_html — never the whole folder.", RED),
    "Allow-list: the 6 HTML pages, style.css, script.js, favicon, logo set, douglas.jpg, blog thumbs.",
    "The folder also holds the CV, source images, docs and memory — keep private.",
])
d.table("DNS & domains", ["Host", "Points to"], [
    ["p3mai.com", "Rise (this site)"],
    ["app.p3mai.com", "Render (PMO Service)"],
    ["prince2.p3mai.com", "Render (Method Map, DNS pending)"],
], col_widths=[4.0, 8.1])
d.bullets("Troubleshooting", [
    "App link shows localhost live → confirm script.js runs.",
    "Cross-links broken locally → serve over http://localhost:4173, not file://.",
    "Header/footer differ → diff pages, restore the shared shell.",
    "A private file went live → remove it, re-publish only the allow-list.",
])
d.bullets("Publish an update (runbook)", [
    "Edit → preview at :4173 → verify → commit & push → FTP the changed allow-list files.",
])
d.save(os.path.join(DOCS, "03_Operation_Manual_Summary.pptx"))
print("done — website decks")
