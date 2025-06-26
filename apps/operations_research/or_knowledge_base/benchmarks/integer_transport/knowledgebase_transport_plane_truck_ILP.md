# Tire Transportation Optimization: Planes vs. Trucks

## Problem Statement
An industrial tire company delivers large tires for equipment to remote engineering sites either by cargo planes or ultrawide trucks. Each cargo plane can transport 10 tires per trip and costs $1000. Each ultrawide truck can transport 6 tires per trip and costs $700. The company needs to transport at least 200 tires and has available $22,000. The number of plane trips cannot exceed the number of truck trips.

## Integer Linear Programming (ILP) Formulation

**Variables**:
- x: number of cargo plane trips (integer, >= 0)
- y: number of ultrawide truck trips (integer, >= 0)

**Objective**:  
Minimize x + y (total number of trips)

**Constraints**:
- 10x + 6y ¡Ý 200 (minimum tires transported)
- 1000x + 700y ¡Ü 22000 (cost constraint)
- x ¡Ü y (plane trips cannot exceed truck trips)

**Optimal solution found (2024):**
- Minimum number of trips: 26 (x=12 planes, y=14 trucks)
- All constraints respected.

## Pyomo Model
See: `ilp_plane_truck_model.py` for an implementation template.

---
*(Saved as part of benchmarked operations research problems, integer transport planning)*
