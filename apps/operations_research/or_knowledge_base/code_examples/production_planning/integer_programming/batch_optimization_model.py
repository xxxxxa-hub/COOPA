# ===== Batch Production Optimization Model (Manager-Ready Summary) =====
# Objective:
#   Maximize total profit from regular and premium batches: 50*x + 30*y
# Variables:
#   x = number of regular batches (integer, 10 <= x <= 60)
#   y = number of premium batches (integer, 11 <= y <= 75)
# Constraints:
#   1) 50*x + 40*y <= 3000   (medicinal ingredient limit)
#   2) 40*x + 60*y <= 3500   (rehydration product limit)
#   3) x < y                 (regular batches less than premium batches)
# Sets/Parameters:
#   All coefficients and bounds are stored as model Params for clarity and future updates.
# Additional Notes:
#   Both variables must be non-negative integers.
#   All Pyomo code uses Params for bounds and coefficients.
#   Objective uses sense=maximize.
#   Model is documented and separated by section in ASCII-only comments.

def solve_batch_optimization():
    # ===== Imports =====
    from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, value, SolverFactory, Integers, maximize

    # ===== Model Definition =====
    model = ConcreteModel()

    # ===== Parameters =====
    model.c_x = Param(initialize=50)     # Objective coefficient for x
    model.c_y = Param(initialize=30)     # Objective coefficient for y
    model.a_x = Param(initialize=50)     # Medicinal constraint: x coefficient
    model.a_y = Param(initialize=40)     # Medicinal constraint: y coefficient
    model.b_x = Param(initialize=40)     # Rehydration constraint: x coefficient
    model.b_y = Param(initialize=60)     # Rehydration constraint: y coefficient

    model.med_limit = Param(initialize=3000)
    model.rehyd_limit = Param(initialize=3500)

    model.x_lower = Param(initialize=10)
    model.x_upper = Param(initialize=60)
    model.y_lower = Param(initialize=11)
    model.y_upper = Param(initialize=75)

    # ===== Variables =====
    def x_bounds(m):
        return (m.x_lower, m.x_upper)
    def y_bounds(m):
        return (m.y_lower, m.y_upper)

    model.x = Var(domain=Integers, bounds=x_bounds)
    model.y = Var(domain=Integers, bounds=y_bounds)

    # ===== Constraints =====
    def medicinal_constraint(m):
        return m.a_x * m.x + m.a_y * m.y <= m.med_limit
    model.medicinal = Constraint(rule=medicinal_constraint)

    def rehydration_constraint(m):
        return m.b_x * m.x + m.b_y * m.y <= m.rehyd_limit
    model.rehydration = Constraint(rule=rehydration_constraint)

    def x_less_than_y(m):
        return m.x <= m.y - 1
    model.ordering = Constraint(rule=x_less_than_y)

    # ===== Objective =====
    def profit_objective(m):
        return m.c_x * m.x + m.c_y * m.y
    model.obj = Objective(rule=profit_objective, sense=maximize)

    # ===== Solver Execution =====
    # Try GLPK first, fallback to CBC if not available
    result = None
    solver_used = None
    for solver_candidate in ['glpk', 'cbc']:
        try:
            solver = SolverFactory(solver_candidate)
            if solver.available():
                result = solver.solve(model)
                solver_used = solver_candidate
                break
        except Exception:
            continue

    if result is None:
        return {
            "status": "error",
            "termination_condition": "No MILP solver available (glpk/cbc not found).",
            "variables": {},
            "objective": None,
            "solver": None
        }

    status = str(result.solver.status)
    termination_condition = str(result.solver.termination_condition)

    # Extract variable values only if feasible/optimal
    if termination_condition.lower().startswith("optimal") or termination_condition.lower().startswith("feasible"):
        x_val = value(model.x)
        y_val = value(model.y)
        obj_val = value(model.obj)
        variables = {"x": x_val, "y": y_val}
    else:
        x_val = y_val = obj_val = None
        variables = {}

    return {
        "status": status,
        "termination_condition": termination_condition,
        "variables": variables,
        "objective": obj_val,
        "solver": solver_used
    }
