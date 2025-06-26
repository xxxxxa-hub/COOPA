
# Travelling Salesman Diet LP (Minimize Sodium Intake)

# Tags/Keywords:
diet LP, sodium, ramen, travelling salesman, food optimization, Pyomo diet, linear programming, MIP, case study

---

See below for full problem formulation, code, and solution details.

## Problem Description
A travelling salesman only eats ramen and fries. Each pack of ramen contains 400 calories, 20g protein, 100mg sodium. Each pack of fries contains 300 calories, 10g protein, 75mg sodium. At most 30% of meals can be ramen. The salesman needs at least 3000 calories and 80g protein per day. Find how many of each to eat to minimize sodium.

## Mathematical Formulation
Let x = packs of ramen, y = packs of fries.

- Minimize: `100x + 75y` (sodium mg)
- Subject to:
    - `400x + 300y >= 3000` (calories)
    - `20x + 10y >= 80` (protein)
    - `x <= 0.3 * (x + y)` (ramen <= 30% of total meals)
        - i.e., `0.7x - 0.3y <= 0`
    - `x >= 0, y >= 0`, integer

## Solution (Optimal)
- x = 0 packs ramen, y = 10 packs fries
- Objective value: 750 mg sodium

All constraints satisfied, integer solution.

## Solver Info
- Linear Programming (LP/MIP), solved with Pyomo + GLPK
- Model file: pyomo_min_sodium.py (see working directory if needed)
