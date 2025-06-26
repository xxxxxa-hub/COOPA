# Integer Programming Example: Autobody Shop Car Jack Resource Allocation

## Problem Template

An autobody shop must decide how many car jacks of each type to purchase to maximize cars processed per hour. Each jack type uses a certain amount of a resource (e.g., electricity or gas), processes cars at a certain rate, and is subject to individual and global resource constraints.

**Variables:**
- x: number of automatic electric jacks (integer, x >= 0)
- y: number of gas-powered jacks (integer, y >= 0)

**Objective:**
Maximize cars processed per hour: C1 * x + C2 * y

**Constraints:**
- x <= UpperBoundX   (e.g., outlet limitation)
- a1 * x <= R1       (resource 1, e.g. electricity)
- a2 * y <= R2       (resource 2, e.g. gas)
- x, y integer >= 0

**Example parameters:**  
C1 = 5, C2 = 4, a1 = 6, a2 = 7, UpperBoundX = 14, R1 = 50, R2 = 80

## Pyomo Integer Programming Model (Python Sample)

## Solution Interpretation

In the sample case:
- x = 8, y = 11
- Maximum = 5*8 + 4*11 = 40 + 44 = 84 cars per hour

Check that all constraints are satisfied for these integer solutions.

## Reuse Guidance

This model can be adapted to any resource allocation problem where:
- Each decision variable represents a count of units/devices/resources,
- Each has a cost/resource usage per assignment,
- There are resource budget constraints,
- The objective is maximizing total throughput or profit.

Set new coefficients and resource limits as required.
