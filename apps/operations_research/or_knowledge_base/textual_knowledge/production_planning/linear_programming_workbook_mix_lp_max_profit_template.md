Title: Linear Programming Template – Workbook (Production) Mix to Maximize Profit with Demand/Total Constraints

Summary: This scenario is common in operations research: Two (or more) product types, each with unit profit, minimum/maximum production bounds, and a combined minimum. Objective: maximize total profit. Solved as a linear program.

Template formulation:
Let x = number of product 1 (e.g., math workbooks)
Let y = number of product 2 (e.g., English workbooks)

Parameters:
p1 = profit per x
p2 = profit per y
x_min, x_max, y_min, y_max = production bounds
total_min = required combined production

Model:
maximize   profit = p1 * x + p2 * y
subject to:
   x_min <= x <= x_max
   y_min <= y <= y_max
   x + y >= total_min

Typical Pyomo/Python solution:
- Use Var domain=NonNegativeReals (or Integers if needed)
- Use positive objective coefficients for x and y
- Bound variables individually with param limits
- Add cumulative min constraint

Best practice: When maximizing, check if the solution is always at upper bounds of most profitable product(s), subject to total minimum constraint.

Use case: Printed workbook production, blending problems, minimum order requirements, etc.
Example script: See 'workbook_profit_optimization.py' in the working directory for a full example.
