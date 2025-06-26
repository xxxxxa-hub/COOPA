# Example: Resource Allocation / Mixture LP Model – Pill Formulation Problem

## Problem Statement
A laboratory has 1000 units of medicinal ingredients to produce two types of pills: large and small. 
- A large pill requires 3 units of medicine and 2 units of filler. 
- A small pill requires 2 units of medicine and 1 unit of filler. 
- At least 100 large pills must be made. 
- At least 60% of all pills produced must be small pills. 
- Objective: Minimize the total filler used.

## Mathematical Model Formulation
Let x = number of large pills (integer)
Let y = number of small pills (integer)

Minimize: 2x + y    (total filler)

Subject to:
- 3x + 2y <= 1000        (total medicine constraint)
- x >= 100               (minimum large pills)
- y >= 0                 (non-negativity for small pills)
- y >= 1.5x              (at least 60 percent of pills are small:
                         y/(x+y) >= 0.6  <=>  y >= 1.5x)
- x, y in integers

## Solution (Pyomo+GLPK)
Optimal: 
- x = 100
- y = 150
- Minimum filler used = 350 units

## Notes
- This is a classic resource allocation (mixture/blending) integer LP.
- Demonstrates handling fixed minimums, percentage (ratio) requirements, and integer variables in resource-based models.
- Useful as a template for discrete blending/resource minimization.

## Tags
linear programming, blending, resource allocation, integer variables, percentage constraint, pill formulation, Pyomo example, worked solution
