Problem: Factory Space Allocation LP ("Bootleg Phones and Laptops" Problem)

Description:
A factory with 100 sq. ft. makes bootleg phones and laptops. Phones require 2 hours labor/sq. ft., cost $12/sq. ft., and generate net revenue of $50/sq. ft. Laptops require 3 hours labor/sq. ft., cost $15/sq. ft., and generate net revenue of $70/sq. ft. Factory is limited to $5000 and 2000 labor hours. Maximize revenue by allocating floor space (x = phones, y = laptops).

Mathematical model:
Variables: x, y >= 0 (sq. ft. allocated)
    x + y <= 100         # Space constraint
    12x + 15y <= 5000    # Cost constraint
    2x + 3y <= 2000      # Labor constraint
Objective: Maximize 50x + 70y

Result: The given parameters only admit the trivial (zero) solution. The constraints are so tight that the only feasible solution is x = y = 0 (zero allocation, zero revenue).
Suggestions: Carefully check the constraint upper bounds in future similar problems.

Pyomo code is included below.
