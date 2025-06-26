# transport_optimizer.py
# ======================= MODEL FIVE-ELEMENT SUMMARY =======================
# Objective:
#     Minimize the total number of workers required for transportation.
#
# Variables:
#     x: Integer. Number of carts used. x >= 0
#     y: Integer. Number of trolleys used. y >= 12
#
# Constraints:
#     1. Minimum number of trolleys:               y >= 12
#     2. Total transport rate (kg/min):            5*x + 7*y >= 100
#     3. Trolley share constraint (linearized):    x >= 2.1*y
#
# Sets/Parameters:
#     - Carts: Each cart transports 5 kg/min, requires 2 workers.
#     - Trolleys: Each trolley transports 7 kg/min, requires 4 workers.
#     - At least 12 trolleys must be used.
#     - No more than 40% of total transportation by trolleys.
#     - Total transport rate required: >=100 kg/min.
#
# Additional notes:
#     - All variables are integer and nonnegative.
#     - The third constraint (trolley share) is derived from:
#         7*y <= 0.4*(5*x + 7*y) --> x >= 2.1*y
#     - All model data are defined as Pyomo Params.
#     - Output will include model script name, solver status, objective value, and optimal variables.
# ===========================================================================

from pyomo.environ import ConcreteModel, Var, Param, Constraint, Objective, SolverFactory, NonNegativeIntegers, value

def solve_transport_optimization():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.cart_rate = Param(initialize=5)
    model.trolley_rate = Param(initialize=7)
    model.cart_workers = Param(initialize=2)
    model.trolley_workers = Param(initialize=4)
    model.min_trolleys = Param(initialize=12)
    model.min_total_rate = Param(initialize=100)
    model.trolley_share_factor = Param(initialize=2.1)  # from share constraint x >= 2.1*y

    # Decision variables
    model.x = Var(domain=NonNegativeIntegers)  # carts
    model.y = Var(domain=NonNegativeIntegers)  # trolleys

    # ===== Constraints =====

    # 1. Minimum number of trolleys
    def trolleys_min_rule(m):
        return m.y >= m.min_trolleys
    model.min_trolleys_con = Constraint(rule=trolleys_min_rule)

    # 2. Total transport rate
    def rate_rule(m):
        return m.cart_rate * m.x + m.trolley_rate * m.y >= m.min_total_rate
    model.total_rate_con = Constraint(rule=rate_rule)

    # 3. Trolley share constraint (x >= 2.1*y)
    def trolley_share_rule(m):
        return m.x >= m.trolley_share_factor * m.y
    model.trolley_share_con = Constraint(rule=trolley_share_rule)

    # ===== Objective Function =====
    def obj_rule(m):
        return m.cart_workers * m.x + m.trolley_workers * m.y
    model.obj = Objective(rule=obj_rule, sense=1)  # sense=1 for minimize

    # ===== Solver Execution =====
    # Try CBC first, fallback to GLPK if necessary.
    for solver_name in ['cbc', 'glpk']:
        try:
            solver = SolverFactory(solver_name)
            if not solver.available():
                continue
            solve_result = solver.solve(model, tee=False)
            break
        except Exception as e:
            continue
    else:
        return {
            'status': 'error',
            'termination_condition': 'No suitable solver available',
            'filename': 'transport_optimizer.py'
        }

    # ===== Results Extraction =====
    status = solve_result.solver.status if hasattr(solve_result, 'solver') else 'Unknown'
    termination = solve_result.solver.termination_condition if hasattr(solve_result, 'solver') else 'Unknown'
    obj_value = value(model.obj)
    x_val = value(model.x)
    y_val = value(model.y)

    return {
        'status': str(status),
        'termination_condition': str(termination),
        'objective': obj_value,
        'x': x_val,
        'y': y_val,
        'filename': 'transport_optimizer.py'
    }
