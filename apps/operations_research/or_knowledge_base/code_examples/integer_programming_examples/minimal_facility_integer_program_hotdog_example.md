
# Minimal Facility Integer Programming Example: Hot Dog Shop Problem

## Problem Statement
A hot dog company can build two types of butcher shops, a small shop and a large shop.  
- A small shop can make 30 hot dogs per day and requires 2 workers.  
- A large shop can make 70 hot dogs per day and requires 4 workers.  
The company must make at least 500 hot dogs per day but they only have available 30 workers.  
**Question:** How many of each butcher shop should the company build to minimize the total number of shops?

## Algebraic Model (Integer Programming Formulation)
Let  
x = number of small shops (integer, x >= 0)  
y = number of large shops (integer, y >= 0)  

Minimize:  
    x + y  

Subject to:  
    30x + 70y >= 500   (production constraint)  
    2x + 4y <= 30      (worker constraint)  
    x, y >= 0 and integer

## Pyomo Implementation

## Solution Summary
- Optimal number of small shops (x): 1  
- Optimal number of large shops (y): 7  
- Minimum total number of shops: **8**  
Constraint satisfaction:  
- 30*1 + 70*7 = 520 >= 500 (production met)  
- 2*1 + 4*7 = 30 <= 30 (workers not exceeded)

---

This is a canonical example of a minimal-facility integer programming model with practical production and resource allocation constraints.

