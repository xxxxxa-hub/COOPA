
"""
Integer Optimization for Camels and Horses Dispatch

Five-element Model Summary:

1. Objective:
   - Minimize the total number of animals (x + y)

2. Variables:
   - x: Number of camels (integer, x >= 0)
   - y: Number of horses (integer, y >= 0)
       (With upper bounds defined as Params)

3. Constraints:
   - 50*x + 60*y >= 1000          # Deliver at least 1000 packages
   - 20*x + 30*y <= 450           # Total food <= 450 units
   - y <= x                       # Horses not more than camels

4. Sets/Parameters:
   - deliver_per_camel (a): 50
   - deliver_per_horse (b): 60
   - food_per_camel (c): 20
   - food_per_horse (d): 30
   - min_packages (e): 1000
   - max_food (f): 450
   - max_camel (u_x): 1000 (arbitrary large for modeling)
   - max_horse (u_y): 1000 (arbitrary large for modeling)

5. Additional Notes:
   - All scalar data used as Pyomo Params.
   - Variable bounds reference Param values.
   - Model uses NonNegativeIntegers for x and y.
   - Solution extraction uses value() from pyomo.environ.
   - Standard ASCII only in code and comments.

"""

# ===== Imports =====
from pyomo.environ import (
    ConcreteModel, Var, Objective, Constraint, NonNegativeIntegers, Param,
    SolverFactory, value, minimize
)

def solve_camels_horses():
    # ===== Model Definition =====
    model = ConcreteModel()

    # ===== Parameters =====
    model.deliver_per_camel = Param(initialize=50)  # a
    model.deliver_per_horse = Param(initialize=60)  # b
    model.food_per_camel = Param(initialize=20)     # c
    model.food_per_horse = Param(initialize=30)     # d
    model.min_packages = Param(initialize=1000)     # e
    model.max_food = Param(initialize=450)          # f

    # Reasonably large upper bounds on number of camels/horses
    model.max_camel = Param(initialize=1000)
    model.max_horse = Param(initialize=1000)

    # ===== Variables =====
    model.x = Var(
        domain=NonNegativeIntegers,
        bounds=(0, model.max_camel)
    )
    model.y = Var(
        domain=NonNegativeIntegers,
        bounds=(0, model.max_horse)
    )

    # ===== Constraints =====
    def packages_rule(m):
        return m.deliver_per_camel * m.x + m.deliver_per_horse * m.y >= m.min_packages
    model.MinPackages = Constraint(rule=packages_rule)

    def food_rule(m):
        return m.food_per_camel * m.x + m.food_per_horse * m.y <= m.max_food
    model.MaxFood = Constraint(rule=food_rule)

    def horse_vs_camel_rule(m):
        return m.y <= m.x
    model.HorsesToCamels = Constraint(rule=horse_vs_camel_rule)

    # ===== Objective =====
    model.TotalAnimals = Objective(expr=model.x + model.y, sense=minimize)

    # ===== Solver Execution =====
    # Try GLPK, CBC, or any other available MIP solver
    solver = None
    for solver_name in ["glpk", "cbc"]:
        if SolverFactory(solver_name).available():
            solver = SolverFactory(solver_name)
            break

    if solver is None:
        return {
            "status": "error",
            "termination_condition": "No suitable MIP solver found (tried glpk, cbc).",
            "x": None, "y": None, "objective": None
        }

    result = solver.solve(model, tee=False)

    # ===== Value Extraction =====
    status = str(result.solver.status)
    termination_condition = str(result.solver.termination_condition)

    feasible = (
        status.lower() == "ok"
        and "optimal" in termination_condition.lower()
    )

    if feasible:
        x_val = int(round(value(model.x)))
        y_val = int(round(value(model.y)))
        obj_val = int(round(value(model.TotalAnimals)))
    else:
        x_val = y_val = obj_val = None

    return {
        "status": status,
        "termination_condition": termination_condition,
        "x": x_val,
        "y": y_val,
        "objective": obj_val
    }
