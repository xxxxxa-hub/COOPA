"""
Five-element model summary:

Objective:
    Maximize total revenue from allocating factory space to phones and laptops.

Variables:
    x: Square feet allocated to phones (continuous, >= 0)
    y: Square feet allocated to laptops (continuous, >= 0)

Constraints:
    1. x + y <= SPACE_MAX          (Space constraint)
    2. 12*x + 15*y <= COST_MAX     (Cost constraint)
    3. 2*x + 3*y <= LABOR_MAX      (Labor constraint)
    4. x >= X_LB
    5. y >= Y_LB

Sets/Parameters:
    REVENUE_X = 50         (Revenue per sq. ft. for phones)
    REVENUE_Y = 70         (Revenue per sq. ft. for laptops)
    SPACE_MAX = 100        (Total space available)
    COST_X = 12            (Cost per sq. ft. for phones)
    COST_Y = 15            (Cost per sq. ft. for laptops)
    COST_MAX = 5000        (Total cost limit)
    LABOR_X = 2            (Labor per sq. ft. for phones)
    LABOR_Y = 3            (Labor per sq. ft. for laptops)
    LABOR_MAX = 2000       (Labor hours available)
    X_LB = 0               (Minimum x)
    Y_LB = 0               (Minimum y)

Additional notes:
    - All parameters are implemented as Pyomo Param objects.
    - Variable lower bounds implemented via Params.
    - The GLPK (open-source) MILP solver is used if present.
    - Feasibility, boundedness, and solution status are explicitly reported.

"""

# ===== Imports =====
from pyomo.environ import ConcreteModel, Param, Var, Objective, Constraint, NonNegativeReals, SolverFactory, value

# ===== Model Definition =====
def solve_factory_allocation():
    # Model
    model = ConcreteModel()

    # Parameters
    model.REVENUE_X = Param(initialize=50)
    model.REVENUE_Y = Param(initialize=70)
    model.SPACE_MAX = Param(initialize=100)
    model.COST_X = Param(initialize=12)
    model.COST_Y = Param(initialize=15)
    model.COST_MAX = Param(initialize=5000)
    model.LABOR_X = Param(initialize=2)
    model.LABOR_Y = Param(initialize=3)
    model.LABOR_MAX = Param(initialize=2000)
    model.X_LB = Param(initialize=0)
    model.Y_LB = Param(initialize=0)

    # Variables (non-negative continuous)
    model.x = Var(within=NonNegativeReals, bounds=(model.X_LB, None))
    model.y = Var(within=NonNegativeReals, bounds=(model.Y_LB, None))

    # Objective: Maximize revenue
    def revenue_rule(m):
        return m.REVENUE_X * m.x + m.REVENUE_Y * m.y
    model.revenue = Objective(rule=revenue_rule, sense=1)  # 1 == maximize

    # Constraints
    def space_constraint(m):
        return m.x + m.y <= m.SPACE_MAX
    model.space_con = Constraint(rule=space_constraint)

    def cost_constraint(m):
        return m.COST_X * m.x + m.COST_Y * m.y <= m.COST_MAX
    model.cost_con = Constraint(rule=cost_constraint)

    def labor_constraint(m):
        return m.LABOR_X * m.x + m.LABOR_Y * m.y <= m.LABOR_MAX
    model.labor_con = Constraint(rule=labor_constraint)

    # ===== Solver Execution =====
    # Try GLPK first, fall back to CBC if needed
    solvers_to_try = ["glpk", "cbc"]
    solver_loaded = False
    for sname in solvers_to_try:
        solver = SolverFactory(sname)
        if solver.available():
            solver_loaded = True
            break
    if not solver_loaded:
        return {
            "status": "error",
            "termination": "No suitable open-source LP solver (GLPK or CBC) available.",
            "objective": None,
            "x": None,
            "y": None,
            "file": "factory_lp_model.py"
        }

    results = solver.solve(model)
    # ===== Results Extraction =====
    try:
        status = results.solver.status
        termination = results.solver.termination_condition
    except Exception as e:
        status = "unknown"
        termination = str(e)
    # Handle infeasible/unbounded/other bad outcomes
    if str(termination).lower() not in ["optimal", "feasible"]:
        return {
            "status": str(status),
            "termination": str(termination),
            "objective": None,
            "x": None,
            "y": None,
            "file": "factory_lp_model.py"
        }

    obj_value = value(model.revenue)
    x_value = value(model.x)
    y_value = value(model.y)

    return {
        "status": str(status),
        "termination": str(termination),
        "objective": obj_value,
        "x": x_value,
        "y": y_value,
        "file": "factory_lp_model.py"
    }


# Purpose: To provide a reference for future problems involving factory layout, space allocation, and resource-constrained LP modeling.
