# continuous_lp_xy_minimize.py - Pyomo Linear Programming Model

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, SolverFactory, NonNegativeReals

model = ConcreteModel()

# Variables: x = fertilizer units, y = seed units
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# Objective: Minimize total effective time
model.obj = Objective(expr=0.5 * model.x + 1.5 * model.y, sense=1)  # sense=1 for minimize

# Constraints
model.c1 = Constraint(expr = model.x + model.y <= 300)
model.c2 = Constraint(expr = model.x >= 50)
model.c3 = Constraint(expr = model.x <= 2*model.y)

# Solve
if __name__ == "__main__":
    solver = SolverFactory('glpk')
    result = solver.solve(model, tee=True)
    print(f"x = {model.x.value}, y = {model.y.value}")
    print(f"Minimum objective value = {model.obj()}")
