# Integer LP: Environmental Transport Problem with Ratio Constraints

## Problem type
Integer linear programming (ILP) for scheduling limited vehicle trips with:
- Distinct trip capacities/times
- Upper/lower bounds on trip counts
- Proportional/rationed use constraints
- Minimum total requirement

### Example: Duck transport after oil spill

#### Variables
- x = integer number of boat trips (capacity: 10, time: 20 min)
- y = integer number of canoe trips (capacity: 8, time: 40 min)

#### Objective
Minimize total transportation time:
    Minimize T = 20*x + 40*y

#### Constraints
1. 10*x + 8*y >= 300          (minimum ducks transported)
2. x <= 12                    (max boat trips)
3. y >= 0.6 * (x + y)         (at least 60% trips must be canoes)
   Equivalent: 2*y >= 3*x
4. x >= 0, y >= 0 and integers

#### Pyomo model sketch

#### Solution (for this scenario)
- Optimal value: 1160 minutes (x=12, y=23)
- Satisfies all constraints including trip proportion

## Modeling tip
Convert percentage/proportion constraints into linear form (e.g. y >= alpha(x + y) -> y >= (alpha/(1-alpha)) x for alpha in (0,1)).

## Application
Suitable for transportation, scheduling, shift planning with vehicle/staff type mix and proportional use constraints.



This file documents an integer LP for a transport scheduling problem featuring trip capacity, max trips, a ratio/proportion constraint on trip types, and a minimum total requirement, along with a Pyomo implementation sketch and modeling tip for generalization.

Description: Integer LP model and code template for transport scheduling with capacity, upper/lower bound, and trip-ratio requirements.
