"""Generate 02_User_Manual.docx for the P3MAI website (visitor/site guide)."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "02_User_Manual.docx")
ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
VER, DATE = "v2.0", "6 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL", VER)
ds.title_page(doc, "DOC-02", "User Manual", "A guide to the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL")
ds.doc_control(doc, [
    ["v1.0", "2026-08-01", "Douglas Colvin", "Initial issue"],
    [VER, "2026-08-06", "Douglas Colvin",
     "Service detail pages, blog articles, services cost estimator, context-carrying contact flow"],
])
ds.add_toc(doc)

ds.heading(doc, "1.  About this guide", 1)
ds.para(doc, "The **P3MAI website** presents P3MAI's program, project and PMO consultancy, six live web "
        "apps, and a self-serve cost estimator. This guide walks a visitor through it all. Maintaining "
        "and publishing the site is covered in the **Operation Manual (DOC-03)**.")
ds.para(doc, "The site lives at **p3mai.com**. Every page shares the same navy/gold header and footer.")

ds.heading(doc, "2.  Navigating the site", 1)
ds.figure(doc, os.path.join(ASSETS, "web_sitemap.png"), "Figure 1 — Site map.")
ds.para(doc, "The top navigation links the five main areas: **Home**, **About**, **Services**, **Blog** "
        "and **Contact**. Services opens onto three detail pages; Blog opens onto four full articles. "
        "On a phone the menu collapses to a hamburger button.")

ds.heading(doc, "3.  Home", 1)
ds.para(doc, "The landing page opens with *“When the program cannot be allowed to fail”* under the "
        "capability strap *AI-Enabled · Sovereign · Safe · Proven*, then: the named clients P3MAI has "
        "delivered for, the problem-we-solve story, the track record (banking & finance, enterprise "
        "delivery, sovereign AI), and **Start Where It Suits You** — a three-step ladder from free tools, "
        "to products, to engaging Douglas directly.")

ds.heading(doc, "4.  About", 1)
ds.para(doc, "Douglas Colvin's story across nine industries, a six-milestone career timeline (Vodafone "
        "1999 → two TOP500 AI supercomputers 2024–25), what “sovereign and safe” means in practice, "
        "values, certifications and education.")

ds.heading(doc, "5.  Services", 1)
ds.para(doc, "Three service cards — **Program Management**, **Project Management** and **PMO** — each "
        "stating who it is for, with three routes onward:")
ds.bullet(doc, "**Service Details** — a full page per service: when you'd call, how it works, a real "
          "case study (Core42 supercomputers / ENBD fraud / Responsible AI PMO + Emirates), and three "
          "ways to start;")
ds.bullet(doc, "**live tool buttons** — six P3MAI apps open directly from the cards (see §9);")
ds.bullet(doc, "**Get in Touch** — opens the contact form with your interest already noted.")
ds.para(doc, "Between the cards and the comparison table sits **Get an Instant Cost Estimate** — the "
        "services estimator (§8).")

ds.heading(doc, "6.  Blog", 1)
ds.para(doc, "Four posts, each with a full **Read more** article: building web sites and apps with "
        "Claude (this site is the case study), why AI programs need a PMO from day one, scaling AI "
        "infrastructure without losing control, and agentic AI in the PMO. Every article ends with "
        "practical takeaways and a route into the tools or a conversation.")

ds.heading(doc, "7.  Contact", 1)
ds.para(doc, "A validated form, the business details, and a location map. Two things happen for you "
        "automatically: if you arrived from a service page or the estimator, **your context is already "
        "in the message box** (edit it freely); and on Send, your enquiry is **emailed directly to "
        "P3MAI** — you'll see an on-page confirmation. If anything goes wrong you're shown the direct "
        "address (drcolvin@p3mai.com) instead.")

ds.heading(doc, "8.  Services Cost Estimator", 1)
ds.para(doc, "The estimator prices P3MAI's actual catalogue interactively: choose a **service line** "
        "(Digital Products / Delivery & Automation / Consulting), pick **products**, set **POTI "
        "dimensions** for consulting items, choose **tier** (Standard / Enhanced / Tailored) and "
        "**licence scale**, add **service days** and an optional **maintenance window**. The running "
        "estimate builds in the right-hand rail in AED, GBP or USD.")
ds.callout(doc, "tip", "Get a Detailed Quote",
           ["The button under the total takes you to the contact form with your full selection — every "
            "line item and the totals — already written into the message. Nothing is stored anywhere "
            "until you choose to send it."])

ds.heading(doc, "9.  The six apps", 1)
ds.table(doc, ["From the Services page", "Opens"], [
    ["PMO card → PMO Example", "A live project-portfolio tool (apps.p3mai.com/pmo)"],
    ["PMO card → P3M3 Maturity Assessment", "A free self-assessment of your delivery maturity (/p3m3)"],
    ["Project card → PRINCE2 / SAFe / PMBOK Method Maps", "Interactive method explorers (/prince2, /safe, /pmbok)"],
    ["Program card → MSP Method Map", "The programme-management method explorer (/msp)"],
], col_widths=[6.6, 8.9])
ds.para(doc, "Each app has its own **Back to Website** link to return you here.")

ds.heading(doc, "10.  Tips & FAQ", 1)
ds.table(doc, ["Question", "Answer"], [
    ["How do I get in touch?", "Any Get in Touch button — the form will already know which service you were reading about."],
    ["Is the cost estimate binding?", "No — indicative. Final pricing follows a scoping conversation."],
    ["Are the apps free?", "The method maps and the P3M3 assessment are free and self-serve."],
    ["Where do I start?", "The home page's Start Where It Suits You ladder: free tools → products → talk to Douglas."],
    ["Does it work on mobile?", "Yes — responsive layout with a hamburger menu."],
], col_widths=[5.0, 10.5])

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
