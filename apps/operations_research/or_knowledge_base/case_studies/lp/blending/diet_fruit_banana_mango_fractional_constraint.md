# Minimizing Sugar in a Zookeeper Fruit Diet Problem (Banana/Mango, Fractional Constraint)

## Problem Statement:
A zookeeper must feed a gorilla bananas and mangoes:
- Each banana: 80 cal, 20g K, 10g sugar
- Each mango: 100 cal, 15g K, 8g sugar
- Diet must provide >=4000 cal, >=150g K
- At most 33% of fruit can be mangoes
- Objective: minimize total sugar

## Linear Program Formulation:
Let x = #bananas, y = #mangoes

Minimize:

Subject to:

## Conversion of Fractional Constraint:
y/(x+y) <= 1/3 => 3y <= x + y => 2y <= x

## Final Linear Constraints:
- 80x + 100y >= 4000
- 20x + 15y >= 150
- 2y <= x
- x >= 0, y >= 0

## Solution Approach:
- Formulate/convert to pure linear program (LP)
- Minimize sugar intake given constraints

## Solver Output (Optimal Solution):
- Minimum sugar = **430.769**
- x ~= 30.77 bananas
- y ~= 15.38 mangoes

## Notes:
- This problem demonstrates handling fractional/ratio constraints by algebraic manipulation to linearize them.
- Useful as a template/model for diet/minimum/ratio-constrained LPs.
