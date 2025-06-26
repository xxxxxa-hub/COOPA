# Wine Bottle Optimization Problem (Linear Programming Example)

## Problem Statement
A vine company bottles wine in vintage (500 ml) and regular (750 ml) bottles, with 100,000 ml total wine available.
- Regular bottles: at least 4 times as many as vintage bottles.
- At least 10 vintage bottles must be made.

**Objective:** Maximize total number of bottles.

## Mathematical Formulation

Variables:
- x: number of vintage bottles (integer, >= 10)
- y: number of regular bottles (integer, >= 0, y >= 4x)

Maximize: x + y

Subject to:
- 500*x + 750*y <= 100000
- y >= 4x
- x >= 10
- x, y >= 0 and integer

## Pyomo/GLPK Solution

Optimal solution:
- Maximum total bottles: **142**
- Vintage bottles: **27**
- Regular bottles: **115**
- Wine used: 99,750 ml

All constraints satisfied.

## File location
- Solution code saved as: `wine_bottle_optimization.py`

## Usage
Edit parameters for bottle volumes, ratios, or wine total, and rerun in Pyomo with GLPK or another compatible IP solver.
