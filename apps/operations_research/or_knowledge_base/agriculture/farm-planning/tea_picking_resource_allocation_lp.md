# Worked Example: Tea Picking Resource Allocation LP

## Problem Statement
A tea estate has 500 acres of land. Leaves can be picked using traditional machines or modern machines, with the following characteristics per acre:
- Traditional: 30 kg tea, 10 kg waste, 20 liters fuel.
- Modern: 40 kg tea, 15 kg waste, 15 liters fuel.

Constraints:
- 9000 liters fuel available
- At most 6000 kg waste

Objective: Maximize total tea leaves picked.

## Algebraic Formulation
Let x = acres with traditional machine, y = modern machine.

Maximize: 30x + 40y

Subject to:
- x + y <= 500     (total acreage)
- 20x + 15y <= 9000  (fuel constraint)
- 10x + 15y <= 6000  (waste constraint)
- x >= 0, y >= 0

## Solution approach
This is a standard LP and can be modeled in Pyomo. See accompanying code file: `tea_optimization_model.py` for reproducible solution steps.

## Summary of optimal solution
- Maximum tea leaves: 17,000 kg
- x (traditional): 300 acres
- y (modern): 200 acres
- All constraints bind at optimum.

## Notes
This example illustrates resource allocation linear programs with multiple resource constraints (land, fuel, waste), and is useful for similar agricultural or manufacturing processes. See also: `hay_lp_example.md` for another agricultural resource allocation LP with acreage, byproduct, and resource limits.
## Code Reference
For reproducibility, see `tea_optimization_model_2.py` in this folder for the Pyomo implementation of the LP solution.
