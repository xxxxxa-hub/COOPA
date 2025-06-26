# Example: Medical Linear Programming – Radiation Therapy (Pancreas, Skin, Tumor) [ALREADY MODELED IN PYOMO]

## Problem Statement:
A patient undergoes radiation therapy using two beams (Beam 1, Beam 2). Each beam delivers a specified dose per minute to the pancreas (benign), skin (benign), and tumor (malignant).
- Beam 1: 0.3 units/min to pancreas, 0.2 units/min to skin, 0.6 units/min to tumor.
- Beam 2: 0.2 units/min to pancreas, 0.1 units/min to skin, 0.4 units/min to tumor.
- Skin may receive at most 4 units in total.
- Tumor must receive at least 3 units in total.

Find minutes for each beam to minimize total pancreas dose.

## Model:

Let x1 = minutes to use Beam 1, x2 = minutes for Beam 2.

Minimize: 0.3*x1 + 0.2*x2  # (total pancreas dose)

Subject to:
0.2*x1 + 0.1*x2 <= 4       # (skin dose constraint)
0.6*x1 + 0.4*x2 >= 3       # (tumor dose constraint)
x1 >= 0, x2 >= 0           # (non-negativity)

Optimal Solution:
- Objective value: 1.5 (units of pancreas dose)
- x1 = 5.0, x2 = 0.0

Pyomo code exemplar: See file 'algebraic_optimizer_lp_model.py' for full code that models and solves this LP using Pyomo+GLPK.

Keywords: radiation therapy, linear programming, medical optimization, Pyomo, constraint, dose minimization
