# School Transportation Pollution Minimization (Integer Programming)

## Problem Description
Children must travel to school using either vans or minibuses, and each vehicle type has a different capacity and pollution output. The objective is to determine the integer number of vans and minibuses required to transport at least 150 children, minimizing total pollution, with some operational restrictions.

- **Van**
    - Capacity: 6 children
    - Pollution: 7 units per van
- **Minibus**
    - Capacity: 10 children
    - Pollution: 10 units per minibus
- At least 150 children must be transported.
- At most 10 minibuses can be used.
- The number of vans used must be greater than the number of minibuses.

## Mathematical Model
- **Variables:**
    - x: integer (number of vans)
    - y: integer (number of minibuses)
- **Objective:**
    
        Minimize   7*x + 10*y

- **Constraints:**
    
        6*x + 10*y >= 150         # Ensure all children are transported
        y <= 10                   # At most 10 minibuses
        x >= y + 1                # More vans than minibuses
        x, y >= 0 integer

## Solution
The optimal solution (verified via Pyomo/GLPK) achieves a minimum total pollution of **160.0** units.

## Keywords
integer programming, school transport, resource allocation, pollution minimization, Pyomo, vehicle scheduling

## Code
See example implementation in the codebase: `code_examples_1/pollution_integer_model.py`

## Source
Curated and indexed by knowledge_curation_agent, 2024-06-09.