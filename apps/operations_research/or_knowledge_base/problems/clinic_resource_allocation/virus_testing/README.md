# Virus Testing Clinic Scheduling (Resource-Constrained Maximum Throughput)

## Problem
A popup clinic does virus testing with spit tests and swabs. A spit test takes 10 minutes; a swab, 15 minutes. At least twice as many spit tests as swabs must be given, with a minimum of 20 swabs. At most 8,000 minutes of working time available. Maximize the number of tests.

## Model Summary
- Variables: spit tests (x, integer >= 0), swab tests (y, integer >= 20)
- Objective: maximize x + y
- Constraints: 10x + 15y <= 8000, x >= 2y, y >= 20
- Method: Pyomo MILP (coded in Python, see virus_testing_model.py)
- Status: Solved to integer optimality

## Best Practices Noted
- Use Param objects for all data
- Use explicit variable bounds and constraint functions in Pyomo
- MILP solvers: CBC or GLPK

## Reusability
This setup is general for maximizing completed "tasks" under assignment, ratio, and resource constraints.
