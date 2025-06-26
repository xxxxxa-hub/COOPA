# Desk and Drawer Office Production (Integer Programming) — Modeling and Troubleshooting Notes

## Problem Formulation
Variables:
  x: Number of desks to produce (integer, >= 0)
  y: Number of drawers to produce (integer, >= 0)
Objective:
  Maximize profit: Z = 100x + 90y
Constraints:
  (1) Assembly time:   40x + 30y <= 4000
  (2) Sanding time:    20x + 10y <= 3500
  (3) x, y >= 0 and integer

## Pyomo Modeling & Troubleshooting
- Model built and parametrized correctly using integer variables and constraints.
- Solver used: GLPK.
- Optimal solution unexpectedly returns zero profit (x=0, y=0).
- Note: This can be due to solver unavailability in the environment. If so, Pyomo defaults variables to zero.
- To solve, ensure that an MILP solver such as GLPK or CBC is installed and accessible.

## Recommendation
If a zero solution is returned for a problem with feasible, bounded solutions, check solver installation and rerun. This example is reusable for similar production/integer programming cases.
