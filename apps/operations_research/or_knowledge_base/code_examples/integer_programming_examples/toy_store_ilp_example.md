# Toy Store Integer Linear Programming Example

## Problem Statement

A toy store sells plush toys and dolls. Each plush toy costs the store $3 and each doll costs the store $2. The store owner can spend at most $700 on inventory. Each plush toy is sold for a profit of $4 and each doll for a profit of $2. At least 90 but at most 190 plush toys are sold each month. The number of dolls sold is at most twice the amount of plush toys sold. Determine how many of each to buy and sell to maximize profit.

## Mathematical Formulation

Let:
- x = number of plush toys (integer)
- y = number of dolls (integer)

Maximize:  
    **Profit = 4x + 2y**

Subject to:  
    3x + 2y <= 700  
    90 <= x <= 190  
    y <= 2x  
    x >= 0, y >= 0

## Solution Approach

- Modelled as an Integer Linear Programming (ILP) problem.
- Used Pyomo/Python.
- Used GLPK or CBC solver to obtain optimal integer solution.

## Solution

Optimal profit = **890.0**

(Further implementation details in `profit_ilp_pyomo.py`, see code for details.)

