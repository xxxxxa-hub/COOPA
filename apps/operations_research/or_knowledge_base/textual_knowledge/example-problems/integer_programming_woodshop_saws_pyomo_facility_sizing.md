### Integer Programming Example: Minimize Number of Saws (Woodshop Problem)

**Problem statement:**
A woodshop can purchase two types of saws, a miter saw and a circular saw:
- Miter saw: cuts 50 planks/day, produces 60 units sawdust/day.
- Circular saw: cuts 70 planks/day, produces 100 units sawdust/day.
- Must cut at least 1500 planks/day.
- Must not produce more than 2000 units sawdust/day.
- Decision variables (integer): x = miter saws, y = circular saws.
- Objective: Minimize x + y (total saws).

**Mathematical Model:**
Minimize x + y
Subject to:
    50x + 70y >= 1500        (plank constraint)
    60x + 100y <= 2000       (sawdust constraint)
    x >= 0, y >= 0, integers

**Pyomo implementation best practices:**
- Use Var(..., domain=NonNegativeIntegers) for x and y.
- Set up data as Pyomo Params for coefficients and RHS values.
- Use GLPK or CBC as open-source ILP solvers.
- Check solver status/termination for optimal results.
- Artificial upper bounds (e.g., 1000) may be used for certainty of feasibility.

**Optimal solution (computed):**
- Minimum number of saws: 26
- Number of miter saws: 15
- Number of circular saws: 11

**Script location in past run:** ilp_miter_circular_saws.py

**Tags:** integer programming, woodshop, saws, pyomo, facility sizing.
