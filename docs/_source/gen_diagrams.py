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


# 1. Site map
f, ax = fig()
ax.text(6, 7.6, "P3MAI Website — Site Map", ha="center", fontsize=15, fontweight="bold", color=NAVY)
box(ax, 4.6, 6.0, 2.8, 1.0, "Home (index)", fill=NAVY)
pages = [("About", 0.4), ("Services", 3.15), ("Blog", 5.9), ("Contact", 8.65)]
for name, x in pages:
    box(ax, x, 3.9, 2.4, 0.95, name, fill=STEEL, fs=11)
    arrow(ax, 6.0, 6.0, x + 1.2, 4.85, color=GREY, style="-|>")
# services children
box(ax, 2.6, 1.9, 3.4, 0.9, "PMO app — 'Example'", fill=GREEN, fs=9, sub="app.p3mai.com")
box(ax, 6.4, 1.9, 3.4, 0.9, "Method Map", fill=GOLDD, fs=9, sub="prince2.p3mai.com")
arrow(ax, 4.1, 3.9, 4.0, 2.8, color=STEEL, style="-|>")
arrow(ax, 4.5, 3.9, 8.0, 2.8, color=STEEL, style="-|>")
box(ax, 4.4, 0.4, 3.2, 0.9, "Cost Estimator (calculator)", fill=PURPLE, fs=9, sub="standalone tool")
ax.text(6, 0.02, "Shared navy/gold header & footer on every page. A standalone Project Cost Estimator sits outside the main nav.",
        ha="center", fontsize=8, color=GREY, fontstyle="italic")
save(f, "web_sitemap.png")


# 2. Hosting & publishing
f, ax = fig()
ax.text(6, 7.6, "P3MAI Website — Hosting & Publishing", ha="center", fontsize=15, fontweight="bold", color=NAVY)
box(ax, 0.5, 4.4, 3.0, 1.3, "Local source", fill="white", fg=NAVY, edge=NAVY, sub="business-website/\n(HTML · CSS · JS)")
box(ax, 4.6, 4.4, 3.0, 1.3, "Rise hosting", fill=NAVY, sub="public_html (FTP)")
box(ax, 8.6, 4.4, 2.9, 1.3, "p3mai.com", fill=GOLDD, sub="the live site")
arrow(ax, 3.5, 5.05, 4.6, 5.05, color=NAVYL, text="upload selected files (FTP)", style="-|>")
arrow(ax, 7.6, 5.05, 8.6, 5.05, color=NAVYL, text="served", style="-|>")
# env-aware links to the two apps on Render
box(ax, 2.6, 1.6, 3.4, 1.0, "PMO Service", fill=GREEN, fs=10, sub="app.p3mai.com → Render")
box(ax, 6.4, 1.6, 3.4, 1.0, "Method Map", fill=STEEL, fs=10, sub="prince2.p3mai.com → Render")
arrow(ax, 9.6, 4.4, 8.1, 2.6, color=GREY, text="subdomains", style="-|>")
arrow(ax, 10.0, 4.4, 5.0, 2.6, color=GREY, style="-|>")
ax.text(6, 0.7, "The Services page links to both apps via env-aware JS (localhost in dev, live domain in prod).",
        ha="center", fontsize=8.5, color=GREY, fontstyle="italic")
ax.text(6, 0.2, "Publish = drop only the approved static files into public_html (never the whole folder).",
        ha="center", fontsize=8.5, color=RED, fontstyle="italic")
save(f, "web_hosting.png")
print("done")
