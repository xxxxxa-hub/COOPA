# Diet Problem with Proportion Constraint Example (Turkey and Tuna)

## Problem Statement
A bodybuilder chooses between two pre-prepared meals:
- Turkey dinner: 20g protein, 30g carbs, 12g fat per meal
- Tuna salad sandwich: 18g protein, 25g carbs, 8g fat per meal

Their requirements:
- At least 150g protein
- At least 200g carbs
- At most 40% of the meals should be turkey dinner

Objective: Minimize total fat intake.

## Algebraic Formulation
Variables:
- x1: number of turkey dinners (continuous, >= 0)
- x2: number of tuna salad sandwiches (continuous, >= 0)

Minimize: 12*x1 + 8*x2

Subject to:
- 20*x1 + 18*x2 >= 150
- 30*x1 + 25*x2 >= 200
- x1 / (x1 + x2) <= 0.4   (if x1 + x2 > 0)
- x1 >= 0, x2 >= 0

### Linearization Note
The ratio constraint is handled by the equivalent linear constraint:
x1 <= 0.4 * (x1 + x2), or 0.6*x1 - 0.4*x2 <= 0

## Pyomo Model Example

```python
from pyomo.environ import *

model = ConcreteModel()
model.x1 = Var(domain=NonNegativeReals)  # turkey dinners
model.x2 = Var(domain=NonNegativeReals)  # tuna sandwiches

model.obj = Objective(expr = 12*model.x1 + 8*model.x2, sense=minimize)
model.protein = Constraint(expr = 20*model.x1 + 18*model.x2 >= 150)
model.carbs = Constraint(expr = 30*model.x1 + 25*model.x2 >= 200)
model.ratio = Constraint(expr = 0.6*model.x1 - 0.4*model.x2 <= 0)

# To solve: SolverFactory('glpk').solve(model)
```

## Solution Summary

- Optimal meals: 0 turkey dinners, 8.33 tuna sandwiches
- Minimized fat: 66.67 grams
- Constraints are all satisfied
- Ratio/proportion constraint handled via linear reformulation

## Keywords
Diet, optimization, Pyomo, ratio constraint, blending, food planning, nutrition, linear programming, algebraic modeling, fat minimization
