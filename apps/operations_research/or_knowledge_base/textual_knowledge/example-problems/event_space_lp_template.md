# Science Fair Table Allocation LP Model (Maximizing Guests)

## Problem Structure
- **Objective:** Maximize the number of guests that the science fair can cater to, by selecting the number of two types of tables under various constraints.
- **Variables:**
    - x = number of circular tables
    - y = number of rectangular tables
- **Parameters for each table type:**
    - Circular table: 4 poster boards, 5 participants, serves 8 guests, occupies 15 units of space.
    - Rectangular table: 4 poster boards, 4 participants, serves 12 guests, occupies 20 units of space.

## Constraints
1. 5x + 4y >= total participants required (e.g., 500)
2. 4x + 4y >= total poster boards needed (e.g., 300)
3. 15x + 20y <= total space available (e.g., 1900)
4. x >= 0, y >= 0

## Objective Function
Maximize: 8x + 12y

## Solution Outline
- Formulate as a linear program (LP), relaxing integrality for tractability.
- Use a standard solver (e.g., Pyomo/GLPK).
- In the example instance with 500 participants, 300 poster boards, and 1900 units of space:
    - Optimal solution: x = 60.0, y = 50.0, guests = 1080.

## Best Practices
- If integer solutions are needed, change the LP variables to the integer domain.
- This formulation and parameterization is generalizable to similar "allocation under constraints" event planning problems.

## References
- See file: table_lp_model.py for the canonical model template.
