# Smoothie Blend Optimization with Resource and Proportion Constraints

**Problem:**  
A smoothie shop wants to produce two types of smoothies (acai berry and banana chocolate) while minimizing total water used. Each type has different raw material requirements. Special constraints: banana chocolate smoothies must be more numerous, but at least 35% of all smoothies must be acai berry. Supplies of acai berries, banana chocolate mix, and water are limited.

**Formulation (LP):**  
Variables:  
- x = number of acai berry smoothies  
- y = number of banana chocolate smoothies

Minimize: 3x + 4y (water units used)

Subject to:  
- 7x <= 3500 (acai berries constraint)  
- 6y <= 3200 (banana chocolate constraint)  
- y >= x + 1 (banana chocolate smoothies more numerous)  
- x >= 0.35(x + y) (at least 35% acai berry smoothies)  
- x, y >= 0  

**Additional notes:**
- The 35% acai constraint can be linearized as 13x - 7y >= 0.
- In the original solution, the variables were continuous. If integers are needed, rounding or integer programming would be necessary.
- The Pyomo code is available in `water_optimization_model.py`.
- Solver used: GLPK (linear programming).

**Objective value (water minimized):** ~12.17 (continuous solution, x ~= 1.17, y ~= 2.17).

**Keywords:** resource allocation, blending, linear programming, proportion constraint, supply constraint, Pyomo, GLPK.

