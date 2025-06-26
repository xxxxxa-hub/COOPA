
# =================================================================
# Five-Element Model Summary
# =================================================================
# Objective:
#   Maximize total rice transported: 30*x + 70*y
#
# Variables:
#   x: Number of medium sized carts (integer, x >= 5)
#   y: Number of large sized carts (integer, y >= 5)
#
# Constraints:
#   1. Horse constraint: 2*x + 4*y <= 60
#   2. Cart ratio: x = 3*y
#   3. Lower bounds: x >= 5, y >= 5
#
# Sets/Parameters:
#   All coefficients, lower bounds, and ratio defined as model Params.
#
# Additional Notes:
#   - All data provided as Pyomo Param objects.
#   - Integer variables.
#   - Objective maximization.
#   - Solution values reported using value().
#   - Requires a MILP solver (GLPK or CBC).
# =================================================================

def solve_carts_model():
    from pyomo.environ import ConcreteModel, Param, Var, Constraint, Objective, SolverFactory, maximize, value, Integers

    # ============================
    # Model Definition
    # ============================
    model = ConcreteModel()

    # Parameters (as required by modeling standard)
    model.a_med = Param(initialize=2)    # coef for x in horse constraint
    model.a_lg = Param(initialize=4)     # coef for y in horse constraint
    model.c_med = Param(initialize=30)   # contribution of x in obj
    model.c_lg = Param(initialize=70)    # contribution of y in obj
    model.horse_cap = Param(initialize=60)  # RHS of horse constraint
    model.ratio_3 = Param(initialize=3)  # x = 3*y ratio
    model.x_lb = Param(initialize=5)     # lower bound for x
    model.y_lb = Param(initialize=5)     # lower bound for y

    # Variables (always use Param bounds)
    model.x = Var(domain=Integers, bounds=lambda m: (m.x_lb, None))
    model.y = Var(domain=Integers, bounds=lambda m: (m.y_lb, None))

    # Constraints
    def horse_constraint(m):
        return m.a_med * m.x + m.a_lg * m.y <= m.horse_cap
    model.horse_con = Constraint(rule=horse_constraint)

    def cart_ratio_constraint(m):
        return m.x == m.ratio_3 * m.y
    model.ratio_con = Constraint(rule=cart_ratio_constraint)

    # Objective
    def rice_objective(m):
        return m.c_med * m.x + m.c_lg * m.y
    model.obj = Objective(rule=rice_objective, sense=maximize)

    # ============================
    # Solver Execution
    # ============================
    # Try GLPK first, if not available try CBC, otherwise report error
    solver = None
    solver_status = None
    termination = None
    solution_found = False

    for sname in ["glpk", "cbc"]:
        try:
            solver = SolverFactory(sname)
            if solver.available(exception_flag=False):
                result = solver.solve(model)
                solver_status = str(result.solver.status)
                termination = str(result.solver.termination_condition)
                if (str(result.solver.termination_condition).lower() == 'optimal' or
                        str(result.solver.termination_condition).lower().startswith('feas')):
                    solution_found = True
                break
        except Exception as e:
            continue

    # ============================
    # Results Extraction
    # ============================
    from pyomo.environ import value
    # Build output dictionary
    output = {}
    output['solver_status'] = solver_status
    output['termination_condition'] = termination
    output['filename'] = 'cart_optimization_model.py'

    if solution_found:
        output['objective_value'] = value(model.obj)
        output['x'] = int(round(value(model.x)))
        output['y'] = int(round(value(model.y)))
    else:
        output['objective_value'] = None
        output['x'] = None
        output['y'] = None

    return output

# End of file
