# Berry Farm Linear Programming Model (Profit Maximization)

## Problem Statement:
John has a 300 acre berry farm on which to plant blueberries and raspberries. John has $10,000 to spend on watering and 575 days worth of labor available. For each acre of blueberries, 6 days of labor and $22 in watering costs are required. For each acre of raspberries, 3 days of labor and $25 in watering costs are required. The profit per acre is $56 for blueberries and $75 for raspberries.

## LP Model Formulation:
**Variables:**
    x = acres of blueberries planted (continuous, >= 0)
    y = acres of raspberries planted (continuous, >= 0)
**Objective:**
    Maximize profit: 56x + 75y
**Constraints:**
    1) Land: x + y <= 300 
    2) Labor: 6x + 3y <= 575
    3) Watering: 22x + 25y <= 10,000
    4) Non-negativity: x, y >= 0

## Optimal Solution:
- Maximum profit: 14,375 (units of currency)
- x = 0 acres (blueberries)
- y ≈ 191.67 acres (raspberries)
- Limiting factors: labor and watering cost (not land)

## Code reference
Python implementation provided: see `berry_farm_lp.py` in the working directory.