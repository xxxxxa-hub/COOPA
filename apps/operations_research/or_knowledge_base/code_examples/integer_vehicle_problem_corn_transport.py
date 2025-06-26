# =============================================================================
# Pyomo Model for Integer Programming Problem: Tractor and Car Shipment
#
# Five-Element Model Summary
#
# Objective:
#   Minimize the total number of vehicles (tractors + cars) required to ship at least 500kg.
#
# Variables:
#   x: Number of tractors (integer, x >= 0)
#   y: Number of cars (integer, y >= 0)
#
# Constraints:
#   1) 40*x + 20*y >= 500                 # Total shipped weight must be at least 500kg
#   2) y >= 2*x                           # Cars at least twice the tractors
#   3) x >= 0 and y >= 0                  # Non-negativity, integrality
#
# Sets/Parameters:
#   model.ship_min_weight = 500           # At least 500kg must be shipped
#   model.tractor_weight = 40             # 1 tractor carries 40kg
#   model.car_weight = 20                 # 1 car carries 20kg
#
# Additional Notes:
# - All constants are specified using model.Params.
# - Variables are restricted to integer non-negative values.
# - The model is solved using the default solver available to Pyomo.
# - All code, comments, and documentation use ASCII only.
# =============================================================================

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, NonNegativeIntegers, SolverFactory, value

def solve_integer_vehicle_problem():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.tractor_weight = Param(initialize=40)
    model.car_weight = Param(initialize=20)
    model.ship_min_weight = Param(initialize=500)

    # Variables
    model.x = Var(domain=NonNegativeIntegers)  # Number of tractors
    model.y = Var(domain=NonNegativeIntegers)  # Number of cars

    # Constraints
    # Weight constraint: 40x + 20y >= 500
    def weight_rule(m):
        return (m.tractor_weight*m.x + m.car_weight*m.y) >= m.ship_min_weight
    model.weight_constraint = Constraint(rule=weight_rule)

    # Cars at least twice tractors: y >= 2x
    def cars_to_tractors_rule(m):
        return m.y >= 2 * m.x
    model.cars_to_tractors_constraint = Constraint(rule=cars_to_tractors_rule)

    # Objective: Minimize total number of vehicles x + y
    model.obj = Objective(expr=model.x + model.y, sense=1)  # 1 = minimize

    # ===== Solver Execution =====
    solver = SolverFactory('glpk')
    results = solver.solve(model, tee=False)

    # ===== Value Extraction and Reporting =====
    status = results.solver.status
    termination = results.solver.termination_condition
    obj_val = value(model.obj) if (termination == 'optimal' or str(termination).lower() == 'optimal') else None
    x_val = value(model.x) if obj_val is not None else None
    y_val = value(model.y) if obj_val is not None else None

    return {
        'status': str(status),
        'termination': str(termination),
        'objective_value': obj_val,
        'x': x_val,
        'y': y_val,
        'code_file': 'integer_vehicle_problem.py'
    }
