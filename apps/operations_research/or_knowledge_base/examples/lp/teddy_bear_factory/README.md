
# Teddy Bear Factory Linear Programming Problem

## Problem Statement

A teddy bear company produces three different colored bears: black, white, and brown. These bears are made in two different factories. Running factory 1 for 1 hour costs $300 and produces 5 black teddy bears, 6 white teddy bears, and 3 brown ones. Running factory 2 for 1 hour costs $600 and produces 10 black teddy bears and 10 white teddy bears (but no brown ones). To meet children's demand, at least 20 black teddy bears, 5 white teddy bears, and 15 brown teddy bears must be made daily. The objective is to minimize the cost of production.

## Mathematical Model

Let:

- x1 = hours to run factory 1 (>=0)
- x2 = hours to run factory 2 (>=0)

**Minimize:**  
    300*x1 + 600*x2

**Subject to:**  
- 5*x1 + 10*x2 >= 20    (black bears)  
- 6*x1 + 10*x2 >= 5     (white bears)  
- 3*x1 >= 15            (brown bears, only made in factory 1)  
- x1 >= 0  
- x2 >= 0

## Optimal Solution

- Minimum total cost: 1500.0
- x1 (hours factory 1): 5.0
- x2 (hours factory 2): 0.0

## Pyomo Model

See lp_bear_factory_model.py for full implementation.
