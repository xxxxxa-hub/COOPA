# =============================================================================
# Linear Programming Model: Minimize Fat Intake from Almonds and Cashews
# =============================================================================

# Five-Element Model Summary:
#
# Objective:
#     Minimize total fat intake from servings of almonds and cashews: 15*x + 12*y.
#
# Variables:
#     x: Servings of almonds (continuous, x >= 0).
#     y: Servings of cashews (continuous, y >= 0).
#
# Constraints:
#     1) 200*x + 300*y >= 10000   (calories)
#     2) 20*x + 25*y  >= 800      (protein)
#     3) x >= 2*y                 (almonds to cashews ratio)
#
# Sets/Parameters:
#     All coefficients and right hand sides (200, 300, 10000, 20, 25, 800, etc.) are scalar values represented as Pyomo Param objects.
#
# Additional Notes:
#     Integer requirements are relaxed; the model is solved as a continuous LP.
#     All code and comments are written with standard ASCII characters.
#     The script is expected to be self-contained and use an open-source solver such as GLPK.
# =============================================================================

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, Param, SolverFactory, value

def solve_nuts_lp():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Define parameters for coefficients and rhs as Pyomo Params
    model.fat_almonds = Param(initialize=15)
    model.fat_cashews = Param(initialize=12)
    model.cal_almonds = Param(initialize=200)
    model.cal_cashews = Param(initialize=300)
    model.cal_required = Param(initialize=10000)
    model.prot_almonds = Param(initialize=20)
    model.prot_cashews = Param(initialize=25)
    model.prot_required = Param(initialize=800)

    # Decision variables: Continuous (nonnegative)
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)

    # Constraints
    def calories_rule(m):
        return m.cal_almonds * m.x + m.cal_cashews * m.y >= m.cal_required
    model.calories = Constraint(rule=calories_rule)

    def protein_rule(m):
        return m.prot_almonds * m.x + m.prot_cashews * m.y >= m.prot_required
    model.protein = Constraint(rule=protein_rule)

    def almond_cashew_ratio_rule(m):
        return m.x >= 2 * m.y
    model.almond_cashew_ratio = Constraint(rule=almond_cashew_ratio_rule)

    # Objective: Minimize fat intake
    def obj_rule(m):
        return m.fat_almonds * m.x + m.fat_cashews * m.y
    model.obj = Objective(rule=obj_rule, sense=1)  # sense=1 for minimize

    # ===== Solver Execution =====
    solver = None
    possible_solvers = ['glpk', 'cbc']  # common LP solvers
    solver_name_used = None
    for s in possible_solvers:
        if SolverFactory(s).available():
            solver_name_used = s
            solver = SolverFactory(s)
            break
    if solver is None:
        return {
            'solver_found': False,
            'message': 'No suitable LP solver (glpk or cbc) is available. Please install a solver.'
        }

    results = solver.solve(model)
    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)
    # Solution extraction (only if solved optimally/infeasible)
    obj_value = None
    x_value = None
    y_value = None
    if hasattr(results.solver, 'termination_condition') and getattr(results.solver, 'termination_condition', None) == 'optimal':
        obj_value = value(model.obj)
        x_value = value(model.x)
        y_value = value(model.y)
    else:
        # Try to extract values if possible even if not strictly 'optimal'
        try:
            obj_value = value(model.obj)
            x_value = value(model.x)
            y_value = value(model.y)
        except:
            obj_value = None
            x_value = None
            y_value = None

    return {
        'solver_found': True,
        'solver_used': solver_name_used,
        'status': status,
        'termination': termination,
        'objective_value': obj_value,
        'x': x_value,
        'y': y_value,
        'model_script': 'lp_nuts_fat_min.py'
    }
