# Pyomo Linear Programming Production Planning Example

This file contains a Python script implementing a linear programming (LP) production planning model using the Pyomo library. The model is structured around a classic resource-constrained machine scheduling and profit maximization scenario, allocating resources between two product lines (graph paper and music paper). It is intended as both a practical template and an educational example for:
- Production optimization
- Profit maximization with machine/resource constraints
- Machine scheduling in multi-product manufacturing
- Pyomo modeling practices

## Model Formulation
- Objective: Maximize profit: 4x + 2.5y
- Constraints:
    - Printing/scanning time: 3x + 1.5y <= 350
    - Binding time: 5.5x + 3y <= 350
    - x, y >= 0
  Where x = graph paper units, y = music paper units.

## Script Features
- Fully parameterized for flexibility and re-use.
- Provides clear instructions for how to run and extract results.
- Includes informative error handling for when required Pyomo solvers (such as GLPK or CBC) are not available.

## Solver Requirements
- Requires Pyomo and an installed LP solver compatible with Pyomo (such as GLPK or CBC). If no solver is available, the script exits with a clear error message.

---

**Purpose:**
To provide a robust, instructor-ready, and industry-applicable codebase for teaching or solving resource-constrained optimization problems in production planning and operations research. Relevant for queries involving production planning, machine allocation, resource-constrained LP, and as a Pyomo modeling example with solver dependencies.

See `pyomo_paper_lp_solver.py` in this folder for full code template.