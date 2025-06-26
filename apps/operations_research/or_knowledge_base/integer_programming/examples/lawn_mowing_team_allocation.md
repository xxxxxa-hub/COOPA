# Integer Programming Example: Lawn Mowing Teams

## Problem Statement

A lawn mowing service operates small and large teams:
- Small team: 3 employees, mows 50 sq ft
- Large team: 5 employees, mows 80 sq ft
- 150 employees available

Requirements:
- Number of small teams >= 3 x number of large teams
- At least 6 large teams and at least 10 small teams

Maximize the amount of lawn mowed.

## Algebraic Formulation

Let:
- x = number of small teams (integer, x >= 10)
- y = number of large teams (integer, y >= 6)

Objective:
- Maximize 50x + 80y

Subject to:
- 3x + 5y <= 150         (employee limit)
- x >= 3y                (small team ratio)
- x >= 10                (minimum small teams)
- y >= 6                 (minimum large teams)
- x, y >= 0, integer

## Pyomo Implementation Stub

## Solution

- Maximum area: 2480 sq ft (x=40, y=6)
- Notes: Employee constraint binding; ratio and minimums satisfied.

---

*This example is useful for team allocation/resource mix integer programming problems involving ratio, minimum, and capacity/resource constraints.*
