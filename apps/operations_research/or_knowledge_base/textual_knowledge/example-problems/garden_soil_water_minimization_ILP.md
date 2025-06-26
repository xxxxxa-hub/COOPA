# Garden Soil Water Minimization ILP

## Problem Summary
This document summarizes an integer linear programming (ILP) problem that addresses minimizing water usage when selecting soil bags for a garden project. The problem involves two soil types: subsoil and topsoil. Each type has a different water usage per bag. The goal is to allocate a number of bags of each type while minimizing total water use, subject to constraints on the total number of bags, and on the percentage of topsoil used.

---

## Problem Definition
- **Decision Variables:**  
  Let x = number of subsoil bags (integer)  
  Let y = number of topsoil bags (integer)

- **Parameters:**  
  N = total number of soil bags needed (integer, given)  
  W_sub = water used per subsoil bag (liters, given)  
  W_top = water used per topsoil bag (liters, given)  
  p_min = minimum fraction of bags that must be topsoil (given, e.g., 0.2)  
  p_max = maximum fraction of bags that can be topsoil (given, e.g., 0.5)

- **Objective Function:**  
  Minimize total water used:  
  min  W_sub * x + W_top * y

- **Constraints:**
  1. Total bags:                 x + y = N
  2. Minimum topsoil fraction:   y >= p_min * N
  3. Maximum topsoil fraction:   y <= p_max * N
  4. Bag counts are non-negative integers: x >= 0, y >= 0, x, y integer

---

## Solution Outline
To solve this problem:
1. Enumerate feasible integer values for y (the number of topsoil bags) in the range [ceil(p_min*N), floor(p_max*N)]
2. For each feasible y, let x = N - y
3. Compute the total water used for each (x, y): W_sub * x + W_top * y
4. Select the (x, y) combination with the smallest total water usage

Or, solve the ILP using standard optimization solvers.

---

## Worked Example
Suppose:
- N = 20 (total bags)
- W_sub = 8 liters
- W_top = 5 liters
- p_min = 0.25 (at least 25 percent topsoil)
- p_max = 0.60 (no more than 60 percent topsoil)

Calculate limits on y:
- y_min = ceil(0.25 * 20) = 5
- y_max = floor(0.60 * 20) = 12

Try each feasible y (from 5 to 12), compute x = 20 - y, then compute water used:
- For y = 5: x = 15 -> water = 8*15 + 5*5 = 120 + 25 = 145
- For y = 6: x = 14 -> water = 8*14 + 5*6 = 112 + 30 = 142
- For y = 7: x = 13 -> water = 8*13 + 5*7 = 104 + 35 = 139
- ...
- For y = 12: x = 8 -> water = 8*8 + 5*12 = 64 + 60 = 124

Best solution (minimal water): y = 12, x = 8, water = 124 liters.

---

## Key Equations
- **Objective:**
    Minimize   W_sub * x + W_top * y
- **Constraints:**
    x + y = N  
    p_min * N <= y <= p_max * N  
    x, y integers >= 0

---

## Notes
- This ILP can be solved using spreadsheet tools, programming languages with optimization libraries, or by hand for small N.
- The approach is widely applicable for similar blending or resource allocation and minimization problems where some components are capped or bounded.
