# Baby Food Blending LP Problem (Fat Maximization)

## Problem Statement

A parent feeds their baby two flavors of baby food, apple and carrot, to meet fat and folate requirements. Details:

- Each serving of apple provides 2 units of fat and 5 units of folate.
- Each serving of carrot provides 4 units of fat and 3 units of folate.
- The child must eat **3 times as many apple servings as carrot servings** (i.e., a = 3c).
- The child must eat at least 2 servings of carrot food (c >= 2).
- The folate intake is limited: **5a + 3c <= 100**.
- Decision variables: a = # servings apple, c = # servings carrot.

**Objective:** Maximize total fat intake: `2*a + 4*c`.

## Mathematical Formulation

## Solution (as of 2024-06)

- Optimal objective value (max fat): **~55.56**
- Optimal servings:
    - a ¡Ö 16.67
    - c ¡Ö 5.56

Solved using Pyomo algebraic modeling and an open-source LP solver. This template is reusable for blending problems with proportional constraints.
