# Diet Optimization: Salmon and Eggs Sodium Minimization

## Problem Summary
A fitness planner must eat only bowls of salmon and eggs. Each bowl of salmon contains 300 calories, 15g protein, 80mg sodium. Each bowl of eggs contains 200 calories, 8g protein, 20mg sodium. The planner must eat at least 2000 calories and 90g protein, and at most 40% of his meals can be eggs. Variables x (bowls salmon) and y (bowls eggs) are integers >=0.

## Mathematical Formulation
Minimize: 80*x + 20*y

Subject to:
- 300*x + 200*y >= 2000       (calories)
- 15*x + 8*y >= 90            (protein)
- y <= 0.4*(x + y)            (at most 40% eggs)
- x >= 0, y >= 0 and integer

## Optimal Solution
Objective value (min sodium): 460mg
x = 5 (bowls of salmon), y = 3 (bowls of eggs)

### Notes
- The "fraction of meals" constraint is encoded as y <= 0.4 * (x + y)
- All constraints are standard in diet/knapsack MILPs
- Model implemented in Pyomo using GLPK
