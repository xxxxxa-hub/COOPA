# Snack Mix LP Optimization (Example)

## Problem Statement
Super Shop sells cat paw and gold shark snacks in bulk, planning to create two snack mixes:
- Mix 1: 20% cat paw, 80% gold shark, profit $12/kg.
- Mix 2: 35% cat paw, 65% gold shark, profit $15/kg.
Available: 20 kg cat paw, 50 kg gold shark. 
Decision: How many kg of each mix to produce to maximize profit?

## LP Formulation
Let x1 = kg of mix 1, x2 = kg of mix 2.

Objective: Maximize 12 x1 + 15 x2

Subject to:
- 0.2 x1 + 0.35 x2 <= 20      (cat paw constraint)
- 0.8 x1 + 0.65 x2 <= 50      (gold shark constraint)
- x1 >= 0, x2 >= 0

## Solution Observations
- Pyomo/GLPK solver returned the all-zero solution (x1=x2=0, max profit $0).
- This may result from numerical issues or be a valid solution depending on constraints.
- In future, check coefficients and attempt feasibility analysis for similar problems.

## Code location
See 'snack_mix_optimization.py' for implementation example.

Purpose: Provide a template and modeling reference for blending/resource allocation LP problems with percentage constraints. Also includes a note on solver corner-case solutions.
