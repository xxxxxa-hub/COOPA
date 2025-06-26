# Milk Tea Shop Production Linear Programming Model

## Problem Statement

A milk tea shop owner wants to decide how many bottles of black milk tea (x) and matcha milk tea (y) to produce, given constraints on available milk and honey, to maximize profit.

| Variable                | Black Milk Tea | Matcha Milk Tea |
|-------------------------|:--------------:|:---------------:|
| Milk per bottle (grams) | 600            | 525             |
| Honey per bottle (grams)| 10             | 5               |
| Profit per bottle ($)   | 7.5            | 5               |

**Constraints:**
- Total milk available: 30,000 grams
- Total honey available: 500 grams
- x >= 0, y >= 0, integers

**Mathematical Formulation:**

Maximize  
    7.5x + 5y

Subject to  
    600x + 525y <= 30000  
    10x + 5y <= 500  
    x >= 0, y >= 0, integer

**Optimal Solution:**  
- x = 50, y = 0  
- Maximum profit: 375.0

---

## Pyomo Implementation Summary

Relevant best practices:
- All constraints and objective encoded as above.
- Integer constraints and explicit maximization imposed.
- GLPK solver used; optimal and reproducible result.

---

## Script Reference

For complete Pyomo model, see: `milk_tea_optimizer.py` (see code in the problem history).

Also reference the script 'milk_tea_optimizer.py', which implements the Pyomo model for the above.
