# ip_parking_optimizer.py

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
