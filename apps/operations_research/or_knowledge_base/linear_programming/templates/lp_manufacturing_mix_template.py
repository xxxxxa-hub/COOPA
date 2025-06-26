# Pyomo LP Template: Manufacturing Mix - Minimize Total Time

from pyomo.environ import *

model = ConcreteModel()

# SETS
model.P = Set(initialize=[...])  # List of product/job names (replace ... with actual names or provide via data)

# PARAMETERS
model.t = Param(model.P, initialize={...})   # Per-unit processing time (replace ... with dictionary)
model.d = Param(model.P, initialize={...})   # Minimum demand (replace ... with dictionary)
model.cap = Param(initialize=...)            # Total available processing time (replace ... with value)

# DECISION VARIABLES
model.x = Var(model.P, domain=NonNegativeReals)  # Use NonNegativeIntegers for integer production if required

# OBJECTIVE: Minimize total (work) time
model.obj = Objective(expr=sum(model.t[p] * model.x[p] for p in model.P), sense=minimize)

# CONSTRAINTS
# Minimum demand for each product
model.demand = ConstraintList()
for p in model.P:
    model.demand.add(model.x[p] >= model.d[p])

# Total processing time cannot exceed available capacity
model.capacity = Constraint(expr=sum(model.t[p] * model.x[p] for p in model.P) <= model.cap)

# (Optional) To solve:
# solver = SolverFactory('glpk')
# solver.solve(model)
# model.x.display()
