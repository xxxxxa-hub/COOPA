# van_pollution_minimization.py

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, minimize, SolverFactory

# Define the model
model = ConcreteModel()

# Decision variables
model.x = Var(domain=NonNegativeIntegers)  # Number of old vans (integer)
model.y = Var(domain=NonNegativeIntegers)  # Number of new vans (integer)

# Objective: Minimize total pollution
model.obj = Objective(expr=50 * model.x + 30 * model.y, sense=minimize)

# Capacity constraint
model.capacity = Constraint(expr=100 * model.x + 80 * model.y >= 5000)

# New van limit
model.new_van_limit = Constraint(expr=model.y <= 30)

# The model is now ready to be solved.
# Example solve code (if solver is available):
# solver = SolverFactory('cbc')
# results = solver.solve(model)
# print('Old vans:', model.x.value, 'New vans:', model.y.value)
