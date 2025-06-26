
# =============================================================================
# Integer Linear Programming Model for Plane & Truck Logistics
#
# Five-Element Format:
#
# Objective:      Minimize the total number of trips (x + y)
#
# Variables:      x: Number of cargo plane trips         (integer, >= 0)
#                 y: Number of ultrawide truck trips     (integer, >= 0)
#
# Constraints:    10*x + 6*y >= 200      (minimum tonnage transported)
#                 1000*x + 700*y <= 22000  (total monetary cost at most 22,000)
#                 x <= y                  (no more planes than trucks)
#
# Sets/Parameters:
#                 All coefficients and bounds are modeled as Pyomo Params.
#
# Additional Notes:
#      - All code and comments are in standard ASCII. 
#      - Only Pyomo modeling constructs are used.
#      - Upper bounds for x, y set to max_trips_param (see below).
#      - Requires a MILP solver such as CBC or GLPK.
# =============================================================================

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, SolverFactory, Param, minimize, value

def solve_ilp():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.min_tonnage = Param(initialize=200)
    model.ton_per_plane = Param(initialize=10)
    model.ton_per_truck = Param(initialize=6)
    model.max_cost = Param(initialize=22000)
    model.cost_plane = Param(initialize=1000)
    model.cost_truck = Param(initialize=700)
    model.max_trips = Param(initialize=2200) # A very generous upper bound

    # Decision Variables
    model.x = Var(domain=NonNegativeIntegers, bounds=(0, model.max_trips))
    model.y = Var(domain=NonNegativeIntegers, bounds=(0, model.max_trips))

    # Constraints
    model.tonnage_constraint = Constraint(expr = model.ton_per_plane * model.x + model.ton_per_truck * model.y >= model.min_tonnage)
    model.cost_constraint = Constraint(expr = model.cost_plane * model.x + model.cost_truck * model.y <= model.max_cost)
    model.order_constraint = Constraint(expr = model.x <= model.y)

    # Objective
    model.total_trips = Objective(expr = model.x + model.y, sense=minimize)

    # ===== Solver Execution =====
    solver = None
    for s in ['cbc', 'glpk']:
        try:
            solver = SolverFactory(s)
            if solver.available():
                break
        except:
            continue
    if not solver or not solver.available():
        return {
            'solver_status': 'ERROR',
            'termination_condition': 'No MILP solver (cbc or glpk) available.',
            'objective_value': None,
            'x_val': None,
            'y_val': None,
            'filename': 'ilp_plane_truck_model.py'
        }
    result = solver.solve(model, tee=False)
    solver_status = result.solver.status
    termination_condition = str(result.solver.termination_condition)

    # ===== Value Extraction =====
    try:
        x_sol = int(round(value(model.x)))
        y_sol = int(round(value(model.y)))
        obj_val = int(round(value(model.total_trips)))
    except:
        x_sol = y_sol = obj_val = None

    return {
        'solver_status': str(solver_status),
        'termination_condition': str(termination_condition),
        'objective_value': obj_val,
        'x_val': x_sol,
        'y_val': y_sol,
        'filename': 'ilp_plane_truck_model.py'
    }
