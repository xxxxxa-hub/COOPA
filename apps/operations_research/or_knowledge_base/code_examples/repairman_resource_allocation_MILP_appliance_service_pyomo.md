# Repairman Resource Allocation Integer Programming Example

## Problem Statement
A repairman fixes washing machines and freezers. 
- Each washing machine takes 30 minutes of inspection and 90 minutes of fixing. 
- Each freezer takes 20 minutes of inspection and 125 minutes of fixing.
- Available: 5,000 minutes of inspection, 20,000 minutes total.
- Each washing machine earns $250, each freezer $375.
- How many of each should he fix to maximize earnings? (Variables integer and >= 0.)

## Mathematical Model
Let:
- x = number of washing machines repaired (integer, >=0)
- y = number of freezers repaired (integer, >=0)

Objective:
    Maximize 250*x + 375*y

Subject to:
    30*x + 20*y <= 5000        # Inspection constraint
    90*x + 125*y <= 20000      # (Fixing+inspection) constraint

## Solution (Pyomo, MILP approach):
- Model as above, x and y are integer variables.
- Set upper bounds for variables based on capacity (x <= 166, y <= 160).
- Use a MILP solver (GLPK, CBC, HiGHS, etc).
- The optimal solution is x = 0, y = 160, maximum profit = 60,000.

## Pyomo Model Example
```python
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, SolverFactory

model = ConcreteModel()
model.x = Var(domain=NonNegativeIntegers)  # washing machines
model.y = Var(domain=NonNegativeIntegers)  # freezers

model.profit = Objective(expr=250*model.x + 375*model.y, sense=-1)  # maximize

model.inspection = Constraint(expr=30*model.x + 20*model.y <= 5000)
model.total_time = Constraint(expr=90*model.x + 125*model.y <= 20000)

# Optional explicit upper bounds, not strictly necessary
# model.x.setub(166)
# model.y.setub(160)

solver = SolverFactory('glpk')
result = solver.solve(model)
print('Washing machines:', model.x.value)
print('Freezers:', model.y.value)
print('Profit:', model.profit.expr())
```

## Optimality Check
Plugging in x = 0, y = 160:
- 30*0 + 20*160 = 3200 <= 5000
- 90*0 + 125*160 = 20000 <= 20000

With x>0, second constraint is exceeded. Thus, all resources are optimally used for freezers.

## Notes
- When adapting for other service/trades resource/profit maximization cases, convert job times & payrates to constraint coefficients and objective function weights.
- This canonical example is widely applicable to appliance repair and general resource-driven service scheduling.
