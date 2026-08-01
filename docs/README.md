# P3MAI Website — Documentation Set

Formal documentation for the **P3MAI website** (the public business site on Rise).
Organised like the *Microsoft Ecosystem – PMO Project*: numbered documents, each
Word document paired with a PowerPoint summary, plus a house style and diagrams.

## Documents

| ID | Document | Word | PowerPoint summary |
|----|----------|------|--------------------|
| DOC-01 | **Architecture & Design** — structure, tech, design system, integrations, hosting | [01_Architecture_and_Design.docx](01_Architecture_and_Design.docx) | [01_…_Summary.pptx](01_Architecture_and_Design_Summary.pptx) |
| DOC-02 | **User Manual** — a visitor guide to the pages and the cost estimator | [02_User_Manual.docx](02_User_Manual.docx) | [02_…_Summary.pptx](02_User_Manual_Summary.pptx) |
| DOC-03 | **Operation Manual** — editing, env-aware links, local preview, publishing to Rise, DNS | [03_Operation_Manual.docx](03_Operation_Manual.docx) | [03_…_Summary.pptx](03_Operation_Manual_Summary.pptx) |

All three are **v1.0, 1 August 2026**. DOC-03 is **OFFICIAL-SENSITIVE** (it lists
the publish allow-list and hosting specifics); the others are **OFFICIAL**.

## Regenerating

Office files are generated from Python (`docs/_source/`, using `python-docx`,
`python-pptx`, `matplotlib`, `Pillow`):

```bash
python gen_diagrams.py   # PNG diagrams → ../assets
python gen_arch.py       # 01
python gen_user.py       # 02
python gen_ops.py        # 03
python gen_decks.py      # the three *_Summary.pptx
```

`docstyle.py` / `deckstyle.py` are the shared P3MAI-branded helpers.

> Word documents contain an auto Table of Contents field — click it and press **F9** on first open to populate it.
