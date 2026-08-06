import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

NAVY='#0B2545'; DARKNAVY='#071830'; GOLD='#C9A227'; LIGHTGOLD='#E7C65C'; SHADE='#8A6B14'; WHITE='#ffffff'

# pyramid polygons from the SVG (y flipped: svg y-down -> mpl y-up)
def pyramid(ax, cx, cy, s):
    """s = scale; SVG coords span x 16..66, y 14..58 with apex point 37,26"""
    def P(x,y): return (cx + (x-41)*s, cy - (y-36)*s)
    ax.add_patch(Polygon([P(16,14),P(66,14),P(37,26)], closed=True, facecolor=LIGHTGOLD, edgecolor=LIGHTGOLD, lw=0.5))
    ax.add_patch(Polygon([P(16,14),P(41,58),P(37,26)], closed=True, facecolor=GOLD,      edgecolor=GOLD,      lw=0.5))
    ax.add_patch(Polygon([P(66,14),P(41,58),P(37,26)], closed=True, facecolor=SHADE,     edgecolor=SHADE,     lw=0.5))

# ---------- 1. Cover banner ----------
fig,ax=plt.subplots(figsize=(16.0,7.4),dpi=200); ax.set_xlim(0,16); ax.set_ylim(0,7.4); ax.axis('off')
ax.add_patch(FancyBboxPatch((0,0),16,7.4,boxstyle="square,pad=0",linewidth=0,facecolor=NAVY))
ax.add_patch(FancyBboxPatch((0,0),16,0.34,boxstyle="square,pad=0",linewidth=0,facecolor=GOLD))
pyramid(ax, 3.05, 4.30, 0.062)
t = ax.text(4.35,4.34,"P3M",ha='left',va='center',fontsize=58,color=WHITE,fontweight='bold')
fig.canvas.draw()
bb = t.get_window_extent().transformed(ax.transData.inverted())
ax.text(bb.x1 - bb.width*0.105,4.34,"AI",ha='left',va='center',fontsize=58,color=GOLD,fontweight='bold')
ax.text(4.42,3.28,"AI PROGRAM AND PROJECT MANAGEMENT DELIVERED AT SCALE",
        ha='left',va='center',fontsize=11.5,color=GOLD,fontweight='bold')
ax.plot([3.05,12.6],[2.55,2.55],color='#33517A',lw=1.4)
ax.text(3.05,1.85,"Program, Project and PMO Management in AI",ha='left',va='center',
        fontsize=12.5,color='#C7D2DF')
ax.text(3.05,1.24,"p3mai.com  ·  Dubai / Abu Dhabi, UAE",ha='left',va='center',
        fontsize=9.5,color='#8FA3BC')
fig.tight_layout(pad=0); fig.savefig("brand_cover.png",bbox_inches='tight',pad_inches=0,facecolor=NAVY)
plt.close(fig)

# ---------- 2. Header logo (navy wordmark, white bg) ----------
fig,ax=plt.subplots(figsize=(6.4,1.30),dpi=300); ax.set_xlim(0,6.4); ax.set_ylim(0,1.30); ax.axis('off')
pyramid(ax, 0.52, 0.65, 0.0125)
t = ax.text(1.02,0.63,"P3M",ha='left',va='center',fontsize=27,color=NAVY,fontweight='bold')
fig.canvas.draw()
bb = t.get_window_extent().transformed(ax.transData.inverted())
ax.text(bb.x1 - bb.width*0.105,0.63,"AI",ha='left',va='center',fontsize=27,color=GOLD,fontweight='bold')
fig.tight_layout(pad=0); fig.savefig("brand_header.png",bbox_inches='tight',pad_inches=0.02,
                                     transparent=True)
plt.close(fig)

# ---------- 3. Footer mark (pyramid + small wordmark) ----------
fig,ax=plt.subplots(figsize=(5.2,1.10),dpi=300); ax.set_xlim(0,5.2); ax.set_ylim(0,1.10); ax.axis('off')
pyramid(ax, 0.42, 0.55, 0.0105)
t = ax.text(0.86,0.53,"P3M",ha='left',va='center',fontsize=20,color=NAVY,fontweight='bold')
fig.canvas.draw()
bb = t.get_window_extent().transformed(ax.transData.inverted())
ax.text(bb.x1 - bb.width*0.105,0.53,"AI",ha='left',va='center',fontsize=20,color=GOLD,fontweight='bold')
fig.tight_layout(pad=0); fig.savefig("brand_footer.png",bbox_inches='tight',pad_inches=0.02,
                                     transparent=True)
plt.close(fig)
print("brand assets built")
