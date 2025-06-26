
# Bakery Resource Allocation LP (Bread and Cookies)

## Problem Statement

A bakery uses a stand-mixer and a slow bake oven to make bread and cookies.
- Each machine: at most 3000 hours/year.
- Bread: 1 hour mixer, 3 hours oven, profit $5/loaf.
- Cookies: 0.5 hour mixer, 1 hour oven, profit $3/batch.

## Mathematical Formulation

Let:
- x = number of loaves of bread baked (>=0)
- y = number of batches of cookies baked (>=0)

Objective:
Maximize    5x + 3y

Subject to:
- Stand-mixer constraint: 1x + 0.5y ¡Ü 3000
- Oven constraint:       3x + 1y ¡Ü 3000

## Solution (using Pyomo LP)

- Optimal value: **9000.0**
- Optimal allocation: x = 0.0, y = 3000.0
- Both constraints are binding.

## File location

Pyomo code: `lp_resource_allocation_solver.py`
