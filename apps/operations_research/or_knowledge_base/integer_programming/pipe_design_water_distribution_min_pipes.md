# Minimum Pipes Integer Programming Problem (Water Distribution)

## Problem Statement
Given two types of pipes for water transport:
- Wide pipes: 25 units/min (flow capacity)
- Narrow pipes: 15 units/min

Minimize the total number of pipes required, subject to:
- At least 900 units/min total flow
- At most one wide pipe per three narrow pipes (w <= n/3)
- At least 5 wide pipes (w >= 5)
- All counts integer and non-negative

## Mathematical Formulation

Variables:
- w: number of wide pipes (integer, w >= 5)
- n: number of narrow pipes (integer, n >= 0)

Constraints:
- 25w + 15n >= 900
- w <= n/3  or  equivalently  3w <= n
- w >= 5
- w, n >= 0 and integer

Objective:
- Minimize w + n

## Pyomo Code Example

## Optimal Solution
- Minimum total number of pipes: 52 (13 wide, 39 narrow)
- All constraints satisfied
