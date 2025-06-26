# Advertisement Allocation Optimization Problem (LP/MILP Template)

## Summary Description
A company aims to allocate a finite advertising budget across multiple platforms to maximize total viewers reached. Each platform (or ad medium) has a fixed cost per ad, a known viewer reach per ad, and may be subject to lower/upper/fractional bounds on the number of ads placed. The problem is typically formulated as a linear or mixed-integer linear program (LP/MILP), serving as a template for similar marketing allocation and planning problems.

### Decision Variables
- Number of ads on each advertising medium (integer, >= 0)

### Objective Function
- Maximize the total number of viewers reached across all platforms

### Common Constraints
- Total advertising cost <= specified budget
- Upper/lower or fractional limits on the number of ads per platform
- Balance constraints (such as minimum/maximum percentage of ads on specific platforms)

### Canonical Example (with Pyomo Model Reference)

Suppose three advertising platforms:
- z-tube: $1000 per ad, reaches 400,000 viewers. Must account for at least 5% of total ads.
- soorchle: $200 per ad, reaches 5,000 viewers. No more than 15 ads allowed.
- wassa: $100 per ad, reaches 3,000 viewers. No more than one-third of total ads.
Budget: $10,000. In the canonical solution, the entire budget is spent on z-tube ads, covering 4,000,000 viewers.

## Pyomo Model Code
See file `ad_allocation_pyomo.py` for the detailed MILP formulation.
- Code implements model declaration, objective, constraints (including linearizations), and solver interaction using Pyomo.
- Covers error handling and solution summary/provenance for template reuse.

---