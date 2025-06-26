# Chocolate Shop Production Time Minimization (Operations Research LP Example)

## Problem Statement
A chocolate shop manufactures milk and dark chocolate bars. Each product uses cocoa and milk in specified amounts, with known production time per bar and limited total resources. Additionally, sales constraints require that at least twice as many milk chocolate bars as dark are produced. The goal is to minimize the total production time.

### Data
- Milk bar: 4 units cocoa, 7 units milk, 15 minutes bar
- Dark bar: 6 units cocoa, 3 units milk, 12 minutes bar
- Total available: 2000 cocoa, 1750 milk
- Sales: milk bars ¡Ý 2 ¡Á dark bars

## Mathematical Formulation

Let:  
x = # of milk chocolate bars  
y = # of dark chocolate bars

Minimize:  
    15x + 12y

Subject to:  
    4x + 6y ¡Ü 2000  
    7x + 3y ¡Ü 1750  
    x ¡Ý 2y  
    x ¡Ý 0, y ¡Ý 0

## Observations
The unconstrained LP minimizes to x=0, y=0 (no production), yielding a total time of zero. In practical settings, require x > 0 or y > 0.

## Pyomo Implementation Pattern

- Use ConcreteModel, Var, Objective, Constraint for direct resource allocation LPs.
- If minimizing objective allows zero output, consider adding production lower bounds.

## File
This knowledge comes from the "chocolate shop production time minimization" problem (June 2024).  
