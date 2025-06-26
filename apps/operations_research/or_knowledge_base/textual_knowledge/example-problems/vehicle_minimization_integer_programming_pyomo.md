# Vehicle Minimization Integer Programming Example (Pyomo)

## Description
This script provides a Pyomo integer programming model for minimizing the number of vehicles (of two types, e.g., sedans and buses) needed by a company, subject to customer capacity requirements and pollution limits.

- **Decision variables:** integer counts of each vehicle type (x: sedans, y: buses)
- **Objective:** minimize x + y
- **Constraints:**
    1. 50x + 250y >= 4600 (customer/day capacity)
    2. 10x + 40y <= 800 (daily pollution max)
    3. x, y >= 0 and integer
- **Specific instance:**
    - 50 seats/sedan
    - 250 seats/bus
    - sedan pollution 10
    - bus pollution 40
    - at least 4600 tourists/day
    - at most 800 pollution units/day

This model can be reused or adapted for similar fleet/combinatorial optimization scenarios.

---

```python
# ===================================================================================
# Integer Linear Programming Model for Vehicle Assignment Problem (Pyomo, ASCII-only)
# ===================================================================================
#
# Five-Element Model Summary
# --------------------------
# Objective:
#   Minimize the total number of vehicles (x + y).
# Variables:
#   x: Number of type 1 vehicles (integer, >=0, <=100).
#   y: Number of type 2 vehicles (integer, >=0, <=100).
# Constraints:
#   1. 50*x + 250*y >= 4600   (supply/demand constraint)
#   2. 10*x + 40*y <= 800     (capacity constraint)
#   3. x >= 0, y >= 0
#   4. x and y are integers
# Sets/Parameters:
#   - a1 = 50      # amount per type 1 vehicle in 1st constraint
#   - a2 = 250     # amount per type 2 vehicle in 1st constraint
#   - b1 = 4600    # RHS minimum for 1st constraint
#   - c1 = 10      # amount per type 1 vehicle in 2nd constraint
#   - c2 = 40      # amount per type 2 vehicle in 2nd constraint
#   - b2 = 800     # RHS maximum for 2nd constraint
# Additional Notes:
#   - All variables and bounds are implemented as model.Param where required.
#   - Solution is extracted, status and values reported.
#   - Upper bounds 100 chosen for x, y (conservative, not restrictive).
#   - Model uses GLPK/MIP solver if available.
#
# ========================
# ===== Model Code =======
# ========================

from pyomo.environ import ConcreteModel, Var, Param, Objective, Constraint, SolverFactory, value, NonNegativeIntegers

def solve_model():
    # ----- Model Definition -----
    model = ConcreteModel()
    
    # Parameters for constraint coefficients and bounds
    model.a1 = Param(initialize=50)
    model.a2 = Param(initialize=250)
    model.c1 = Param(initialize=10)
    model.c2 = Param(initialize=40)
    model.b1 = Param(initialize=4600)
    model.b2 = Param(initialize=800)
    model.x_max = Param(initialize=100)  # conservative upper bound
    model.y_max = Param(initialize=100)

    # ----- Decision Variables -----
    model.x = Var(domain=NonNegativeIntegers, bounds=(0, model.x_max))
    model.y = Var(domain=NonNegativeIntegers, bounds=(0, model.y_max))

    # ----- Objective Function -----
    model.obj = Objective(expr=model.x + model.y, sense=1)  # sense=1 <=> minimize

    # ----- Constraints -----
    def constraint1_rule(m):
        return m.a1 * m.x + m.a2 * m.y >= m.b1
    model.cons1 = Constraint(rule=constraint1_rule)

    def constraint2_rule(m):
        return m.c1 * m.x + m.c2 * m.y <= m.b2
    model.cons2 = Constraint(rule=constraint2_rule)

    # ----- Solver Execution -----
    # Use CBC if available; otherwise try GLPK
    status = None
    termination = None
    objval = None
    xval = None
    yval = None
    feasible = True
    used_solver = None
    for solvername in ['cbc','glpk']:
        if SolverFactory(solvername).available():
            opt = SolverFactory(solvername)
            used_solver = solvername
            break
    else:
        # No solver found
        return {
            'status': 'ERROR',
            'termination': 'No integer solver (cbc or glpk) is available.',
            'objval': None,
            'x': None,
            'y': None,
            'feasible': False,
            'filename': '{}'.format(__file__),
            'solver': None
        }
    result = opt.solve(model)
    status = result.solver.status
    termination = result.solver.termination_condition

    # Check infeasibility
    if str(termination).lower() in ['infeasible', 'no solution', 'other']:
        feasible = False
        return {
            'status': str(status),
            'termination': str(termination),
            'objval': None,
            'x': None,
            'y': None,
            'feasible': False,
            'filename': '{}'.format(__file__),
            'solver': used_solver
        }

    xval = int(round(value(model.x)))
    yval = int(round(value(model.y)))
    objval = int(round(value(model.obj)))
    return {
        'status': str(status),
        'termination': str(termination),
        'objval': objval,
        'x': xval,
        'y': yval,
        'feasible': feasible,
        'filename': '{}'.format(__file__),
        'solver': used_solver
    }
```
