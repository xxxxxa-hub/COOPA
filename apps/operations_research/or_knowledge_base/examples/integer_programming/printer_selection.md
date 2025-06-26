# Integer Programming: Printer Selection Problem

## Problem Description

An office must purchase two types of printers (premium and regular):
- Premium model: prints 30 pages/min, uses 4 units ink/min.
- Regular model: prints 20 pages/min, uses 3 units ink/min.
Constraints:
- Print at least 200 pages/min.
- Use at most 35 units ink/min.
- Regular printers < premium printers.
- Minimize total printers.

## Variables

x = # of premium printers (integer, >=0)  
y = # of regular printers (integer, >=0)

## Model

Minimize x+y  
subject to:
- 30x + 20y >= 200
- 4x + 3y <= 35
- y <= x-1

## Solution

Optimal: x=7, y=0, total printers=7.

Model implemented in Pyomo (see associated code file).
