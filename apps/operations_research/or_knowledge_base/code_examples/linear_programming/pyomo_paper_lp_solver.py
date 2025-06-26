# =============================================================================
# Linear Programming Model for Paper Production Optimization (Pyomo)
#
# FIVE-ELEMENT FORMAT
# -----------------------------------------------------------------------------
# 1. Objective:
#    Maximize total profit from daily production of graph paper and music paper.
#
# 2. Variables:
#    x : Number of reams of graph paper produced per day (continuous, x >= 0).
#    y : Number of reams of music paper produced per day (continuous, y >= 0).
#
# 3. Constraints:
#    - Printing machine time:    3*x + 1.5*y <= 350
#    - Scanning machine time:    5.5*x + 3*y <= 350
#    - Nonnegativity:            x >= 0, y >= 0
#
# 4. Sets/Parameters:
#    - c_x:      Profit per ream for graph paper (4)
#    - c_y:      Profit per ream for music paper (2.5)
#    - a1_x:     Printing time per ream graph paper (3)
#    - a1_y:     Printing time per ream music paper (1.5)
#    - b1:       Printing machine time limit (350)
#    - a2_x:     Scanning time per ream graph paper (5.5)
#    - a2_y:     Scanning time per ream music paper (3)
#    - b2:       Scanning machine time limit (350)
#    - lb_x, lb_y:   Lower bounds for x and y (both 0)
#
# 5. Additional Notes:
#    - All parameters are implemented as Pyomo Param objects.
#    - Variable bounds use Params (not raw literals).
#    - Model uses concrete values here, but could be easily adapted.
#    - The CBC or GLPK solver is used if available.
# =============================================================================

def solve_paper_lp():
    from pyomo.environ import (
        ConcreteModel, Var, Objective, Constraint, Param, NonNegativeReals,
        SolverFactory, maximize, value
    )
    import pyomo.environ as pyo

    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.c_x = Param(initialize=4.0)        # profit per ream, graph paper
    model.c_y = Param(initialize=2.5)        # profit per ream, music paper
    model.a1_x = Param(initialize=3.0)       # printing time per ream, graph paper
    model.a1_y = Param(initialize=1.5)       # printing time per ream, music paper
    model.b1   = Param(initialize=350.0)     # total printing machine time
    model.a2_x = Param(initialize=5.5)       # scanning time per ream, graph paper
    model.a2_y = Param(initialize=3.0)       # scanning time per ream, music paper
    model.b2   = Param(initialize=350.0)     # total scanning machine time

    model.lb_x = Param(initialize=0.0)       # lower bound for x
    model.lb_y = Param(initialize=0.0)       # lower bound for y

    # Variable upper bounds (can be set to None)
    model.ub_x = Param(initialize=None, mutable=True)        # upper bound for x
    model.ub_y = Param(initialize=None, mutable=True)        # upper bound for y

    # ===== Decision Variables =====
    model.x = Var(domain=NonNegativeReals, bounds=(model.lb_x, model.ub_x))
    model.y = Var(domain=NonNegativeReals, bounds=(model.lb_y, model.ub_y))

    # ===== Constraints =====
    def printing_constraint(m):
        return m.a1_x * m.x + m.a1_y * m.y <= m.b1
    model.printing_time = Constraint(rule=printing_constraint)

    def scanning_constraint(m):
        return m.a2_x * m.x + m.a2_y * m.y <= m.b2
    model.scanning_time = Constraint(rule=scanning_constraint)

    # ===== Objective =====
    def profit_rule(m):
        return m.c_x * m.x + m.c_y * m.y
    model.profit = Objective(rule=profit_rule, sense=maximize)

    # ===== Solver Execution =====
    # Try CBC first, then fallback to GLPK
    for solver_name in ['cbc', 'glpk']:
        try:
            solver = SolverFactory(solver_name)
            if not solver.available():
                continue
            results = solver.solve(model, tee=False)
            break
        except Exception as e:
            continue
    else:
        # No solver found: report error
        print("ERROR: No suitable solver (CBC, GLPK) was found in the environment.")
        return {
            "status": "error",
            "reason": "No suitable LP solver found."
        }

    # ===== Solution Reporting =====
    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)

    feasible = termination.lower() in [
        "optimal",
        "locallyOptimal".lower(),
        "feasible"
    ]

    result_dict = {
        "solver_status": status,
        "termination": termination,
        "filename": "paper_lp_solver.py"
    }

    if not feasible:
        print("WARNING: Model was not solved to optimality (status: {}, reason: {}).".format(status, termination))
        # If model is infeasible or unbounded, output diagnosis tips
        result_dict["warning"] = "Model not solved to optimality: status={}, termination={}.".format(status, termination)
        if "infeasible" in termination.lower():
            result_dict["possible_issue"] = "Infeasible: check constraints and resource availability."
        elif "unbounded" in termination.lower():
            result_dict["possible_issue"] = "Unbounded: check if all variables are properly constrained."
        return result_dict

    # Get variable values and the optimal profit
    x_value = value(model.x)
    y_value = value(model.y)
    optimal_profit = value(model.profit)

    print("=== PAPER PRODUCTION LP RESULTS ===")
    print("Solver status: " + status)
    print("Termination: " + termination)
    print("Optimal value (total profit): {:.4f}".format(optimal_profit))
    print("x (reams of graph paper): {:.4f}".format(x_value))
    print("y (reams of music paper): {:.4f}".format(y_value))
    print("Pyomo model file: paper_lp_solver.py")

    # For detailed inspection
    result_dict.update({
        "optimal_value": optimal_profit,
        "x": x_value,
        "y": y_value,
    })
    return result_dict
