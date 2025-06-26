
# Ice Cream Production Linear Programming Example

This knowledge base entry summarizes a classic LP production planning problem and provides ready-to-use Pyomo code.

## Problem Statement

An ice cream store makes chocolate and vanilla ice cream by the gallon. In a week, they must make at least 5 gallons of each type but at most 10 gallons of chocolate ice cream and at most 8 gallons of vanilla ice cream.
- It takes 1 hour to produce a gallon of chocolate ice cream and 2 hours per gallon of vanilla.
- 30 labor hours are available per week.
- At least 6 worker-hours are required in total, interpreted as 1 per gallon of chocolate, 2 per vanilla.
- Profit: $200 per gallon chocolate, $300 per gallon vanilla.
- Goal: Maximize profit.

## Mathematical Formulation

Variables:
- x: gallons of chocolate ice cream (integer), 5 ¡Ü x ¡Ü 10
- y: gallons of vanilla ice cream (integer), 5 ¡Ü y ¡Ü 8

Objective:
- Maximize 200*x + 300*y

Constraints:
- x + 2*y ¡Ü 30    (Time)
- x + 2*y ¡Ý 6     (Minimum worker requirement)
- 5 ¡Ü x ¡Ü 10
- 5 ¡Ü y ¡Ü 8
- x, y integer

## Pyomo Model Example

## Optimal Solution

- Maximum profit: **4400**
- (x, y) = (10, 8)
