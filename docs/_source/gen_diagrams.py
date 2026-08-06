"""P3MAI-branded diagrams for the P3MAI website docs."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ASSETS = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS, exist_ok=True)
NAVY = "#0B2545"; NAVYL = "#1B3F6E"; GOLD = "#C9A227"; GOLDD = "#A8841C"
GREEN = "#2E7D5B"; RED = "#C0392B"; PURPLE = "#8E5BE0"; GREY = "#5B6675"
BG = "#F6F7F9"; STEEL = "#3D5A80"


def box(ax, x, y, w, h, text, fill=NAVY, fg="white", fs=11, bold=True, edge=None, sub=None):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                linewidth=1.4, edgecolor=edge or fill, facecolor=fill, zorder=2))
    ax.text(x + w / 2, y + h / 2 + (0.12 if sub else 0), text, ha="center", va="center",
            color=fg, fontsize=fs, fontweight="bold" if bold else "normal", zorder=3)
    if sub:
        ax.text(x + w / 2, y + h / 2 - 0.2, sub, ha="center", va="center", color=fg, fontsize=fs - 2.5, zorder=3)


def arrow(ax, x1, y1, x2, y2, color=GREY, text=None, style="-|>", lw=1.6):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=13,
                                 color=color, linewidth=lw, zorder=1))
    if text:
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + 0.12, text, ha="center", va="bottom",
                color=color, fontsize=8, fontstyle="italic")


def fig():
    f, ax = plt.subplots(figsize=(11, 6.6), dpi=150)
    ax.set_xlim(0, 12); ax.set_ylim(0, 8); ax.axis("off")
    f.patch.set_facecolor("white")
    return f, ax


def save(f, name):
    f.savefig(os.path.join(ASSETS, name), bbox_inches="tight", facecolor="white", pad_inches=0.15)
    plt.close(f); print("wrote", name)


# 1. Site map — 12 pages + estimator + the six-app front door
f, ax = fig()
ax.text(6, 7.7, "P3MAI Website — Site Map", ha="center", fontsize=15, fontweight="bold", color=NAVY)
box(ax, 4.6, 6.3, 2.8, 0.9, "Home (index)", fill=NAVY)
pages = [("About", 0.4), ("Services", 3.15), ("Blog", 5.9), ("Contact", 8.65)]
for name, x in pages:
    box(ax, x, 4.7, 2.4, 0.85, name, fill=STEEL, fs=11)
    arrow(ax, 6.0, 6.3, x + 1.2, 5.55, color=GREY, style="-|>")
# services children: 3 detail pages + estimator + the apps hub
box(ax, 0.3, 3.0, 3.6, 0.85, "3 service detail pages", fill=NAVYL, fs=9,
    sub="program · project · pmo")
box(ax, 4.15, 3.0, 3.3, 0.85, "Services Cost Estimator", fill=PURPLE, fs=9,
    sub="quote → contact form")
box(ax, 7.75, 3.0, 4.0, 0.85, "apps.p3mai.com front door", fill=GREEN, fs=9,
    sub="pmo · p3m3 · prince2 · msp · safe · pmbok")
arrow(ax, 3.9, 4.7, 2.1, 3.85, color=STEEL, style="-|>")
arrow(ax, 4.35, 4.7, 5.8, 3.85, color=STEEL, style="-|>")
arrow(ax, 4.8, 4.7, 9.7, 3.85, color=STEEL, style="-|>")
# blog children + contact backend
box(ax, 4.6, 1.4, 3.4, 0.85, "4 full articles", fill=GOLDD, fs=9,
    sub="Claude build · PMO day one · scaling AI · agentic AI")
arrow(ax, 7.1, 4.7, 6.3, 2.25, color=GREY, style="-|>")
box(ax, 8.65, 1.4, 3.0, 0.85, "contact.php", fill=RED, fs=9,
    sub="emails drcolvin@p3mai.com")
arrow(ax, 9.85, 4.7, 10.1, 2.25, color=GREY, style="-|>")
ax.text(6, 0.55, "Shared navy/gold shell on every page. Get in Touch buttons carry ?interest= context;",
        ha="center", fontsize=8, color=GREY, fontstyle="italic")
ax.text(6, 0.15, "the estimator's quote button carries the full basket to the contact form via ?details=.",
        ha="center", fontsize=8, color=GREY, fontstyle="italic")
save(f, "web_sitemap.png")


# 2. Hosting & publishing — Rise + StackCDN, front door, mail pipeline
f, ax = fig()
ax.text(6, 7.7, "P3MAI Website — Hosting & Publishing", ha="center", fontsize=15, fontweight="bold", color=NAVY)
box(ax, 0.4, 5.2, 2.9, 1.3, "Local source", fill="white", fg=NAVY, edge=NAVY,
    sub="business-website/\n(HTML · CSS · JS · PHP)")
box(ax, 4.1, 5.2, 2.9, 1.3, "Rise hosting", fill=NAVY, sub="public_html\n(File Manager / FTP)")
box(ax, 7.8, 5.2, 3.6, 1.3, "p3mai.com", fill=GOLDD, sub="behind StackCDN\n(assets cached by exact URL)")
arrow(ax, 3.3, 5.85, 4.1, 5.85, color=NAVYL, text="allow-list upload", style="-|>")
arrow(ax, 7.0, 5.85, 7.8, 5.85, color=NAVYL, text="served", style="-|>")
# the mail pipeline + the front door
box(ax, 1.0, 2.9, 3.6, 0.95, "contact.php → mailbox", fill=RED, fs=9,
    sub="drcolvin@p3mai.com (SPF via noreply@)")
arrow(ax, 8.6, 5.2, 3.4, 3.85, color=GREY, text="form posts", style="-|>")
box(ax, 5.4, 2.9, 3.2, 0.95, "?v=N cache-busting", fill=STEEL, fs=9,
    sub="bump on change · pre-warm after deploy")
box(ax, 9.0, 2.9, 2.6, 0.95, "apps front door", fill=GREEN, fs=9,
    sub="apps.p3mai.com/<slug>\n6 apps on Render")
arrow(ax, 10.3, 5.2, 10.3, 3.85, color=GREY, text="env-aware links", style="-|>")
ax.text(6, 1.6, "Never probe a future ?v=N URL before the file is deployed — the probe caches the old content under the new string.",
        ha="center", fontsize=8.5, color=RED, fontstyle="italic")
ax.text(6, 1.15, "Publish = only the approved allow-list into public_html (never the whole folder). Distinct zip names per release.",
        ha="center", fontsize=8.5, color=GREY, fontstyle="italic")
save(f, "web_hosting.png")
print("done")
