# Pharmaceutical Paste Container Blending Linear Program

## Problem statement
Given small and large containers producing pharmaceutical paste with different material requirements, find the optimal numbers of each to maximize paste output under fixed water and powdered pill constraints.

### Details:
- Small container: 10 units water, 15 units pill, yields 20 units paste
- Large container: 20 units water, 20 units pill, yields 30 units paste
- Available: 500 units water, 700 units pill

## Algebraic formulation
Let x = number of small containers, y = number of large containers.

Maximize:  
    20x + 30y  

Subject to:  
    10x + 20y <= 500          (water constraint)  
    15x + 20y <= 700          (pill constraint)  
    x >= 0, y >= 0

## Optimal solution (LP relaxation)
- x = 40, y = 5
- Maximum paste produced: 950 units

## Best Practices
- Formulate as an LP; use integer programming (MIP) if integrality is required.
- Both constraints can be binding at optimum.

## Sample Pyomo model location
See: container_blend_pyomo_model.py (created during this solution process)
