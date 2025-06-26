# Digital Keyboard Production Linear Programming Problem

## Problem Statement

A music company produces two types of digital keyboards: full-weighted and semi-weighted. Both have the following parameters:
- Full-weighted: sells for $2800, requires 20 oscillator chips, takes 1.2 hours to produce
- Semi-weighted: sells for $2400, requires 15 oscillator chips, takes 1.2 hours to produce
- Daily resources: 3500 oscillator chips, 6 production hours

## Formulation

Let x = number of full-weighted keyboards, y = number of semi-weighted keyboards.

Maximize: 2800*x + 2400*y  
s.t.  
20x + 15y <= 3500          (chip constraint)  
1.2x + 1.2y <= 6           (time constraint)  
x >= 0, y >= 0, integer

## Optimal Solution

- Maximum revenue: $14,000
- Make 5 full-weighted, 0 semi-weighted keyboards

Time is the binding constraint.

## Pyomo Model Reference

See `keyboard_lp_pyomo.py` for a complete, reusable model and solver function.

---
