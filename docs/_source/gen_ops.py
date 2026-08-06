"""Generate 03_Operation_Manual.docx for the P3MAI website."""
import os
import docstyle as ds

OUT = os.path.join(os.path.dirname(__file__), "..", "03_Operation_Manual.docx")
VER, DATE = "v2.0", "6 August 2026"

doc = ds.new_doc()
ds.footer(doc, "OFFICIAL-SENSITIVE", VER)
ds.title_page(doc, "DOC-03", "Operation Manual", "Maintaining & publishing the P3MAI website",
              VER, DATE, "Douglas Colvin, P3MAI", "OFFICIAL-SENSITIVE")
ds.doc_control(doc, [
    ["v1.0", "2026-08-01", "Douglas Colvin", "Initial issue"],
    [VER, "2026-08-06", "Douglas Colvin",
     "New allow-list (12 pages + contact.php + tile icons), CDN cache-busting discipline, "
     "contact-pipeline operations, front-door link targets"],
])
ds.add_toc(doc)

ds.heading(doc, "1.  Purpose & audience", 1)
ds.para(doc, "For whoever maintains and publishes the **P3MAI website**. Covers editing, the env-aware "
        "app links, the contact-mail pipeline, local preview, publishing to Rise, the CDN cache "
        "discipline, DNS, version control and troubleshooting. Structure/design is in **DOC-01**; the "
        "visitor guide is **DOC-02**.")

ds.heading(doc, "2.  System summary", 1)
ds.table(doc, ["Item", "Value"], [
    ["What", "Hand-written HTML/CSS/JS + one PHP mail handler; no build step"],
    ["Repository", "github.com/DRC63/p3mai-website (private)"],
    ["Hosting", "Rise (UK shared cPanel/FTP) behind StackCDN"],
    ["Live URL", "p3mai.com"],
    ["Enquiry mailbox", "drcolvin@p3mai.com (fed by contact.php)"],
    ["Local preview", "python -m http.server 4173 (also in .claude/launch.json as business-website)"],
    ["Asset versions at this issue", "style.css?v=7 · script.js?v=8"],
], col_widths=[3.6, 11.9])

ds.heading(doc, "3.  Editing content", 1)
ds.para(doc, "Each page is a single HTML file; shared styling in `style.css`, shared behaviour in "
        "`script.js`, the mail handler in `contact.php`. Edit, preview, publish.")
ds.callout(doc, "pitfall", "Keep the header/footer identical",
           ["The header and footer markup is byte-identical across all twelve pages (except the active "
            "nav item). After editing, verify with a diff so the shell stays consistent."])
ds.para(doc, "Standard verification after changes: header/footer diff, CSS brace balance, HTML tag "
        "balance, `node --check script.js`.")

ds.heading(doc, "4.  The CDN cache-busting discipline", 1)
ds.para(doc, "StackCDN caches static assets **by exact URL**, so `style.css` and `script.js` are "
        "referenced with `?v=N` version strings. The rules, learned the hard way:")
ds.bullet(doc, "**Any change to style.css or script.js requires bumping its ?v=N** — in every page that "
          "references it — and re-uploading those pages with the file.")
ds.bullet(doc, "**Never request the next version's URL before the file is on the server.** The probe "
          "itself caches the OLD content under the NEW version string (this happened: v=6 was poisoned "
          "by a pre-deploy check). Verify the origin with a throwaway query (`?check=123`) first.")
ds.bullet(doc, "**Pre-warm after deploy**: once the origin is confirmed current, request the real ?v=N "
          "URL once so the CDN caches the correct content before any visitor arrives.")
ds.bullet(doc, "Diagnosis pattern: `x-cdn-cache-status: HIT` + an old `last-modified` = stale cache "
          "entry; fresh `last-modified` + old content = the wrong file was uploaded.")

ds.heading(doc, "5.  The env-aware app links", 1)
ds.para(doc, "Six Services-page buttons link the P3MAI apps. Their hrefs are **dev defaults** "
        "(localhost:5173–5178); `script.js` rewrites them to the live front-door URLs "
        "(apps.p3mai.com/pmo, /p3m3, /prince2, /msp, /safe, /pmbok) when not on localhost.")
ds.callout(doc, "pitfall", "Do not hardcode the localhost links",
           ["To change a production target, edit the swap value in `script.js` (and bump its ?v=N), "
            "not the HTML."])

ds.heading(doc, "6.  The contact-mail pipeline", 1)
ds.para(doc, "`contact.html` posts to `contact.php`, which emails the enquiry to **drcolvin@p3mai.com** "
        "(From: noreply@p3mai.com so SPF passes; Reply-To: the visitor, so replying just works). "
        "Get in Touch buttons pass `?interest=`, the estimator passes `?details=`; script.js prefills "
        "the Message field from both.")
ds.bullet(doc, "**Spam defence**: a hidden honeypot field — submissions that fill it are silently "
          "accepted and dropped. No CAPTCHA by design.")
ds.bullet(doc, "**Safety**: field length caps and CR/LF stripping (header-injection guard) in contact.php.")
ds.bullet(doc, "**Failure mode**: if mail() fails the visitor sees the direct address — check the inbox "
          "and Rise's mail logs if enquiries stop arriving; test with a real submission after any change.")
ds.callout(doc, "note", "Test after every deploy touching the form",
           ["curl -F 'name=Test' -F 'email=you@example.com' -F 'message=test' -F 'website=' "
            "https://p3mai.com/contact.php  → expect {\"ok\":true} AND the email in the inbox."])

ds.heading(doc, "7.  Local preview", 1)
ds.para(doc, "Serve over HTTP — never open pages as file:// (empty hostname breaks env-detection, and "
        "browsers block file↔http navigation):")
ds.code_block(doc, "python -m http.server 4173   # or start-local.bat for site + both PMO dev servers")
ds.para(doc, "contact.php cannot run locally (no PHP) — the form shows its graceful failure message in "
        "local dev; that is expected. The success path is verified on the live site.")

ds.heading(doc, "8.  Publishing to Rise", 1)
ds.para(doc, "Upload the approved files into Rise's `public_html` (File Manager or FTP). **Upload only "
        "these — never the whole project folder:**")
ds.code_block(doc,
              "index.html  about.html  services.html  blog.html  contact.html\n"
              "program-management.html  project-management.html  pmo-services.html\n"
              "building-web-apps-with-claude.html  ai-programs-need-a-pmo.html\n"
              "scaling-ai-infrastructure.html  agentic-ai-in-the-pmo.html\n"
              "p3mai_services_cost_estimator.html  calculator.html  contact.php\n"
              "style.css  script.js  favicon.svg\n"
              "logo-triangle-navy.svg  logo-triangle-white.svg\n"
              "douglas.jpg\n"
              "blog-thumb-agentic.jpg  blog-thumb-pmo.jpg  blog-thumb-scale.jpg\n"
              "blog-thumb-claude-build.jpg\n"
              "governance-and-control.png  delivery-at-scale.png  ai-powered-pmo.png\n"
              "delivery-excellence.png  trusted-partnership.png\n"
              "mini-budget-governance.png  mini-team-leadership.png  mini-ai-infrastructure.png")
ds.callout(doc, "pitfall", "Zip hygiene",
           ["When deploying by zip: use a distinct, purpose-named zip per release; check its file count "
            "against the release note before extracting (fresh timestamps + stale content on the server "
            "means the WRONG zip was extracted); delete the zip from public_html afterwards; clear "
            "superseded zips from Downloads."])
ds.callout(doc, "pitfall", "Never drop the entire folder",
           ["The project folder contains the CV, source images, planning documents, this docs set and "
            "memory — none of which may go public. The allow-list above is the whole publish set."])

ds.heading(doc, "9.  DNS & domains", 1)
ds.table(doc, ["Host", "Points to", "For"], [
    ["p3mai.com", "Rise (StackDNS zone)", "This site"],
    ["apps.p3mai.com", "Render (the apps front door / reverse proxy)", "All six apps at /<slug>"],
    ["app.p3mai.com", "Legacy — 301s to apps.p3mai.com/pmo", "Old PMO deep links"],
], col_widths=[3.6, 6.4, 5.5])
ds.callout(doc, "note", "CNAME values are bare hostnames",
           ["A pasted URL (https://…/) in a CNAME value breaks resolution — this happened during the "
            "original app.p3mai.com setup. Diagnose against the authoritative nameservers "
            "(ns1–4.stackdns.com), not the local resolver."])

ds.heading(doc, "10.  Version control", 1)
ds.para(doc, "Git repository at github.com/DRC63/p3mai-website (private). Local commit identity is set "
        "per-repo (Douglas Colvin / drcolvin@yahoo.com). `.gitignore` excludes Office lock files, OS "
        "junk, .env files and the internal reference/ folder. Commit and push with every published "
        "change — the repo is the rollback plan.")

ds.heading(doc, "11.  Troubleshooting", 1)
ds.table(doc, ["Symptom", "Likely cause", "Fix"], [
    ["CSS/JS change not visible live", "CDN serving the old exact URL", "Bump ?v=N in all pages, upload, pre-warm (§4)"],
    ["Fresh upload, old content", "Wrong zip extracted", "Check zip fingerprint; re-upload the right one (§8)"],
    ["Enquiries not arriving", "mail() failing or mailbox issue", "Run the §6 curl test; check spam folder and Rise mail logs"],
    ["App link goes to localhost live", "script.js edit broke env-detection", "Check the swap block; confirm script.js?v=N loads"],
    ["Cross-links broken locally", "Opened as file://", "Serve over http://localhost:4173 (§7)"],
    ["Form works locally but no email", "Expected — PHP only runs on Rise", "Verify on the live site (§7)"],
    ["Header/footer differ between pages", "Edited one page only", "Diff all twelve; restore the identical shell"],
], col_widths=[4.6, 4.1, 6.8])

ds.heading(doc, "12.  Routine runbooks", 1)
ds.heading(doc, "12.1  Publish an update", 2)
ds.para(doc, "Edit → preview at localhost:4173 → verify (shell diff, brace/tag balance, node --check) → "
        "bump ?v=N if CSS/JS changed → commit & push → upload the changed allow-list files → verify the "
        "live pages (and pre-warm any new ?v=N) → if the form was touched, run the §6 mail test.")
ds.heading(doc, "12.2  Change an app link target", 2)
ds.para(doc, "Edit the swap value in script.js, bump script.js ?v=N everywhere, preview, commit, publish.")
ds.heading(doc, "12.3  Add a blog article", 2)
ds.para(doc, "Copy an existing article page as the pattern (identical shell), add the teaser card to "
        "blog.html with its thumbnail, wire the Read more link, add both files to the allow-list, publish.")

doc.save(OUT)
print("wrote", os.path.basename(OUT), os.path.getsize(OUT), "bytes")
