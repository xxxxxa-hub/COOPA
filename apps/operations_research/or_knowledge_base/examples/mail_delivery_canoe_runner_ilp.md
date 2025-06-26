# Mail Delivery ILP Example: Canoe and Runner Delivery Allocation

## Problem Statement:
A village delivers mail to nearby villages using runners and canoers:
- Runners: Carry 3 bags, take 4 hours per trip.
- Canoers: Carry 10 bags, take 2 hours per trip.
- Canoe deliveries can be at most 33% of total deliveries.
- At most 200 total hours can be used.
- At least 4 runner deliveries are required.

### Variables:
x = number of runner deliveries (integer, x >= 4)
y = number of canoe deliveries (integer, y >= 0)

### Objective:
Maximize total mail delivered: `max 3x + 10y`

### Constraints:
1. Time: `4x + 2y <= 200`
2. Share of canoe trips: `y <= 0.33 * (x + y)` (at most one-third by canoe)
3. Minimum runner: `x >= 4`
4. Integrality: `x, y` integers

### Solution approach:
Formulate and solve with integer linear programming (ILP).
The canoe share constraint is equivalent to `y <= (0.33/0.67) x` in terms of x only.

### Optimal Solution:
- x = 40 (runner), y = 19 (canoe)
- Maximum mail delivered: 310 bags

### Best practices:
- Model "share" constraints by algebraic rearrangement to linear form when possible.
- Always enforce integrality when transportation batches are indivisible.
- Use descriptive variable names, and document unit interpretations.


This is a canonical example of a constrained delivery allocation ILP with an at-most-percentage constraint on one method.
