# Transportation Mix Integer Programming Example (Van/Truck)
## Problem Context
A business chooses between two transport modes (owned vans vs. rented trucks) to meet shipment, budget, and marketing requirements. 

## Key Features Modeled
- Integer variables: counts of van trips (x), truck trips (y)
- Capacity & budget constraints: 
    - 50x + 80y >= total boxes required
    - 30x + 50y <= budget
- Marketing: x > y (i.e., 'number of van trips must exceed truck trips')
- Objective: minimize total trips (x + y)
- Integer and nonnegative variable restrictions

## Modeling Tips
- Strict inequality x > y can be modeled as x >= y + 1 when x, y are integer.
- Set upper bounds on variables for solver efficiency.
- All variables should be explicitly set as integer in the model.

## Pyomo Excerpt

## Notes
- Result: Optimal (x, y) = (13, 11), minimum trips = 24 with all constraints satisfied (boxes, budget, marketing).
- x > y is correctly enforced for integer variables as x >= y+1.

## Relevance
This template covers integer decision modeling for transport/resource mix with costs, capacities, strict-logic, and marketing-type real-world constraints.
