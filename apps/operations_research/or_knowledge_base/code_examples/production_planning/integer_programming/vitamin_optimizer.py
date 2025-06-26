
# Vitamin Optimization Model
# --------------------------------------
# Five-element model summary:
#
# 1. Objective:
#    Maximize the total number of people supplied:
#    maximize 10*x + 7*y
#
# 2. Variables:
#    x: number of batches of vitamin shots (integer, 0 <= x <= 10)
#    y: number of batches of vitamin pills (integer, y >= 0)
#
# 3. Constraints:
#    30*x + 50*y <= 1200    (Vitamin C constraint)
#    40*x + 30*y <= 1500    (Vitamin D constraint)
#    y >= x + 1             (Pills are more popular, integer strictness y > x)
#    x <= 10                (At most 10 batches of shots)
#    x >= 0
#    y >= 0
#
# 4. Sets/Parameters:
#    All coefficients such as batch yields and available vitamins are modeled as Params.
#
# 5. Additional Notes:
#    - All decision variables are nonnegative integers.
#    - The problem is solved as an integer program.
#    - Objective uses sense=maximize.
#    - The model is self-contained and does not use any non-ASCII characters.

from pyomo.environ import ConcreteModel, Var, Objective, Constraint, Param, NonNegativeIntegers, SolverFactory, value, maximize

def solve_vitamin_problem():
    # ====== Model Definition ======
    model = ConcreteModel()

    # --- Parameters
    model.c_shot = Param(initialize=30)     # Vitamin C per batch of shots
    model.c_pill = Param(initialize=50)     # Vitamin C per batch of pills
    model.d_shot = Param(initialize=40)     # Vitamin D per batch of shots
    model.d_pill = Param(initialize=30)     # Vitamin D per batch of pills
    model.c_avail = Param(initialize=1200)  # Total available vitamin C
    model.d_avail = Param(initialize=1500)  # Total available vitamin D
    model.shot_limit = Param(initialize=10) # Max batches of shots
    model.shot_obj = Param(initialize=10)   # Objective: people per batch of shots
    model.pill_obj = Param(initialize=7)    # Objective: people per batch of pills

    # --- Variables
    model.x = Var(within=NonNegativeIntegers, bounds=(0, value(model.shot_limit)))
    model.y = Var(within=NonNegativeIntegers, bounds=(0, None))

    # --- Constraints

    # Vitamin C constraint
    def vitamin_c_rule(m):
        return m.c_shot * m.x + m.c_pill * m.y <= m.c_avail
    model.vitamin_c = Constraint(rule=vitamin_c_rule)

    # Vitamin D constraint
    def vitamin_d_rule(m):
        return m.d_shot * m.x + m.d_pill * m.y <= m.d_avail
    model.vitamin_d = Constraint(rule=vitamin_d_rule)

    # Popularity constraint: y > x  (for integers, y >= x + 1)
    def popularity_rule(m):
        return m.y >= m.x + 1
    model.popularity = Constraint(rule=popularity_rule)

    # Additional upper bound already on x via bounds

    # --- Objective
    def obj_rule(m):
        return m.shot_obj * m.x + m.pill_obj * m.y
    model.obj = Objective(rule=obj_rule, sense=maximize)

    # ====== Solver Execution ======

    # Try using CBC first, fall back on GLPK if unavailable
    solver_status = ""
    for solver_name in ["cbc", "glpk"]:
        try:
            solver = SolverFactory(solver_name)
            if not solver.available():
                continue
            results = solver.solve(model, tee=False)
            solver_status = f"Solved with {solver_name}"
            break
        except Exception as e:
            solver_status = f"Solver {solver_name} failed: {e}"
            continue
    else:
        return {
            "status": "failure",
            "termination": "No suitable MILP solver (CBC or GLPK) available.",
            "objective": None,
            "x": None,
            "y": None,
            "file": "vitamin_optimizer.py"
        }

    status = str(results.solver.status)
    termination = str(results.solver.termination_condition)

    # ====== Value Extraction ======
    try:
        x_val = int(round(value(model.x)))
        y_val = int(round(value(model.y)))
        obj_val = int(round(value(model.obj)))
    except Exception as ex:
        return {
            "status": "failure",
            "termination": f"Model solved but unable to extract variable values: {ex}",
            "objective": None,
            "x": None,
            "y": None,
            "file": "vitamin_optimizer.py"
        }

    return {
        "status": status,
        "termination": termination,
        "objective": obj_val,
        "x": x_val,
        "y": y_val,
        "file": "vitamin_optimizer.py",
        "solver_status": solver_status
    }
