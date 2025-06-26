# =============================================================================
# MILP Volunteer Optimization Model - Pyomo
# =============================================================================
#
# Five-element format summary:
#
# Objective:
#   Maximize the total number of gifts delivered by selecting how many seasonal
#   and full-time volunteers to field, subject to points and composition rules.
#
# Variables:
#   s : Number of seasonal volunteers (integer, >= 0)
#   f : Number of full-time volunteers (integer, >= 0, min 10)
#
# Constraints:
#   (a) Points constraint:      2*s + 5*f <= 200
#   (b) Fraction seasonal:      7*s <= 3*f
#   (c) Min full-time:          f >= 10
#
# Sets/Parameters:
#   gift_s     : gifts delivered by 1 seasonal volunteer (5)
#   point_s    : points earned by 1 seasonal volunteer (2)
#   gift_f     : gifts delivered by 1 full-time volunteer (8)
#   point_f    : points earned by 1 full-time volunteer (5)
#   points_max : max total points allowed (200)
#   min_f      : minimum number of full-time volunteers (10)
#   seasonal_frac_limit : max seasonal fraction (0.3)
#
# Additional Notes:
#   - Variables are modeled as integer and all data is Pyomo Param.
#   - Model is solved using the first available MILP solver.
#   - All logic and results are ASCII-only.
#
# =============================================================================

from pyomo.environ import ConcreteModel, Var, Param, Constraint, Objective, SolverFactory, value, Integers, maximize

def solve_milp_volunteers():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.gift_s = Param(initialize=5)          # Gifts per seasonal
    model.point_s = Param(initialize=2)         # Points per seasonal
    model.gift_f = Param(initialize=8)          # Gifts per full-time
    model.point_f = Param(initialize=5)         # Points per full-time
    model.points_max = Param(initialize=200)    # Max points
    model.min_f = Param(initialize=10)          # Min full-time
    model.seasonal_frac_limit = Param(initialize=0.3)  # Seasonal fraction

    # Variables
    model.s = Var(domain=Integers, bounds=(0, None))
    model.f = Var(domain=Integers, bounds=(model.min_f, None))

    # Constraints
    def points_constraint(m):
        return m.point_s * m.s + m.point_f * m.f <= m.points_max
    model.c_points = Constraint(rule=points_constraint)

    def fraction_seasonal_constraint(m):
        # Linearized: 7*s <= 3*f   (derived from s <= 0.3*(s+f))
        return 7 * m.s <= 3 * m.f
    model.c_frac = Constraint(rule=fraction_seasonal_constraint)

    # Objective
    def gifts_obj(m):
        return m.gift_s * m.s + m.gift_f * m.f
    model.obj = Objective(rule=gifts_obj, sense=maximize)

    # ===== Solver Execution =====
    # Try the solvers in this order: 'cbc', 'glpk', 'gurobi', 'scip', 'highs'
    solvers_to_try = ['cbc', 'glpk', 'gurobi', 'scip', 'highs']
    solver_used = None
    for sname in solvers_to_try:
        solver = SolverFactory(sname)
        if solver.available(exception_flag=False):
            solver_used = sname
            break

    if solver_used is None:
        result_summary = {
            "status": "error",
            "message": "No MILP solver available (cbc, glpk, gurobi, scip, highs). Cannot solve problem."
        }
        return result_summary

    results = solver.solve(model, tee=False)
    status = results.solver.status
    term_cond = results.solver.termination_condition

    # Check if a solution was found
    if (str(term_cond).lower() not in ['optimal', 'feasible', 'locallyOptimal'.lower(), 'locally optimal']):
        return {
            "status": str(status),
            "termination_condition": str(term_cond),
            "message": "Solver did not produce an optimal or feasible solution.",
            "solver_used": solver_used
        }

    # Variable and objective extraction
    s_val = int(round(value(model.s)))
    f_val = int(round(value(model.f)))
    gifts_val = int(round(value(model.obj)))
    points_spent = value(model.point_s * s_val + model.point_f * f_val)

    return {
        "status": str(status),
        "termination_condition": str(term_cond),
        "solver_used": solver_used,
        "s_val": s_val,
        "f_val": f_val,
        "total_gifts": gifts_val,
        "points_used": points_spent
    }
