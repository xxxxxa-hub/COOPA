# Integer Linear Program: Minimum Vehicles with Luggage and Pollution Constraints

## Problem Statement
Given two vehicle types, each with fixed luggage capacity and pollution output, find the minimum number of vehicles needed to satisfy a daily luggage movement requirement without exceeding a daily pollution cap.

- 4-wheeler: 60 luggage/day, 30 pollution units/day
- 3-wheeler: 40 luggage/day, 15 pollution units/day
- Must move at least 1000 luggage/day
- Must not exceed 430 pollution units/day

## Mathematical Model

**Variables:**
- x: Number of 4-wheelers (integer, >= 0)
- y: Number of 3-wheelers (integer, >= 0)

**Objective:**  
Minimize x + y

**Constraints:**
- 60x + 40y >= 1000  (luggage requirement)
- 30x + 15y <= 430   (pollution cap)

## When to Use
Use this template for knapsack-like integer programs where distinct item types provide different capacity and cost (or pollution), and you wish to minimize the number to meet minimum/maximum requirements.

## Example Pyomo Usage
See accompanying `.py` code file for a reproducible Pyomo implementation and solution reporting template.

---

_Saved by AI agent as solution to "minimum vehicles for luggage/pollution constraint" problem._
