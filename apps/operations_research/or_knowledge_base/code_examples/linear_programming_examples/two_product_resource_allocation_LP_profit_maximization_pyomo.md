# Two-Product Resource Allocation – Linear Programming Example

## Problem
Maximize profit by deciding quantities of two products with resource constraints.

## Formulation
Decision variables, objective function, and constraints outlined for arbitrary coefficients (profits and resource usage).

## Example Coefficients
- Profit per scooter: 200, per bike: 300
- Resources: 
    - design team: 2 hr/scooter, 4 hr/bike, 5000 hr total
    - engineering team: 3 hr/scooter, 5 hr/bike, 6000 hr total

## Standard Model (Pyomo, GLPK Solver)

```
from pyomo.environ import *

model = ConcreteModel()
model.x = Var(domain=NonNegativeReals)  # Scooters
model.y = Var(domain=NonNegativeReals)  # Bikes

# Objective: maximize profit
model.obj = Objective(expr=200*model.x + 300*model.y, sense=maximize)

# Constraints
model.design_team = Constraint(expr=2*model.x + 4*model.y <= 5000)
model.engineering_team = Constraint(expr=3*model.x + 5*model.y <= 6000)

solver = SolverFactory('glpk')
result = solver.solve(model)
print('Scooters:', model.x.value)
print('Bikes:', model.y.value)
print('Max profit:', model.obj.expr())
```

## Optimal Solution Context
For the coefficients above: produce 2,000 scooters, 0 bikes, for $400,000 profit.

## Use
Adapt coefficients for similar production/resource allocation LPs.

## Tags
linear programming, resource allocation, Pyomo, operations research, profit maximization, two-product
