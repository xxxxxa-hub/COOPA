# Grilled Cheese Shop: Ratio-Constrained Integer LP Example

## Problem Statement

A grilled cheese shop sells a light and heavy grilled cheese sandwich.
- Light sandwich: 2 slices bread, 3 slices cheese, 10 minutes to make.
- Heavy sandwich: 3 slices bread, 5 slices cheese, 15 minutes to make.
- Must produce at least 3 times as many heavy as light sandwiches.
- Bread available: 300 slices. Cheese available: 500 slices.

**Minimize total production time.** Variables are integer and non-negative.

## Model Structure

Let `x`: number of light sandwiches (integer, >=0)  
Let `y`: number of heavy sandwiches (integer, >=0)

**Objective:**
Minimize `10*x + 15*y`

**Constraints:**
- Bread:      `2*x + 3*y <= 300`
- Cheese:     `3*x + 5*y <= 500`
- Ratio:      `y >= 3*x`    (at least 3 times as many heavy as light)
- Non-negativity: `x >= 0, y >= 0` and both integer

## Pyomo Formulation Outline

## Notes
- The ratio constraint `y >= k*x` is a commonly encountered requirement and can be encoded directly.
- Model produces 0 as the optimal production if no minimum production is enforced.
- To require a minimum number of sandwiches, add: `model.min_prod = Constraint(expr=model.x + model.y >= 1)`.

## Use Case
- Useful as a template for production scheduling or resource allocation with ratio and resource constraints.

**File Origin:** Created from a solved grilled cheese shop ratio-LP example.