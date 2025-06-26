# Clinic Drop-In Test Scheduling — Integer Programming Example

## Problem Statement

A drop-in clinic offers two test types:
- **Ear test**: takes 5 minutes.
- **Blood test**: takes 30 minutes (more accurate).

**Constraints:**
- At least 3 times as many blood tests as ear tests (`y >= 3x`).
- At least 12 ear tests (`x >= 12`).
- Total available time: 7525 minutes.
- Only whole tests allowed (x and y integers).

**Objective:**  
Maximize `x + y`, the total number of tests.

## Mathematical Formulation

Let:
- `x =` number of ear tests
- `y =` number of blood tests

Maximize:  
    `x + y`

Subject to:  
    `x >= 12`  
    `y >= 3x`  
    `5x + 30y <= 7525`  
    `x, y in Z+`

## Solution

The optimal (integer) solution is:
- **Ear tests (`x`) = 12**
- **Blood tests (`y`) = 36**
- **Total tests = 48**

All constraints satisfied.
- Time used: `5*12 + 30*36 = 60 + 1080 = 1140` min (**<< 7525**, so time is not a bottleneck).

**Related code:**  
See `ear_blood_test_optimizer.py` in the working directory (Pyomo model).

---
*Curated: Clinic test-mix IP model & solution example for reference.*
