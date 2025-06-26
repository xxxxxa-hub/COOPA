# ===== Five-Element Model Summary =====
'''
Objective: 
    Minimize total transport time (in minutes), given by total_time = 40*x + 30*y,
    where x is the number of helicopter trips and y the number of car trips.

Variables: 
    x : number of helicopter trips, integer, 0 <= x <= 5
    y : number of car trips, integer, y >= 0

Constraints:
    1. 30*x + 20*y >= 300      # Enough fish are transported
    2. x <= 5                  # At most 5 helicopter trips
    3. y >= 1.5*x              # At least 60% of trips by car
    4. x + y >= 1              # At least one trip (strictly positive integer)

Sets/Parameters:
    - model.time_per_helicopter : Minutes per helicopter trip (40)
    - model.time_per_car : Minutes per car trip (30)
    - model.fish_per_helicopter : Fish units per helicopter trip (30)
    - model.fish_per_car : Fish units per car trip (20)
    - model.min_fish : Minimum fish units required (300)
    - model.max_helicopters : Upper bound on helicopter trips (5)

Additional Notes:
    - All input data is encoded as Pyomo Param.
    - Variables are NonNegativeIntegers with parametric bounds.
    - x + y >= 1 encodes the strict 'at least one trip' using integer property.
    - The model is solved using an available MILP solver (CBC, GLPK, or similar).
    - All reporting is via ASCII comments and documentation only.
'''

# ===== Model and Function Definition =====
def solve_integer_transport():
    from pyomo.environ import (ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, Param, SolverFactory, value)
    import pyomo.environ as pyo

    # Model instantiation
    model = ConcreteModel()

    # ===== Parameters =====
    model.time_per_helicopter = Param(initialize=40)
    model.time_per_car = Param(initialize=30)
    model.fish_per_helicopter = Param(initialize=30)
    model.fish_per_car = Param(initialize=20)
    model.min_fish = Param(initialize=300)
    model.max_helicopters = Param(initialize=5)

    # ===== Variables =====
    # x: number of helicopter trips, integer in [0, max_helicopters]
    model.x = Var(domain=NonNegativeIntegers, bounds=(0, value(model.max_helicopters)))
    # y: number of car trips, integer in [0, +inf)
    model.y = Var(domain=NonNegativeIntegers)

    # ===== Constraints =====

    # 1. Fish transported constraint: 30*x + 20*y >= 300
    def fish_constraint_rule(m):
        return m.fish_per_helicopter * m.x + m.fish_per_car * m.y >= m.min_fish
    model.fish_constraint = Constraint(rule=fish_constraint_rule)

    # 2. x <= max_helicopters automatically enforced in variable bounds

    # 3. At least 60% trips must be car trips: y >= 1.5*x
    def car_prop_constraint_rule(m):
        return m.y >= 1.5 * m.x
    model.car_prop_constraint = Constraint(rule=car_prop_constraint_rule)

    # 4. At least one trip (x + y >= 1)
    def at_least_one_trip_rule(m):
        return m.x + m.y >= 1
    model.min_trip_constraint = Constraint(rule=at_least_one_trip_rule)

    # ===== Objective =====
    def total_time_rule(m):
        return m.time_per_helicopter * m.x + m.time_per_car * m.y
    model.obj = Objective(rule=total_time_rule, sense=pyo.minimize)

    # ===== Solver Execution =====
    # Try CBC first, fallback to GLPK if necessary
    status = None
    termination = None
    solution_x = None
    solution_y = None
    optimal_obj = None
    solver_name = None

    solver = None
    for candidate_solver in ['cbc', 'glpk']:
        if SolverFactory(candidate_solver).available():
            solver = SolverFactory(candidate_solver)
            solver_name = candidate_solver
            break

    result_message = ""
    if solver is None:
        result_message = (
            "No available MILP solver (CBC or GLPK) found in the environment. "
            "Please install CBC or GLPK to solve integer programming problems in Pyomo."
        )
    else:
        solve_result = solver.solve(model)
        status = solve_result.solver.status
        termination = solve_result.solver.termination_condition

        if (termination == pyo.TerminationCondition.optimal or 
            termination == 'optimal'):
            solution_x = int(round(value(model.x)))
            solution_y = int(round(value(model.y)))
            optimal_obj = int(round(value(model.obj)))
            result_message = (
                f"Solver: {solver_name}\nStatus: {status}\nTermination: {termination}\n"
                f"Objective (minimal total time): {optimal_obj}\n"
                f"x (helicopter trips): {solution_x}\n"
                f"y (car trips): {solution_y}\n"
            )
        else:
            result_message = (
                f"Solver: {solver_name}\nStatus: {status}\nTermination: {termination}\n"
                f"Model was not solved to optimality. Please check constraint consistency and solver configuration."
            )

    # ===== Result Return =====
    return {
        'solver': solver_name,
        'status': str(status),
        'termination': str(termination),
        'optimal_obj': optimal_obj,
        'x': solution_x,
        'y': solution_y,
        'file': 'helicopter_car_transport_optimize.py',
        'message': result_message
    }
