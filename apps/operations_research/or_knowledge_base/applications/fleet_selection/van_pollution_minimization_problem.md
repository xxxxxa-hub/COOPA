# Van Pollution Minimization Problem

## Problem Statement Summary
Given two types of vans (old and new) with different transport capacities and pollution levels, determine the integer number of each van type to acquire so as to minimize total pollution, while ensuring that a required minimum amount of goods is transported and that the use of cleaner (new) vans is capped. 

## Variables
- x: Number of old vans (must be a non-negative integer)
- y: Number of new vans (must be a non-negative integer)

## Objective
Minimize total pollution:  
    Minimize 50x + 30y
where:
- Old van: 50 units of pollution per van
- New van: 30 units of pollution per van

## Constraints
1. Transport Capacity: Ensure total transport meets at least 5000 units:
       100x + 80y >= 5000
      (Old van carries 100 units, new van carries 80 units)
2. Limit on New Vans:
       y <= 30
3. Non-negativity & Integer Requirements:
       x >= 0, integer
       y >= 0, integer

## Linear/Integer Programming Formulation
- Decision variables:  x (old vans), y (new vans)
- Objective:           Minimize 50x + 30y
- Subject to:
      100x + 80y >= 5000
      y <= 30
      x, y >= 0 and integer

## Generalization
This model pattern is broadly applicable to fleet selection problems where decision makers must select integer quantities of different vehicle types to minimize cost, pollution, or other metrics, subject to capacity, environmental, and operational constraints. It can be extended by adding more vehicle types, additional constraints (such as budget or geographic limits), or by optimizing for multi-objective scenarios.
