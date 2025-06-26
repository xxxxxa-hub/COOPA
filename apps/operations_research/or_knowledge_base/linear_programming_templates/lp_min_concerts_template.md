# Minimizing Total Number of Concerts with Audience, Practice, and Proportion Constraints

## Problem statement (template)
A performer has two types of concerts: Type A and Type B. Each Type A event brings in `a` audience, requires `p_a` practice days; each Type B brings `b` audience, requires `p_b` practice days. At least `A_min` audience are needed in total, only `P_max` practice days are available, and at most fraction `f` of concerts may be of Type B.

### Variables
- x: Number of Type A concerts (continuous or integer)
- y: Number of Type B concerts (continuous or integer)

### Objective
Minimize: x + y

### Constraints
1. `a*x + b*y >= A_min` (Audience minimum)
2. `p_a*x + p_b*y <= P_max` (Practice days maximum)
3. Proportion: `y <= f*(x + y)`  
   Equivalent: `y <= f*x + f*y => (1-f)*y <= f*x => f*x - (1-f)*y >= 0`
   For f = 0.4: `2x - 3y >= 0`
4. x >= 0, y >= 0

#### Example ("Pop" and "R&B" concerts)
- Pop: 100 audience, 2 practice days
- R&B: 240 audience, 4 practice days
- Audience required: 10000
- Practice available: 180 days
- At most 40% R&B concerts

#### Canonical Pyomo model structure

#### Solution (continuous variables):
- Minimum concerts: 64.103
- x (pop): 38.462, y (R&B): 25.641

#### Notes
- For integer requirements, declare variables as Integers.
- Generalize coefficients for other event settings.
- Add additional business rules as needed.

---

This template is useful for any event-mix minimization with such audience, time, and composition bounds.
