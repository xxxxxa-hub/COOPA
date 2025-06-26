# =============================================================================
# Integer Linear Programming Model: Banana-haters and Combo Packages Optimization
# =============================================================================
#
# Five-Element Model Summary:
#
# Objective:
#     Maximize total profit: 6*x + 7*y
# Variables:
#     x : integer >= 0, number of banana-haters packages
#     y : integer >= 0, number of combo packages
# Constraints:
#     6*x + 5*y <= 10      (apples)
#     6*y <= 20            (bananas)
#     30*x + 20*y <= 80    (grapes)
#     x, y >= 0 and integer
# Sets/Parameters:
#     All coefficients and right hand sides below defined as Param objects
# Additional Notes:
#     All data and variable domains explicitly set. Integer linear program. GLPK is used as the solver.
#
# =============================================================================

def solve_ilp():
    # ===== Imports =====
    from pyomo.environ import (
        ConcreteModel, Param, Var, Constraint, Objective, SolverFactory,
        NonNegativeIntegers, maximize, value
    )

    # ===== Model Definition =====
    model = ConcreteModel()

    # ---- Parameters ----
    model.profit_x = Param(initialize=6)
    model.profit_y = Param(initialize=7)

    model.apple_coeff_x = Param(initialize=6)
    model.apple_coeff_y = Param(initialize=5)
    model.apple_rhs = Param(initialize=10)

    model.banana_coeff_y = Param(initialize=6)
    model.banana_rhs = Param(initialize=20)

    model.grape_coeff_x = Param(initialize=30)
    model.grape_coeff_y = Param(initialize=20)
    model.grape_rhs = Param(initialize=80)

    # ---- Variables ----
    model.x = Var(domain=NonNegativeIntegers)
    model.y = Var(domain=NonNegativeIntegers)

    # ---- Constraints ----
    def apple_constraint_rule(m):
        return m.apple_coeff_x * m.x + m.apple_coeff_y * m.y <= m.apple_rhs
    model.apple_constraint = Constraint(rule=apple_constraint_rule)

    def banana_constraint_rule(m):
        return m.banana_coeff_y * m.y <= m.banana_rhs
    model.banana_constraint = Constraint(rule=banana_constraint_rule)

    def grape_constraint_rule(m):
        return m.grape_coeff_x * m.x + m.grape_coeff_y * m.y <= m.grape_rhs
    model.grape_constraint = Constraint(rule=grape_constraint_rule)

    # ---- Objective ----
    def obj_rule(m):
        return m.profit_x * m.x + m.profit_y * m.y
    model.obj = Objective(rule=obj_rule, sense=maximize)

    # ====== Solver Execution =====
    solver = SolverFactory('glpk')
    result = solver.solve(model)

    # ====== Value Extraction and Reporting ======
    status = str(result.solver.status)
    termination = str(result.solver.termination_condition)

    obj_val = value(model.obj)
    x_val = int(round(value(model.x)))
    y_val = int(round(value(model.y)))

    report = {
        'solver_status': status,
        'termination_condition': termination,
        'objective_value': obj_val,
        'x_value': x_val,
        'y_value': y_val,
    }

    # Also print the report to ensure it's available on stdout
    for k, v in report.items():
        print(f"{k}: {v}")

    return report
