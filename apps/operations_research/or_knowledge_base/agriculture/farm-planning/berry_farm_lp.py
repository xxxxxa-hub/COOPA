# =============================================================================
# Berry Farm LP: Maximize profit from planting blueberries and raspberries
#
# Five-element model summary:
#
# Objective:
#   Maximize total profit: 56 * x + 75 * y
#
# Variables:
#   x: Acres of blueberries to plant (continuous, >= 0)
#   y: Acres of raspberries to plant (continuous, >= 0)
#
# Constraints:
#   1. Land:             x + y <= 300
#   2. Labor:            6x + 3y <= 575
#   3. Watering cost:    22x + 25y <= 10000
#   4. Non-negativity:   x >= 0, y >= 0
#
# Sets/Parameters:
#   a_land = 300         (Total available acres)
#   a_labor = 575        (Total available labor units)
#   a_water = 10000      (Watering cost budget)
#   profit_x = 56        (Profit per acre of blueberries)
#   profit_y = 75        (Profit per acre of raspberries)
#   labor_x = 6          (Labor units per acre blueberries)
#   labor_y = 3          (Labor units per acre raspberries)
#   water_x = 22         (Water cost per acre blueberries)
#   water_y = 25         (Water cost per acre raspberries)
#
# Additional Notes:
#   - All data is entered as Param in the Pyomo model.
#   - Variable bounds use Param.
#   - Problem is a standard LP, solved with Pyomo and GLPK (or default solver).
# =============================================================================

from pyomo.environ import (
    ConcreteModel, Var, Param, NonNegativeReals, Constraint, Objective, maximize,
    SolverFactory, value
)

def solve_lp():
    # ===== Model Definition =====
    model = ConcreteModel()

    # --- Parameters ---
    model.a_land  = Param(initialize=300)      # land constraint
    model.a_labor = Param(initialize=575)      # labor constraint
    model.a_water = Param(initialize=10000)    # watering cost constraint
    model.profit_x = Param(initialize=56)
    model.profit_y = Param(initialize=75)
    model.labor_x = Param(initialize=6)
    model.labor_y = Param(initialize=3)
    model.water_x = Param(initialize=22)
    model.water_y = Param(initialize=25)

    # Lower and upper bounds for variables
    model.LB_x = Param(initialize=0)
    model.UB_x = Param(initialize=model.a_land)
    model.LB_y = Param(initialize=0)
    model.UB_y = Param(initialize=model.a_land)

    # --- Decision Variables ---
    def x_bounds(m):
        return (m.LB_x, m.UB_x)
    def y_bounds(m):
        return (m.LB_y, m.UB_y)
    model.x = Var(bounds=x_bounds)
    model.y = Var(bounds=y_bounds)

    # --- Constraints ---
    def land_rule(m):
        return m.x + m.y <= m.a_land
    model.land_con = Constraint(rule=land_rule)

    def labor_rule(m):
        return m.labor_x * m.x + m.labor_y * m.y <= m.a_labor
    model.labor_con = Constraint(rule=labor_rule)

    def water_rule(m):
        return m.water_x * m.x + m.water_y * m.y <= m.a_water
    model.water_con = Constraint(rule=water_rule)

    # --- Objective Function ---
    def obj_rule(m):
        return m.profit_x * m.x + m.profit_y * m.y
    model.profit = Objective(rule=obj_rule, sense=maximize)

    # ===== Solver Execution =====
    try:
        solver = SolverFactory('glpk')
        results = solver.solve(model)
        # Extract solve status and termination
        solve_status = results.solver.status
        termination = results.solver.termination_condition
    except Exception as e:
        # Try alternate solver if GLPK not found
        try:
            solver = SolverFactory('cbc')
            results = solver.solve(model)
            solve_status = results.solver.status
            termination = results.solver.termination_condition
        except Exception as e2:
            # If no solver, report error
            return {
                "status": "Failure",
                "message": "Could not solve LP: Neither GLPK nor CBC solver available. Exception: {} ; {}".format(str(e), str(e2))
            }

    # Check feasibility/infeasibility
    infeasible = ("infeasible" in str(termination).lower())
    if infeasible:
        return {
            "status": "Infeasible",
            "solve_status": str(solve_status),
            "termination": str(termination),
            "message": "Model infeasible. Check whether constraints are too restrictive."
        }

    x_opt = value(model.x)
    y_opt = value(model.y)
    obj_opt = value(model.profit)

    # ===== Results =====
    results_dict = {
        "status": "Optimal",
        "solve_status": str(solve_status),
        "termination": str(termination),
        "optimal_x": x_opt,
        "optimal_y": y_opt,
        "optimal_profit": obj_opt,
        "filename": "berry_farm_lp.py"
    }
    print("Solver status:", solve_status)
    print("Termination condition:", termination)
    print("Optimal value of x (blueberries):", x_opt)
    print("Optimal value of y (raspberries):", y_opt)
    print("Maximum profit:", obj_opt)
    print("Model file: berry_farm_lp.py")
    return results_dict

