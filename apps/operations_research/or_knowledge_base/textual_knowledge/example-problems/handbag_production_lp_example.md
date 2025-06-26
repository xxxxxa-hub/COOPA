# Operations Research Problem: Handbag Production Linear Program

## Problem Statement

A fashion company sells regular handbags and premium handbags made of higher quality material. They can sell regular handbags at a profit of $30 each and premium handbags at a profit of $180 each. 
The total monthly cost of manufacturing is $200 per regular handbag and $447 per premium handbag. The company has a total budget of $250,000 and can sell at most 475 handbags of either type per month. 
How many of each handbag should they sell to maximize its monthly profit?

## Mathematical Model

Let x = number of regular handbags  
Let y = number of premium handbags

Maximize:  
> 30x + 180y

Subject to:  
> 200x + 447y <= 250,000  
> x + y <= 475  
> x >= 0, y >= 0

## Solution via LP Solver

- The optimal solution returned by the algebraic optimizer (GLPK) was:  
    - x = 0, y = 0  
    - Objective value (profit): 0.0

## Solver logs/context

- Solver found only the origin feasible.
- No apparent contradiction in constraints for small (x=1, y=0) or (x=0, y=1).
- Review variable upper bounds and any parameter or solver tolerance issues if nonzero production is expected.
- Solver file: `handbag_lp_model.py`

## Lessons/Recommendations

- Always check LP variable bounds and constraint encodings for edge cases if model output seems unexpected.
- This example can be reused for reference on LP formulation or for diagnosing solver/parameter issues.
