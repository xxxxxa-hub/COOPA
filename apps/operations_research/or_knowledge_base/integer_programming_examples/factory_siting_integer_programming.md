# Factory Siting Integer Programming OR Model (Cell Phones Example)

## Problem Statement
A cell phone company must decide how many rural and urban factories to build:
- Each rural factory produces 100 phones/day, requires 8 managers.
- Each urban factory produces 200 phones/day, requires 20 managers.
- Maximum available managers: 260
- Required daily phone production: at least 3000
- Objective: Minimize total number of factories

## Model: Integer Programming
### Variables:
- x: number of rural factories (integer ¡Ý 0)
- y: number of urban factories (integer ¡Ý 0)

### Constraints:
- **Manager limitation:** 8x + 20y ¡Ü 260
- **Production requirement:** 100x + 200y ¡Ý 3000

### Objective:
- Minimize x + y

## Solution Approach
Formulate as Mixed-Integer Linear Programming (MILP). Model can be solved with Pyomo (Python) and GLPK solver.

- Optimal solution: x=20, y=5
    - Total factories: 25
    - Managers used: 260
    - Phones produced: 3000

## Pyomo/GLPK Best Practices
- Use integer `Var` for x and y
- Constraints as indicated
- Minimize objective
- Recommended script filename: `factory_siting_pyomo.py`

## Verification
- All constraints meet limits at bounds, confirming efficiency and optimality.
