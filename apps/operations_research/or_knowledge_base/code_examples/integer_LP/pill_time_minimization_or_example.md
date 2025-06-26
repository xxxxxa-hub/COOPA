
# Pill Time Minimization Problem (Operations Research Integer Programming Example)

## Problem Statement
A student must take at least 130 medication pills in a month, with at least 40 being vitamin D pills (the rest calcium). Each calcium pill takes 5 minutes to be effective; each vitamin D pill, 6 minutes. The student must take more calcium than vitamin D pills. The aim is to **minimize the total time required for the medication to be effective**.

## Five-Element Model Structure

- **Objective**: Minimize total time T = 5x + 6y
- **Variables**: x (integer, ¡Ý0): #calcium pills; y (integer, ¡Ý0): #vitamin D pills
- **Constraints**:
    - x + y ¡Ý 130 (total pills)
    - y ¡Ý 40 (minimum vitamin D)
    - x > y (more calcium than vitamin D, integer: x ¡Ý y+1)
    - x, y ¡Ý 0, integer
- **Parameters**:
    - Calcium pill effective time: 5 min
    - Vitamin D pill effective time: 6 min

## Pyomo Code (for reproducibility)

## Solution

Optimal total time: **690 minutes**
- Calcium pills (x): **90**
- Vitamin D pills (y): **40**

All constraints satisfied; solution is integer and minimal.
