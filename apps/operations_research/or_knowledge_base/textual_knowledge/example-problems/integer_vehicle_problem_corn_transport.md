# Integer Programming - Minimize Number of Vehicles (Corn Transport Problem)

## Problem Statement
A farmer must transport at least 500 kg of corn using tractors (40 kg capacity each) and cars (20 kg capacity each). The number of cars must be at least twice the number of tractors. Objective: Minimize total vehicles used (tractors + cars). Both variables are integers >= 0.

### Formulation
Variables:
- x: number of tractors (integer, >= 0)
- y: number of cars (integer, >= 0)

Objective:
- Minimize x + y

Constraints:
- 40*x + 20*y >= 500
- y >= 2*x

### Optimal Solution
- Min vehicles (x + y): 19
- x = 6 tractors, y = 13 cars

The Pyomo-based solution script is named `integer_vehicle_problem_corn_transport.py`. Solver used: GLPK.

This example illustrates capacity-mix IP under ratio and integrality constraints and is useful for transportation/vehicle mix problems in integer programming.