Title: Production Planning LP Template and Flooring Company Example

Content:
This addition provides a general-purpose linear programming (LP) template for production/profit maximization problems with resource, demand, and contractual constraints, as well as a fully worked example based on a flooring company scenario.

1. General LP Template (Production/Profit Maximization):

- Variables: Quantities of products to produce/sell (x1, x2, ..., xn).
- Objective: Maximize total profit = sum(profit_i * xi)
- Constraints:
    - Demand constraints (xi >= demand_min for each product)
    - Resource/capacity constraints (xi <= capacity_max for each product)
    - Combined contractual/minimum shipment constraints (sum(xi) >= total_min)
    - Non-negativity (xi >= 0)
- Solvable by algebraic modeling languages (e.g., Pyomo).

2. Flooring Company Example:

- x = square feet of laminate planks produced weekly
- y = square feet of carpets produced weekly

Objective:
    Maximize Profit = 2.1 * x + 3.3 * y

Subject to:
    x >= 15,000           (laminate demand)
    y >= 5,000            (carpet demand)
    x + y >= 50,000       (shipping contract)
    x <= 40,000           (laminate cap)
    y <= 20,000           (carpet cap)
    x, y >= 0

Optimal Solution:
    x = 40,000
    y = 20,000
    Maximum profit = $150,000

See 'laminate_carpet_max_profit.py' for complete Pyomo code.

Use this template and example for future LP modeling of production/resource allocation problems with similar structure.
