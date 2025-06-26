# Example: Two-Process Resource Allocation (Production Planning LP/IP)

## Problem Description

A lab conducts two experiments (alpha and beta) to produce electricity. Each requires certain resources:
- Experiment alpha: 3 units metal, 5 units acid, produces 8 units electricity.
- Experiment beta: 5 units metal, 4 units acid, produces 10 units electricity.
Lab resources: 800 units metal, 750 units acid.

**Objective:** Maximize total electricity produced by deciding how many times to conduct alpha and beta.

## Mathematical Model (LP/IP Formulation)

Let:
- x = number of experiment alpha runs (integer, >=0)
- y = number of experiment beta runs (integer, >=0)

Maximize:  
    8x + 10y

Subject to:  
    3x + 5y <= 800      (metal constraint)  
    5x + 4y <= 750      (acid constraint)  
    x >= 0, y >= 0 and integer

## Solution

The optimal solution (using integer programming):

- Maximum electricity produced: **1680 units**
- Experiments: alpha (x): 40 times; beta (y): 136 times

This example is a template for modeling and solving resource allocation/production maximization with discrete choices and two resources. Model is solved using a standard algebraic modeling language (Pyomo) and open-source MIP solver.
