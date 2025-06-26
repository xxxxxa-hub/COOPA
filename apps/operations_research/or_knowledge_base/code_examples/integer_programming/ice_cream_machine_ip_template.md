# Ice Cream Machine Allocation Integer Programming Template

## Description
This problem concerns selecting how many machines of each type to buy to satisfy output and resource constraints, while minimizing the number of machines.

## Model Structure
- **Variables:**
    - `x`: integer, number of counter-top sized machines (>= 0)
    - `y`: integer, number of fridge-sized machines (>= 0)
- **Objective:** Minimize x + y (total machines)
- **Constraints:**
    - Production: `a1 * x + a2 * y >= D` (required number of items)
    - Resource:   `b1 * x + b2 * y <= R` (resource/capacity, e.g., heat)
    - x, y in {0, 1, 2, ...}

## Example Instantiation (from solved problem)
- a1 = 80, a2 = 150, D = 1000
- b1 = 50, b2 = 70, R = 500
- Solved using Pyomo/GLPK: Solution x = 0, y = 7, minimum = 7

## Pyomo Model Template (replace coefficients as needed)
```python
from pyomo.environ import *

model = ConcreteModel()

# Variables
model.x = Var(domain=NonNegativeIntegers)
model.y = Var(domain=NonNegativeIntegers)

# Objective: minimize total machines
model.obj = Objective(expr = model.x + model.y, sense=minimize)

# Constraints (replace with your coefficients)
a1, a2, D = 80, 150, 1000
b1, b2, R = 50, 70, 500
model.production = Constraint(expr = a1*model.x + a2*model.y >= D)
model.resource   = Constraint(expr = b1*model.x + b2*model.y <= R)

# To solve:
# SolverFactory('glpk').solve(model)
print('x:', value(model.x))
print('y:', value(model.y))
print('Minimum number of machines:', value(model.obj))
```

## Solution approach
Use a MILP solver (e.g., GLPK).

## Result
For coefficients above, the minimum number of machines = 7.

## Keywords
integer programming, resource allocation, production planning, Pyomo, MILP
