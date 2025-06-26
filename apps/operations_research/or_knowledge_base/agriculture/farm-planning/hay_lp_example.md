# Example: Agricultural Resource Allocation Problem (Hay Processing)

## Problem Statement

A farmer has 200 acres of land to process hay using either a windrower or hay harvester. 
- Each acre processed by windrower: 10 kg hay, 5 kg methane, 2 kg fuel.
- Each acre processed by harvester: 8 kg hay, 3 kg methane, 1 kg fuel.
- Available fuel: 300 kg.
- Methane gas limit: 800 kg.
- Objective: Maximize total hay processed.

## Linear Programming Formulation

Let:
- x = acres processed by windrower
- y = acres processed by harvester

Maximize:  
    **10*x + 8*y**

Subject to:
- x + y <= 200  (land)
- 2x + y <= 300  (fuel)
- 5x + 3y <= 800  (methane)
- x >= 0, y >= 0

## Pyomo Code (outline)

## Solution

- Optimal acres windrower (x): 100
- Optimal acres harvester (y): 100
- **Max hay processed:** 1800 kg

All constraints are tight/binding at optimum.

---

*This example demonstrates resource allocation in a farm context and can be adapted for problems involving acreage limits, process choice, and byproduct/emission constraints.*
