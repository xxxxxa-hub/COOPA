# Helicopter and Car Fish Transport Optimization (Mixed-Integer Programming Example)

## Problem Summary
This example demonstrates how to minimize the total transportation time required to move at least 300 fish using helicopters and cars, given capacity and operational constraints.

- **Helicopter**: 30 fish/trip, 40 min/trip, maximum 5 trips allowed
- **Car**: 20 fish/trip, 30 min/trip
- **Fractional/ratio constraint**: At least 60% of the trips must be made by car.

### Decision Variables
- `x`: Number of helicopter trips (integer, >= 0)
- `y`: Number of car trips (integer, >= 0)

### Objective
Minimize the total transportation time: `min 40*x + 30*y`

### Constraints
- `30*x + 20*y >= 300`        (All fish must be transported)
- `x <= 5`                    (Helicopter trip limit)
- `y >= 1.5*x`                (At least 60% trips by car)
- `x + y >= 1`                (At least one trip)

### Key Result
- Minimum total time: **430 minutes**, with **x = 4** (helicopter trips), **y = 9** (car trips)

---

## Solution Method
- Formulated and solved as a Mixed-Integer Linear Program (MILP).
- Solved using **Pyomo** (Python optimization modeling language) and **GLPK** (open-source solver).

### Reference Code
The full Pyomo implementation is available in the codebase as `helicopter_car_transport_optimize.py` in the code_examples directory.

---

## Keywords
- Mixed-integer programming
- MILP
- Transport scheduling
- Vehicle mix optimization
- Pyomo
- Ratio constraint

