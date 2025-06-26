# Minimize Total Effective Time of Fertilizer and Seeds: Linear Programming Example

## Problem Statement
Minimize the total effective time for both fertilizer and seeds while satisfying the following linear constraints.

## Variables
- x = units of fertilizer
- y = units of seeds

## Objective
Minimize:  
    0.5x + 1.5y

## Subject to Constraints
- x + y <= 300
- x >= 50
- x <= 2y
- x >= 0
- y >= 0

## Solution
- Optimal: x = 50.0, y = 25.0
- Minimum objective value: 62.5
- Solved with Pyomo using GLPK.
- See associated Python implementation file: `continuous_lp_xy_minimize.py`

## Pyomo (Python) model template

```python
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals

model = ConcreteModel()

# Decision variables
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# Objective: Minimize total effective time
model.obj = Objective(expr=0.5 * model.x + 1.5 * model.y, sense=1)

# Constraints
model.c1 = Constraint(expr=model.x + model.y <= 300)
model.c2 = Constraint(expr=model.x >= 50)
model.c3 = Constraint(expr=model.x <= 2 * model.y)

# Solve
solver = SolverFactory('glpk')
results = solver.solve(model, tee=True)

print(f"x = {model.x.value}, y = {model.y.value}")
print(f"Minimum objective value = {model.obj()}.")
```

## Notes
- This structure and code can be adapted as a template for other continuous-variable linear programming minimization problems with similar constraints.
