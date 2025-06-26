# Minimizing Total Trip Time for Transporting Groups with Bus/Car Choices (Integer Programming Example)

## Summary
This entry provides a generic formulation and solution approach for problems where groups (such as animals or passengers) need to be transported from location A to B using two vehicle types with different capacities, trip durations, and minimum trip proportion constraints. The model lets you minimize the total trip time, subject to integer and operational constraints, and is useful for logistics, operations research, and optimization in resource scheduling scenarios.

## Mathematical Formulation

**Variables:**
- x: number of trips of type 1 (e.g., bus), integer, x >= 0
- y: number of trips of type 2 (e.g., car), integer, y >= 0

**Parameters:**
- time1_per_trip: duration per trip with vehicle 1 (bus)
- time2_per_trip: duration per trip with vehicle 2 (car)
- capacity1: capacity per trip of vehicle 1
- capacity2: capacity per trip of vehicle 2
- total_demand: total units/passengers to transport
- max_trips_type1: (Optional) maximum allowed trips of type 1
- alpha: minimum proportion of total trips that must be type 2, 0 < alpha < 1

**Objective:**
- Minimize total trip time:   time1_per_trip * x + time2_per_trip * y

**Constraints:**
1. Main constraint (meet demand):           capacity1*x + capacity2*y >= total_demand
2. Max trips for type 1 (if restricted):   x <= max_trips_type1
3. Proportion constraint:                  y >= alpha*(x + y)   or equivalently   y >= (alpha/(1-alpha)) * x
4. Integrality:                            x, y integer, x >= 0, y >= 0

**Example (Pyomo-style pseudocode):**

    Minimize:  time1*x + time2*y
    Subject to:
        capacity1*x + capacity2*y >= total_to_move
        x <= max_bus_trips
        y >= alpha*(x + y)
        x >= 0, y >= 0
        x, y integer

## Detailed Example

A zoo must transport 300 monkeys using two options: buses or cars.
- Buses: 20 monkeys per trip, 30 minutes per trip, max 10 trips
- Cars: 6 monkeys per trip, 15 minutes per trip
- At least 60% of total trips must be by car

**Model:**

    Minimize:   30*x + 15*y
    Subject to:
        20*x + 6*y >= 300
        x <= 10
        y >= 1.5*x   (from y >= 0.6(x + y), which rearranges to y >= 1.5x)
        x >= 0, y >= 0, x, y integer

**Solution:**
- x = 10, y = 17
- Minimal total trip time = 30*10 + 15*17 = 300 + 255 = 555 minutes

## Application Notes
- The proportion constraint can encode critical operational or ethical requirements (e.g., animal comfort, driver utilization).
- Modifications can easily incorporate other limits or objectives (such as cost or fuel usage).

## Related Entries
- See also: 'code_examples/chicken_transport_integer_programming.md' for a similar problem with different numbers.
- Other transport and assignment integer programming models are found in 'textual_knowledge/example-problems/'.
