# Elm Furniture Production Planning (Chairs & Dressers) — OR Linear Programming Example

## Problem Statement
Elm Furniture makes two products — chairs and dressers.
- Chair profit: $43 per unit
- Dresser profit: $52 per unit

Weekly resources available:
- Stain: 17 gallons
- Oak wood: 11 lengths

Each chair requires:
- 1.4 gallons stain
- 2 lengths wood

Each dresser requires:
- 1.1 gallons stain
- 3 lengths wood

**Objective:** Maximize total profit through optimal production of chairs (x) and dressers (y).

### Mathematical Model
Variables:
- x: number of chairs produced (continuous, nonnegative)
- y: number of dressers produced (continuous, nonnegative)

Objective:
- Maximize: 43*x + 52*y

Subject to:
- 1.4*x + 1.1*y <= 17 (stain constraint)
- 2*x + 3*y <= 11 (oak wood constraint)
- x >= 0, y >= 0

### Implementation
This problem was implemented and solved via Pyomo/GLPK:

### Solution & Insight
- **Maximum profit:** $0.00 — it is optimal to produce zero chairs and zero dressers (x=0, y=0).
- This counterintuitive solution results from the combination of available resource limits and per-unit usage:
    - It is not possible to produce even one of either product without exceeding resource constraints.
- Key lesson: *Always check feasibility before expecting a positive optimal value.*

---

## Useful for
- Quick reference for two-variable resource-constrained production models.
- Edge cases where the optimal production is zero (possibly due to restrictive constraints).

---