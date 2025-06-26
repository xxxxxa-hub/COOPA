# Solved Integer Programming Example: Hand Sanitizer Production Planning (Pyomo)

## Problem Statement
A company produces two types of hand sanitizers: liquid and foam. Both require different amounts of water and alcohol per unit, and the total available resources are limited. The goals are:
- Decide how many integer units of each sanitizer (liquid: x, foam: y) to produce.

### Constraints:
- All variables are integer valued.
- Number of foam units must strictly exceed the number of liquid units (y > x).
- At most 30 liquid sanitizers may be produced (x <= 30).
- Total water and alcohol used must not exceed available supply (resource constraints; see code for exact coefficients).

### Objective:
- Maximize the total number of hands that can be cleaned (linear function of x and y; coefficients given in code).

The problem was solved to proven integer optimality in Pyomo using GLPK. See 'pyomo_model_max_hands_cleaned.py' for the code implementing this model, including all data, constraints, and solution extraction logic.

## Full Pyomo Code
- See the companion code file:
  - code_examples/integer_LP/pyomo_model_max_hands_cleaned.py

---

This example demonstrates how to model and solve an integer programming production planning problem with Pyomo, including variable inequalities, resource bounds, integer restrictions, and linear maximization objectives.
