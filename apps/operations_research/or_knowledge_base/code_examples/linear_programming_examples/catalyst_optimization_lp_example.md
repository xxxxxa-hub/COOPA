# LP Example: Automotive Catalyst Optimization

## Problem Statement
An automotive company is comparing two different catalysts:
- Palladium-heavy catalyst: requires 15 units of platinum and 25 units of palladium, conversion rate: 5 units/sec.
- Platinum-heavy catalyst: requires 20 units of platinum and 14 units of palladium, conversion rate: 4 units/sec.

Resources available: 450 units of platinum, 390 units of palladium.

## Variables
- x = number of palladium-heavy catalysts used
- y = number of platinum-heavy catalysts used

## Mathematical Formulation
Maximize:
    5x + 4y

Subject to:
    15x + 20y <= 450   (platinum constraint)
    25x + 14y <= 390   (palladium constraint)
    x >= 0, y >= 0

## Solution Insight
- The feasible region only includes the origin (x=0, y=0), meaning the problem is over-constrained.
- No positive usage of either catalyst is feasible given the resource constraints and coefficients.
- Objective value: 0.0 (no conversion possible).

## Takeaways
- Always check the feasibility of LPs for extreme constraint coefficients.
- This example can be reused for similar catalyst/resource allocation problems.
