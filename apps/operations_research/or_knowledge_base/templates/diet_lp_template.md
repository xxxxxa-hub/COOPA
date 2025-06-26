# Diet Problem Linear Programming Template (with Integer Variables)

## Problem Type:
Minimize (or maximize) a target nutritional or financial objective (e.g., cost, cholesterol intake, calories) by choosing quantities of food items, under constraints on nutrients, caloric content, and possible additional ratios or limits.

## Mathematical Form:
Let x_i = integer variable for quantity of each food item i.

### Objective:
Minimize:    sum_j c_j * x_j      # c_j = cholesterol (or cost, or other quantity) per unit of food j

### Constraints:
- sum_j fat_j * x_j   >= min_fat_required
- sum_j cal_j * x_j   >= min_cal_req
- (other nutrients and bounds as needed)
- Additional relationships/ratios: e.g. x_pizza >= 2 * x_burger

All x_j >= 0 and integer.

## Typical Usage:
- Choose appropriate coefficients and constraints based on the specific foods/nutrient needs.
- Can be extended to add maximum intake constraints or cost limits, or to minimize/maximize other objectives.

## Example modeling instruction for algebraic_optimizer_agent:

"""
Variables:
    x1: (name/meaning), integer >= 0
    x2: (name/meaning), integer >= 0
    ...

Objective:
    Minimize: objective_expression

Subject to:
    constraint_1
    constraint_2
    ...
"""

---
