
# Hospital Pill Dosage and Discharge LP Example

## Problem Statement
A patient can take two types of pills:
- **Pill 1:** 0.2 units pain med, 0.3 units anxiety med, 0.3 units discharge per pill.
- **Pill 2:** 0.6 units pain med, 0.2 units anxiety med, 0.1 units discharge per pill.

**Constraints:**
- Pain medication: at most 6 units (¡Ü 6)
- Anxiety medication: at least 3 units (¡Ý 3)
- Amount of pills: nonnegative, continuous

**Objective:** Minimize total discharge.

## Mathematical Model

Let x = # of pill 1, y = # of pill 2

Minimize: `0.3x + 0.1y`  
Subject to:  
`0.2x + 0.6y ¡Ü 6` (pain constraint)  
`0.3x + 0.2y ¡Ý 3` (anxiety constraint)  
`x ¡Ý 0, y ¡Ý 0` (nonnegativity)

## Optimal Solution (Analytical)

Solving:

Yields:
- x* = 4.2857
- y* = 8.5714
- Min discharge = 2.1429

## Pyomo Template (See algebraic_optimizer_lp_min_model.py)

    from pyomo.environ import *
    model = ConcreteModel()
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)
    model.obj = Objective(expr=0.3*model.x + 0.1*model.y, sense=minimize)
    model.pain = Constraint(expr=0.2*model.x + 0.6*model.y <= 6)
    model.anxiety = Constraint(expr=0.3*model.x + 0.2*model.y >= 3)
    SolverFactory('glpk').solve(model)

This template can be reused for any pill-type or discharge minimization hospital problem with at most two medications and linear constraints.

## Use Cases

- Medication dosage optimization with side-effect minimization under coupling constraints.
- Bounded, continuous LPs with two variables for healthcare, nutrition, or industrial mixing.

