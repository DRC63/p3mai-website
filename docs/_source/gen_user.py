"""Generate 02_User_Manual.docx for the P3MAI website (visitor/site guide)."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "02_User_Manual.docx")
ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
VER, DATE = "v1.0", "1 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL", VER)
ds.title_page(doc, "DOC-02", "User Manual", "A guide to the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL")
ds.doc_control(doc, [[VER, "2026-08-01", "Douglas Colvin", "Initial issue"]])
ds.add_toc(doc)

ds.heading(doc, "1.  About this guide", 1)
ds.para(doc, "The **P3MAI website** presents P3MAI's programme, project and PMO consultancy and links to "
        "its two web apps. This guide walks a visitor through the pages and the interactive Project Cost "
        "Estimator. Maintaining and publishing the site is covered in the **Operation Manual (DOC-03)**.")
ds.para(doc, "The site lives at **p3mai.com**. Every page shares the same navy/gold header and footer, so "
        "navigation is consistent throughout.")

ds.heading(doc, "2.  Navigating the site", 1)
ds.figure(doc, os.path.join(ASSETS, "web_sitemap.png"), "Figure 1 — Site map.")
ds.para(doc, "The top navigation bar links the five main pages: **Home**, **About**, **Services**, "
        "**Blog** and **Contact**. On a phone the menu collapses to a hamburger button.")

ds.heading(doc, "3.  Home", 1)
ds.para(doc, "The landing page introduces P3MAI with the tagline *AI Program and Project Management "
        "Delivered at Scale*, three feature cards, a CV-sourced track record, and a call to action to "
        "get in touch.")

ds.heading(doc, "4.  About", 1)
ds.para(doc, "Douglas Colvin's biography and career timeline (drawn from the CV), certifications and "
        "values — who is behind P3MAI and the depth of delivery experience.")

ds.heading(doc, "5.  Services", 1)
ds.para(doc, "Three service cards — **Program Management**, **Project Management** and **PMO** — each "
        "with what it covers and a **Get in Touch** button, plus a comparison table of how each engages.")
ds.para(doc, "Two of the cards also demonstrate a live P3MAI tool:")
ds.bullet(doc, "the **Project Management** card links to the **PRINCE2 Method Map**;")
ds.bullet(doc, "the **PMO** card links (**Example**) to the **PMO Service** app.")

ds.heading(doc, "6.  Blog", 1)
ds.para(doc, "Short articles on AI, programme and project management.")

ds.heading(doc, "7.  Contact", 1)
ds.para(doc, "A validated contact form (it checks the fields before submitting), the business contact "
        "details, and a location map. The quickest way to start a conversation with P3MAI.")

ds.heading(doc, "8.  Project Cost Estimator", 1)
ds.para(doc, "The **calculator** page is a standalone, interactive **Project Cost Estimator**. Choose the "
        "options that describe your project and it produces an instant estimate in real time, then points "
        "you to email **hello@P3MAI.com** to take it further. Nothing is stored — it is a quick, private "
        "guide to likely cost.")
ds.callout(doc, "tip", "Use it as a conversation starter",
           ["The estimate is indicative — a starting point. Follow the on-screen prompt to get in touch "
            "for a tailored quote."])

ds.heading(doc, "9.  The two apps", 1)
ds.table(doc, ["From the Services page", "Opens"], [
    ["PMO card → Example", "The PMO Service — a live project-portfolio tool (app.p3mai.com)"],
    ["Project Management card → PRINCE2 Method Map", "An interactive PRINCE2 method explorer"],
], col_widths=[6.0, 9.5])
ds.para(doc, "Each app has its own **Back to Website** link to return you here.")

ds.heading(doc, "10.  Tips & FAQ", 1)
ds.table(doc, ["Question", "Answer"], [
    ["How do I get in touch?", "Use the Contact page form, or the details listed there."],
    ["Is the cost estimate binding?", "No — it's indicative; contact P3MAI for a tailored quote."],
    ["What are the two apps?", "The PMO Service (portfolio tool) and the PRINCE2 Method Map (method explorer)."],
    ["Does it work on mobile?", "Yes — the layout is responsive with a hamburger menu."],
], col_widths=[5.0, 10.5])

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
