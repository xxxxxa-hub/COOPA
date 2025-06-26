# Integer Programming Example: Minimizing Wagons for Ore Transport

## Problem Statement
A mining operation sends ore to the surface using two types of wagons:
- Small wagon: Holds 20 units of ore.
- Large wagon: Holds 50 units of ore.

Constraints:
- The number of small wagons (x) must be at least twice the number of large wagons (y): x >= 2y.
- At least 10 large wagons must be used: y >= 10.
- The total ore required at surface: 2000 units: 20x + 50y >= 2000.
- x, y must be non-negative integers.

Objective:
- Minimize the total number of wagons required: Minimize x + y.

## Mathematical Formulation

Variables:
- x: Number of small wagons (integer).
- y: Number of large wagons (integer).

Minimize: 
    x + y

Subject to:
    20*x + 50*y >= 2000
    x >= 2*y
    y >= 10
    x >= 0, y >= 0, x, y integer

## Optimal Solution (as computed by MIP/GLPK/Pyomo)
- Minimum wagons required: 67
- Small wagons: 45
- Large wagons: 22

## Notes
This template is useful for variant transportation and allocation models requiring integer programming, especially when minimizing counts under ratio and lower bound constraints.
