# LP Template: Two-Product Profit Maximization with Shipping and Capacity Bounds

**Problem Structure:**  
- Maximize total profit from producing two flooring products (or similar) with per-unit profits.
- Each product has minimum and maximum weekly production constraints.
- There is a minimum total shipment constraint.
- Objective: Max profit = c1 * x1 + c2 * x2  
  Subject to:
    - x1_min <= x1 <= x1_max
    - x2_min <= x2 <= x2_max
    - x1 + x2 >= total_min
    - x1, x2 >= 0

**Code Resource:**  
See `linear_program_hardwood_vinyl.py` for an example of how to implement and solve this problem using Pyomo and GLPK solver in Python.

**Typical Use:**  
- Any two-product linear profit maximization with individual and total shipment/production bounds.

## Files
- linear_program_hardwood_vinyl.py : Full Pyomo model and driver code.
