
# Bank Branch Siting Integer Programming Example

## Problem Statement
A bank can build small and large branches to serve their customers.  
- A small branch serves 50 customers/day, requires 10 tellers.  
- A large branch serves 100 customers/day, requires 15 tellers.  
- Bank has at most 200 tellers total and must serve at least 1200 customers/day.

**Objective**: Minimize the total number of branches.  
**Variables**:  
- x = number of small branches (integer, ¡Ý0)  
- y = number of large branches (integer, ¡Ý0)  

**Constraints**:  
- 50x + 100y ¡Ý 1200 (customers-demand met)  
- 10x + 15y ¡Ü 200 (teller capacity)  

## Algebraic Formulation
Minimize:  
    x + y  
Subject to:  
    50x + 100y ¡Ý 1200  
    10x + 15y ¡Ü 200  
    x ¡Ý 0, y ¡Ý 0, integers

## Solution
The minimum total number of branches is **12**.  
At optimality:  
- x = 0 (no small branches)  
- y = 12 (twelve large branches)  

**Justification**:  
- Serves exactly 1200 customers (100 ¡Á 12)  
- Uses 180 tellers (15 ¡Á 12), which is ¡Ü 200 tellers.  
- All constraints (integer, bounds, right-hand sides) are satisfied.

## Modeling Notes
- Pyomo or standard MILP methods can solve this efficiently.
- For other customer/teller limits, adjust coefficients and re-solve.
