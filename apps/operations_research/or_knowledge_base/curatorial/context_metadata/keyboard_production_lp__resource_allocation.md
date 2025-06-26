# File: textual_knowledge/keyboard_production_lp.md
This file describes a classic two-product resource allocation linear programming (LP) problem in the context of manufacturing digital keyboards. It contains:
- Quantitative problem setup (parameters for full-weighted and semi-weighted keyboards, resource limits)
- Mathematical formulation (variables, constraints, integer requirement)
- Optimal solution and binding constraint analysis
- Explicit reference to a Pyomo model implementing this problem.

This document is relevant for anyone designing, studying, or solving manufacturing LP or MILP problems where the goal is to maximize profit given resource and time constraints. This includes education, benchmarking, or real-world planning of factories with two or more similar products and shared resource limits.

# File: code_examples/integer_LP/keyboard_lp_pyomo.py
This Python file contains a reusable Pyomo model for solving two-product integer LP profit maximization problems with resource and time constraints. Its key features are:
- Clean definition of decision variables, objective, and constraints for a production planning scenario
- Integer/binary requirement for product variables
- An objective function to maximize profit
- Solver and solution extraction ready for use in larger scripts or notebooks
- Adaptability to related resource-constrained manufacturing LP/MILP problems

This code is highly relevant for operational researchers, optimization engineers, and educators dealing with resource allocation, scheduling, and profit maximization in multi-product settings under capacity or time limitations.

# Keywords/tags:
resource allocation, linear programming, manufacturing, production planning, integer programming, Pyomo, profit maximization, factory, resource constraints, operation research, two products, modeling, MILP, education, code example, documentation
