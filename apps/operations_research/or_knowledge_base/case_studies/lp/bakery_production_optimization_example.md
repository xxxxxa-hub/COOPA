# Bakery Production Optimization: Integer Linear Programming Example

## Problem Structure

A bakery produces two types of items (e.g., brownies and lemon squares). Each item requires specific amounts of multiple resources (mixes, supplements). The goal is to determine the number of each item to produce, in order to **minimize a given resource usage** (e.g., total fiber), subject to:

- Ingredient supply constraints
- Product mix/proportion constraints (minimum/maximum product ratios, e.g., at least 40% must be one product)
- Demand or profitability-driven constraints (one product must have larger batch)
- Non-negativity and (typically) integrality constraints on production amounts.

## General Mathematical Form

**Variables:**
- x: number of product A (integer, >= 0)
- y: number of product B (integer, >= 0)

**Parameters:**
- a1, a2: amount of resource 1 to produce A, B
- b1, b2: amount of resource 2 to produce A, B
- s1, s2: available resource 1, 2
- p, q: resource coefficients in the *objective*
- batch ratio R: e.g. y >= x + 1
- composition lower bound: x >= α(x + y)  (e.g., at least 40% brownies: α=0.4)

**Constraints (example):**
- a1 * x <= s1          (ingredient 1 constraint)
- b2 * y <= s2          (ingredient 2 constraint)
- y >= x + 1            (product mix constraint: more B than A)
- 3x >= 2y              (A is at least 40% of total: x >= 0.4(x+y))
- x, y >= 0 and integer

**Objective:**
- Minimize: p*x + q*y    (total resource usage, e.g., total fiber)

## Pyomo Implementation Outline

> Adapt coefficients for your context.

## Solution

Use Pyomo with GLPK or another open-source solver for mixed-integer LPs/IPs.

---

**Applied Example:**  
This structure was used to minimize fiber required for a bakery using mix and product constraints (June 2024). Minimum found for the sample numbers: 2 brownies, 3 lemon squares; minimum fiber: 26 units.

---

Keywords: bakery, fiber minimization, linear programming, production proportions, Pyomo, integer programming, production planning, recipe, resource allocation, batch ratio, case study.

Location/Indexing Guidance: Place under `case_studies/lp/bakery_production_optimization_example.md` or an analogous folder. Index for searches on 'bakery', 'fiber minimization', 'linear programming with production proportions'.
