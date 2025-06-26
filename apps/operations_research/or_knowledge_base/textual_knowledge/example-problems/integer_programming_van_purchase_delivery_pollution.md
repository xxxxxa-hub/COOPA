# Van Purchase Integer Programming Problem (Delivery & Pollution Constraints)

## Problem
A shipping company can purchase regular and hybrid vans. A regular van can deliver 500 packages/day and produces 200 units of pollutant. A hybrid van can deliver 300 packages/day and produces 100 units of pollutant. At most 7000 units of pollutants per day are allowed. At least 20000 packages per day must be delivered.
Objective: Minimize the total number of vans required.

## Mathematical Formulation
Let x = number of regular vans (integer, >= 0)
Let y = number of hybrid vans (integer, >= 0)

minimize:    x + y  
subject to:  
  500x + 300y >= 20000         (delivery constraint)  
  200x + 100y <= 7000          (pollution constraint)  
  x, y >= 0 and integer

## Solution (via Integer Programming/GLPK/Pyomo)
Optimal solution: 10 regular vans and 50 hybrid vans  
Objective value: 60  
Constraints satisfied at equality.

## Reference code
A Pyomo implementation was saved as: van_optimization.py
