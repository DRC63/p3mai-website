# tools

Build scripts for P3MAI brand assets.

| Script | What it does |
|---|---|
| `brand-assets.py` | Generates `brand_cover.png`, `brand_header.png` and `brand_footer.png` — the P3MAI lockups embedded in Word and PowerPoint deliverables. Draws the pyramid from the same polygon geometry as the SVG logos, and renders the wordmark **two-tone**: `P3M` in navy or white, `AI` in gold. |

## Running it

```bash
python tools/brand-assets.py     # writes the three PNGs into the working directory
```

## The one fragile part

The wordmark is drawn as two separate text objects. `AI` is positioned at
`bb.x1 - bb.width*0.105`, where `bb` is the measured bounding box of `P3M`. That correction
removes the trailing side-bearing which otherwise leaves a visible gap between `P3M` and `AI`.

**It is empirical, not derived.** If you change the font, the weight or the size, re-render and
look at the result before trusting it.

See `memory/approach/brand-lockup.md` for the wordmark rule itself and the audit command.
