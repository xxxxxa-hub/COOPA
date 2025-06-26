# Diet Problem: Maximize Protein Under Caloric and Ratio Constraints

## Problem Statement
A woman needs to maximize her protein intake by consuming two food types:
- Smoothies: 2 units protein, 300 calories
- Protein bars: 7 units protein, 250 calories

Constraints:
- She must have twice as many protein bars as smoothies: b = 2s
- Total calories must not exceed 2000

## Mathematical Formulation

Let:
- s = number of smoothies (integer, >=0)
- b = number of protein bars (integer, >=0)

Maximize:
    protein = 2*s + 7*b

Subject to:
    b = 2*s
    300*s + 250*b <= 2000
    s, b >= 0 and integer

## Solution

Optimal value: **32** (s=2, b=4)

Calculation:
- 2x2 + 7x4 = 32 total protein
- 300x2 + 250x4 = 1600 <= 2000

## Pyomo/Linear Programming Implementation

- This is a standard integer LP.
- Can be implemented with Pyomo as in 'smoothie_bar_lp.py' (see workflow from 2024-04-12).
- Useful for 'maximize nutrients under budget' and 'item ratio constraint' scenarios.

---
Saved by: Assistant (2024-04-12), from an operations research Q&A session.
