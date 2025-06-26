# virus_testing_model.py

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, SolverFactory, Param

# Data
SPIT_TIME = 10
SWAB_TIME = 15
TOTAL_TIME = 8000
SWAB_MIN = 20

model = ConcreteModel()
model.spit_time = Param(initialize=SPIT_TIME)
model.swab_time = Param(initialize=SWAB_TIME)
model.total_time = Param(initialize=TOTAL_TIME)
model.swab_min = Param(initialize=SWAB_MIN)

# Variables
model.x = Var(domain=NonNegativeIntegers)  # Spit tests
model.y = Var(domain=NonNegativeIntegers, bounds=(SWAB_MIN, None))  # Swab tests, at least 20

# Objective
model.obj = Objective(expr = model.x + model.y, sense=1)

# Constraints
def time_constraint_rule(m):
    return m.spit_time * m.x + m.swab_time * m.y <= m.total_time
model.time_constraint = Constraint(rule=time_constraint_rule)

def ratio_constraint_rule(m):
    return m.x >= 2*m.y
model.ratio_constraint = Constraint(rule=ratio_constraint_rule)

# If running standalone:
if __name__ == "__main__":
    solver = SolverFactory('cbc')
    result = solver.solve(model, tee=True)
    print(f"status: {result.solver.status}")
    print(f"termination: {result.solver.termination_condition}")
    print(f"spit tests: {model.x.value}")
    print(f"swab tests: {model.y.value}")
    print(f"total tests: {model.x.value + model.y.value}")
