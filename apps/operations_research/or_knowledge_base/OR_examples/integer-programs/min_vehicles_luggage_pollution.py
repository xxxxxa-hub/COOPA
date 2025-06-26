############################################################
# Integer Linear Program: Vehicle Selection
# 
# Objective: 
#   Minimize the total number of vehicles (x + y)
#
# Variables:
#   x: Number of 4-wheeler vehicles (integer, >= 0)
#   y: Number of 3-wheeler vehicles (integer, >= 0)
#
# Constraints:
#   1. 60 * x + 40 * y >= 1000    # Luggage capacity requirement
#   2. 30 * x + 15 * y <= 430     # Pollution constraint
#
# Sets/Parameters:
#   - LUGGAGE_4W: Luggage capacity per 4-wheeler (60)
#   - LUGGAGE_3W: Luggage capacity per 3-wheeler (40)
#   - POLLUTION_4W: Pollution per 4-wheeler (30)
#   - POLLUTION_3W: Pollution per 3-wheeler (15)
#   - LUGGAGE_REQ: Minimum luggage capacity required (1000)
#   - POLLUTION_MAX: Maximum total pollution allowed (430)
#
# Additional Notes:
#   - Model is formulated and solved using Pyomo.
#   - All input data is defined as Pyomo Params.
#   - Only standard ASCII characters are used throughout.
#   - Variable bounds are enforced using Params.
############################################################

def solve_ilp_vehicle_problem():
    # ===== Imports =====
    from pyomo.environ import (
        ConcreteModel, Var, Objective, Constraint, Integers, Param, NonNegativeIntegers,
        SolverFactory, value
    )

    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters
    model.LUGGAGE_4W = Param(initialize=60)
    model.LUGGAGE_3W = Param(initialize=40)
    model.POLLUTION_4W = Param(initialize=30)
    model.POLLUTION_3W = Param(initialize=15)
    model.LUGGAGE_REQ = Param(initialize=1000)
    model.POLLUTION_MAX = Param(initialize=430)

    # Enforce (conservative) upper bounds for computational purposes
    # Maximum x: cannot put more than all luggage in 4-wheelers
    max_x = (model.LUGGAGE_REQ() // model.LUGGAGE_4W()) + 10
    max_y = (model.LUGGAGE_REQ() // model.LUGGAGE_3W()) + 25

    model.x_ub = Param(initialize=max_x)
    model.y_ub = Param(initialize=max_y)

    # Variables
    model.x = Var(domain=NonNegativeIntegers, bounds=(0, model.x_ub))
    model.y = Var(domain=NonNegativeIntegers, bounds=(0, model.y_ub))

    # Constraints
    def luggage_rule(m):
        return m.LUGGAGE_4W * m.x + m.LUGGAGE_3W * m.y >= m.LUGGAGE_REQ
    model.luggage_constraint = Constraint(rule=luggage_rule)

    def pollution_rule(m):
        return m.POLLUTION_4W * m.x + m.POLLUTION_3W * m.y <= m.POLLUTION_MAX
    model.pollution_constraint = Constraint(rule=pollution_rule)

    # Objective function: minimize the total number of vehicles
    model.total_vehicles = Objective(
        expr=model.x + model.y,
        sense=1  # Minimize
    )

    # ===== Solver Execution =====

    # Try to use CBC if available, otherwise GLPK, otherwise fail
    result = None
    solver_names = ['cbc', 'glpk']
    last_exception = None
    for solver_name in solver_names:
        opt = SolverFactory(solver_name)
        if opt is not None and opt.available():
            try:
                result = opt.solve(model)
                break
            except Exception as ex:
                last_exception = ex
                continue

    # ===== Output Results =====

    solution_status = ""
    termination_condition = ""
    objective_value = None
    x_value = None
    y_value = None
    infeas_note = ""
    solved = False

    if result is not None:
        solution_status = str(result.solver.status)
        termination_condition = str(result.solver.termination_condition)
        if (result.solver.status == 'ok' or result.solver.status == 'optimal') and            (str(result.solver.termination_condition).lower() in ['optimal', 'feasible']):
            solved = True
        try:
            objective_value = int(value(model.x) + value(model.y)) if value(model.x) is not None and value(model.y) is not None else None
            x_value = int(value(model.x)) if value(model.x) is not None else None
            y_value = int(value(model.y)) if value(model.y) is not None else None
        except:
            pass
    else:
        solution_status = "no_solver_found"
        termination_condition = str(last_exception) if last_exception is not None else "Could not find a solver."

    # Print/Return all required info
    print("===== Task outcome (short version) =====")
    if solved and objective_value is not None:
        print("Optimal value of x + y:", objective_value)
    else:
        print("No optimal solution found.")

    print("\n===== Task outcome (extremely detailed version) =====")
    print("Script file: ilp_vehicles_pyomo.py")
    print("Objective: Minimize x + y (total number of vehicles)")
    print("Variables: x (4-wheelers) =", x_value, ", y (3-wheelers) =", y_value)
    print("Constraints:")
    print("  Luggage capacity: 60*x + 40*y >= 1000")
    print("  Pollution:        30*x + 15*y <= 430")
    print("Parameters:")
    print("  LUGGAGE_4W =", value(model.LUGGAGE_4W))
    print("  LUGGAGE_3W =", value(model.LUGGAGE_3W))
    print("  POLLUTION_4W =", value(model.POLLUTION_4W))
    print("  POLLUTION_3W =", value(model.POLLUTION_3W))
    print("  LUGGAGE_REQ =", value(model.LUGGAGE_REQ))
    print("  POLLUTION_MAX =", value(model.POLLUTION_MAX))
    print("")
    print("Solver status:", solution_status)
    print("Solver termination condition:", termination_condition)
    if solved and objective_value is not None:
        print("Optimal x:", x_value)
        print("Optimal y:", y_value)
        print("Optimal total vehicles (x + y):", objective_value)
    else:
        print("No optimal solution or solution is infeasible/unavailable.")
        print("Last solver exception:", termination_condition)

    print("\n===== Additional context =====")
    if not solved:
        print("Try installing or making available a supported open-source MILP solver such as CBC or GLPK.")
        print("Verify that the model data and constraints are correct and consistent.")

    # Return the value for automation
    return {
        "solved": solved,
        "objective": objective_value,
        "x": x_value,
        "y": y_value,
        "solution_status": solution_status,
        "termination_condition": termination_condition,
        "script_file": "ilp_vehicles_pyomo.py"
    }
