# LP Pattern: Manufacturing Mix - Minimize Total Time

## Problem Pattern Summary
This pattern addresses linear programming (LP) problems where a manufacturing facility must determine the optimal mix of products to produce, such that total processing (or work) time is minimized. Each product requires a certain amount of production time per unit, and the facility must satisfy demand and resource constraints.

**Common applications:**
- Scheduling jobs on machines
- Minimizing makespan (completion time)
- Optimizing workforce allocation

---

## Typical Mathematical Formulation

**Sets:**
- Let `P` be the set of products (or jobs).

**Parameters:**
- `t[p]`: Unit processing time for product `p`.
- `d[p]`: Minimum demand for product `p`.
- `cap`: Total available processing time.

**Decision variables:**
- `x[p]`: Number of units of product `p` to produce (continuous or integer, depending on context).

**Objective:**
Minimize total processing time:

    minimize    sum(t[p] * x[p] for p in P)

**Subject to:**
- Demand:  x[p] >= d[p]    for all p in P
- Capacity: sum(t[p] * x[p] for p in P) <= cap
- Non-negativity: x[p] >= 0    for all p in P

---

## Pyomo Template

```python
from pyomo.environ import *

model = ConcreteModel()

# Sets
model.P = Set(initialize=[...])  # list of product/job names

# Parameters
model.t = Param(model.P, initialize={...})   # processing time per unit
model.d = Param(model.P, initialize={...})   # minimum demand per product
model.cap = Param(initialize=...)            # total available processing time

# Decision variables
model.x = Var(model.P, domain=NonNegativeReals)  # or NonNegativeIntegers

# Objective: Minimize total processing time
model.obj = Objective(expr=sum(model.t[p] * model.x[p] for p in model.P), sense=minimize)

# Constraints
model.demand = ConstraintList()
for p in model.P:
    model.demand.add(model.x[p] >= model.d[p])

model.capacity = Constraint(expr=sum(model.t[p] * model.x[p] for p in model.P) <= model.cap)
```

---

## Best Practices
- **Define Inputs Clearly:** List all products/jobs explicitly; clearly specify parameters for each.
- **Data Validation:** Check for typos or mismatched set/member names.
- **Scalability:** For problems with many products/jobs, use data files (e.g., CSV) for set and parameter initialization.
- **Variable Domains:** Use `NonNegativeReals` for continuous LP; if integer-valued production is necessary, use `NonNegativeIntegers`.
- **Interpret Solution:** The solution gives the optimal product mix that meets demand at the lowest total processing time, without exceeding capacity.

---

## When to Use This Pattern
- You need to minimize time or makespan, not cost/profit.
- Resource (time) constraints and minimum demand must be met.
- Problem structure is linear (no nonlinearities, no binaries or sequenced tasks).

---

## Related Patterns
- [Manufacturing Mix: Maximize Profit](../lp_manufacturing_mix_max_profit.md)
- [Job Shop Scheduling (discrete sequencing)](../job_shop_scheduling.md)

