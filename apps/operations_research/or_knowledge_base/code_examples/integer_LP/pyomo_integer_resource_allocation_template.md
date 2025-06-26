# Pyomo Integer Resource Allocation Template: Production/Resource Planning

This template provides a general framework for resource allocation or production planning with integer decision variables in Pyomo.

## Features
- Multiple products (arbitrary set)
- Resource constraints (customizable for water, labor, materials, etc)
- Integer/binary restrictions
- Capacity or ratio constraints
- Linear objective (maximization or minimization)
- Custom variable inequalities between products (e.g., y > x)

## Usage
Copy the template and modify products, resources, coefficients, and constraints as needed. Suitable for scenarios with multiple products competing for limited resources, integer requirements, and linear objectives.

## Template Pyomo Code

```python
from pyomo.environ import *

model = ConcreteModel()

# SETS
model.PRODUCTS = Set(initialize=['A', 'B'])
model.RESOURCES = Set(initialize=['Resource1', 'Resource2'])

# PARAMETERS
model.requirement = Param(model.PRODUCTS, model.RESOURCES, initialize={('A','Resource1'): 1, ('A','Resource2'): 2,
                                                                       ('B','Resource1'): 2, ('B','Resource2'): 1})
model.capacity = Param(model.RESOURCES, initialize={'Resource1': 20, 'Resource2': 30})
model.contribution = Param(model.PRODUCTS, initialize={'A': 10, 'B': 12}) # e.g., profit/benefit per unit

# VARIABLES
model.x = Var(model.PRODUCTS, within=NonNegativeIntegers)

# RESOURCE CONSTRAINTS
def resource_constraint_rule(model, r):
    return sum(model.requirement[p, r] * model.x[p] for p in model.PRODUCTS) <= model.capacity[r]
model.resource_constraint = Constraint(model.RESOURCES, rule=resource_constraint_rule)

# CUSTOM/PAIRWISE CONSTRAINTS EXAMPLES
def pairwise_product_rule(model):
    return model.x['B'] > model.x['A']
model.pairwise_con = Constraint(rule=pairwise_product_rule)
# (Add further relationships and capacity constraints as needed)

# OBJECTIVE
model.objective = Objective(expr=sum(model.contribution[p]*model.x[p] for p in model.PRODUCTS), sense=maximize)

# SOLVING
# SolverFactory('glpk').solve(model)
```

---
You should adapt sets, parameter values, and constraint structures for your scenario. For more details, see the solved example: worked_examples/integer_programming/hand_sanitizer_production_maxhands.md and code_examples/integer_LP/pyomo_model_max_hands_cleaned.py.