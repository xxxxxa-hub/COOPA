# Workforce Sizing MILP Example – Snow Remover Staffing with Budget and Coverage Constraints (Pyomo)

## Problem Summary:
This example presents a classic mixed-integer programming (MILP) problem for determining the optimal composition of a workforce for snow removal operations. The task is to decide the number of two types of workers to hire (seasonal and permanent), each type associated with different shift durations and wages, such that the total number of workers is minimized while achieving required coverage and not exceeding a given budget.

- **Variables:**
    - x = number of seasonal workers (integer >= 0)
    - y = number of permanent workers (integer >= 0)
- **Objective:**
    - Minimize total number of workers hired: `min x + y`
- **Constraints:**
    1. Labor-hours coverage: `6x + 10y >= 300`
    2. Budget cap: `120x + 250y <= 6500`
    3. Integer nonnegativity: `x, y >= 0, integer`

## Mathematical Formulation:
```
Minimize:
    x + y
Subject to:
    6x + 10y >= 300             # Labor-hours constraint
    120x + 250y <= 6500         # Budget constraint
    x >= 0, y >= 0, integer
```

## Pyomo Model Skeleton (Reusable Reference):
```python
import pyomo.environ as pyo
model = pyo.ConcreteModel()

# Decision variables
model.x = pyo.Var(within=pyo.NonNegativeIntegers)
model.y = pyo.Var(within=pyo.NonNegativeIntegers)

# Objective: Minimize number of workers
model.obj = pyo.Objective(expr = model.x + model.y, sense = pyo.minimize)

# Labor-hours constraint
model.labor_coverage = pyo.Constraint(expr = 6*model.x + 10*model.y >= 300)

# Budget constraint
model.budget_cap = pyo.Constraint(expr = 120*model.x + 250*model.y <= 6500)
```

## Applicability and Notes:
- This template is applicable to workforce minimization or sizing tasks involving fixed and variable labor profiles, shift lengths, and cost limits.
- Adaptable to any two-category crew staffing problem with linear constraints and objectives.
- Solvable with open source MILP solvers such as GLPK or CBC directly from within Pyomo.

## Use Case Benefits:
- Clarifies how to set up labor coverage and cost/affordability constraints in the same model.
- Focuses on integer-only staff selection rather than fractional or continuous assignments.
- Shows the trade-offs between hiring lower-wage short-shift staff in greater numbers vs. fewer higher-wage, longer-shift permanent staff while controlling for cost.

