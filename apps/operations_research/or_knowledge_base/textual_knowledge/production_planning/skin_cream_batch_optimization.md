# Skin Cream Batch Optimization Example (Production Planning)

## Problem Statement

A pharmaceutical company makes skin cream in batches, a regular batch and premium batch, to sell to hospitals.
- The regular batch requires 50 units of medicinal ingredients and 40 units of rehydration product.
- A premium batch requires 40 units of medicinal ingredients and 60 units of rehydration product.
- The company has available 3000 units of medicinal ingredients and 3500 units of rehydration product.
- The number of regular batches must be less than the number of premium batches, and at least 10 regular batches must be made.
- A regular batch treats 50 people; a premium batch treats 30 people.
- Objective: maximize the treated population.

## Mathematical Model

Let x = number of regular batches (integer, x >= 10)  
Let y = number of premium batches (integer, y > x)

**Maximize:**  
    50*x + 30*y

**Subject to:**  
    50*x + 40*y <= 3000    # Medicinal ingredient constraint  
    40*x + 60*y <= 3500    # Rehydration product constraint  
    x < y  
    x >= 10  
    x, y >= 0 and integer

**Optimal Solution:**  
- Regular batches: x = 32  
- Premium batches: y = 35  
- Maximum people treated: 2650

## Source Code

See the code example ('batch_optimization_model.py') for the implementation using Pyomo.
