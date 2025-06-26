# Pill Blending Problem – Cost Minimization (Linear Programming Example)

## Problem Statement

A person needs to take at least 5g of Z1 and 10g of D3 per day. There are two available pills:
- **Zodiac**: 1.3g Z1, 1.5g D3, $1 per pill.
- **Sunny**: 1.2g Z1, 5g D3, $3 per pill.

Find the optimal (possibly fractional) number of each pill to minimize cost, while meeting daily minimum dosage requirements.

## LP Formulation

Let:
- x = number of Zodiac pills
- y = number of Sunny pills

Minimize: `cost = 1 * x + 3 * y`

Subject to:
- `1.3 * x + 1.2 * y >= 5` (Z1 requirement)
- `1.5 * x + 5 * y >= 10` (D3 requirement)
- `x >= 0, y >= 0`

## Solution (as of 2024)

- Minimum cost: **6.2766**
- x (Zodiac pills): 2.766
- y (Sunny pills): 1.170

Solved with GLPK, continuous variables.

---
This serves as a standard example of a blending/diet nutrition linear program with non-integer variables for lowest-cost fulfillment.

## References

See also: 'zodiac_sunny_minimization.py' for Pyomo code version.
