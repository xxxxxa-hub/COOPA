
# Cruise Ship Optimization (Integer Linear Programming Example)

## Problem Statement

A cruise company can operate two types of trips: large cruise ship and small cruise ship.
- Large cruise ship trip: 2000 customers, 20 units pollution, at most 7 trips.
- Small cruise ship trip: 800 customers, 15 units pollution, at least 40% of total trips.
- The goal is to transport **at least 20000 customers**.
- Minimize the total pollution produced.

## Mathematical Formulation

Let:
- x = number of large cruise ship trips (integer)
- y = number of small cruise ship trips (integer)

**Objective:**
Minimize:   20x + 15y

**Constraints:**
1. x ¡Ü 7
2. y ¡Ý 0.4 * (x + y)
3. 2000x + 800y ¡Ý 20000
4. x, y ¡Ý 0 and integer

## Solution

- Optimal solution: x = 7, y = 8
- Minimum pollution: 20*7 + 15*8 = **260**
- All constraints satisfied.

## Pyomo Model (example)

