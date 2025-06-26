# Cost Minimization for Dual Annotation Providers under Split Constraint - Pyomo LP Example

# Problem Statement
# A researcher must allocate the annotation of at least N images between two third-party companies:
# - Specialized company: annotates S1 images/hour at cost C1 $/hour.
# - Common company: annotates S2 images/hour at cost C2 $/hour.
# - At least a fraction alpha of images must be handled by the specialized company.

# Formulate as:
# Variables:
# - x: images assigned to the specialized company
# - y: images assigned to the common company
#
# Objective:
#     Minimize (C1/S1) * x + (C2/S2) * y
#
# Subject to:
#     x + y >= N
#     x >= alpha * (x + y)
#     x >= 0
#     y >= 0

# Pyomo Implementation Template

import pyomo.environ as pyo

# PARAMETERS (set these according to your use case)
N = 1000      # Total images (demand)
S1 = 50       # Specialized rate (images/hour)
C1 = 100      # Specialized cost ($/hour)
S2 = 60       # Common rate (images/hour)
C2 = 60       # Common cost ($/hour)
alpha = 0.6   # Minimum fraction for specialized provider

model = pyo.ConcreteModel()
model.x = pyo.Var(domain=pyo.NonNegativeReals)
model.y = pyo.Var(domain=pyo.NonNegativeReals)

# Objective: Minimize total cost
model.cost = pyo.Objective(expr=(C1/S1)*model.x + (C2/S2)*model.y, sense=pyo.minimize)

# Constraints
model.total = pyo.Constraint(expr=model.x + model.y >= N)
model.split = pyo.Constraint(expr=model.x >= alpha * (model.x + model.y))

# SOLVER
# solver = pyo.SolverFactory('glpk')
# result = solver.solve(model, tee=True)

# To access solution:
# print('Specialized images:', pyo.value(model.x))
# print('Common images:', pyo.value(model.y))
# print('Total cost:', pyo.value(model.cost))

# Notes:
# - This template can be easily adapted for any two-provider cost split problem with minimum allocation fraction and total demand.
# - Set the parameters at the top for your specific situation.
# - Per-unit costs are derived as (cost/hour) / (images/hour) = cost/image.
# - Change N, C1, S1, C2, S2, or alpha as needed.
# - Use any Pyomo-compatible LP solver.
