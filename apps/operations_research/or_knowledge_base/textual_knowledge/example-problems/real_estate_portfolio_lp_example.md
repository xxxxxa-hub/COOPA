# Investment Portfolio LP Example (Condos & Detached Houses)

## Problem Statement
Given a fixed total budget, choose allocations between two investment options (condos and detached houses) to maximize profit, subject to:
- Ratio constraint between two options (at least 20% of total in condos)
- Minimum investment constraint in detached houses
- Non-negativity and total budget constraint

### Variables:
- x1: amount invested in condos
- x2: amount invested in detached houses

### LP Formulation
Objective:
    Maximize 0.5*x1 + 1*x2

Constraints:
    x1 + x2 <= Total_Budget
    x1 >= 0.2*(x1 + x2)
    x2 >= 20000
    x1 >= 0
    x2 >= 0

### Solution Notes
- Ratio constraint is equivalent to x1 >= 0.25 * x2
- Profit structure with higher per-dollar profit on one option causes solution at minimum allowable amounts by ratio/minimum constraints
- When ratio and lower bound are binding, total budget is non-binding
- Useful model for any two-asset investment problem with similar constraints

### Pyomo/Python snippet:
See file: lp_investment_model.py

### Example Solution:
For a budget of $760,000, maximizing profit given the constraints yields:
    - Invest $5,000 in condos, $20,000 in detached houses
    - Maximum profit = $22,500

### Generalization:
This structure can apply for:
- Asset allocation with min/max ratios per asset
- Investment/portfolio LP problems with per-asset returns and minimum/maximum allocation policies
