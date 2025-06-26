# Production Planning: Ingredient Constraints and Proportions (Reference Note)
**Timestamp:** 2025-05-19 14:14:52.448589

---

## Integer Programming Example: Crepe Production with Ingredient Constraints

### Problem Template
A food shop makes two types of food (e.g., crepes) each needing specific quantities of ingredients (e.g., spread, mix). There may be minimum, maximum, percentage, or ratio constraints between product types. The objective is often to minimize or maximize use of a particular resource.

### Variables
- Let x = number of item A (e.g., chocolate crepes)
- Let y = number of item B (e.g., peanut butter crepes)

### Typical Constraints
- Ingredient availability: coeff_a*x + coeff_b*y <= resource_limit
- Ratio (e.g., peanut > chocolate, strictly): y >= x + 1
- Minimum proportion (e.g., at least 25% are chocolate): 
    x >= 0.25 * (x + y) 
    => rearranged to: 3x >= y
- Non-negativity and integrality: x, y >= 0, integer

### Objective
- Minimize total key resource use: total = c1*x + c2*y

### Pyomo Modeling Tips
- Strict inequalities for integers (y > x) are modeled as y >= x + 1.
- "At least P% of total" for variable x: x >= (P/100) * (x + y) => (1-P)*x >= P*y (when rearranged).
- All input resource constraints and product ratio constraints can be written naturally.
- Use integer variables if fractions are not meaningful.

### Example (from crepe shop):
Minimize: 6x + 7y
Subject to:
    3x <= 400
    4y <= 450
    y >= x + 1
    3x >= y
    x, y >= 0 and integer

### Application
This template directly supports production planning, menu optimization, resource allocation, etc., especially when one product must be more popular and a minimum proportion of another required.

---

**For rapid reference in food production and resource allocation modeling and teaching. Adapt for other integer programming planning contexts as needed.**
