# Amusement Park Game Allocation Problem (Resource Allocation MILP Example)

## Problem Statement
An amusement park offers two types of games: throwing and climbing. Each game type attracts a certain number of customers per hour, and each has a prize cost per hour. There must be at least twice as many throwing games as climbing games, with a minimum number required for climbing games, and a budget cap on total hourly prize costs. The goal is to maximize the total customers attracted each hour.

## Decision Variables
- T: Number of throwing games (integer, >= 0)
- C: Number of climbing games (integer, >= 0)

## Example Data
- Throwing games: Attract 15 customers/hour, cost $2/hour
- Climbing games: Attract 8 customers/hour, cost $3/hour
- At least twice as many throwing games as climbing
- At least 5 climbing games
- Prize cost <= $100/hour

## Mathematical Formulation
Maximize: 15*T + 8*C

Subject to:
- 2*T + 3*C <= 100          (Prize cost)
- T >= 2*C                  (Throwing-to-climbing ratio)
- C >= 5                    (Minimum climbing)
- T, C >= 0 and integer

## Solution Method
This is a Mixed Integer Linear Program (MILP). Recommended to use Pyomo with CBC or GLPK for solution. Example implementation in `throwing_climbing_optimizer.py`.

## Reusability
- Adapt coefficients and bounds for new hourly rates, costs, or minimum requirements.
- Template useful for other resource allocation or mix optimization tasks with bounded resources and integer constraints.

## References
- Original solution implemented and scripted as 'throwing_climbing_optimizer.py'.


This file is a template and summary for solving and explaining such integer programming problems.
