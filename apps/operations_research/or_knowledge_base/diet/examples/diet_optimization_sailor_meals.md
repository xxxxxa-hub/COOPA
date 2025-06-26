# Diet Optimization Example: Sailor's Meals (Vitamin & Fat Constraints)

**Problem Statement**

A sailor must choose between crab cakes and lobster rolls for meals. Each meal must satisfy minimum vitamin requirements with a restriction on the percentage of lobster rolls consumed, and the goal is to minimize unsaturated fat intake.

## Variables
- x: Number of crab cakes (continuous)
- y: Number of lobster rolls (continuous)

## Data Table

|              | Crab Cake (per unit) | Lobster Roll (per unit) |
|--------------|----------------------|-------------------------|
| Vitamin A    | 5                    | 8                       |
| Vitamin C    | 7                    | 4                       |
| Unsat. Fat   | 4                    | 6                       |

## Constraints

- Vitamin A:      5x + 8y >= 80
- Vitamin C:      7x + 4y >= 100
- Lobster Limit:  y <= 0.4(x + y)  (at most 40% lobster rolls)
- Non-negativity: x >= 0, y >= 0

- The lobster constraint can be rewritten as:
    - y <= 0.4(x + y) -> 0.6y <= 0.4x -> 2x - 3y >= 0

## Objective

- Minimize total unsaturated fat:  4x + 6y

## Solution (LP with Pyomo)

Optimal solution:
- x ~= 13.33 (crab cakes)
- y ~= 1.67 (lobster rolls)
- **Minimum unsaturated fat intake = 63.33 units**

Solution found using Pyomo (see 'optimize_diet_lp.py' if referenced in code).

---

*This problem serves as a reusable LP template for diet optimization involving component limits and nutritional needs.*

---
