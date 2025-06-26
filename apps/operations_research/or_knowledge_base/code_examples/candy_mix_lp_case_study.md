
# Candy Mix Linear Programming Case Study

## Problem Statement

A candy store mixes regular and sour candy to prepare two products: regular mix and sour surprise mix.
- Each kg of regular mix contains 0.8 kg regular candy and 0.2 kg sour candy. Profit: $3/kg
- Each kg of sour surprise mix contains 0.1 kg regular candy and 0.9 kg sour candy. Profit: $5/kg
- Stock: 80 kg regular candy, 60 kg sour candy.

**Goal**: Maximize profit by deciding production quantities of each mix.

## Algebraic Formulation

Variables:
- x1: kg of regular mix produced (>= 0)
- x2: kg of sour surprise mix produced (>= 0)

Objective: Maximize profit  
Profit = 3*x1 + 5*x2

Constraints:
- 0.8*x1 + 0.1*x2 <= 80      (regular candy limit)
- 0.2*x1 + 0.9*x2 <= 60      (sour candy limit)
- x1 >= 0
- x2 >= 0

## Pyomo Code

## Example Solution

Optimal values:
- x1 ¡Ö 94.29 (regular mix, kg)
- x2 ¡Ö 45.71 (sour surprise mix, kg)
- Objective value (maximum profit) ¡Ö 511.43

Both stock constraints become binding at the optimal solution.
