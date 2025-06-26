# =============================================================================
# Pyomo LP Model for Hardwood & Vinyl Optimization
# =============================================================================
# Five-element model summary:
# Objective:
#   Maximize profit = 2.5 * x1 + 3.0 * x2
# Variables:
#   x1: square feet of hardwood (continuous), 
#   x2: square feet of vinyl (continuous)
#   Both with lower and upper bounds set as Params.
# Constraints:
#   x1 >= lb_x1     [minimum hardwood produced]
#   x2 >= lb_x2     [minimum vinyl produced]
#   x1 + x2 >= demand_min [total minimum production]
#   x1 <= ub_x1     [maximum hardwood allowed]
#   x2 <= ub_x2     [maximum vinyl allowed]
# Sets/Parameters:
#   All data hard-coded as Params.
# Additional notes:
#   - All bounds and coefficients encoded as model Params.
#   - Model is continuous, two-variable LP.
#   - Solves with default available solver (e.g. glpk, cbc).

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, NonNegativeReals, SolverFactory, value

def solve_linear_program():
    # ===== Model Definition =====
    model = ConcreteModel()

    # --- Parameters ---
    model.profit_coeff1 = Param(initialize=2.5)      # Coefficient for x1
    model.profit_coeff2 = Param(initialize=3.0)      # Coefficient for x2
    model.lb_x1 = Param(initialize=20000)            # x1 >= lower bound
    model.lb_x2 = Param(initialize=10000)            # x2 >= lower bound
    model.ub_x1 = Param(initialize=50000)            # x1 <= upper bound
    model.ub_x2 = Param(initialize=30000)            # x2 <= upper bound
    model.demand_min = Param(initialize=60000)       # x1 + x2 >= demand_min

    # --- Variables (bounds via parameters) ---
    model.x1 = Var(domain=NonNegativeReals, bounds=lambda m: (m.lb_x1, m.ub_x1))
    model.x2 = Var(domain=NonNegativeReals, bounds=lambda m: (m.lb_x2, m.ub_x2))

    # --- Constraints ---
    def total_min_demand_rule(m):
        return m.x1 + m.x2 >= m.demand_min
    model.total_min_demand = Constraint(rule=total_min_demand_rule)

    # --- Objective ---
    def obj_rule(m):
        return m.profit_coeff1 * m.x1 + m.profit_coeff2 * m.x2
    model.obj = Objective(rule=obj_rule, sense=1)   # sense=1 means maximize

    # ===== Solver Execution =====
    # Try GLPK, fallback to CBC if available
    solvers_to_try = ['glpk', 'cbc']
    solver = None
    for solver_name in solvers_to_try:
        try:
            s = SolverFactory(solver_name)
            if s.available():
                solver = s
                break
        except:
            continue
    if solver is None:
        print('ERROR: No suitable solver ("glpk" or "cbc") available in environment.')
        return {'status': 'solver_not_found'}

    results = solver.solve(model, tee=False)

    # ===== Results Extraction =====
    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)
    if termination.lower() not in ('optimal', 'feasible', 'locally optimal'):
        print('Model did not solve to optimality. Status:', status, 'Termination:', termination)
        return {
            'status': status,
            'termination': termination
        }

    x1_value = value(model.x1)
    x2_value = value(model.x2)
    obj_value = value(model.obj)

    print('Solver status:', status)
    print('Termination condition:', termination)
    print('Objective (profit) value:', obj_value)
    print('x1 (hardwood, sqft):', x1_value)
    print('x2 (vinyl, sqft):', x2_value)
    print('Source file: linear_program_hardwood_vinyl.py')
    return {
        'status': status,
        'termination': termination,
        'objective': obj_value,
        'x1': x1_value,
        'x2': x2_value,
        'filename': 'linear_program_hardwood_vinyl.py'
    }
