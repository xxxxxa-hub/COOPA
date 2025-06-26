# =============================================
# Five-Element Model Summary
#
# Objective:
#   Minimize the total number of transportation units (trains + trams).
#
# Variables:
#   x: Number of trains (integer, >= 0)
#   y: Number of trams (integer, >= 0)
#
# Constraints:
#   - 120*x + 30*y >= 600  (capacity requirement)
#   - y >= 2*x             (trams at least double trains)
#
# Sets/Parameters:
#   train_capacity = 120   (people per train per hour)
#   tram_capacity = 30     (people per tram per hour)
#   min_total_capacity = 600 (minimum people/hour transported)
#
# Additional Notes:
#   - All parameters are defined as Pyomo Param objects.
#   - Variables are integer and non-negative.
#   - The objective function is explicit and set to 'sense=minimize'.
#   - Model is implemented in Pyomo for an MILP solver (e.g., GLPK).
# =============================================

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, NonNegativeIntegers, value, SolverFactory

def solve_transportation_optimizer():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.train_capacity = Param(initialize=120)
    model.tram_capacity = Param(initialize=30)
    model.min_total_capacity = Param(initialize=600)

    # Lower bounds as Param
    model.zerobound = Param(initialize=0)

    # Variables (integer and bounded below)
    model.x = Var(domain=NonNegativeIntegers)  # trains
    model.y = Var(domain=NonNegativeIntegers)  # trams

    # Constraints
    def capacity_rule(m):
        return m.train_capacity * m.x + m.tram_capacity * m.y >= m.min_total_capacity
    model.capacity_constraint = Constraint(rule=capacity_rule)

    def tram_train_rule(m):
        return m.y >= 2 * m.x
    model.tram_train_constraint = Constraint(rule=tram_train_rule)

    # Objective: minimize total units
    model.total_units = Objective(expr=model.x + model.y, sense=1) # sense=1 for minimize

    # ===== Solver Execution =====
    solver = SolverFactory('glpk')
    result = solver.solve(model)

    # ===== Results Extraction =====
    info = dict()
    info['solver_status'] = str(result.solver.status)
    info['termination_condition'] = str(result.solver.termination_condition)

    # Only extract variable/objective values if solved to optimality
    if str(result.solver.termination_condition) == 'optimal':
        info['objective_value'] = value(model.total_units)
        info['x_trains'] = int(round(value(model.x)))
        info['y_trams'] = int(round(value(model.y)))
        
        # Constraint verification
        info['capacity_achieved'] = (
            value(model.train_capacity) * info['x_trains'] +
            value(model.tram_capacity) * info['y_trams']
        )
        info['tram_train_diff'] = info['y_trams'] - 2 * info['x_trains']
    else:
        # If not optimal, don't return variable values
        info['objective_value'] = None
        info['x_trains'] = None
        info['y_trams'] = None
        info['capacity_achieved'] = None
        info['tram_train_diff'] = None

    return info
