# Meat Processing Plant Blending LP Example (Pyomo)

"""
This is a full Pyomo code example for a meat processing plant blending/resource allocation linear program (LP).
The model formulates and solves a typical blending problem: minimize material cost by blending several meat cuts to produce a final product with specified nutritional and supply constraints.
"""

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, SolverFactory, value, Set, Param, summation

# Example Data: Fill in real or didactic data as appropriate
M = ['cut1', 'cut2', 'cut3']  # Meat cuts
cost = {'cut1': 2.0, 'cut2': 3.0, 'cut3': 2.5}      # $/kg
fat = {'cut1': 0.20, 'cut2': 0.15, 'cut3': 0.25}    # fraction of mass
protein = {'cut1': 0.18, 'cut2': 0.16, 'cut3': 0.22}
supply = {'cut1': 100, 'cut2': 80, 'cut3': 120}      # kg available

# Requirements for blend
total_required = 200   # kg of final blend
fat_lower = 0.17 * total_required
fat_upper = 0.22 * total_required
protein_lower = 0.17 * total_required
protein_upper = 0.21 * total_required

model = ConcreteModel()
model.M = Set(initialize=M)
model.x = Var(model.M, within=NonNegativeReals)

# Objective: Minimize cost
model.cost = Objective(expr=sum(cost[i] * model.x[i] for i in model.M))

# Constraints
model.total_blend = Constraint(expr=sum(model.x[i] for i in model.M) == total_required)
model.fat_content = Constraint(expr=sum(fat[i] * model.x[i] for i in model.M) >= fat_lower)
model.fat_content2 = Constraint(expr=sum(fat[i] * model.x[i] for i in model.M) <= fat_upper)
model.protein_content = Constraint(expr=sum(protein[i] * model.x[i] for i in model.M) >= protein_lower)
model.protein_content2 = Constraint(expr=sum(protein[i] * model.x[i] for i in model.M) <= protein_upper)
model.supply = ConstraintList()
for i in M:
    model.supply.add(model.x[i] <= supply[i])

# Solve
solver = SolverFactory('glpk')  # Or your solver of choice
results = solver.solve(model, tee=True)

# Display results
print('Status:', results.solver.status)
print('Termination Condition:', results.solver.termination_condition)
print('Amounts to use (kg):')
for i in model.M:
    print(f'{i}: {value(model.x[i]):.2f} kg')
print('Total Cost: ${:.2f}'.format(value(model.cost)))
