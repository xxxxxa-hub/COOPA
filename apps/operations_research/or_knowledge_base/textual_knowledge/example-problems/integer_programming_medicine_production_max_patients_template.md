# Integer Programming Example: Maximizing Treated Patients in Medicine Production

**Problem Type**: Integer Linear Programming (ILP) – resource allocation, two products, maximize treated population.

## Problem Statement

A lab produces two medicines (A and B), each using two limited resources and subject to product and comparative quantity constraints.
- Each med has unit resource requirements and treatment counts per dose.
- Limits: total resource, max doses of A, B must strictly exceed A.
- Objective: Maximize patients treated.

## Algebraic Formulation

Let x = doses of medicine A (integer >= 0)  
Let y = doses of medicine B (integer >= 0)  

Maximize:  
    12x + 8y

Subject to:  
    30x + 40y <= 300   (imported material)  
    50x + 30y <= 400   (mRNA)  
    x <= 5             (max A doses)  
    y >= x + 1         (B strictly more than A)  
    x, y >= 0 and integer

## Solution (Pyomo/GLPK or CBC)

- Solve with integer constraints using Pyomo.
- Model is parameterized for resource needs and product constraints.
- For this example, optimal is x=3, y=5, objective=76.

**Pyomo code template and solution details available in 'integer_program_solver.py' (June 2024)**

---

**Use this as a template for similar two-product, two-resource bounded integer programming/production allocation problems.**

---