README: banana_combo_ilp.py

Summary: Pyomo integer program for finding the optimal mix of packages (products, bundles, combos) to maximize profit subject to resource consumption and stock constraints.

File: banana_combo_ilp.py
- Contains a complete, parametric, and reproducible Pyomo model for profit maximization using two package types with resource/ingredient constraints (generic archatype for integer programming).
- Integer variables represent the number of each package type produced subject to limited stock of 3 ingredients.
- Easy to adapt for similar use cases (product mix, store liquidation, bundle selection, production with limiting resources etc).
- Includes formulae, constraint method, and sample data; suitable for extension or adaptation to other problems requiring resource-constrained combinatorial optimization.

Related files:
- This folder also contains related integer LP examples (e.g., keyboard_lp_pyomo.py, pyomo_integer_resource_allocation_template.md).

Usage:
- The model can be modified for more package types, resources, or different profit and recipe coefficients as needed.

See banana_combo_ilp.py for detailed documentation and example usage.