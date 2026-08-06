# P3MAI Pricing Model — the estimator's commercial logic

**Status:** Adopted 5 August 2026. Implemented in `p3mai_services_cost_estimator.html`.
**Governs:** how P3MAI offerings are structured, priced and quoted. Change this file and the
estimator together — they must not drift apart.

## The shape of the model

Three **towers** (which set rates), twelve **products** (fixed price), and a set of
**multipliers**. Products and services are priced separately and never contaminate each other.

```
one-time total  =  (products × tier × licence)  +  (days × day-rate × (1 + mobilisation))
maintenance     =  months × monthly-rate            [recurring, quoted separately]
```

## 1. Towers — set the rates, not the products

| Tower | Day rate | Label on the card | Monthly rate |
|---|---|---|---|
| Digital Products | $600 | tailoring / day | $250 |
| Delivery & Automation | $900 | delivery / day | $450 |
| Consulting | $1,400 | advisory / day | $900 |

The tower drives **only** the day rate and the maintenance monthly rate. It does not gate which
products can be bought — all twelve are available under any tower, and switching tower never
changes a product price or clears a selection.

## 2. Products — fixed price, complexity-ordered

All three families are visible together, each under its own heading, priced in ascending
complexity.

**Digital Products** — *Deploy once, use many times*
Document Templates $450 · Worked Examples $850 · Framework Mappings $1,450 · Delivery Process Pack $2,400

**Delivery & Automation Products** — *Functional Tooling*
Requirements Gathering $1,800 · Initiation $3,200 · Audit $4,800 · Recovery $6,800 · Acceleration $9,500

**Consulting Products** — *Priced per POTI dimension*
Design $2,400 · Training $1,600 · Mentoring $1,200 — **each multiplied by the number of POTI
dimensions selected**. Design across all four dimensions is $9,600.

## 3. POTI — the consulting multiplier

Processes · Organization · Technology · Information. Applies **only** to the three consulting
products. Digital and Delivery products ignore it entirely.

**Guard rail:** if a consulting product is selected with zero POTI dimensions it is *excluded*
from the total and an amber warning appears. It is never silently priced at zero. One dimension
(Processes) is pre-selected on load so the trap cannot fire unprompted.

## 4. Multipliers — both apply to products only

**Product tier** — what is included with each product:
Standard ×1 (installation + documentation) · Enhanced ×2 (+ training) · Tailored ×4 (+ full tailoring)

**Licence scale** — number of instances deployed in the organisation:
Solo ×1 · Small ×2 · Medium ×3 · Large ×5 · Enterprise ×8

They **compound**: Tailored + Large = ×20 on the product price. Neither touches service days or
maintenance.

## 5. Engagement horizon = a costed maintenance window

Not a percentage uplift. Handover only · Operational 3 months · Tactical 12 months · Strategic
24 months, charged at the tower's monthly rate. Always quoted **separately** from the one-time
total, never folded into it.

## 6. Mobilisation timeline — services only

Planned +0% · Priority +30% · Immediate +60%, applied to the **service days alone**. Product
prices are unaffected by how fast we mobilise, because compression costs delivery capacity, not
product cost. No days selected means no uplift, ever.

## 7. Currency

Base USD internally. Displayed in AED (default), GBP and USD, all three shown on the total.
USD 1 = AED 3.6725 (pegged) · USD 1 = GBP 0.7434. Rounded to the nearest 5 units.

## 8. Defaults on load

Everything at zero. Digital Products tower, no products selected, Processes only, Standard tier,
Solo licence, **0 days**, no maintenance window, Planned timeline → **total 0**. Nothing is
pre-charged, so the first number a visitor sees is one they built themselves.

## Interface conventions

Estimate breakdown is a **sticky right-hand rail**, never a block below the form — it stays
visible while the selections are made. Grouped Products / Services / Maintenance with a subtotal
each, so the arithmetic reconciles to the headline figure rather than relying on the reader to
add rounded lines.

## Open questions — decide before this goes public

1. **Licence multiplier currently applies to consulting products too.** Licensing instances makes
   obvious sense for a template pack; less so for a mentoring engagement. Consider restricting it
   to Digital Products, or to everything except Consulting.
2. **Tier and licence compound to ×32 at the top.** Tailored × Enterprise on the heaviest Delivery
   packs runs into seven figures. Arithmetically correct; commercially worth a cap or a
   "let's talk" state.
3. **Unit rates are internal judgement**, not published benchmarks. The market research
   (`memory/approach/route-to-market.md`) found *no* independent rate data for AI/PMO services —
   every published guide is written by a seller. These numbers are Douglas's to set and defend.

## Testing

A 55-check suite covers structure, defaults, wiring, pricing logic, reconciliation and boundary
behaviour. Re-run it after any change to rates or structure. Key invariants:

- mobilisation uplift never touches products, and never fires at zero days
- licence never touches services or maintenance; Enterprise == Solo × 8 exactly
- products + services == the one-time total; maintenance stays outside it
- totals never decrease when anything is added
- an empty basket totals zero regardless of multipliers, timeline or maintenance
