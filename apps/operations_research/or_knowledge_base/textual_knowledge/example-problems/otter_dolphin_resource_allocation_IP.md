# Otter & Dolphin Resource Allocation – Linear/Integer Program Example

## Problem Statement

An aquarium does shows with otters and dolphins. Otters perform 3 tricks at a time (need 3 treats), dolphins 1 trick (need 5 treats). At least 10 dolphins, and at most 30% of performers can be otters. Maximum 200 treats. Maximize number of tricks.

## Variables

- `x`: Number of otters (`x ∈ N, x >= 0`)
- `y`: Number of dolphins (`y ∈ N, y >= 0`)

## Objective

Maximize total tricks:  
`maximize 3x + y`

## Constraints

- Treats: `3x + 5y <= 200`
- Dolphins minimum: `y >= 10`
- Otter proportion: `x/(x+y) <= 0.3` (if `x + y > 0`)
  - Linearized (when `x + y > 0`): `7x <= 3y`
- Integer and nonnegativity: `x, y ∈ N, x >= 0, y >= 0`

## Solution Notes

- For small integer regions, this can be efficiently solved by brute-force or enumeration.
- For algebraic solvers (e.g., Pyomo), use Big-M or ratio linearization as above.
- The optimal solution (as of this problem):
    - `x = 13` (otters)
    - `y = 32` (dolphins)
    - Objective value: `3*13 + 32 = 71` tricks

## Brute-Force Enumeration Example (Python-like pseudo-code)

## Applicability

- Useful for problems involving resource allocation with mix/proportion and budget/capacity constraints.
- Shows typical linearization technique for fractional constraints.
