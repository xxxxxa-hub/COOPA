## Problem: Minimizing Pain Killer Usage in Dental Fillings (Resin Limited, Ratio-Constrained LP)

**Problem Statement:**  
A dentist must schedule the number of molar (x) and canine (y) cavities to fill, given a resin limit, different resource requirements, and population/service mix constraints:
- Total resin available: 3000 units.
- Molar: 20 units resin, 3 units pain killer per filling
- Canine: 15 units resin, 2.3 units pain killer per filling
- At least 60% of cavities filled must be canines (y / (x + y) >= 0.6)
- At least 45 molar cavities must be filled
- Objective: Minimize total pain killer needed (3x + 2.3y)

**Mathematical Model:**
Let:
- x = number of molar cavities to fill
- y = number of canine cavities to fill

Minimize:  
    3x + 2.3y

Subject to:  
    20x + 15y <= 3000  
    x >= 45  
    y >= 1.5x     # (derived from y/(x+y) >= 0.6)
    x >= 0  
    y >= 0

**Best Practices and Takeaways:**
- If a ratio constraint is present (e.g., y/(x+y) >= alpha), algebraically simplify to a linear constraint (here, y >= (alpha/(1-alpha)) x).
- Minimum or mandatory fill quantities are modeled as lower bounds (e.g., x >= 45).
- This model is a standard LP and can be implemented using Pyomo or other modeling libraries.
- Tightest constraints (lower bounds in this case) often dictate the optimal solution; check which are active at optimality.

**Reference Pyomo Code:**  
(Stored as 'painkiller_minimization_model.py' in previous runs, using GLPK solver.)

---

### Application
- Use this template for other medical/materials minimization problems, altering coefficients and constraints per specifics.

Tags: [lp, resource allocation, resin minimization, pain killer, healthcare operations research, pyomo example]
