# Party Transportation Vehicle Optimization (Limousines & Buses)

## Problem Statement

A party organizer has to transport at least 400 people to an event using two types of vehicles: limousines and buses.
- Limousines have 12 seats each.
- Buses have 18 seats each.
- At least 70% of the vehicles used must be limousines.
- The goal is to **minimize the total number of vehicles used**.

## Mathematical Formulation

- Let x = number of limousines (integer, >= 0)
- Let y = number of buses (integer, >= 0)

### Objective
Minimize: **x + y**

### Subject to:
- Seating: 12x + 18y >= 400
- Limousine dominance: x / (x + y) >= 0.7 (i.e., at least 70% of vehicles are limousines)
    - This can be rewritten as: 3x >= 7y   (after rearranging)
- x, y are non-negative integers

## Solution Summary

- Optimal total vehicles (x + y): **30**
- Optimal solution: 22 limousines, 8 buses
    - 12*22 + 18*8 = 408 >= 400 (seating constraint)
    - 22 / 30 ≈ 0.733 >= 0.7 (limousine proportion)

## Modeling
An integer program can be formulated and solved with Pyomo, CBC, or GLPK. The limousine proportion constraint can be linearized as above.

---

*This template and solution approach can be adapted for any similar vehicle allocation/transportation problem with minimum quotas and proportions.*
