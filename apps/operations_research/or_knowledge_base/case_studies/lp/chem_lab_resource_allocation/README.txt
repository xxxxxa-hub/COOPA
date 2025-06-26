[File: chem_lab_resource_allocation_lp.md]
This file contains a full problem statement, algebraic LP formulation, and a discussion of the degenerate solution resulting from a tight resource constraint in a chemical laboratory resource allocation scenario. This case is especially useful for understanding degenerate LP solutions and tight constraints in chemical/batch planning.

[File: green_gas_pyomo_model.py]
This file provides a Pyomo implementation of the chemical lab resource allocation problem described above, allowing users to model and solve this LP computationally. The code provides concrete reference for building and solving degenerate LP resource allocation problems in code.

Both files are intended for use as clear examples when teaching, diagnosing, or designing resource allocation models where degenerate solutions are possible due to multiple tight constraints.

Purpose: To serve as an accessible reference example for linear programming in resource allocation and chemistry experiments. The example is particularly valuable for cases with degeneracy due to very tight constraints.