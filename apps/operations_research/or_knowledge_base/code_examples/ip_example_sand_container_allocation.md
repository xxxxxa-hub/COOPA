Title: Sand Company Container Delivery Integer Programming Example

Problem Summary:
A sand company delivers sand in small and large containers:
- Small container: 1 person to unload, holds 20 units.
- Large container: 3 people to unload, holds 50 units.
Constraints:
- Number of small containers (x) is 3 times the number of large containers (y).
- At least 5 small and 3 large containers: x >= 5, y >= 3.
- No more than 100 people available: x + 3y <= 100.
Objective:
Maximize total sand delivered: S = 20x + 50y.

Integer Programming Formulation:
Variables:
- x: integer, x >= 5
- y: integer, y >= 3

Constraints:
1) x + 3*y <= 100
2) x = 3*y
3) x >= 5
4) y >= 3

Objective: Maximize S = 20x + 50y

Optimally solved with Pyomo (CBC/GLPK). Maximum S = 1760 with x=48, y=16.

Comment: Illustrates classic resource allocation with integer, proportional, and lower bound constraints—solvable as MILP.
