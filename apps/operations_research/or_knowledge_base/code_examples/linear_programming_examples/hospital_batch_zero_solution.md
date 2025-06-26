**Hospital Batch Production Linear Program Example**

A hospital prepares batches of medication patches and anti-biotic creams. Each medication patch requires 3 minutes to prepare and 5 units of materials. Each anti-biotic cream requires 5 minutes to prepare and 6 units of materials. Since anti-biotic creams are used more often, there must be at least twice as many anti-biotic creams as medication patches. Due to storage reasons, the hospital can make at most 100 batches in total. There are 400 available staff minutes and 530 units of materials. 
Each batch of medication patches can treat 3 people and each batch of anti-biotic cream can treat 2 people. 

**Formulation**
Let x = batches of medication patches  
Let y = batches of anti-biotic creams  

Maximize:  3x + 2y

Subject to:  
3x + 5y <= 400   (time constraint)
5x + 6y <= 530   (materials constraint)
y >= 2x          (cream vs patch ratio)
x + y <= 100     (storage constraint)
x >= 0, y >= 0

**Remark:** The optimal solution is x = 0, y = 0 (objective = 0) due to the restrictiveness of the y >= 2x constraint with the other resource constraints.


--- PYOMO CODE ---

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, maximize, SolverFactory

model = ConcreteModel()
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

model.time_constraint = Constraint(expr = 3*model.x + 5*model.y <= 400)
model.materials_constraint = Constraint(expr = 5*model.x + 6*model.y <= 530)
model.ratio_constraint = Constraint(expr = model.y >= 2*model.x)
model.storage_constraint = Constraint(expr = model.x + model.y <= 100)

model.objective = Objective(expr = 3*model.x + 2*model.y, sense=maximize)

solver = SolverFactory('glpk')
result = solver.solve(model)
print('x =', model.x.value, 'y =', model.y.value, 'objective =', model.objective.expr())


--- NOTES ---

This example provides an instance of an LP for health resource allocation, featuring a ratio constraint (y >= 2x) which, when combined with material and workload constraints, leads to a zero decision solution. 
Useful for: ratio constraints, infeasibility or degenerate optimal solutions, healthcare production planning.
