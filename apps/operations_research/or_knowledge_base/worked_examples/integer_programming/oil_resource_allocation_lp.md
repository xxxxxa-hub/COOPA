# Car Oils Resource Allocation LP Example

## Problem Statement

A car manufacturer makes two types of car oils: Oil Max and Oil Max Pro, each using different quantities of three resources (substances A, B, C). The objective is to maximize profit, subject to constraints on the total available resources.

### Data Example

- Oil Max: 46g A, 43g B, 56g C per container, $10 profit per container
- Oil Max Pro: 13g A, 4g B, 45g C per container, $15 profit per container
- Total available: 1345g A, 346g B, 1643g C

## Mathematical Model

Variables:
- x: Oil Max containers (integer, >=0)
- y: Oil Max Pro containers (integer, >=0)

Objective:
- Maximize profit: 10x + 15y

Constraints:
- 46x + 13y <= 1345  (A constraint)
- 43x + 4y  <= 346   (B constraint)
- 56x + 45y <= 1643  (C constraint)
- x, y >= 0, integers

## Solution Approach

- Formulate as an integer linear program (ILP).
- Use Pyomo with GLPK or CBC as an open-source solver.
- Ensure the solver invoked is capable of integer/mixed-integer programming.

## Troubleshooting & Best Practices

- If the solution returns zero or infeasible with resources apparently sufficient, check:
  - Solver supports integer programming (GLPK needs to be called with mip support).
  - All constraints and coefficients were entered correctly.
  - No copy-paste or ordering errors in model definitions.
- Manual cross-checking of feasibility is recommended when solver output is counterintuitive.
- If in doubt, cross-validate by trying small integer values for variables using simple calculation.

## Common Pitfalls

- Using an LP solver instead of an integer-capable solver.
- Misspecification of variable bounds or data types.
- Solver-specific configuration issues in Pyomo or related libraries.
- Not examining the solver log for hidden warnings/errors.

## File Reference

- `oil_optimizer.py` (example Pyomo model and solve script).

---
This entry can be referenced as a standard LP/ILP example for two-product resource allocation with material constraints and integer variables.
