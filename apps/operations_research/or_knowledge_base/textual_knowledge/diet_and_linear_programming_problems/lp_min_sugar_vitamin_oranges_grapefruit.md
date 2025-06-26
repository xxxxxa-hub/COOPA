# Linear Programming: Minimize Sugar for Vitamin Intake (Oranges & Grapefruit)

## Problem Statement

A patient must consume oranges and grapefruit to meet minimum vitamin C (>= 80 units) and vitamin A (>= 70 units) requirements. Each fruit has different nutrient and sugar content. The patient must eat at least twice as many oranges as grapefruit.

| Fruit      | Vitamin C | Vitamin A | Sugar |
|------------|-----------|-----------|-------|
| Orange     | 5 units   | 3 units   | 5 g   |
| Grapefruit | 7 units   | 5 units   | 6 g   |

**Variables:**
- x: number of oranges (integer, >= 0)
- y: number of grapefruit (integer, >= 0)

## Mathematical Model

Objective:  
Minimize total sugar:  
    min 5x + 6y

Subject to:
- 5x + 7y >= 80    (Vitamin C constraint)
- 3x + 5y >= 70    (Vitamin A constraint)
- x >= 2y          (Preference constraint)
- x, y >= 0 and integer

## Solution

- Optimal fruit combination: x = 15 (oranges), y = 5 (grapefruit)
- Minimum sugar: **105 grams**

**Constraint Verification:**
- 5*15 + 7*5 = 110 (>= 80)—OK
- 3*15 + 5*5 = 70 (>= 70)—OK
- 15 >= 2*5 = 10—OK

**Model Solved using:** Integer Linear Programming (GLPK or CBC via Pyomo).

## Useful for:

- Diet optimization with micronutrient, sugar, and ratio constraints.
- Integer linear programming (ILP) with bounded variables and resource minimums.


Include all problem details, solution verification, and mark the model as Python/Pyomo compatible. Place the file in the section for basic diet/resource allocation problems.