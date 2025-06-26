# Dessert Shop Flavoring Minimization (Ice Cream and Sorbet Production)

## Problem Statement
A dessert shop produces two desserts: matcha ice cream and orange sorbet. Each matcha ice cream requires 2 units of flavoring, 4 units of ice cream. Each orange sorbet requires 4 units of flavoring, 3 units of water. The shop has 600 units of ice cream and 550 units of water available. More orange sorbet must be made than matcha ice cream, and at least 15% of desserts must be matcha ice cream. The goal is to **minimize the total amount of flavoring needed**.

## Five-Element Model Summary
- **Objective**: Minimize total flavoring used (2x + 4y)
- **Variables**:
    - x: Integer >= 0 (matcha ice creams)
    - y: Integer >= 0 (orange sorbets)
- **Constraints**:
    1. 4x <= 600        (ice cream availability)
    2. 3y <= 550        (water availability)
    3. y >= x + 1       (more orange sorbets)
    4. x >= 0.15(x + y) (at least 15% matcha)
    5. x, y integer, x >= 0, y >= 0
- **Parameters**: All coefficients, mix % and resource bounds are parameterized.
- **Notes**: Integer solution required. This is a blending/production planning type IP.

## Solution
- Optimal total flavoring: **10 units**
- Decision: Produce **1 matcha ice cream**, **2 orange sorbets**

## Pyomo Implementation



Purpose: Serve as an example for integer linear programming with blending/resource and minimum mix constraints, solved using Pyomo, including five-element summary, Python code, and solution.
