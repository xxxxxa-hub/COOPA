# Case Study: Recycling Bin Allocation Optimization

## Problem Statement
A recycling company must allocate small and large bins for neighborhood collection, aiming to maximize recycling collected with the following:
- Each small bin: requires 2 workers, holds 25 units
- Each large bin: requires 5 workers, holds 60 units
- Available workers: 100
- Small bins must be three times the number of large bins
- Min 10 small bins, min 4 large bins

## Algebraic Model
Let x = number of small bins (integer)
Let y = number of large bins (integer)

Maximize:      25x + 60y  
Subject to:   
  2x + 5y <= 100  
  x = 3y  
  x >= 10  
  y >= 4  
  x, y >= 0 and integer

## Solution
Optimal: x = 27, y = 9  
Max recycling collected: 1215 units

## Pyomo Model
See `recycling_bin_optimization.py` for an implementation using Pyomo and open-source solvers.

## Context
This formulation is useful for proportional discrete allocation, bin packing, and resource-constrained assignment problems.
