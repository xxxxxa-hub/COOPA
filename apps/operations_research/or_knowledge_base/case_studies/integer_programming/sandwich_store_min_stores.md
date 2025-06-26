# Problem: Minimizing Number of Sandwich Chain Stores (Integer Programming Example)

## Problem statement
A sandwich company can open two types of stores:
- A dine-in place (makes 100 sandwiches/day, requires 8 employees)
- A food-truck (makes 50 sandwiches/day, requires 3 employees)

The company must:
- Make at least 500 sandwiches per day
- May employ at most 35 employees

## Decision variables
x: Number of dine-in places (integer, >= 0)
y: Number of food-trucks (integer, >= 0)

## Model formulation

Objective: 
    Minimize x + y

Subject to: 
    100x + 50y >= 500        # Sandwich capacity constraint
     8x + 3y  <= 35          # Employee constraint
     x, y >= 0, integer

## Solution
- Optimal value (minimum stores): 8
- x = 2 dine-in places
- y = 6 food-trucks

(Solved using algebraic_optimizer_agent. See also: ilp_dinein_foodtruck.py for a Pyomo implementation.)


Short description: Integer programming example for minimizing the number of sandwich stores under staff and production constraints, with formulation and solution.
