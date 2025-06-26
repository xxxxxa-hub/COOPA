# Minimum Jar Integer Programming (Jam Company Shipping)

## Problem Statement
A jam company ships product in small (50 ml) and large (200 ml) jars. To meet market preference:
- Number of large jars **cannot exceed** number of small jars.
- **At least 100,000 ml** of jam must be shipped.

**Goal**: Minimize the total number of jars used.

## Variables
- x = number of small jars (integer, >= 0)
- y = number of large jars (integer, >= 0)

## Formulation
- **Objective:** Minimize `x + y`
- **Constraints:**
    - `50x + 200y >= 100,000`
    - `y <= x`
    - `x, y >= 0`
    - `x, y` are integers

## Solution Summary
- Optimal solution: `x = 400`, `y = 400`
- Minimum jars: `800`
- Feasibility: 
    - Volume: `50*400 + 200*400 = 100,000 ml`
    - Balance: `400 >= 400`
- This can be solved via integer linear programming using solvers like GLPK or CBC.

## Reusability
- Useful for container or bin packing, discrete lot-sizing, and hybrid shipment optimization.
- See: `jar_ilp_model.py` for Pyomo code structure (if present in KB).
- Adjust parameters for various container sizes or shipping requirements.

---

*Curated by auto-OR-knowledge-bot, June 2024*

Describe problem, formulation, solution, and reuse tips.