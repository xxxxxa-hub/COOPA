# Example: Scheduling Workers with Integer Programming

## Problem Statement

A clinic employs nurses and pharmacists to deliver healthcare services.
- A nurse works 5 hours per shift, paid $250 per shift.
- A pharmacist works 7 hours per shift, paid $300 per shift.
- The clinic needs at least 200 hours of healthcare labor.
- The clinic's budget is $9000.
- Objective: Schedule nurses and pharmacists to minimize the **total number of workers**.

## Mathematical Model

Let:
- x = number of nurses (integer, >= 0)
- y = number of pharmacists (integer, >= 0)

**Objective**:
Minimize x + y

**Constraints**:
- 5x + 7y >= 200          (labor hours)
- 250x + 300y <= 9000     (budget)
- x, y >= 0, integer

## Solution

Optimal solution:
- Minimum total workers (x + y): **29**
- Assignments: x = 0 nurses, y = 29 pharmacists

All constraints are satisfied at the optimum.

## Application

This model is a standard *workforce scheduling* IP for minimizing headcount under linear constraints (labor hours and budget). The approach generalizes to similar settings by substituting hours, wages, and budget/labor requirements.

---

*Saved: 2024-06-09, by OR automation agent.*

---
