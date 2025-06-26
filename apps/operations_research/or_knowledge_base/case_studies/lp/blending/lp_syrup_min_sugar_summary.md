# Syrup Sugar Minimization LP Example

## Problem statement

A patient can drink two syrups for treatment. Per serving:
- Syrup 1 delivers 0.5 units of medicine to the throat, 0.4 units to the lungs, and contains 0.5 units of sugar.
- Syrup 2 delivers 0.2 units of medicine to the throat, 0.5 units to the lungs, and contains 0.3 units of sugar.

The patient requires at most 5 units to the throat and at least 4 units to the lungs. How many servings of each syrup minimizes total sugar intake?

## LP formulation

Variables:
- x1: servings of syrup 1 (>=0)
- x2: servings of syrup 2 (>=0)

Objective:
Minimize sugar: 0.5*x1 + 0.3*x2

Constraints:
- 0.5*x1 + 0.2*x2 <= 5          (throat)
- 0.4*x1 + 0.5*x2 >= 4          (lungs)
- x1 >= 0, x2 >= 0

## Solution (certified optimal)

- Minimum sugar intake: 2.4 units
- Servings: x1=0.0, x2=8.0

Verified to satisfy all constraints.

- Pyomo/GLPK code is available in lp_syrup_min_sugar.py
