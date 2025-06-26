# Electronics Store Inventory Optimization Problem (LP Formulation)

**Problem (2024-06):**
- Store sells only phones (profit $120, 1 sq ft, $400 cost) and laptops (profit $40, 4 sq ft, $100 cost).
- Max floor space: 400 sq ft.
- Budget: $6000 max to stock inventory.
- At least 80% of stocked items (by count) must be laptops.

**LP Formulation:**
Let x = number of phones, y = number of laptops.

Maximize: 120 x + 40 y

Subject to:
- x + 4y <= 400      (floor space)
- 400x + 100y <= 6000  (budget)
- y >= 0.8 (x + y)    (80% of all inventory must be laptops) <=> y >= 4x
- x >= 0, y >= 0

**Solution discovered (using Pyomo/GLPK):**
- The only feasible solution (as of stated params/constraints) was x = 0, y = 0; i.e., no inventory is stocked, maximum profit is 0.
- Reason: the combination of constraints, especially y >= 4x, budget, and floor space, is too restrictive.

**Takeaway:**  
When modeling inventory mix problems with severe percentage and budget constraints, feasible region may be empty/non-useful unless parameters are checked for compatibility.

(Stored: 2024-06)
