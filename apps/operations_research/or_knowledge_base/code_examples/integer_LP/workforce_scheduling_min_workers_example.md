# Title: Workforce Scheduling with Two Types of Workers (Integer Programming)

### Problem Statement:
An accounting firm employs part time and full time workers. Full time workers work 8 hours/shift, part time 4 hours/shift; paid $300/shift for full time, $100/shift for part time. Given a required 500 labor hours and a $15,000 budget, how many of each to schedule to *minimize the total number of workers*?

### Mathematical Formulation:
Variables:
- x = number of full time workers (integer, >= 0)
- y = number of part time workers (integer, >= 0)

Objective:
- Minimize x + y

Subject to:
- 8x + 4y >= 500 (labor hours)
- 300x + 100y <= 15000 (budget)

### Solution Approach:
- Model as Integer Linear Program (ILP)
- Implemented and solved in Pyomo with GLPK solver
- Code saved as 'ilp_worker_assign.py'

### Result:
Minimum total workers: **100** (x = 25 full-time, y = 75 part-time)

