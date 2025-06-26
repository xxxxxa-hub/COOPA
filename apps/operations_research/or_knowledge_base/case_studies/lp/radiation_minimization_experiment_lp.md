# Radiation Minimization for In-Vivo/Ex-Vivo Experiments - Standard LP Formulation

## Problem Description
A researcher must perform two types of experiments: in-vivo and ex-vivo. Each experiment type requires specific preparation and execution times and contributes to the total radiation received by the researcher.

- In-vivo experiment: 30 min prep, 60 min exec, 2 radiation units per experiment
- Ex-vivo experiment: 45 min prep, 30 min exec, 3 radiation units per experiment
- Total available: 400 min prep, 500 min exec

## Mathematical Formulation

Let:
- x1 = number of in-vivo experiments (continuous or integer, >= 0)
- x2 = number of ex-vivo experiments (continuous or integer, >= 0)

Objective:
    Minimize total radiation:
        minimize   2*x1 + 3*x2

Subject to:
    30*x1 + 45*x2 <= 400      # preparation time constraint
    60*x1 + 30*x2 <= 500      # execution time constraint
    x1 >= 0, x2 >= 0

## Pyomo Implementation Hint

Define variables as NonNegativeReals (or NonNegativeIntegers if needed). Use constraint expressions as shown above. For default case (no minimum experiments), solution may be (x1, x2) = (0, 0).

## Remark

If a minimum number of total experiments or other requirements are desired, add more constraints (e.g., x1 + x2 >= N).

Related file: See 'radiation_minimization_model.py' for a concrete Pyomo implementation.
