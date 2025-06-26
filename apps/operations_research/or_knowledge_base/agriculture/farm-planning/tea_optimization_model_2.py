from pyomo.environ import ConcreteModel, Var, Objective, Constraint, NonNegativeReals, SolverFactory

def tea_lp_model():
    model = ConcreteModel()
    # Variables: x = acres with traditional, y = acres with modern
    model.x = Var(domain=NonNegativeReals)
    model.y = Var(domain=NonNegativeReals)
    # Objective: maximize total tea picked
    model.obj = Objective(expr=30*model.x + 40*model.y, sense=1)
    # Constraints
    model.acreage = Constraint(expr=model.x + model.y <= 500)
    model.fuel = Constraint(expr=20*model.x + 15*model.y <= 9000)
    model.waste = Constraint(expr=10*model.x + 15*model.y <= 6000)
    return model

if __name__ == '__main__':
    model = tea_lp_model()
    solver = SolverFactory('glpk')
    result = solver.solve(model)
    print('Traditional acres:', model.x.value)
    print('Modern acres:', model.y.value)
    print('Maximum tea:', model.obj.expr())
