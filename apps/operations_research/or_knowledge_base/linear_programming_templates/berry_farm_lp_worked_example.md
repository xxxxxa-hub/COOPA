# Berry Farm Linear Programming Problem

## Problem Statement
A berry farmer has two farms (old and new) with the following characteristics:

- **Old Farm:** Cost: $300/day, Raspberries: 2 kg/day, Blueberries: 2 kg/day, Strawberries: 4 kg/day
- **New Farm:** Cost: $200/day, Raspberries: 4 kg/day, Blueberries: 1 kg/day, Strawberries: 2 kg/day

**Contract requirements:**  
- Raspberries: 10 kg  
- Blueberries: 9 kg  
- Strawberries: 15 kg

**Goal:**  
Determine number of days to operate each farm (x = old, y = new) to minimize total cost, while meeting delivery requirements.

## Mathematical Model

Variables:
- x: days old farm operates (continuous, >= 0)
- y: days new farm operates (continuous, >= 0)

Objective:  
Minimize total cost = 300 * x + 200 * y

Subject to:
- 2x + 4y >= 10   (raspberries)
- 2x + 1y >= 9    (blueberries)
- 4x + 2y >= 15   (strawberries)
- x >= 0, y >= 0

## Solution (Continuous Relaxation)
Optimal # days to operate:
- Old farm (x): 4.333...
- New farm (y): 0.333...

Minimum cost: $1366.67

## Notes
- LP solved using Pyomo + GLPK.
- See: `berry_farm_optimizer.py` for full Pyomo implementation.
- Provides a reference template for similar two-resource, multi-commodity LPs.
