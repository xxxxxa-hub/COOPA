
# =============================================================================
# Optimization Model for Minimizing the Number of Printers
# =============================================================================
# Five-Element Model Summary
#
# Objective:
#   Minimize the total number of printers (x + y).
#
# Variables:
#   x : Integer, number of premium printers (x >= 0)
#   y : Integer, number of regular printers (y >= 0)
#
# Constraints:
#   1. Total printing speed constraint:       30*x + 20*y >= 200
#   2. Total ink units constraint:            4*x + 3*y <= 35
#   3. Regular printers less than premium:    y <= x - 1
#
# Sets/Parameters:
#   All constants (speeds, ink usage, bounds) are treated as model Params
#
# Additional Notes:
#   - Model uses Pyomo (https://www.pyomo.org/) for problem formulation.
#   - Only standard ASCII characters are used.
#   - Solution extraction uses 'value()' for variables/objective.
#   - Uses available open-source solver (GLPK or CBC).
# =============================================================================

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Integers, NonNegativeIntegers, Param, value, SolverFactory, TerminationCondition

def solve_printer_problem():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters (all constants, as Params)
    model.speed_premium = Param(initialize=30)   # Speed per premium printer
    model.speed_regular = Param(initialize=20)   # Speed per regular printer
    model.ink_premium = Param(initialize=4)      # Ink units per premium printer
    model.ink_regular = Param(initialize=3)      # Ink units per regular printer
    model.min_total_speed = Param(initialize=200)
    model.max_total_ink = Param(initialize=35)
    model.x_lower = Param(initialize=0)          # lower bound
    model.y_lower = Param(initialize=0)          # lower bound

    # Decision Variables (integers, >= 0)
    model.x = Var(domain=NonNegativeIntegers)
    model.y = Var(domain=NonNegativeIntegers)

    # Objective: Minimize total printers
    model.total_printers = Objective(
        expr = model.x + model.y,
        sense = 1  # 1 for minimize
    )

    # Constraints:
    # 1. Printing speed
    model.speed_constraint = Constraint(
        expr = model.speed_premium * model.x + model.speed_regular * model.y >= model.min_total_speed
    )
    # 2. Ink units
    model.ink_constraint = Constraint(
        expr = model.ink_premium * model.x + model.ink_regular * model.y <= model.max_total_ink
    )
    # 3. Regular printers less than premium: y <= x - 1
    model.regular_less_than_premium = Constraint(
        expr = model.y <= model.x - 1
    )

    # ===== Solver Execution =====
    # Try GLPK first, fall back to CBC if not available
    solver_name = None
    for candidate in ['glpk', 'cbc']:
        if SolverFactory(candidate).available(exception_flag=False):
            solver_name = candidate
            break

    if solver_name is None:
        print("ERROR: No compatible MILP solver (glpk or cbc) found in the environment.")
        return {
            'status': 'solver_not_found',
            'termination': 'No compatible solver found',
            'file': 'printer_optimization.py'
        }

    solver = SolverFactory(solver_name)
    result = solver.solve(model)

    # ===== Results Extraction =====
    # Read solver status and termination
    status = str(result.solver.status)
    termination = str(result.solver.termination_condition)

    print("Solver used: {}".format(solver_name))
    print("Solver status:", status)
    print("Termination condition:", termination)

    # Check for infeasibility, unbounded, or solver error
    if result.solver.termination_condition != TerminationCondition.optimal:
        print("*** Warning: Solver did not find an optimal solution. ***")
        x_val = None
        y_val = None
        obj_val = None
    else:
        # Obtain variable values and objective
        x_val = int(round(value(model.x)))
        y_val = int(round(value(model.y)))
        obj_val = int(round(value(model.total_printers)))

        print("Optimal total printers:", obj_val)
        print("Premium printers (x):", x_val)
        print("Regular printers (y):", y_val)

    return {
        'status': status,
        'termination': termination,
        'x': x_val,
        'y': y_val,
        'objective': obj_val,
        'file': 'printer_optimization.py'
    }

