# Scooter and Rickshaw Optimization Problem
#
# Structured summary:
#
# Objective:
#   Minimize the number of scooters (x) needed to transport at least 300 people,
#   allowing the use of rickshaws (y), with at most 40% of all vehicles being rickshaws.
#
# Decision Variables:
#   x : integer >= 0 : number of scooters
#   y : integer >= 0 : number of rickshaws
#
# Constraints:
#   1. 2*x + 3*y >= 300     # Total transport capacity
#   2. For x + y > 0: y / (x + y) <= 0.4  # At most 40% of vehicles are rickshaws
#       This is equivalent to: y <= 0.4*(x + y)
#       Rearranged: 0.6*y <= 0.4*x  or  3*y <= 2*x
#       Final linear form for integers: 3*y <= 2*x
#   3. x, y >= 0 and integer
#
# Parameters:
#   - Scooters carry 2 people
#   - Rickshaws carry 3 people
#   - Need to transport at least 300 people
#
# Special requirements:
#   - Use OR-Tools and encode all logic using only standard ASCII
#
# ------------------ OR-Tools CP-SAT implementation ------------------

from ortools.sat.python import cp_model

def solve_problem():
    model = cp_model.CpModel()

    # Decision variables
    x = model.NewIntVar(0, 1000, 'x')  # scooters (upper bound reasonably large)
    y = model.NewIntVar(0, 1000, 'y')  # rickshaws (upper bound reasonably large)

    # Constraint 1: Transport at least 300 people
    model.Add(2 * x + 3 * y >= 300)
    # Constraint 2: At most 40% of vehicles can be rickshaws (if x + y > 0)
    # For x + y == 0, no vehicles needed (solution will always use at least some).
    # Linearized: 3*y <= 2*x
    model.Add(3 * y <= 2 * x)

    # Objective: Minimize x
    model.Minimize(x)

    # Solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        # Results:
        result = dict()
        result['x'] = solver.Value(x)
        result['y'] = solver.Value(y)
        result['total_vehicles'] = solver.Value(x) + solver.Value(y)
        result['scooter_capacity'] = 2 * solver.Value(x)
        result['rickshaw_capacity'] = 3 * solver.Value(y)
        result['total_capacity'] = result['scooter_capacity'] + result['rickshaw_capacity']
        result['fraction_rickshaws'] = (solver.Value(y) / result['total_vehicles']) if result['total_vehicles'] > 0 else 0
        result['status'] = 'OPTIMAL' if status == cp_model.OPTIMAL else 'FEASIBLE'
        return result
    else:
        return {'status': 'INFEASIBLE_OR_UNBOUNDED'}

if __name__ == '__main__':
    solution = solve_problem()
    print('Solution:', solution)
