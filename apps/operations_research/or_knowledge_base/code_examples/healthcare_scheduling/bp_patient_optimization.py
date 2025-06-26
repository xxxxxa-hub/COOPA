# Blood Pressure Patient Optimization Model
#
# Five-Element Model Overview:
#
# Objective:
#   Maximize the total number of patients (x + y) served under time and policy constraints.
#
# Variables:
#   x : Number of patients processed by automatic machine (integer, x >= 20)
#   y : Number of patients processed manually (integer, y >= 0)
#
# Constraints:
#   10*x + 15*y <= total_time          (Total processing time limit)
#   y >= 2*x                           (Manual at least two times automatic)
#   x >= 20                            (Minimum automatic patients)
#   x, y >= 0                          (Nonnegativity)
#   x, y integer                       (Integrality)
#
# Sets/Parameters:
#   total_time = 20000                 (Total available clinic time, minutes)
#   t_auto = 10                        (Automatic patient time, min)
#   t_manual = 15                      (Manual patient time, min)
#
# Additional Notes:
#   - Model uses Pyomo and GLPK solver.
#   - All parameters defined as model.Param().
#   - All output produced in plain ASCII and printed after the solve.

def solve_bp_patient_optimization():
    from pyomo.environ import ConcreteModel, Var, Param, Objective, Constraint, NonNegativeIntegers, maximize, SolverFactory, value
    # ===== Model Definition =====
    model = ConcreteModel()
    
    # Parameters
    model.t_auto = Param(initialize=10)
    model.t_manual = Param(initialize=15)
    model.total_time = Param(initialize=20000)
    model.x_min = Param(initialize=20)
    
    # Decision Variables
    model.x = Var(domain=NonNegativeIntegers, bounds=lambda m: (m.x_min, None))
    model.y = Var(domain=NonNegativeIntegers, bounds=(0, None))
    
    # Objective: Maximize total number of patients
    model.total_patients = Objective(expr=model.x + model.y, sense=maximize)
    
    # Constraint 1: Total processing time
    model.time_constraint = Constraint(expr= model.t_auto * model.x + model.t_manual * model.y <= model.total_time)
    
    # Constraint 2: Manual at least twice automatic
    model.manual_vs_auto = Constraint(expr= model.y >= 2 * model.x)
    
    # ===== Solver Execution =====
    # Attempt solver using GLPK (open-source integer solver)
    solver = SolverFactory('glpk')
    results = solver.solve(model, tee=False)
    
    # ===== Output Results =====
    # Capture status and termination reason
    status = results.solver.status
    termination = results.solver.termination_condition
    
    # If solve fails or is infeasible, print diagnosis and return results dictionary.
    if (termination != 'optimal') and (termination != 'feasible'):
        print('Solver status:', status)
        print('Termination condition:', termination)
        return {
            'status': str(status),
            'termination': str(termination),
            'message': 'The problem did not solve to optimality. Review constraints for infeasibility or solver limits.'
        }
    # Otherwise, collect optimal variable values
    opt_x = int(value(model.x))
    opt_y = int(value(model.y))
    opt_total = int(value(model.total_patients))
    time_used = model.t_auto.value * opt_x + model.t_manual.value * opt_y
    
    print('Solver status:', status)
    print('Termination condition:', termination)
    print('Objective value (maximum patients):', opt_total)
    print('Optimal x (automatic patients):', opt_x)
    print('Optimal y (manual patients):', opt_y)
    print('Total time used:', time_used, 'minutes (of', model.total_time.value, 'available)')
    
    results_dict = {
        'status': str(status),
        'termination': str(termination),
        'opt_x': opt_x,
        'opt_y': opt_y,
        'opt_total': opt_total,
        'time_used': time_used,
    }
    return results_dict