# Example: Diet Planning - Minimize Fat Intake with Protein & Iron Constraint

## Problem
A patient must choose numbers of fish and chicken meals to meet nutritional protein and iron requirements. The objective is to minimize fat intake by determining optimal meal counts under the following constraints:

- Each fish meal: 10 units protein, 12 units iron, 7 units fat.
- Each chicken meal: 15 units protein, 8 units iron, 10 units fat.
- At least 130 units protein and 120 units iron needed in total.
- At least twice as many chicken meals as fish meals.
- Variables are integers.

## Linear Integer Programming Model

Variables:
- x = number of fish meals (integer, x >= 0)
- y = number of chicken meals (integer, y >= 0)

Objective:
Minimize total fat: 7x + 10y

Constraints:
- 10x + 15y >= 130     (protein)
- 12x + 8y >= 120      (iron)
- y >= 2x              (chicken >= 2 x fish)
- x, y >= 0, integer

## Optimal Solution
- Fish meals (x): 4
- Chicken meals (y): 9
- Minimum fat intake: 118 units

_Solved using Pyomo and GLPK. This example illustrates how to model and solve a blend/diet integer LP problem._
