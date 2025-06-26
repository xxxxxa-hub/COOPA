# =====================================================
# Ad Allocation Optimization Model using Pyomo
#
# Five-Element Model Summary:
#
# Objective:
#   Maximize total number of viewers reached by placing ads on three platforms
#
# Variables:
#   x1 : integer >= 0 - number of ads on z-tube
#   x2 : integer >= 0 - number of ads on soorchle
#   x3 : integer >= 0 - number of ads on wassa
#
# Constraints:
#   (1) Budget constraint:         1000*x1 + 200*x2 + 100*x3 <= 10000
#   (2) Sorchle ad limit:          x2 <= 15
#   (3) Wassa ad fraction:         x3 <= (x1 + x2 + x3)/3   <- [linear: 2x3 - x1 - x2 <= 0]
#   (4) Z-tube ad minimum:         x1 >= 0.05*(x1 + x2 + x3) [linear: 0.95x1 - 0.05x2 - 0.05x3 >= 0]
#   (5) Integrality, non-negativity: x1, x2, x3 >= 0 and integers
#
# Sets/Parameters:
#   Cost per ad:      c = [1000, 200, 100] for [z-tube, soorchle, wassa]
#   Viewer per ad:    v = [400000, 5000, 3000] for [z-tube, soorchle, wassa]
#   Weekly budget:    B = 10000
#   Sorchle max ads:  U2 = 15
#
# Additional Notes:
#   - All data defined as Param objects.
#   - Problem is a Mixed Integer Linear Program (MILP).
#   - Uses CBC or GLPK if available.
#   - Reports infeasibility or solver errors.
# =====================================================

from pyomo.environ import (
    ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers,
    Param, maximize, SolverFactory, value
)

def solve_ads_allocation():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Indices for platforms
    PLATFORMS = [1,2,3]
    ZTUBE, SOORCHLE, WASSA = 1, 2, 3

    # Parameters
    cost_vals   = {ZTUBE:1000, SOORCHLE:200, WASSA:100}
    viewer_vals = {ZTUBE:400000, SOORCHLE:5000, WASSA:3000}
    sorchle_limit = 15
    budget = 10000

    model.cost = Param(PLATFORMS, initialize=cost_vals)
    model.viewer = Param(PLATFORMS, initialize=viewer_vals)
    model.budget = Param(initialize=budget)
    model.sorchle_limit = Param(initialize=sorchle_limit)
    model.min_z_pct = Param(initialize=0.05)

    # ===== Variables =====
    model.x = Var(PLATFORMS, domain=NonNegativeIntegers)

    # ===== Constraints =====
    # (1) Budget constraint
    def budget_rule(m):
        return sum(m.cost[j]*m.x[j] for j in PLATFORMS) <= m.budget
    model.budget_constr = Constraint(rule=budget_rule)

    # (2) Soorchle ad limit
    def soorchle_limit_rule(m):
        return m.x[SOORCHLE] <= m.sorchle_limit
    model.soorchle_constr = Constraint(rule=soorchle_limit_rule)

    # (3) Wassa ad fraction (linearized: 2x3 - x1 - x2 <= 0)
    def wassa_fraction_rule(m):
        return 2*m.x[WASSA] - m.x[ZTUBE] - m.x[SOORCHLE] <= 0
    model.wassa_fraction_constr = Constraint(rule=wassa_fraction_rule)

    # (4) Z-tube ad minimum (linearized: 0.95x1 - 0.05x2 - 0.05x3 >= 0)
    def ztube_min_pct_rule(m):
        return 0.95*m.x[ZTUBE] - 0.05*m.x[SOORCHLE] - 0.05*m.x[WASSA] >= 0
    model.ztube_min_constr = Constraint(rule=ztube_min_pct_rule)

    # ===== Objective =====
    def total_viewers_rule(m):
        return sum(m.viewer[j]*m.x[j] for j in PLATFORMS)
    model.obj = Objective(rule=total_viewers_rule, sense=maximize)

    # ===== Solver Execution =====
    solution_summary = {}
    solvers_to_try = ['cbc', 'glpk', 'highs']
    found_solver = None
    for solver_name in solvers_to_try:
        if SolverFactory(solver_name).available():
            found_solver = solver_name
            break

    if not found_solver:
        solution_summary['status'] = 'error'
        solution_summary['msg'] = ('No MILP solver available (cbc, glpk, highs). '
                                   'Install one of these solvers to obtain a solution.')
        print(solution_summary)
        return solution_summary

    solver = SolverFactory(found_solver)
    results = solver.solve(model, tee=False)

    solution_summary['solver'] = found_solver
    solution_summary['solver_status'] = str(results.solver.status)
    solution_summary['termination_condition'] = str(results.solver.termination_condition)

    # Check status
    if (results.solver.status != 'ok' or
        str(results.solver.termination_condition).lower() not in ['optimal', 'feasible']):
        solution_summary['status'] = 'error'
        solution_summary['msg'] = 'Solver did not return an optimal or feasible solution'
        print(solution_summary)
        return solution_summary

    solution_summary['status'] = 'success'

    # Extract variables
    x1 = int(round(value(model.x[ZTUBE])))
    x2 = int(round(value(model.x[SOORCHLE])))
    x3 = int(round(value(model.x[WASSA])))
    obj_val = int(round(value(model.obj)))

    solution_summary['x1'] = x1
    solution_summary['x2'] = x2
    solution_summary['x3'] = x3
    solution_summary['max_viewers'] = obj_val
    solution_summary['var_details'] = {'z-tube_ads':x1, 'soorchle_ads':x2, 'wassa_ads':x3}
    solution_summary['obj_val'] = obj_val

    # Report constraint satisfaction
    budget_lhs = cost_vals[ZTUBE]*x1 + cost_vals[SOORCHLE]*x2 + cost_vals[WASSA]*x3
    wassa_fraction_lhs = 2*x3 - x1 - x2
    ztube_pct_lhs = 0.95*x1 - 0.05*x2 - 0.05*x3

    solution_summary['constraint_violations'] = {}
    solution_summary['constraint_violations']['budget'] = (budget_lhs, "<=", budget)
    solution_summary['constraint_violations']['soorchle_limit'] = (x2, "<=", sorchle_limit)
    solution_summary['constraint_violations']['wassa_f'] = (wassa_fraction_lhs, "<=", 0)
    solution_summary['constraint_violations']['ztube_pct'] = (ztube_pct_lhs, ">=", 0)

    # Print summary
    print("Solver used:", found_solver)
    print("Solver status:", results.solver.status)
    print("Termination condition:", results.solver.termination_condition)
    print("Optimal values: x1 (z-tube ads) =", x1, ", x2 (soorchle ads) =", x2, ", x3 (wassa ads) =", x3)
    print("Maximum total viewers:", obj_val)
    print("Constraint verification:")
    print(" - Budget LHS/RHS:", budget_lhs, "<=", budget)
    print(" - Soorchle ad limit:", x2, "<=", sorchle_limit)
    print(" - Wassa fraction constraint:", wassa_fraction_lhs, "<=", 0)
    print(" - Z-tube fraction constraint:", ztube_pct_lhs, ">=", 0)
    print("Filename: ad_allocation_pyomo.py")

    return solution_summary
