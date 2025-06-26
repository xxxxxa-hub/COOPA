# Workforce Scheduling with Minimum Multiple Constraint and Resource Budget

## Problem Template
- Decision variables:
    - x: Number of 'expensive' tests/resources (e.g., blood tests), integer >= min_x.
    - y: Number of 'cheaper' or more common tasks (e.g., temp checks), integer >= 0.
- Constraints:
    - x >= min_x (minimum of expensive procedure)
    - y >= k * x  ('at least k times as many of y as x')
    - resource_x * x + resource_y * y <= total_resource
    - x, y >= 0 and integer
- Objective: Maximize x + y (total number of patients/tests).

## Example (from Disease Testing Station, 2024-05):
Blood test: 10 min, Temp check: 2 min.
    - x >= 45
    - y >= 5x
    - 10x + 2y <= 22000
    - x, y >= 0, integer
Objective: Maximize x + y

## Pyomo Snippet:
from pyomo.environ import *

def solve_blood_temp_model():
    model = ConcreteModel()
    model.x_min = Param(initialize=45)
    model.k = Param(initialize=5)
    model.r_x = Param(initialize=10)
    model.r_y = Param(initialize=2)
    model.total = Param(initialize=22000)
    model.x = Var(domain=NonNegativeIntegers, bounds=(model.x_min, None))
    model.y = Var(domain=NonNegativeIntegers)
    model.multiple = Constraint(expr=model.y >= model.k * model.x)
    model.limit = Constraint(expr=model.r_x * model.x + model.r_y * model.y <= model.total)
    model.obj = Objective(expr=model.x + model.y, sense=maximize)
    SolverFactory('glpk').solve(model)
    return int(value(model.x)), int(value(model.y)), int(value(model.x + model.y))

## Solution Approach
- Often optimal to set x to its lowest feasible value, making y = kx.
- Always check binding of constraints and total used resources.
- Expand if minimization, or for other structures, adapt the template.

## Use Cases
- Workforce/treatment scheduling, test allocation, minimizing costly procedures, maximizing throughput under a minimum coverage ratio.

## See also: Minimum ratio constraints, additive integer programming, resource allocation under proportional requirements.
