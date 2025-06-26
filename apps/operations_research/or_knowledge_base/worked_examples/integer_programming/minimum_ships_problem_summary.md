# Minimum Number of Ships¡ªAlgebraic Model (Pyomo, Integer Programming)
## Problem Statement
An international shipping company uses large and small ships to transport containers.  
- Large ship capacity: 500 containers  
- Small ship capacity: 200 containers  
- Large ship count cannot exceed small ship count (L <= S)  
- At least 3000 containers must be shipped  
- Objective: Minimize the total number of ships used

## Formulation
Let  
L = number of large ships (integer >= 0)  
S = number of small ships (integer >= 0)

Minimize L + S  
Subject to:  
500*L + 200*S >= 3000  
L <= S  
L, S >= 0 and integer

## Solution (Optimal)
- Minimum total number of ships: 9
- 4 large ships, 5 small ships (total containers: 3000, constraint satisfied)
- Method: Pyomo MILP with open-source solver (GLPK or CBC). See 'ship_optimization_model.py' for implementation.

## Useful for
- Shipping optimization problems with integer variables and capacity constraints
- Demonstrates how 'min total units' models often lead to mixed integer programs
