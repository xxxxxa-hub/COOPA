# Integer Programming Example: Clinic Swab Scheduling Optimization

## Problem statement

A clinic aims to maximize the number of patients seen by performing either throat or nasal swabs, given:

- Throat swab: 5 minutes per patient
- Nasal swab: 3 minutes per patient
- At least 30 nasal swabs must be performed.
- Number of throat swabs must be at least four times the number of nasal swabs (to reduce discomfort).
- Total operational time: 20,000 minutes.

## Model formulation

Let:
- x = number of throat swabs (integer, >=0)
- y = number of nasal swabs (integer, >=0)

Objective:
- Maximize total patients: **x + y**

Subject to:
- 5x + 3y <= 20,000  (time constraint)
- y >= 30            (minimum nasal swabs)
- x >= 4y            (throat-to-nasal ratio)

## Solution

- This is an Integer Linear Program (ILP).
- The optimal value (maximum patients): **4347**
  - Optimal swabs: x=3479 throat, y=868 nasal.
- The solution tightly satisfies the total time: 5*3479 + 3*868 = 20,000.
- Other constraints are satisfied.

## Best practices

- Clearly define variables, objectives, and all constraints
- Formulate ratio-based constraints (e.g., "at least 4 times as many x as y": x >= 4y)
- Consider time, minimum, and ratio requirements in resource allocation and healthcare scheduling problems.
- Use exact integer programming solvers (GLPK, CBC via Pyomo).

## Reference

- Problem solved using Pyomo (Python) with GLPK solver.
- Useful structure for healthcare or resource-constrained assignment/scheduling problems.
