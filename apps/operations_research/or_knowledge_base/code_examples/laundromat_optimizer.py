
# ===============================================================
# Five-Element Model Summary
# ===============================================================
#
# Objective:
#   Minimize the total number of washing machines: x + y
#
# Variables:
#   x: Number of top-loading machines (Integer, x >= 0)
#   y: Number of front-loading machines (Integer, y >= 0)
#
# Constraints:
#   1. Capacity constraint:   50*x + 75*y >= 5000
#   2. Energy constraint:     85*x + 100*y <= 7000
#   3. Mix constraint:        x <= 0.4 * (x + y)    [i.e., at most 40 percent are top-loading]
#   4. Minimum front-loaders: y >= 10
#
# Sets/Parameters:
#   - Capacity per top-loader:        a = 50
#   - Capacity per front-loader:      b = 75
#   - Total minimum capacity:         c = 5000
#   - Energy per top-loader:          d = 85
#   - Energy per front-loader:        e = 100
#   - Maximum total energy:           f = 7000
#   - Max proportion top-loaders:     p = 0.4
#   - Minimum number of front-loaders:min_y = 10
#
# Additional Notes:
#   - All variables are integer-valued (Integral).
#   - All constraints and parameters formulated using Pyomo Param objects.
#   - Script intended for Pyomo and standard open-source solvers (glpk or cbc).
#   - Model is self-contained and uses only ASCII characters.
#
# ===============================================================

from pyomo.environ import ConcreteModel, Var, Param, Constraint, Objective, SolverFactory, value, Integers, minimize

def solve_laundromat_optimization():
    # ===== Model Definition =====
    model = ConcreteModel()

    # ---- Parameters ----
    model.a = Param(initialize=50)           # capacity per top-loader
    model.b = Param(initialize=75)           # capacity per front-loader
    model.c = Param(initialize=5000)         # required minimum capacity
    model.d = Param(initialize=85)           # energy per top-loader
    model.e = Param(initialize=100)          # energy per front-loader
    model.f = Param(initialize=7000)         # max allowed energy usage
    model.p = Param(initialize=0.4)          # max fraction top-loaders
    model.min_y = Param(initialize=10)       # minimum front-loaders

    # ---- Variables ----
    model.x = Var(domain=Integers, bounds=(0, None))
    model.y = Var(domain=Integers, bounds=(model.min_y, None))

    # ---- Constraints ----

    # 1. Capacity: a*x + b*y >= c
    def capacity_rule(m):
        return m.a * m.x + m.b * m.y >= m.c
    model.capacity_con = Constraint(rule=capacity_rule)

    # 2. Energy: d*x + e*y <= f
    def energy_rule(m):
        return m.d * m.x + m.e * m.y <= m.f
    model.energy_con = Constraint(rule=energy_rule)

    # 3. Mix constraint: x <= p * (x + y)
    def mix_rule(m):
        # Rearranged: (1 - p)*x - p*y <= 0
        return (1 - m.p) * m.x - m.p * m.y <= 0
    model.mix_con = Constraint(rule=mix_rule)

    # 4. Minimum front-loaders: y >= min_y  [enforced by variable bound]

    # ---- Objective ----
    def obj_rule(m):
        return m.x + m.y
    model.obj = Objective(rule=obj_rule, sense=minimize)

    # ===== Solver Execution =====

    # Try to use glpk if available, else cbc
    for solver_name in ["glpk", "cbc"]:
        if SolverFactory(solver_name).available():
            solver = SolverFactory(solver_name)
            break
    else:
        return {
            "solver_status": "error",
            "message": "No suitable solver (glpk/cbc) available. Please install glpk or cbc."
        }

    result = solver.solve(model, tee=False)

    # ===== Value Extraction =====
    solver_status = str(result.solver.status)
    solver_termination = str(result.solver.termination_condition)

    if solver_termination.lower() not in ["optimal", "feasible"]:
        # Infeasible or other problem; gather details
        return {
            "solver_status": solver_status,
            "solver_termination": solver_termination,
            "message": "Problem not solved to optimality. Try relaxing or double-checking your constraints and parameters."
        }
    # Solution found
    total_machines = int(round(value(model.x) + value(model.y)))
    optimal_x = int(round(value(model.x)))
    optimal_y = int(round(value(model.y)))
    objective_value = value(model.obj)

    return {
        "solver_status": solver_status,
        "solver_termination": solver_termination,
        "objective_value": objective_value,
        "total_machines": total_machines,
        "x_opt": optimal_x,
        "y_opt": optimal_y,
        "filename": "laundromat_optimizer.py"
    }
