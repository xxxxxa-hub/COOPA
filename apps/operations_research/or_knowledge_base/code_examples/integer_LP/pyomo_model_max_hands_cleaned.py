# =============================================================================
# Integer Programming Model for Maximum Hands Cleaned ¨C Five-Element Format
# =============================================================================
#
# Objective: 
#     Maximize total number of hands that can be cleaned: 30*x + 20*y
#
# Variables:
#     x : integer, number of units of type x, 0 <= x <= xmax
#     y : integer, number of units of type y, y >= ymin, no explicit upper bound
#
# Constraints:
#     1. 40*x + 60*y <= rhs1
#     2. 50*x + 40*y <= rhs2
#     3. y - x >= gap (where gap=1)
#     4. x <= xmax (where xmax=30)
#     5. x >= 0
#     6. y >= 0
#
# Sets/Parameters:
#     c1_x = 40, c1_y = 60, rhs1 = 2000
#     c2_x = 50, c2_y = 40, rhs2 = 2100
#     coef_x = 30, coef_y = 20
#     gap = 1
#     xmax = 30
#
# Additional Notes:
#     All variables are required to be integer-valued (x, y in integers).
#     Model will be solved by Pyomo using an open-source MILP solver if available.
#     All data and variable bounds are provided as Pyomo Param.
#
# =============================================================================

from pyomo.environ import (
    ConcreteModel, Var, Objective, Constraint,
    NonNegativeIntegers, maximize, SolverFactory, Param, value
)

def solve_ip_model():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    # Objective coefficients
    model.coef_x = Param(initialize=30)
    model.coef_y = Param(initialize=20)

    # Constraint coefficients and RHS
    model.c1_x = Param(initialize=40)
    model.c1_y = Param(initialize=60)
    model.rhs1 = Param(initialize=2000)

    model.c2_x = Param(initialize=50)
    model.c2_y = Param(initialize=40)
    model.rhs2 = Param(initialize=2100)

    model.gap = Param(initialize=1)
    model.xmax = Param(initialize=30)

    # ===== Variable Definitions =====
    def x_bounds_rule(m):
        return (0, m.xmax)
    model.x = Var(domain=NonNegativeIntegers, bounds=x_bounds_rule)
    model.y = Var(domain=NonNegativeIntegers)

    # ===== Constraints =====
    def linear_con1(m):
        return m.c1_x * m.x + m.c1_y * m.y <= m.rhs1
    model.con1 = Constraint(rule=linear_con1)

    def linear_con2(m):
        return m.c2_x * m.x + m.c2_y * m.y <= m.rhs2
    model.con2 = Constraint(rule=linear_con2)

    def y_minus_x_gap(m):
        return m.y - m.x >= m.gap
    model.con3 = Constraint(rule=y_minus_x_gap)

    # x bound handled in bounds; y bound handled by domain (NonNegative)
    # ===== Objective Function =====
    def obj_rule(m):
        return m.coef_x * m.x + m.coef_y * m.y
    model.obj = Objective(rule=obj_rule, sense=maximize)

    # ===== Solver Execution =====
    # Try CBC, then GLPK if CBC is unavailable
    solvers_to_try = ['cbc', 'glpk']
    results = None
    solver_used = None
    for solver in solvers_to_try:
        try:
            opt = SolverFactory(solver)
            if opt is not None and opt.available():
                results = opt.solve(model)
                solver_used = solver
                break
        except Exception as e:
            continue

    if results is None:
        return "No suitable MILP solver (CBC or GLPK) is available in the environment. Please install CBC or GLPK."

    # ===== Results Extraction =====
    status = results.solver.status if hasattr(results.solver, 'status') else str(results)
    termination = results.solver.termination_condition if hasattr(results.solver, 'termination_condition') else "Unknown"

    is_feasible = (str(termination).lower() == "optimal" or str(termination).lower() == "feasible")

    # Prepare result string
    output = []
    output.append("===== Pyomo Integer Program Results =====")
    output.append("Solver used: %s" % solver_used)
    output.append("Solver status: %s" % status)
    output.append("Termination condition: %s" % termination)
    if is_feasible:
        x_val = int(round(value(model.x)))
        y_val = int(round(value(model.y)))
        obj_val = value(model.obj)
        output.append("Optimal variable values:")
        output.append("  x = %d" % x_val)
        output.append("  y = %d" % y_val)
        output.append("Objective value (hands cleaned): %.0f" % obj_val)
    else:
        output.append("Model is infeasible, unbounded, or no feasible integer solution found.")
        x_val = None
        y_val = None
        obj_val = None
    output.append("pyomo_model_max_hands_cleaned.py")

    # Package as a dictionary for use by caller
    return {
        "solver": solver_used,
        "status": str(status),
        "termination": str(termination),
        "x": x_val,
        "y": y_val,
        "objective": obj_val,
        "output_lines": output,
        "filename": "pyomo_model_max_hands_cleaned.py",
        "feasible": is_feasible
    }
