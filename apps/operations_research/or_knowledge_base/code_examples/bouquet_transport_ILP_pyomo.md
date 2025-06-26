# Optimal Bouquet Transport: Integer Linear Programming Example

## Problem

A florist transports his flowers to stores in small bouquets and large bouquets.
- A small bouquet has 5 flowers, a large bouquet has 10 flowers.
- At most 80 small bouquets and 50 large bouquets can be transported.
- At most 70 bouquets in total.
- At least 20 large bouquets.
- Must transport at least twice as many small bouquets as large bouquets.
- Objective: Maximize the total number of flowers sent to stores.

## Variables
- x: small bouquets (integer, >=0)
- y: large bouquets (integer, >=0)

## Constraints
- x <= 80
- y <= 50
- x + y <= 70
- y >= 20
- x >= 2*y
- x, y >= 0, x and y are integers

## Objective
Maximize: `5x + 10y`

## Solution Outline

Modeled as an Integer Linear Programming (ILP) problem using Pyomo:

```python
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, SolverFactory

model = ConcreteModel()
model.x = Var(domain=NonNegativeIntegers)   # Small bouquets
model.y = Var(domain=NonNegativeIntegers)   # Large bouquets

# Constraints
model.c1 = Constraint(expr = model.x <= 80)
model.c2 = Constraint(expr = model.y <= 50)
model.c3 = Constraint(expr = model.x + model.y <= 70)
model.c4 = Constraint(expr = model.y >= 20)
model.c5 = Constraint(expr = model.x >= 2 * model.y)

# Objective: Maximize total flowers
model.obj = Objective(expr = 5 * model.x + 10 * model.y, sense=1)

# To solve:
# solver = SolverFactory('glpk')
# solver.solve(model)
# print('Small bouquets:', model.x.value)
# print('Large bouquets:', model.y.value)
# print('Total flowers:', 5 * model.x.value + 10 * model.y.value)
```

## Optimal Solution

- Small bouquets (x): 40
- Large bouquets (y): 20
- Maximum flowers delivered: 400

## Notes

- This pattern is typical for logistics and capacity-constrained transport optimization.
- Useful constraints for "at least k times as many" and lower/upper bounds on discrete variables.
- Pyomo code can be adapted quickly for similar real-world logistics LP/MIP problems.
