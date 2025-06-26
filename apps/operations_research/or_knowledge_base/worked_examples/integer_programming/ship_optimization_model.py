
# ================================================================
# MODEL SUMMARY (Five-Element Format)
# ================================================================
# Objective:
#     Minimize the total number of ships (L + S), where L is the number of large ships, and S is the number of small ships.
#
# Variables:
#     L: Integer variable, number of large ships, L >= 0
#     S: Integer variable, number of small ships, S >= 0
#
# Constraints:
#     1. 500*L + 200*S >= 3000    (Total shipping capacity requirement)
#     2. L <= S                   (No more large ships than small ships)
#     3. L >= 0, integer
#     4. S >= 0, integer
#
# Sets/Parameters:
#     Parameters are provided as model Params within Pyomo:
#         - large_capacity = 500 (capacity per large ship)
#         - small_capacity = 200 (capacity per small ship)
#         - total_required = 3000 (total required shipping capacity)
#
# Additional Notes:
#     - Only integer, non-negative solutions are permissible.
#     - All model data is defined using Pyomo Param objects; no raw Python data is used in constraint or objective expressions.
#     - This script requires an open-source MILP solver accessible to Pyomo (e.g., GLPK, CBC).
#
# ================================================================
# MODEL DEFINITION AND SOLVER FUNCTION
# ================================================================
from pyomo.environ import (
    ConcreteModel, Param, Var, Constraint, Objective, SolverFactory, NonNegativeIntegers, minimize, value
)

def solve_ship_model():
    # ==============================
    # Model Definition
    # ==============================
    model = ConcreteModel()

    # Parameters
    model.large_capacity = Param(initialize=500)
    model.small_capacity = Param(initialize=200)
    model.total_required = Param(initialize=3000)

    # Variables
    model.L = Var(within=NonNegativeIntegers)
    model.S = Var(within=NonNegativeIntegers)

    # Constraints
    def capacity_constraint(m):
        return m.large_capacity * m.L + m.small_capacity * m.S >= m.total_required
    model.capacity_constraint = Constraint(rule=capacity_constraint)

    def ratio_constraint(m):
        return m.L <= m.S
    model.ratio_constraint = Constraint(rule=ratio_constraint)

    # Objective
    model.obj = Objective(expr=model.L + model.S, sense=minimize)

    # ==============================
    # Solver Execution
    # ==============================
    solver = None
    for solver_name in ["cbc", "glpk"]:
        if SolverFactory(solver_name).available():
            solver = SolverFactory(solver_name)
            break
    if solver is None:
        return {
            "status": "failed",
            "termination_condition": "No suitable MILP solver found (requires CBC or GLPK).",
            "objective": None,
            "L": None,
            "S": None,
            "details": "Ensure a solver like GLPK or CBC is installed and accessible to Pyomo."
        }
    result = solver.solve(model, tee=False)

    # Extract solver info
    status = str(result.solver.status)
    termination = str(result.solver.termination_condition)

    # Check optimality
    if termination.lower() != "optimal":
        return {
            "status": status,
            "termination_condition": termination,
            "objective": None,
            "L": None,
            "S": None,
            "details": "Non-optimal termination. Check data/model."
        }

    objective_value = value(model.obj)
    L_value = value(model.L)
    S_value = value(model.S)

    return {
        "status": status,
        "termination_condition": termination,
        "objective": objective_value,
        "L": L_value,
        "S": S_value,
        "details": "Optimal solution found."
    }
