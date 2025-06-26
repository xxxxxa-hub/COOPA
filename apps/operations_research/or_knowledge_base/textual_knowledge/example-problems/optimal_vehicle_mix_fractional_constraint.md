# Optimal Mix of Transportation Vehicles with Fractional Constraints

## Problem statement

Given two types of vehicles, each with passenger capacities, determine the optimal quantity of each to meet a minimum transportation requirement, where:

- The objective is to minimize the use of one vehicle type
- No more than a certain fraction of all vehicles can be of the other type

## General formulation (integer programming)

Let:
- x = number of vehicle type 1 (e.g., scooters)
- y = number of vehicle type 2 (e.g., rickshaws)
- a, b = capacities of vehicle 1 and 2
- D = minimum passengers to transport
- f = maximum allowed fraction of vehicle 2

Objective: Minimize x

Subject to:
- a*x + b*y >= D
- y / (x + y) <= f    (if x + y > 0)

Linearize ratio constraint for integer programming ("y / (x + y) <= f" -> "(1-f)*y <= f*x" )

## Example formulation (from theme park problem):

- a = 2, b = 3, D = 300, f = 0.4
- Objective: Minimize x
- Constraints:
    1. 2x + 3y >= 300
    2. y / (x + y) <= 0.4 -> 3y <= 2x
    3. x, y integers >= 0

Solved using OR-Tools CP-SAT solver. See associated Python code for implementation. 

## Saved code

Python script for OR-Tools implementation saved as `scooter_rickshaw_optimization.py`.
