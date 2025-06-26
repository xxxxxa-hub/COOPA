# Example: Integer Resource Allocation – Coin Plating Problem

## Problem Statement

Two processes, A and B, can be used to plate coins with gold.  
- Process A: Uses 3 units of gold, 2 wires, plates 5 coins per run.  
- Process B: Uses 5 units of gold, 3 wires, plates 7 coins per run.  
- Resource constraints: 500 units of gold, 300 wires available.

**Question:**  
How many processes of each type should be run to maximize the total number of coins plated? (Both x and y must be integers.)

## Mathematical Model

Let  
- x = # runs of process A  
- y = # runs of process B

**Maximize:**  
5x + 7y

**Subject to:**  
3x + 5y <= 500 (gold constraint)  
2x + 3y <= 300 (wire constraint)  
x >= 0, y >= 0, x, y integers

## Solution

- Optimal solution: x = 150, y = 0
- Max coins plated: 750

**Resource use:**  
- Gold: 3x150 + 5x0 = 450 <= 500  
- Wire: 2x150 + 3x0 = 300 <= 300

## Pyomo Model

A reference Pyomo model for this problem is available as: `algebraic_optimizer_model.py` (integer programming, solved with GLPK).

---  
**Category:** Integer Programming / Resource Allocation / Production Planning  
**Last updated:** 2024-06  
