# Mango and Guava Optimization Problem (Product Mix LP/IP Example)

## Problem Description
A food truck owner wants to maximize profit by choosing how many mangos and guavas to buy and sell, given budget, price, sales bounds, and a ratio constraint.

## Mathematical Model

Let:
- m: number of mangos sold (integer), 100 <= m <= 150
- g: number of guavas sold (integer), g >= 0, g <= m/3

**Constraints:**
1. Budget: 5*m + 3*g <= 20000
2. 100 <= m <= 150
3. g <= m / 3

**Objective:**
Maximize profit: 3*m + 4*g

## Pyomo Model (snippet)

**Optimal solution:** m = 150, g = 50, max profit = 650.

## Use Case:
- Use for product mix/IP and similar allocation problems with budget and ratio constraints.
