# Food Delivery Shift Scheduling Integer Program (Maximize Tips)

## Description
This entry documents a canonical integer linear programming formulation and solution approach for the shift scheduling and tips maximization problem for food delivery workers who can choose between two transport modes (bikes and scooters), each having different energy usage, revenue, and minimum requirements. 

The formulation is suitable as a template for similar workforce scheduling, energy-constrained assignment, and resource allocation optimization problems. The problem is modeled and solved in Python using Pyomo and GLPK, and all key parameters, variables, constraints, and objectives are provided in the referenced implementation.

### Model Structure and Features
- **Decision Variables**: Integer (number of shifts assigned to bikes and scooters)
- **Objective Function**: Maximize total tips earned across all shifts
- **Constraints**:
    - Overall limit on number of shifts
    - Total energy budget constraint
    - Minimum required number of orders
    - Required minimum number of shifts on at least one transport type
    - Integrality (variables are integer)
- **Implementation**: Pyomo (Python optimization modeling language)
- **Solver**: GLPK (open-source mixed-integer programming solver)
- **Sample Instance - Optimal Value**: 1965 (see referenced script for parameter details and output)

### Key Files
- **ilp_max_tips_model.py**: Contains the full Pyomo model for this shift scheduling and tips maximization problem. Store and reference this script for adaptation to related problems.

### Use case tags
shift-scheduling, workforce assignment, integer-programming, Pyomo, resource allocation, tips maximization

---

For more details and the complete code, see `code_examples/ilp_max_tips_model.py` in this knowledge base.
