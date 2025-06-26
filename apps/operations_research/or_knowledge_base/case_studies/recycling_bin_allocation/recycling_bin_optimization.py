# =============================================================================
# Recycling Bin Allocation Optimization Model - Five Element Format
# =============================================================================
# Objective:
#   Maximize total recycling collected: 25*x + 60*y
#
# Variables:
#   x : Number of small bins (integer >= 0)
#   y : Number of large bins (integer >= 0)
#
# Constraints:
#   1. 2*x + 5*y <= 100         (worker constraint)
#   2. x = 3*y                  (proportional constraint)
#   3. x >= 10                  (minimum small bins)
#   4. y >= 4                   (minimum large bins)
#   5. x, y >= 0 and integer
#
# Sets/Parameters:
#   model.s_coeff         : Worker time per small bin (2)
#   model.l_coeff         : Worker time per large bin (5)
#   model.worker_limit    : Total worker resource available (100)
#   model.proportion      : Proportion of small to large bins (3)
#   model.obj_s           : Recycling per small bin (25)
#   model.obj_l           : Recycling per large bin (60)
#   model.x_min           : Minimum small bins (10)
#   model.y_min           : Minimum large bins (4)
#
# Additional Notes:
#   All inputs are model Params, not raw constants (per rules).
#   The model uses Pyomo's integer variables and a solver such as CBC or GLPK.
# =============================================================================

def solve_recycling_optimization():
    from pyomo.environ import ConcreteModel, Var, Param, Constraint, Objective, SolverFactory, value, Integers, maximize, NonNegativeIntegers
    
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.s_coeff = Param(initialize=2)
    model.l_coeff = Param(initialize=5)
    model.worker_limit = Param(initialize=100)
    model.proportion = Param(initialize=3)
    model.obj_s = Param(initialize=25)
    model.obj_l = Param(initialize=60)
    model.x_min = Param(initialize=10)
    model.y_min = Param(initialize=4)

    # Variables - using bounds from Params
    model.x = Var(domain=NonNegativeIntegers, bounds=lambda m: (m.x_min, None))
    model.y = Var(domain=NonNegativeIntegers, bounds=lambda m: (m.y_min, None))

    # Constraints
    def worker_constraint(m):
        return m.s_coeff * m.x + m.l_coeff * m.y <= m.worker_limit
    model.worker_con = Constraint(rule=worker_constraint)
    
    def proportional_bins_constraint(m):
        return m.x == m.proportion * m.y
    model.proportional_con = Constraint(rule=proportional_bins_constraint)

    # Objective
    def obj_rule(m):
        return m.obj_s * m.x + m.obj_l * m.y
    model.total_recycling = Objective(rule=obj_rule, sense=maximize)

    # ===== Solver Execution =====
    # Try CBC, then GLPK
    solvers = ["cbc", "glpk"]
    solved = False
    last_exception = None
    for solver_name in solvers:
        try:
            solver = SolverFactory(solver_name)
            result = solver.solve(model, tee=False)
            solved = True
            break
        except Exception as e:
            last_exception = e
            continue

    if not solved:
        print("Solver failed to run. Exception:", last_exception)
        return {
            "status": "Solver failed",
            "termination": str(last_exception),
            "x": None,
            "y": None,
            "objective": None,
            "filename": "recycling_bin_optimization.py"
        }

    # ===== Result Reporting =====
    status = result.solver.status
    termination = result.solver.termination_condition

    if (termination == 'infeasible' or termination == 'no solution'):
        print("Problem is infeasible or no solution.")
        return {
            "status": str(status),
            "termination": str(termination),
            "x": None,
            "y": None,
            "objective": None,
            "filename": "recycling_bin_optimization.py"
        }

    x_val = value(model.x)
    y_val = value(model.y)
    obj_val = value(model.total_recycling)

    print("Solver status:", status)
    print("Termination reason:", termination)
    print("Optimal solution:")
    print(" - x (small bins):", x_val)
    print(" - y (large bins):", y_val)
    print("Maximized total recycling collected:", obj_val)
    return {
        "status": str(status),
        "termination": str(termination),
        "x": x_val,
        "y": y_val,
        "objective": obj_val,
        "filename": "recycling_bin_optimization.py"
    }
