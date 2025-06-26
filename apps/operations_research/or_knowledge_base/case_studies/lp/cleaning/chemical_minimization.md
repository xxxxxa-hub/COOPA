# Cleaning Company Chemical Usage: LP Formulation & Solution

## Problem Statement
A cleaning company uses two chemicals in house cleaning:
- Cleansing chemical (per unit: 4 min effective time)
- Odor-removing chemical (per unit: 6 min effective time)

**Objective:**  
Minimize total time to clean a house.

**Variables:**
- x = units of cleansing chemical used (x >= 0)
- y = units of odor-removing chemical used (y >= 0)

**Objective Function:**  
Minimize 4x + 6y

**Constraints:**
1. At least 100 units of cleansing chemical:      x >= 100
2. At least 300 units of chemicals total:         x + y >= 300
3. Cleansing chemical at most twice odor-removing: x <= 2y

## Solution
Optimal usage:
- x = 200.0 units (cleansing chemical)
- y = 100.0 units (odor-removing chemical)

Minimum cleaning time = **1400.0**

**Solution Method:**  
LP modeled in Pyomo, solved with GLPK/CBC.

## Typical Usage
Use this model for:
- Resource/blending problems with proportionality and minimum/maximum constraints.
- House cleaning, chemical blends, or process optimization where "per unit cost/time" and "quantity minimum/maximum" are given.
