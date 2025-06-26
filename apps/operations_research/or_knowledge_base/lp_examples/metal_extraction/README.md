# Example: Maximizing Metal Extraction Using Linear Programming in Pyomo

## Problem Statement
There are two ways to extract a metal from mined ores.
- Process J: Extracts 5 units of metal, uses 8 units of water, produces 3 units of pollution.
- Process P: Extracts 9 units of metal, uses 6 units of water, produces 5 units of pollution.
There can be at most 1500 units of water and at most 1350 units of pollution available.

### Decision Variables
- x: Number of times Process J is performed (integer, >= 0)
- y: Number of times Process P is performed (integer, >= 0)

### Linear Program
Maximize: 5x + 9y  
Subject to:  
8x + 6y <= 1500  
3x + 5y <= 1350  
x >= 0, y >= 0

## Solution Approach
- Model the above problem using Pyomo.
- Solve using an open-source solver (GLPK).

## Optimal Result
- Maximum amount of metal extracted: 2250 units (at x=0, y=250).

## Pyomo Implementation
See the included `lp_metal_extract.py` for the full scripted solution and documentation.
