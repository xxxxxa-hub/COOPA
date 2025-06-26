# Thermometer Scheduling ILP Problem (Doctor's Office)

## Problem Statement
A doctor's office has two types of thermometers:
- Electronic: 3 minutes per reading (more accurate)
- Regular: 2 minutes per reading

Rules:
- At least twice as many patients must use the electronic thermometer as use the regular one.
- At least 50 patients must use the regular thermometer.
- The office is open for 15,000 minutes (total time constraint).
- Objective: maximize the total number of patient readings (using any thermometer).

## Mathematical Formulation
Variables:
- x: Number of patients using electronic thermometer (integer, >= 0)
- y: Number of patients using regular thermometer (integer, >= 0)

Objective:
- Maximize x + y

Constraints:
1. 3x + 2y <= 15,000  (total time available)
2. x >= 2y            (electronic at least twice regular)
3. y >= 50            (minimum regular patients)
4. x, y >= 0 (integer variables)

## Solution (via Pyomo MILP)
Optimal solution: x=100, y=50, maximum total patients = 150

Key Pyomo implementation aspects:
- All variables are integer, with lower bounds.
- Coefficients and right-hand side values are parameters.
- Model prepared to run on cbc, glpk, or highs solvers.
- Script: `ilp_thermometer_model.py` (check for best practices, docstring, and variable extraction).

## Usage
This formulation and Pyomo code can be adapted for other scheduling problems involving two resources, minimum quotas, ratio constraints, and a time/resource budget.
