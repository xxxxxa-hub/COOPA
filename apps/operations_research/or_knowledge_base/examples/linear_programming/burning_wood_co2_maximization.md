# CO2 Production Optimization from Wood Burning

## Problem Statement

Given two processes for burning wood to produce CO2 (with and without catalyst), maximize total CO2 under limited wood and oxygen.

**Process Data:**
- With catalyst: 10 wood, 20 oxygen -> 15 CO2
- Without catalyst: 15 wood, 12 oxygen -> 18 CO2

Available: 300 wood, 300 oxygen. Let x = # with catalyst, y = # without catalyst.

## Model

- Maximize: 15x + 18y
- Subject to:
    - 10x + 15y <= 300 (wood)
    - 20x + 12y <= 300 (oxygen)
    - x >= 0, y >= 0

## Pyomo Implementation

**Optimal value:** 375 (continuous), at x = 5, y ~= 16.67

---

For integer solutions: use `domain=NonNegativeIntegers`.

---
