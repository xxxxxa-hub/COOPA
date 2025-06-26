## Linear Programming Template: Meal Combo Production with Waste Constraints

### Problem Description
A restaurant offers several meal combos. Each meal type generates certain amounts of food waste and wrapping waste and requires time to cook. Regulatory upper bounds exist on both food and wrapping waste. Determine the production plan (number of each meal) that minimizes the total cooking time.

### Variables
- Let x_i = number of meal i to produce (continuous, x_i >= 0 or integer, as required)

### Parameters (per meal type i)
- c_i: cooking time per meal i (minutes)
- f_i: food waste per meal i (units)
- w_i: wrapping waste per meal i (units)
- F_max: maximum total food waste allowed (units)
- W_max: maximum total wrapping waste allowed (units)

### Objective
Minimize total cooking time:
    minimize sum_i c_i * x_i

### Constraints
- Food waste: sum_i f_i * x_i <= F_max
- Wrapping waste: sum_i w_i * x_i <= W_max
- Non-negativity: x_i >= 0 for all i (or integer, per specific case)

### Typical Insights
- If there is no minimum production requirement, the optimal strategy for minimizing cooking time may default to producing zero meals (trivial solution).
- To obtain a practical production plan, consider adding lower bounds such as minimum required meals or total meals constraints.

### Example (Original + Experimental Meal)
Variables:
x = original, y = experimental
c = [10, 15], f = [20, 25], w = [45, 35]
F_max = 800, W_max = 900

Formulation:
    minimize 10*x + 15*y
    subject to
        20*x + 25*y <= 800
        45*x + 35*y <= 900
        x >= 0, y >= 0

Optimal solution with no minimum requirement: x = 0, y = 0, objective = 0.
