# Optimal Production of Dog Bones (Linear Programming Worked Example)

## Problem Summary
- A dog hospital produces small and large bones using two resources: tooth medication (limited supply), and meat (objective to minimize usage).
- Each small bone requires 10 units of medication and 12 units of meat. Each large bone requires 15 units of medication and 15 units of meat.
- Constraints include a medication limit (2000 units), at least 50% of bones must be small, and at least 30 large bones must be produced.
- Objective: Minimize total meat used.

## Mathematical Formulation
**Variables:**
  x = number of small bones (integer, >= 0)
  y = number of large bones (integer, >= 0)

**Minimize:**
  12 * x + 15 * y

**Subject to:**
  10*x + 15*y <= 2000
  x >= y
  y >= 30

## Notable Features
- Proportional constraint (at least half of all bones are small: x >= y).
- Lower bounds on production.
- Resource/capacity constraint.
- Integer decision variables sometimes, but solution here is integer even in LP-relaxation.

## Solution
- The optimal solution: Produce 30 small bones and 30 large bones for a minimum total meat usage of 810 units.
- The critical point is found by making both x and y as small as the constraints allow.

## Keywords
linear program; resource allocation; proportions; production planning; minimum objective; explicit worked example.

## Purpose
This file is to serve as a direct example for future problems about minimum resource production decisions with percentage/product mix constraints.
