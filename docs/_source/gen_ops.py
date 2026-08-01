"""Generate 03_Operation_Manual.docx for the P3MAI website."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "03_Operation_Manual.docx")
VER, DATE = "v1.0", "1 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL-SENSITIVE", VER)
ds.title_page(doc, "DOC-03", "Operation Manual", "Maintaining & publishing the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL-SENSITIVE")
ds.doc_control(doc, [[VER, "2026-08-01", "Douglas Colvin", "Initial issue"]])
ds.add_toc(doc)

ds.heading(doc, "1.  Purpose & audience", 1)
ds.para(doc, "For whoever maintains and publishes the **P3MAI website**. Covers editing content, the "
        "design system, the env-aware app links, local preview, publishing to Rise, DNS, version control, "
        "verification and troubleshooting. Structure/design is in **DOC-01**; the visitor guide is **DOC-02**.")

ds.heading(doc, "2.  System summary", 1)
ds.table(doc, ["Item", "Value"], [
    ["What", "Static site — hand-written HTML/CSS/JS, no build step"],
    ["Repository", "github.com/DRC63/p3mai-website (private)"],
    ["Hosting", "Rise (UK shared cPanel/FTP)"],
    ["Live URL", "p3mai.com"],
    ["Local preview", "python -m http.server 4173"],
], col_widths=[3.2, 12.3])

ds.heading(doc, "3.  Editing content", 1)
ds.para(doc, "Each page is a single HTML file; shared styling is in `style.css` and shared behaviour in "
        "`script.js`. There is no build step — edit, preview, publish.")
ds.callout(doc, "pitfall", "Keep the header/footer identical",
           ["The header and footer markup is byte-identical across all five pages (except the active nav "
            "item). After editing, verify with a diff so the shell stays consistent."])
ds.para(doc, "Standard verification after changes: CSS brace balance, HTML tag balance, and "
        "`node --check script.js` for the JavaScript.")

ds.heading(doc, "4.  The env-aware app links", 1)
ds.para(doc, "The Services page links to the PMO Service and the Method Map. Their hrefs in "
        "`services.html` are **dev defaults** (`localhost:5173` and `localhost:5175`); `script.js` "
        "rewrites them to the live URLs when the site is not on localhost.")
ds.callout(doc, "pitfall", "Do not hardcode the localhost links",
           ["Replacing the localhost hrefs with hardcoded production URLs breaks local development. To "
            "change a production target, edit the swap value in `script.js`, not the HTML."])
ds.para(doc, "When the Method Map's custom domain is live, change its production swap target in "
        "`script.js` from `method-map.onrender.com` to `prince2.p3mai.com`.")

ds.heading(doc, "5.  Local preview", 1)
ds.para(doc, "Serve the site over HTTP (not opened as a raw file) so the cross-links and transitions "
        "behave. A `business-website` preview config runs a simple server:")
ds.code_block(doc, "python -m http.server 4173")
ds.callout(doc, "note", "Why HTTP, not file://",
           ["`window.location.hostname` is empty for `file://` pages, and browsers block navigation "
            "between file:// and http://. Serving over HTTP (localhost:4173) keeps the env-detection and "
            "cross-links working."])

ds.heading(doc, "6.  Publishing to Rise", 1)
ds.para(doc, "Publishing means uploading the approved static files into Rise's `public_html` by FTP / "
        "File Manager. **Upload only these files — never the whole project folder** (it contains source "
        "assets, documents and memory that must not be public):")
ds.code_block(doc,
              "index.html  about.html  services.html  blog.html  contact.html  calculator.html\n"
              "style.css   script.js   favicon.svg\n"
              "logo-triangle-navy.svg  logo-triangle-white.svg  logo-triangle-icon.svg\n"
              "logo-triangle-icon.png  logo-triangle-white.png\n"
              "douglas.jpg\n"
              "blog-thumb-agentic.jpg  blog-thumb-pmo.jpg  blog-thumb-scale.jpg")
ds.callout(doc, "pitfall", "Never drop the entire folder",
           ["Dropping the whole business-website/ folder into public_html also uploads the CV, source "
            "images, .docx files, this docs set and the memory — all of which must stay private."])

ds.heading(doc, "7.  DNS & domains", 1)
ds.para(doc, "`p3mai.com` resolves to the Rise-hosted site. Two subdomains point at the P3MAI apps on "
        "Render:")
ds.table(doc, ["Host", "Points to", "For"], [
    ["p3mai.com", "Rise", "This static site"],
    ["app.p3mai.com", "Render", "PMO Service"],
    ["prince2.p3mai.com", "Render (CNAME method-map.onrender.com)", "Method Map (DNS pending)"],
], col_widths=[3.6, 6.4, 5.5])

ds.heading(doc, "8.  Version control", 1)
ds.para(doc, "Git repository at github.com/DRC63/p3mai-website (private). Local commit identity is set "
        "per-repo (Douglas Colvin / drcolvin@yahoo.com). `.gitignore` excludes Office lock files and OS "
        "junk.")

ds.heading(doc, "9.  Troubleshooting", 1)
ds.table(doc, ["Symptom", "Likely cause", "Fix"], [
    ["App link goes to localhost on the live site", "script.js didn't run / was edited", "Confirm script.js loads; check the env-detection block"],
    ["Cross-links broken locally", "Opened as file:// not http://", "Serve over http://localhost:4173"],
    ["Header/footer differ between pages", "Edited one page only", "Diff the pages; restore identical shell"],
    ["A private file is live", "Whole folder was uploaded", "Remove it from public_html; re-publish only the allow-list (§6)"],
    ["Broken layout after CSS edit", "Unbalanced braces", "Check CSS brace balance; revert and reapply"],
], col_widths=[4.6, 4.1, 6.8])

ds.heading(doc, "10.  Routine runbooks", 1)
ds.heading(doc, "10.1  Publish an update", 2)
ds.para(doc, "Edit → preview at localhost:4173 → verify (diff shell, brace/tag balance, node --check) → "
        "commit & push → upload the changed allow-list files to Rise public_html.")
ds.heading(doc, "10.2  Change an app link target", 2)
ds.para(doc, "Edit the production swap value in `script.js` (not the HTML), preview, commit, publish.")
ds.heading(doc, "10.3  Add a blog post", 2)
ds.para(doc, "Copy the pattern of an existing post in blog.html, keep the shared shell intact, add any "
        "thumbnail to the allow-list, publish.")

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
