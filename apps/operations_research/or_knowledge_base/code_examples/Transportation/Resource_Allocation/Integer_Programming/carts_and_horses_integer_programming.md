
# Problem: Carts and Horses Integer Programming

A factory transports rice to the city using medium and large horse-drawn carts.
- Medium cart: 2 horses, carries 30 kg rice.
- Large cart: 4 horses, carries 70 kg rice.
- 60 horses available.
- Medium carts must be 3 times the number of large carts.
- At least 5 of each cart.

Variables:
x = number of medium carts (integer, x >= 5)
y = number of large carts  (integer, y >= 5)

Constraints:
1. 2x + 4y <= 60
2. x = 3y

Objective:
Maximize 30x + 70y

Optimal solution:
x = 18, y = 6, maximum rice transported = 960 kg.


---

# Pyomo Model

```python
1:
2:# =================================================================
3:# Five-Element Model Summary
4:# =================================================================
5:# Objective:
6:#   Maximize total rice transported: 30*x + 70*y
7:#
8:# Variables:
9:#   x: Number of medium sized carts (integer, x >= 5)
10:#   y: Number of large sized carts (integer, y >= 5)
11:#
12:# Constraints:
13:#   1. Horse constraint: 2*x + 4*y <= 60
14:#   2. Cart ratio: x = 3*y
15:#   3. Lower bounds: x >= 5, y >= 5
16:#
17:# Sets/Parameters:
18:#   All coefficients, lower bounds, and ratio defined as model Params.
19:#
20:# Additional Notes:
21:#   - All data provided as Pyomo Param objects.
22:#   - Integer variables.
23:#   - Objective maximization.
24:#   - Solution values reported using value().
25:#   - Requires a MILP solver (GLPK or CBC).
26:# =================================================================
27:
28:def solve_carts_model():
29:    from pyomo.environ import ConcreteModel, Param, Var, Constraint, Objective, SolverFactory, maximize, value, Integers
30:
31:    # ============================
32:    # Model Definition
33:    # ============================
34:    model = ConcreteModel()
35:
36:    # Parameters (as required by modeling standard)
37:    model.a_med = Param(initialize=2)    # coef for x in horse constraint
38:    model.a_lg = Param(initialize=4)     # coef for y in horse constraint
39:    model.c_med = Param(initialize=30)   # contribution of x in obj
40:    model.c_lg = Param(initialize=70)    # contribution of y in obj
41:    model.horse_cap = Param(initialize=60)  # RHS of horse constraint
42:    model.ratio_3 = Param(initialize=3)  # x = 3*y ratio
43:    model.x_lb = Param(initialize=5)     # lower bound for x
44:    model.y_lb = Param(initialize=5)     # lower bound for y
45:
46:    # Variables (always use Param bounds)
47:    model.x = Var(domain=Integers, bounds=lambda m: (m.x_lb, None))
48:    model.y = Var(domain=Integers, bounds=lambda m: (m.y_lb, None))
49:
50:    # Constraints
51:    def horse_constraint(m):
52:        return m.a_med * m.x + m.a_lg * m.y <= m.horse_cap
53:    model.horse_con = Constraint(rule=horse_constraint)
54:
55:    def cart_ratio_constraint(m):
56:        return m.x == m.ratio_3 * m.y
57:    model.ratio_con = Constraint(rule=cart_ratio_constraint)
58:
59:    # Objective
60:    def rice_objective(m):
61:        return m.c_med * m.x + m.c_lg * m.y
62:    model.obj = Objective(rule=rice_objective, sense=maximize)
63:
64:    # ============================
65:    # Solver Execution
66:    # ============================
67:    # Try GLPK first, if not available try CBC, otherwise report error
68:    solver = None
69:    solver_status = None
70:    termination = None
71:    solution_found = False
72:
73:    for sname in ["glpk", "cbc"]:
74:        try:
75:            solver = SolverFactory(sname)
76:            if solver.available(exception_flag=False):
77:                result = solver.solve(model)
78:                solver_status = str(result.solver.status)
79:                termination = str(result.solver.termination_condition)
80:                if (str(result.solver.termination_condition).lower() == 'optimal' or
81:                        str(result.solver.termination_condition).lower().startswith('feas')):
82:                    solution_found = True
83:                break
84:        except Exception as e:
85:            continue
86:
87:    # ============================
88:    # Results Extraction
89:    # ============================
90:    from pyomo.environ import value
91:    # Build output dictionary
92:    output = {}
93:    output['solver_status'] = solver_status
94:    output['termination_condition'] = termination
95:    output['filename'] = 'cart_optimization_model.py'
96:
97:    if solution_found:
98:        output['objective_value'] = value(model.obj)
99:        output['x'] = int(round(value(model.x)))
100:        output['y'] = int(round(value(model.y)))
101:    else:
102:        output['objective_value'] = None
103:        output['x'] = None
104:        output['y'] = None
105:
106:    return output
107:
108:# End of file

```