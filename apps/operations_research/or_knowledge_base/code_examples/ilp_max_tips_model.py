
# =============================================================================
# INTEGER LINEAR PROGRAM FOR MAXIMIZING TOTAL TIPS
#
# Five-Element Model Summary:
#
# Objective:
#   Maximize total tips: 50*x + 43*y
#
# Variables:
#   x: Integer, x >= 0
#   y: Integer, y >= 5
#
# Constraints:
#   1. x + y <= 40
#   2. 5x + 6y <= 230
#   3. 10x + 7y >= 320
#   4. y >= 5
#   5. x >= 0
#
# Sets/Parameters:
#   - All coefficients and right-hand-sides defined as Params.
#
# Additional Notes:
#   - All model data is encoded via Pyomo Params.
#   - All code, comments, and outputs are in standard ASCII.
# =============================================================================
from pyomo.environ import (
    ConcreteModel,
    Param,
    Var,
    Constraint,
    Objective,
    Integers,
    SolverFactory,
    value,
    maximize,
)

def solve_ilp_max_tips():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.c1 = Param(initialize=50)
    model.c2 = Param(initialize=43)
    model.a1 = Param(initialize=1)
    model.a2 = Param(initialize=1)
    model.cap1 = Param(initialize=40)
    model.b1 = Param(initialize=5)
    model.b2 = Param(initialize=6)
    model.cap2 = Param(initialize=230)
    model.d1 = Param(initialize=10)
    model.d2 = Param(initialize=7)
    model.rhs3 = Param(initialize=320)
    model.x_lower = Param(initialize=0)
    model.y_lower = Param(initialize=5)

    # Variables
    model.x = Var(within=Integers, bounds=(model.x_lower, None))
    model.y = Var(within=Integers, bounds=(model.y_lower, None))

    # Constraints
    def cons1(m):
        return m.a1*m.x + m.a2*m.y <= m.cap1
    model.cons1 = Constraint(rule=cons1)

    def cons2(m):
        return m.b1*m.x + m.b2*m.y <= m.cap2
    model.cons2 = Constraint(rule=cons2)

    def cons3(m):
        return m.d1*m.x + m.d2*m.y >= m.rhs3
    model.cons3 = Constraint(rule=cons3)

    # Objective
    model.obj = Objective(expr=model.c1*model.x + model.c2*model.y, sense=maximize)

    # ===== Solver Execution =====
    result = {}
    try:
        solver = None
        used_solver = ""
        if SolverFactory("cbc").available():
            solver = SolverFactory("cbc")
            used_solver = "cbc"
        elif SolverFactory("glpk").available():
            solver = SolverFactory("glpk")
            used_solver = "glpk"
        else:
            result["solver_status"] = "No suitable solver (cbc/glpk) found."
            result["solver_termination"] = None
            result["obj_value"] = None
            result["x_val"] = None
            result["y_val"] = None
            result["solver_name"] = ""
            result["script_file"] = "ilp_max_tips_model.py"
            return result

        sol = solver.solve(model)
        result["solver_name"] = used_solver
        result["solver_status"] = str(sol.solver.status)
        result["solver_termination"] = str(sol.solver.termination_condition)

        if str(sol.solver.termination_condition).lower() in ["optimal","integer optimal solution"]:
            result["obj_value"] = int(round(value(model.obj)))
            result["x_val"] = int(round(value(model.x)))
            result["y_val"] = int(round(value(model.y)))
        elif str(sol.solver.termination_condition).lower() == "infeasible":
            result["obj_value"] = None
            result["x_val"] = None
            result["y_val"] = None
        else:
            result["obj_value"] = None
            result["x_val"] = None
            result["y_val"] = None

    except Exception as e:
        result["solver_status"] = "Error: " + str(e)
        result["solver_termination"] = None
        result["obj_value"] = None
        result["x_val"] = None
        result["y_val"] = None
        result["solver_name"] = used_solver if "used_solver" in locals() else ""
    result["script_file"] = "ilp_max_tips_model.py"
    return result
