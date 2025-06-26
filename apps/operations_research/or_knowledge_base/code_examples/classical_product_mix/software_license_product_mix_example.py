# solve_license_optimization.py
from pyomo.environ import *

def solve_license_optimization():
    model = ConcreteModel()
    # Decision variables: x = # personal, y = # commercial (integer)
    model.x = Var(within=NonNegativeIntegers)
    model.y = Var(within=NonNegativeIntegers)

    # Objective: maximize profit
    model.profit = Objective(expr=450*model.x + 1200*model.y, sense=maximize)

    # Constraints
    model.cost_constraint = Constraint(expr=550*model.x + 2000*model.y <= 400000)
    model.license_constraint = Constraint(expr=model.x + model.y <= 300)

    solver = SolverFactory("glpk")
    result = solver.solve(model)
    x_opt, y_opt = int(value(model.x)), int(value(model.y))
    max_profit = value(model.profit)
    print(f"Optimal: Personal Licenses: {x_opt}, Commercial Licenses: {y_opt}, Max Profit: ${max_profit:,.0f}")
    return x_opt, y_opt, max_profit

if __name__ == "__main__":
    solve_license_optimization()
