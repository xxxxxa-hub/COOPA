# Diet/Blending Linear Programming Example: Dog Food Mixing Problem

## Problem Description

A generic *diet/blending problem* seeks to minimize the cost of combining resources (foods, raw materials) to satisfy a set of nutritional/compositional requirements.

### Example (Dog Food Mixing)

Lucy wants to mix two brands of dog food:
- **Regular:** $20/bag, 4 Ca, 7 Vit, 10 Protein per bag
- **Premium:** $35/bag, 12 Ca, 10 Vit, 16 Protein

**Requirements:**
- >=15 units calcium
- >=20 units vitamin
- >=20 units protein

**Variables:**
- x = number of regular bags (continuous >= 0)
- y = number of premium bags (continuous >= 0)

## LP Formulation

Minimize:  
    cost = 20x + 35y

Subject to:  
    4x + 12y >= 15 (calcium)  
    7x + 10y >= 20 (vitamin)  
    10x + 16y >= 20 (protein)  
    x, y >= 0

## Pyomo Code Example

```python
from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, SolverFactory

model = ConcreteModel()

# Variables: x (regular bags), y (premium bags)
model.x = Var(domain=NonNegativeReals)
model.y = Var(domain=NonNegativeReals)

# Objective: Minimize cost
model.cost = Objective(expr=20*model.x + 35*model.y)

# Constraints
model.calcium = Constraint(expr=4*model.x + 12*model.y >= 15)
model.vitamin = Constraint(expr=7*model.x + 10*model.y >= 20)
model.protein = Constraint(expr=10*model.x + 16*model.y >= 20)

# Solve (you need a solver installed, e.g., glpk or cplex)
# solver = SolverFactory('glpk')
# result = solver.solve(model)
# print('x:', model.x.value, 'y:', model.y.value)
```

## Notes

- This structure applies to many diet/blending/food formulation LPs.
- Allow variables as continuous unless integer constraints are specified.
- Swap coefficients/data for other applications as needed.

---
Related files:
- code_examples/production_planning/meat_plant_blending_lp_summary.md: Overview of resource allocation and blending LPs; Pyomo usage.
- case_studies/lp/blending/reference_baby_food_blending_lp__description_and_categorization.md: Baby food blend LP, formulation/categorization.
- code_examples/integer_LP/resource_allocation_pill_formulation_example.md: Integer-blending/resource formulation example with Pyomo.
