# Stamping Machines Integer Programming Example

## Problem Statement
A post office is purchasing stamping machines, either dual or single model. 
- Dual model stamps 50 letters/min and requires 20 units of glue/min.
- Single model stamps 30 letters/min and requires 15 units of glue/min.
- Single machines must be more numerous than dual machines.
- Must stamp at least 300 letters/min.
- At most 135 units of glue/min can be used.
- Objective: Minimize total number of machines purchased.

## Pyomo Integer Programming Formulation

**Variables:**
- x: number of dual model machines (integer, >= 0)
- y: number of single model machines (integer, >= 0)

**Objective:**  
Minimize z = x + y

**Constraints:**
- 50x + 30y >= 300           (stamping requirement)
- 20x + 15y <= 135           (glue limit)
- y >= x + 1                 (more singles than duals)
- x, y integer >= 0

**Optimal Solution (as computed by Pyomo/IP solver):**
- x = 3 (dual), y = 5 (single)
- Minimum total machines z = 8

## Solution Verification
- Stamping: 50*3 + 30*5 = 300 letters/min
- Glue: 20*3 + 15*5 = 135 units/min
- Single > dual: 5 > 3

## Usage
This is a classic small-scale ILP for resource allocation with variable dominance, capacity, and combinatorial constraints. Useful as a teaching example or template for machine selection, resource allocation, or similar constraint-based decisions. See also: 'stamping_machine_ilp.py' for the full Pyomo implementation.
