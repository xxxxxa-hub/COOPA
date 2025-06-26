# Example: Diet Problem (Nutrition Cost Minimization) with Pyomo

## Problem Statement

Minimize the cost of a diet meeting nutrition constraints:

- Each serving of vegetables: 2 units vitamins, 3 units minerals, cost $3.
- Each serving of fruits: 4 units vitamins, 1 unit minerals, cost $5.
- At least 20 units of vitamins and 30 units of minerals required.
- Variables: servings of vegetables (`x`), servings of fruit (`y`), both continuous and >= 0.

**Algebraic Model:**

Minimize:  
  3x + 5y

Subject to:  
  2x + 4y >= 20 (vitamins)  
  3x + 1y >= 30 (minerals)  
  x >= 0, y >= 0

## Pyomo Modeling Structure

- Variables: `x` and `y`, continuous and non-negative.
- Objective: Minimize cost `3x + 5y`
- Constraints: Nutrition requirements for vitamins and minerals.
- Solver: Open-source LP solver (GLPK/CBC).
- This form is reusable for other diet/cost minimization problems by adjusting coefficients.

## Solution

Optimal cost: **30.0**  
Optimal servings:  
  x = 10.0 servings of vegetables  
  y = 0.0 servings of fruits

## Example Pyomo Implementation

See: `nutrition_min_cost.py` (in working directory)
