## Linear Programming Template: Mixture/Blending Problem (Production/Resource Constraints)

**Problem structure:**
- Objective: Maximize total output (e.g., profit, amount of product, etc.) using available resources.
- Constraints: Each "recipe" or process requires fixed quantities of several resources and may generate byproducts/waste or other side limits.
- Variables: Number (possibly fractional) of times each process is run.

### Example problem (from solved case)
A summer camp combines ingredients in two beaker types to maximize slime production:
- Beaker 1: 4 flour, 6 liquid -> 5 slime, 4 waste
- Beaker 2: 6 flour, 3 liquid -> 3 slime, 2 waste
- Available: 150 flour, 100 liquid, max 30 waste

Let x = # of beaker 1 runs, y = # of beaker 2 runs.

#### Model:
Maximize: 5*x + 3*y
Subject to:
4x + 6y <= 150         (flour)
6x + 3y <= 100         (liquid)
4x + 2y <= 30          (waste)
x >= 0, y >= 0

#### Pyomo code snippet (for general problems with this structure):

**Best Practices:**
- Structure objectives and all constraints using model variables and parameters.
- Use Param or input data structures for coefficients if you want to create parameterized models.
- Single script can be re-used for similar problems by changing coefficients.
- The optimal solution may hit a "side" constraint (e.g., waste limit) rather than traditional resource limits.

**Reference:**  
This template originates from solving a "maximize slime given beaker recipes and resource/waste limits" problem (summer camp experiment context).
