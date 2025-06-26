# Mail Delivery Fleet Mix Optimization (Integer Programming)

## Problem Structure

Given:
- Two vehicle (boat) types, each with fixed per-trip capacity and resource (fuel/gas) consumption.
- A fixed mail delivery demand (pieces of mail to deliver).
- Trip limits and policy constraints (e.g., maximum number of regular trips, speed boats must account for at least 50% of trips).

## Decision Variables
- `x`: Number of regular boat trips (integer, bounded above by maximum fleet or other constraints).
- `y`: Number of speed boat trips (integer, bounded below, often related to policy/ratio with x).

## Objective
Minimize total gas used:
    objective: min 10*x + 20*y

## Constraints
1. Mail delivery demand constraint: 20*x + 30*y >= 1000
2. Fleet/operational bounds (e.g., x <= 20).
3. Policy constraints (e.g., y >= x for at least 50% speed boat trips).

## Pyomo Model Outline

## Example/Result

For the 2024 mail delivery fleet problem:
- Minimum gas consumed: **600**
- 20 regular boat trips, 20 speed boat trips.

## Notes

- This model generalizes to any problem with multiple fleet types, per-trip capacities, resource consumption, and trip-mix constraints.
- If you encounter a similar "fleet mix", "minimum fuel/cost" with per-trip ratios, use this pattern.
