# Croissant Production Time Minimization (Operations Research Example)

## Problem Statement

A bakery makes almond and pistachio croissants.

- **Almond croissant:** 5 units butter, 8 units flour, 12 min per piece.
- **Pistachio croissant:** 3 units butter, 6 units flour, 10 min per piece.
- **Inventory:** 600 butter, 800 flour.
- **Popularity constraint:** At least 3 times as many almond croissants as pistachio.
- **Objective:** Minimize total production time.

## LP Formulation

Let:
- A = number of almond croissants (integer >= 0)
- P = number of pistachio croissants (integer >= 0)

**Objective:**
Minimize total time:  
T = 12 * A + 10 * P

**Constraints:**
- 5A + 3P <= 600      (butter)
- 8A + 6P <= 800      (flour)
- A >= 3P             (popularity)
- A, P >= 0 and integer

## Pyomo Model Prototype

## Standard Solution

With the above model, the optimal solution is:
- **A = 0, P = 0; Minimized time = 0.0**

This is *mathematically correct* (cost-minimizing, zero production is feasible under all constraints).

**If you require at least one croissant to be made, add the constraint:**
- A + P >= 1

## Notes

- This is a basic example of a resource-constrained, time-minimization LP with integer variables and a popularity (ratio) constraint.
- The objective function is non-negative and allows a trivial solution unless production is forced.

## References

- Croissant minimization problem, solved using Pyomo + GLPK
- Saved by the autonomous assistant (date: 2024-XX-XX)
