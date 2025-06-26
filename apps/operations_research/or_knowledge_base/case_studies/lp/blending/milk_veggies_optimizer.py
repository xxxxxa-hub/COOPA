
# ==============================================================================
# Milk & Vegetables Diet Cost Minimization Linear Program
# ==============================================================================
# Five-Element Model Summary:
#
# 1. Objective:
#    Minimize total cost: cost = 1 * x + 2 * y
#
# 2. Variables:
#    x: number of glasses of milk (continuous, x >= 0)
#    y: number of plates of vegetables (continuous, y >= 0)
#
# 3. Constraints:
#    40 * x + 15 * y >= 100    (calcium constraint)
#    25 * x + 30 * y >= 50     (iron constraint)
#    x >= 0, y >= 0            (non-negativity)
#
# 4. Sets/Parameters:
#    All coefficients specified below as params.
#
# 5. Additional Notes:
#    All coefficients are modeled as Pyomo Param objects.
#    Variables are continuous and non-negative.
#    Solver status, solution, and detailed outcome will be printed.
# ==============================================================================

from pyomo.environ import ConcreteModel, Var, Param, Objective, Constraint, NonNegativeReals, SolverFactory, value, minimize, ConstraintList

def solve_milk_veggie_optimizer():
    # ===== Model Definition =====
    model = ConcreteModel()

    # Parameters for objective function coefficients
    model.c_milk = Param(initialize=1)
    model.c_veggie = Param(initialize=2)
    
    # Nutrient parameters for constraints
    model.calcium_milk = Param(initialize=40)
    model.calcium_veggie = Param(initialize=15)
    model.iron_milk = Param(initialize=25)
    model.iron_veggie = Param(initialize=30)
    
    # Right-hand sides and variable upper bounds
    model.calcium_min = Param(initialize=100)
    model.iron_min = Param(initialize=50)
    model.x_ub = Param(initialize=1000) # Large upper bound for practical purposes
    model.y_ub = Param(initialize=1000)
    
    # Decision Variables
    def x_bounds(m):
        return (0, m.x_ub)
    def y_bounds(m):
        return (0, m.y_ub)
    model.x = Var(bounds=x_bounds, domain=NonNegativeReals)
    model.y = Var(bounds=y_bounds, domain=NonNegativeReals)

    # Constraints
    def calcium_constraint(m):
        return m.calcium_milk * m.x + m.calcium_veggie * m.y >= m.calcium_min
    model.calcium_constraint = Constraint(rule=calcium_constraint)
    
    def iron_constraint(m):
        return m.iron_milk * m.x + m.iron_veggie * m.y >= m.iron_min
    model.iron_constraint = Constraint(rule=iron_constraint)

    # Objective: Minimize cost
    def total_cost(m):
        return m.c_milk * m.x + m.c_veggie * m.y
    model.obj = Objective(rule=total_cost, sense=minimize)

    # ===== Solver Execution =====
    # Solver: Use GLPK if available, else try CBC.
    status = None
    termination = None
    x_val = None
    y_val = None
    obj_val = None
    solver_name = "glpk"
    try:
        solver = SolverFactory(solver_name)
        results = solver.solve(model, tee=False)
        status = str(results.solver.status)
        termination = str(results.solver.termination_condition)
    except Exception:
        # Try CBC if GLPK fails
        solver_name = "cbc"
        try:
            solver = SolverFactory(solver_name)
            results = solver.solve(model, tee=False)
            status = str(results.solver.status)
            termination = str(results.solver.termination_condition)
        except Exception as e:
            print("Solver Error:", str(e))
            print("Neither GLPK nor CBC is available.")
            return {
                "solver_status": "Error",
                "termination": str(e),
                "x": None,
                "y": None,
                "objective": None,
                "filename": "milk_veggies_optimizer.py"
            }
    # ===== Value Extraction and Reporting =====
    try:
        x_val = value(model.x)
        y_val = value(model.y)
        obj_val = value(model.obj)
        # Verification of feasibility
        constraints_ok = (
            model.calcium_milk()*x_val + model.calcium_veggie()*y_val >= model.calcium_min()
            and model.iron_milk()*x_val + model.iron_veggie()*y_val >= model.iron_min()
            and x_val >= 0 and y_val >= 0
        )
    except Exception as e:
        print("Value extraction error:", str(e))
        x_val = None
        y_val = None
        obj_val = None
        constraints_ok = False

    print("===== Solution Report (milk_veggies_optimizer.py) =====")
    print("Solver used     :", solver_name.upper())
    print("Solver status   :", status)
    print("Termination     :", termination)
    print("Objective value :", obj_val)
    print("x (milk)        :", x_val)
    print("y (veggie)      :", y_val)
    print("File            : milk_veggies_optimizer.py")
    if not constraints_ok:
        print("WARNING: Solution may not be feasible!")
    print("========================================================")
    return {
        "solver_status": status,
        "termination": termination,
        "x": x_val,
        "y": y_val,
        "objective": obj_val,
        "filename": "milk_veggies_optimizer.py"
    }
