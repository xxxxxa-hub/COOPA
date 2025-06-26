# Integer Programming Example: Snack Suitcase Export Problem

## Problem Statement
A snack exporter must send snacks in small (50 snacks) and large (80 snacks) suitcases. The exporter:
- Must use **at least twice as many small as large suitcases** (x >= 2y)
- Has at most 70 small and 50 large suitcases available
- Must send **at least 15 large suitcases**
- Can send at most 70 suitcases total
- Objective: **maximize total snacks sent**

## Model Formulation

Let:
- x = number of small suitcases (integer, >=0)
- y = number of large suitcases (integer, >=0)

**Objective:**  
Maximize 50x + 80y

**Constraints:**  
x >= 2y  
x <= 70  
y <= 50  
y >= 15  
x + y <= 70  

## Pyomo Model Code

## Optimal Solution

- Small suitcases (x): **47**
- Large suitcases (y): **23**
- **Max snacks delivered:** 4190

*(Solved with GLPK via Pyomo. See script: suitcase_integer_program.py)*
