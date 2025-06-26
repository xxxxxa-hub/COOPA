### Problem Type: Integer Programming - Resource Allocation, Capacity & Resource Constraints

#### Example: Ski Lift Installation Minimization

**Problem Description:**  
Given two types of machines with different capacities and resource usages (electricity/space/etc.), select the number of each to:
- Meet or exceed a minimum demand (capacity constraint)
- Not exceed a total resource limit (electricity, budget, etc.)
- Satisfy minimum or maximum count rules for each type

**Variables:**  
- x: Number of Type A machines (integer)
- y: Number of Type B machines (integer, y >= minB)

**Objective:**  
Minimize total machines: x + y

**Constraints:**  
- (a1)x + (b1)y >= Required Capacity (Minimum capacity constraint)
- (a2)x + (b2)y <= Resource Limit (e.g. max electricity/budget)
- y >= minB (e.g. minimum number of beginner-friendly machines)
- x, y >= 0, integer

**Pyomo Model Filename Example:**  
ski_lift_installation_model.py

**Key Takeaway:**  
This is a canonical form "minimum units to satisfy capacity and resource constraints" ILP. Formulate, then solve with standard integer programming techniques.

**Typical Applications:**  
- Machine or vehicle selection
- Facility or equipment installation
- Staff scheduling with resource limits

**See also:**  
- ski_lift_installation_model.py for runnable code example and formulation.

---

Directly generalize to any setting involving machine selection (multiple types/costs/capacities).
