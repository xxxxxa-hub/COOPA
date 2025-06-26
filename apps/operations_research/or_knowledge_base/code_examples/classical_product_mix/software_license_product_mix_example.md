# Software License Product Mix Optimization Example

## Problem Description

A company sells two types of software licenses:
- Personal License: Cost = $550, Profit = $450
- Commercial License: Cost = $2000, Profit = $1200

Constraints:
- At most 300 licenses in total per month.
- Total production budget: \$400,000.
- Integer (no fractional) licenses.

Objective:
- Maximize total profit.

## Mathematical Formulation

Let x = # of Personal Licenses, y = # of Commercial Licenses

Maximize:  
    Profit = 450*x + 1200*y

Subject to:
    550*x + 2000*y <= 400,000      (Budget constraint)
    x + y <= 300                   (License upper bound)
    x >= 0, y >= 0; x, y integer

## Solution (GLPK, Pyomo):

Optimal values:
- x = 138
- y = 162
- Maximum profit = \$256,500

## Pyomo Implementation Template

(See adjacent .py file for code.)

---

This example can be adapted for any two-product budgeted product mix problem with similar constraints.
