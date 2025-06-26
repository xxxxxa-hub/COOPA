# Minimizing Pollution for Tourist Transport in the Mountains

## Problem Statement
A tourist spot in the mountains transports visitors to the top using hot-air balloons or gondola lifts. Objective: Minimize total pollution while transporting at least 70 visitors.

### Decision variables
- Number of hot-air balloon rides (integer, 0 <= x_b <= 10)
- Number of gondola lift rides (integer, x_g >= 0)

### Parameters
- Hot-air balloon: 4 visitors/ride, 10 units pollution/ride, max 10 rides
- Gondola lift: 6 visitors/ride, 15 units pollution/ride

### Model
- Objective: Minimize 10*x_b + 15*x_g
- Subject to:
    - 4*x_b + 6*x_g >= 70
    - x_b <= 10
    - x_b, x_g >= 0, integer

### Solution (from Pyomo, solver GLPK)
- Minimum total pollution: **175**
- Balloon rides: 1
- Gondola lift rides: 11
- Total visitors: 70

### Pyomo model file
- See `transport_min_pollution.py` in the working directory for the solver implementation.

---

This entry documents a classic integer programming model for transport optimization with both capacity and environmental constraints.
