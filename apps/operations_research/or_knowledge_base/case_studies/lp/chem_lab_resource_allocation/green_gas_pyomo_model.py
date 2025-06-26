"""

==============================================================================
Linear Program Model Summary (Five-Element Format)
==============================================================================

1. Objective:
   Maximize the total amount of green gas produced by choosing the number of times each experiment is performed.

2. Variables:
   x1: Number of times experiment 1 is performed (continuous, x1 >= 0)
   x2: Number of times experiment 2 is performed (continuous, x2 >= 0)

3. Constraints:
   - 3*x1 + 5*x2 <= 80     # Total red liquid used cannot exceed available supply
   - 4*x1 + 3*x2 <= 70     # Total blue liquid used cannot exceed available supply
   - 1*x1 + 2*x2 <= 10     # Total smelly gas produced cannot exceed allowed limit

4. Sets/Parameters:
   All coefficients and resource limits are set as model parameters (see code).

5. Additional Notes:
   - The model allows fractional (continuous) values of x1, x2.
   - Implementation uses the Pyomo modeling language.
   - The GLPK solver is assumed to be available.

==============================================================================

"""

# ===== Imports =====
from pyomo.environ import ConcreteModel, Var, Param, Constraint, Objective, SolverFactory, NonNegativeReals, value

def solve_green_gas_maximization():
    # ===== Model Definition =====
    model = ConcreteModel()
    
    # ==== Parameters ====
    model.red_coeff = Param(initialize=3)   # red liquid per experiment 1
    model.red_coeff2 = Param(initialize=5)  # red liquid per experiment 2
    model.red_limit = Param(initialize=80)
    
    model.blue_coeff = Param(initialize=4)  # blue liquid per experiment 1
    model.blue_coeff2 = Param(initialize=3) # blue liquid per experiment 2
    model.blue_limit = Param(initialize=70)
    
    model.smelly_coeff = Param(initialize=1)   # smelly gas per experiment 1
    model.smelly_coeff2 = Param(initialize=2)  # smelly gas per experiment 2
    model.smelly_limit = Param(initialize=10)
    
    model.green_coeff = Param(initialize=5)    # green gas per experiment 1
    model.green_coeff2 = Param(initialize=6)   # green gas per experiment 2
    
    # ===== Variables =====
    model.x1 = Var(domain=NonNegativeReals)
    model.x2 = Var(domain=NonNegativeReals)
    
    # ===== Constraints =====
    def red_constraint(m):
        return m.red_coeff * m.x1 + m.red_coeff2 * m.x2 <= m.red_limit
    model.red_con = Constraint(rule=red_constraint)
    
    def blue_constraint(m):
        return m.blue_coeff * m.x1 + m.blue_coeff2 * m.x2 <= m.blue_limit
    model.blue_con = Constraint(rule=blue_constraint)
    
    def smelly_constraint(m):
        return m.smelly_coeff * m.x1 + m.smelly_coeff2 * m.x2 <= m.smelly_limit
    model.smelly_con = Constraint(rule=smelly_constraint)
    
    # ===== Objective =====
    def green_gas_objective(m):
        return m.green_coeff * m.x1 + m.green_coeff2 * m.x2
    model.obj = Objective(rule=green_gas_objective, sense=1) # 1 means maximize
    
    # ===== Solver Execution =====
    solver = SolverFactory('glpk')
    result = solver.solve(model)
    
    # ===== Results Extraction =====
    # Extract solver status and values
    status = str(result.solver.status)
    termination = str(result.solver.termination_condition)
    
    x1_val = value(model.x1)
    x2_val = value(model.x2)
    obj_val = value(model.obj)
    
    output = {}
    output['solver_status'] = status
    output['termination_condition'] = termination
    output['x1'] = x1_val
    output['x2'] = x2_val
    output['objective_value'] = obj_val
    return output
