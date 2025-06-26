# Integer Linear Programming for Diet/Supplement Minimization Problems (Pyomo Example)

## Problem Summary

Given a set of supplements (or foods), each containing known quantities of nutrients, and known costs, minimize the cost of purchasing supplements to meet or exceed daily minimum requirements for each nutrient. All decision variables (number of pills/quantities) are integer and non-negative.

### Mathematical Formulation

Let there be n supplements and m nutrients.

Variables:
- \( x_i \): number of units (e.g., pills) of supplement \( i \) to purchase, \( x_i \in \mathbb{Z}_{\geq 0} \)

Parameters:
- \( a_{ij} \): units of nutrient \( j \) provided by one unit of supplement \( i \)
- \( b_j \): minimum required units of nutrient \( j \)
- \( c_i \): cost per unit of supplement \( i \)

Objective:
Minimize: \( \sum_{i=1}^{n} c_i x_i \)

Subject to:
\( \sum_{i=1}^{n} a_{ij} x_i \geq b_j \),   for all \( j=1,...,m \)
\( x_i \geq 0 \) and integer, for all \( i \)

---

## Example: Two-Supplement Iron/Calcium Problem

- Supplement A: 5 iron, 10 calcium, $2 per pill
- Supplement B: 4 iron, 15 calcium, $3 per pill
- Need at least 40 units iron and 50 units calcium

### Pyomo Implementation

### Solution for the Example

- Minimum cost: $16.0 (8 pills of A, 0 of B)
- All constraints satisfied

---

## Usage Notes

- Adapt the variables and parameters for any number of supplements/nutrients.
- Use `NonNegativeIntegers` for integer/whole pill counts.
- Larger diet problems can be modeled by introducing indexed sets and parameters in Pyomo.

