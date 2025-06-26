# Parking Spot/Resource Minimization with Mixed Vehicle Types (Integer Programming Example)

## Parking Spot Minimization for Production Units: Integer Programming Example

### Problem Statement
A production company must transport their equipment and staff using two types of mobile production units:
- Large unit: holds 6 people, uses 2 parking spots.
- Small unit: holds 2 people, uses 1 parking spot.

**Constraints:**
- At least 5 small units (stars' preference)
- Large units must make up at least 75% of the total number of vehicles (i.e., x >= 3*y)
- Must transport at least 80 people in total
- Minimize total parking spots required

**Model:**
Let x = number of large units, y = number of small units (both non-negative integers)
- Objective: Minimize 2x + y
- Constraints:
    - 6x + 2y >= 80
    - y >= 5
    - x >= 3y
    - x, y >= 0 and integer

### Solution (using Pyomo and GLPK)
- Optimal value: 35 parking spots (x=15, y=5)

### Pyomo implementation (ip_parking_optimizer.py):

```python
from pyomo.environ import *

model = ConcreteModel()

# Decision variables
model.x = Var(domain=NonNegativeIntegers)  # Number of large units
model.y = Var(domain=NonNegativeIntegers)  # Number of small units

# Objective: Minimize total parking spots
model.obj = Objective(expr=2*model.x + model.y, sense=minimize)

# Constraints
model.transport = Constraint(expr=6*model.x + 2*model.y >= 80)
model.min_small = Constraint(expr=model.y >= 5)
model.ratio = Constraint(expr=model.x >= 3*model.y)

# Solve
solver = SolverFactory('glpk')
result = solver.solve(model)

# Print results
print(f'Optimal parking spots: {model.obj():.0f}')
print(f'Large units (x): {model.x():.0f}')
print(f'Small units (y): {model.y():.0f}')
```

---
This example demonstrates a real-world, integer programming resource allocation task involving capacity, resource minimization, and ratio constraints with a clear practical application and reusable code.