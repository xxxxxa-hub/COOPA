# Integer Programming: Maximize Sports Equipment Production

## Problem Statement

A handmade sports equipment manufacturing company makes basketballs and footballs.

- **Basketballs**: require 5 units of materials, 1 hour to make
- **Footballs**: require 3 units of materials, 2 hours to make
- **Resource limits**: 1500 materials, 750 labor hours
- **Business rules**:
    - At least 3x as many basketballs as footballs
    - At least 50 footballs

**Objective:** Maximize the total number of sports equipment produced (x + y).

## Mathematical Formulation

Let
- `x`: number of basketballs (integer, >= 0)
- `y`: number of footballs (integer, >= 0)

Maximize:  
    `x + y`

Subject to:
- `5x + 3y <= 1500`   (materials)
- `x + 2y <= 750`   (labor)
- `x >= 3y`           (basketball ratio)
- `y >= 50`           (minimum footballs)
- `x, y` integer and >= 0

## Solution Approach

- Enumerate values for y from 50 up, compute minimum x = 3y. For each feasible (x, y), check constraints and maximize x + y.
- Solution can also be obtained using integer programming solvers (Pyomo MIP, etc.).

## Optimal Solution

The maximum number of products that can be made is **333**.

*(Details of variable values can be recomputed or are available in logs if needed.)*

---

*Saved from actual problem instance, including full formulation and solution methodology (2024-06).*
