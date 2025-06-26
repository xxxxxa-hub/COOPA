# Integer Programming Example: Fish Transportation with Ratio Constraint

## Problem Statement

A large fishing boat sends fish back to shore either by small canoes or smaller diesel boats.  
- A canoe can carry back 10 fish.  
- A small diesel boat can carry back 15 fish.  
- The number of small canoes used has to be at least 3 times as many as the number of diesel boats used.
- At least 1000 fish need to be transported.
- **Objective:** Minimize the total number of canoes and diesel boats needed.

## Mathematical Formulation

Let:
- x: number of canoes (integer, >= 0)
- y: number of diesel boats (integer, >= 0)

Minimize:  
  x + y

Subject to:  
  10x + 15y >= 1000  
  x >= 3y  
  x, y >= 0 and integer

## Solution

Optimal solution:
- x = 67 (canoes)
- y = 22 (diesel boats)
- Minimum total number of boats required = x + y = **89**

Both constraints are active at the optimum.
Model solved using Pyomo and an open-source MIP solver.

## Keywords
integer programming, transportation, ratio constraint, minimum boats, Pyomo, operations research, example
