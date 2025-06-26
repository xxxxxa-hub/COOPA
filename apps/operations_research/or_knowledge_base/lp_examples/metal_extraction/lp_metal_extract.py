# ===============================
# Linear Programming Model for Metal Extraction
# 
# Five-Element Model Summary:
# 
# Objective:
#   Maximize total metal extracted: 5*x + 9*y
# 
# Variables:
#   x: integer >= 0 (number of times Process J is performed)
#   y: integer >= 0 (number of times Process P is performed)
#
# Constraints:
#   8*x + 6*y <= 1500   (First resource constraint)
#   3*x + 5*y <= 1350   (Second resource constraint)
#   x >= 0, integer
#   y >= 0, integer
#
# Sets/Parameters:
#   Parameters for coefficients and right-hand sides are defined in the model.
#
# Additional Notes:
#   - Model solved as a Mixed-Integer Linear Program (MILP).
#   - Only open-source solvers (GLPK, CBC) are expected to be available.
#   - The script prints solver status, the optimal objective value, and variable values.
#   - All ASCII comments and code; no special characters.
# ===============================

from pyomo.environ import ConcreteModel, Var, Constraint, Objective, SolverFactory, Param, value, NonNegativeIntegers, maximize

def solve_lp():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Data as Params for full reproducibility
    model.c_x = Param(initialize=5)   # Objective coefficient for x
    model.c_y = Param(initialize=9)   # Objective coefficient for y

    model.a1_x = Param(initialize=8)  # Constraint 1 coefficient for x
    model.a1_y = Param(initialize=6)  # Constraint 1 coefficient for y
    model.b1 = Param(initialize=1500) # Constraint 1 RHS

    model.a2_x = Param(initialize=3)  # Constraint 2 coefficient for x
    model.a2_y = Param(initialize=5)  # Constraint 2 coefficient for y
    model.b2 = Param(initialize=1350) # Constraint 2 RHS

    # Lower bounds for variables (using Params for compliance)
    model.lb_x = Param(initialize=0)
    model.lb_y = Param(initialize=0)

    # Decision variables (must be integer and >= 0)
    model.x = Var(domain=NonNegativeIntegers, bounds=lambda m: (value(m.lb_x), None))
    model.y = Var(domain=NonNegativeIntegers, bounds=lambda m: (value(m.lb_y), None))

    # Constraints
    def resource1_rule(m):
        return m.a1_x * m.x + m.a1_y * m.y <= m.b1
    model.resource1 = Constraint(rule=resource1_rule)

    def resource2_rule(m):
        return m.a2_x * m.x + m.a2_y * m.y <= m.b2
    model.resource2 = Constraint(rule=resource2_rule)

    # Objective function
    model.obj = Objective(expr = model.c_x * model.x + model.c_y * model.y, sense=maximize)

    # ===== Solver Execution =====
    # Try to use GLPK, fallback to CBC if available.
    solvers_tried = []
    solver = None
    for sname in ["glpk", "cbc"]:
        try:
            candidate = SolverFactory(sname)
            if candidate.available():
                solver = candidate
                solvers_tried.append(sname)
                break
        except Exception:
            pass
        solvers_tried.append(sname + "_not_available")
    if solver is None:
        print("No suitable MILP solver (GLPK or CBC) is available in this environment.")
        return {
            "status": "No solver",
            "reason": "GLPK and CBC could not be found",
            "tried": solvers_tried
        }

    results = solver.solve(model)
    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)

    # ===== Results Extraction =====
    print("="*60)
    print("Solver status:", status)
    print("Termination condition:", termination)
    if status == "ok" and termination.lower() in ["optimal", "feasible", "feasible solution"]:
        optimal_value = value(model.obj)
        x_val = value(model.x)
        y_val = value(model.y)
        print("Optimal objective value (total metal extracted):", optimal_value)
        print("x (Process J) =", x_val)
        print("y (Process P) =", y_val)
    else:
        optimal_value = None
        x_val = None
        y_val = None
        print("No optimal solution found.")
    print("Pyomo model file: lp_metal_extract.py")
    print("Solver tried:", solvers_tried)
    print("="*60)
    return {
        "status": status,
        "termination": termination,
        "objective_value": optimal_value,
        "x": x_val,
        "y": y_val,
        "file": "lp_metal_extract.py",
        "solvers_tried": solvers_tried
    }

