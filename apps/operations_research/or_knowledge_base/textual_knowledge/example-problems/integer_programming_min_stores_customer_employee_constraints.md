# Integer Programming Example - Minimizing Number of Stores to Meet Customer and Staffing Constraints

## Description
This document describes the algebraic modeling and solution of an integer programming problem where a company must decide how to allocate resources between two types of stores to minimize the number of stores open while meeting minimum customer service and employee availability constraints.

## Problem Statement Example
A company can open x 'retail stores' (serving a per-store customer count and requiring a per-store staff count) and y 'factory outlets' (serving fewer customers per store but needing fewer employees). The company must serve at least a required number of customers and has a maximum available employees.

### Variables
- x: integer, number of retail stores to open
- y: integer, number of factory outlets to open

### Parameters
- R: Customers per retail store (e.g., 200)
- F: Customers per factory outlet (e.g., 80)
- S_r: Employees per retail store (e.g., 6)
- S_f: Employees per factory outlet (e.g., 4)
- Customers_min: Minimum customers that must be served (e.g., 1200)
- Employees_max: Maximum employees that can be assigned (e.g., 50)

### Algebraic Model
Minimize:         x + y
Subject to:
    R * x + F * y >= Customers_min        (Customer coverage constraint)
    S_r * x + S_f * y <= Employees_max    (Employee capacity constraint)
    x, y >= 0 and integer

## Optimal Solution Example
For R=200, F=80, S_r=6, S_f=4, Customers_min=1200, Employees_max=50:
- Minimum number of stores: 6
- x (retail stores): 6, y (factory outlets): 0

## Implementation
Typical solution is via integer linear programming (e.g., Pyomo/GLPK).

## Use Cases
- Resource allocation with simultaneous minimum service requirements and maximum resource caps.
- Can be generalized to more than two types of facilities.
- Useful framework for retail, manufacturing, and service industry operations research.

---
This document can be copied and reused as a template or guidance for similar resource allocation problems.
