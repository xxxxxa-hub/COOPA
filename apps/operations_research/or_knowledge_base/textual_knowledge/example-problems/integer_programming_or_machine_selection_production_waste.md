# Example: Integer Programming for Metal-Working Equipment Selection

## Problem Statement
A metal-working shop must select between two machine types (chop saws and steel cutters) to meet production and waste constraints, while minimizing the number of machines.

### Variables
- x: Number of chop saws (integer, x >= 0)
- y: Number of steel cutters (integer, y >= 0)

### Parameters
| Machine       | Steel processed (lbs/day) | Waste generated (units/day) |
|---------------|--------------------------|-----------------------------|
| Chop Saw      | 25                       | 25                          |
| Steel Cutter  | 5                        | 3                           |

- Demand: At least 520 lbs steel processed per day
- Waste: At most 400 units per day

### Mathematical Formulation

Minimize:  
 x + y

Subject to:  
 25x + 5y >= 520   (production constraint)  
 25x + 3y <= 400   (waste constraint)  
 x, y >= 0, integer

### Pyomo/Python Model (snippet)

### Solution (as per IP solver)
- x = 8 (chop saws)
- y = 64 (steel cutters)
- Minimum total machines: 72

Constraints satisfied:
- Production: 25*8 + 5*64 = 520 >= 520
- Waste: 25*8 + 3*64 = 392 <= 400

---

This formulation and workflow serve as a pattern for assigning/buying machines to meet minimum/maximum resource constraints with integer programming.
