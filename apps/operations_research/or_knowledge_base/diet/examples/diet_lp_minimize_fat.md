# Linear Diet Problem: Minimize Fat Intake from Almonds and Cashews

## Problem Statement
A woman must decide how many servings of almonds (A) and cashews (C) to eat in order to fulfill weekly nutritional constraints while minimizing fat intake.
- Almonds: 200 cal/serving, 20g protein/serving, 15g fat/serving
- Cashews: 300 cal/serving, 25g protein/serving, 12g fat/serving
- Calorie requirement: at least 10,000
- Protein requirement: at least 800g
- Almond servings at least twice cashew servings (A >= 2*C)
- Objective: Minimize total fat = 15*A + 12*C

## Mathematical Model

Minimize: 15A + 12C

Subject to:
- 200A + 300C >= 10000
- 20A + 25C >= 800
- A >= 2C
- A >= 0, C >= 0 (continuous relaxation)

## Pyomo Implementation

A complete Pyomo model and solution routine is saved as 'lp_nuts_fat_min.py' (see working directory).
Optimal solution (by LP relaxation):
- Almonds: ~28.57 servings
- Cashews: ~14.29 servings
- Minimum fat: 600g

Model uses GLPK and was solved successfully.

## Useful for
- Classic diet/minimization of nutritional quantity problems
- Linear programming with dietary/ratio constraints
- Constructing and solving LPs in Pyomo

## Reference File
The code implementation is saved as 'lp_nuts_fat_min.py' (in working directory), to be located alongside this documentation for user access.
