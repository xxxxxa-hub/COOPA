
# Five-Element Model Summary (ASCII Only)
#
# Objective:
#   Minimize total number of boxes: s + l
#
# Variables:
#   s: Number of small boxes (integer, >= 0)
#   l: Number of large boxes (integer, >= 0)
#
# Constraints:
#   1. 25*s + 45*l >= 750          (at least 750 masks)
#   2. s >= 3*l                    (at least 3 times as many small as large boxes)
#   3. l >= 5                      (at least 5 large boxes)
#
# Sets/Parameters:
#   All coefficients and requirements are specified as constants in model Params.
#
# Additional Notes:
#   This is a small mixed-integer linear program. Uses Pyomo and any available MILP solver.

def solve_mask_box_optimization():
    # ===== Imports =====
    from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, Integers, NonNegativeIntegers, value, SolverFactory

    # ===== Model Definition =====
    model = ConcreteModel()

    # --- Parameters ---
    model.small_box_size = Param(initialize=25)   # Masks per small box
    model.large_box_size = Param(initialize=45)   # Masks per large box
    model.min_total_masks = Param(initialize=750)
    model.min_large_boxes = Param(initialize=5)

    # For generality, max_s and max_l are unbounded above in this problem.
    model.max_s = Param(initialize=10000, mutable=True)
    model.max_l = Param(initialize=10000, mutable=True)

    # --- Variables ---
    model.s = Var(domain=NonNegativeIntegers, bounds=(0, model.max_s))
    model.l = Var(domain=NonNegativeIntegers, bounds=(model.min_large_boxes, model.max_l))

    # --- Constraints ---
    # 1. Total number of masks constraint
    def masks_constraint(m):
        return m.small_box_size * m.s + m.large_box_size * m.l >= m.min_total_masks
    model.masks_con = Constraint(rule=masks_constraint)

    # 2. Small vs. large boxes
    def box_ratio_constraint(m):
        return m.s >= 3 * m.l
    model.box_ratio_con = Constraint(rule=box_ratio_constraint)

    # 3. Minimum large boxes constraint (already handled by bounds, but included for clarity)
    def min_large_constraint(m):
        return m.l >= m.min_large_boxes
    model.min_large_con = Constraint(rule=min_large_constraint)

    # --- Objective ---
    def total_boxes_objective(m):
        return m.s + m.l
    model.obj = Objective(rule=total_boxes_objective, sense=1)  # sense=1 means minimize

    # ===== Solver Execution =====
    solver = None
    possible_solvers = ['cbc', 'glpk', 'highs']
    solved = False
    last_solver = None
    for solver_name in possible_solvers:
        try:
            solver = SolverFactory(solver_name)
            if solver.available():
                last_solver = solver_name
                results = solver.solve(model)
                solved = True
                break
        except:
            continue
    if not solved:
        return {
            'status': 'error',
            'termination': 'No MILP solver (cbc, glpk, highs) available in Pyomo environment.',
            'filename': 'mask_box_optimization.py'
        }

    # ===== Extract Results =====
    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)
    if termination.lower() not in ['optimal', 'feasible', 'locallyOptimal', 'locally optimal']:
        return {
            'status': status,
            'termination': termination,
            'filename': 'mask_box_optimization.py'
        }

    s_val = int(round(value(model.s)))
    l_val = int(round(value(model.l)))
    total_boxes = int(round(value(model.obj)))
    total_masks = value(model.s) * value(model.small_box_size) + value(model.l) * value(model.large_box_size)
    ratio_ok = (s_val >= 3 * l_val)
    large_ok = (l_val >= value(model.min_large_boxes))

    return {
        'status': status,
        'termination': termination,
        'solver_used': last_solver,
        's': s_val,
        'l': l_val,
        'total_boxes': total_boxes,
        'total_masks': int(total_masks),
        'ratio_ok': ratio_ok,
        'large_ok': large_ok,
        'filename': 'mask_box_optimization.py'
    }
