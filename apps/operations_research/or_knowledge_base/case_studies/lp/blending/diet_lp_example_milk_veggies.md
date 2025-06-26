# Diet/Nutrition Linear Programming Example - Milk and Vegetables

## Problem Statement:
Minimize the cost for a child to meet daily calcium and iron requirements using milk and vegetable portions, where each has known cost and nutrient content.

## Model:
**Variables:**
  - x: glasses of milk (continuous)
  - y: plates of vegetables (continuous)

**Objective:**
  Minimize cost = 1*x + 2*y

**Constraints:**
  40*x + 15*y >= 100   (Calcium)
  25*x + 30*y >= 50    (Iron)
  x, y >= 0

## Solution approach:
Modeled and solved with Pyomo + LP solver (GLPK). Solution (continuous): x=2.5, y=0, minimum cost = 2.5.

Reference code: 'milk_veggies_optimizer.py' (see code for implementation details).

**Best practices:** Use variable bounds, Pyomo Param objects, and validate solution feasibility.

**Applications:** Any resource allocation or diet planning linear program with multiple constraints and cost minimization objective.
