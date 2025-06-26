# Oil & Gas Pipes Integer Programming Example

**Problem Statement:**  
An oil and gas company must allocate high-volume and low-volume pipes daily to satisfy operational, safety, and staffing constraints.

- High-volume pipe: 10,000 US gallons/day, requires 12 technicians, higher risk (at most 35% of total pipes)
- Low-volume pipe: 5,000 US gallons/day, requires 5 technicians, at least 8 must be used
- Daily demand: at least 150,000 US gallons
- Technician availability: 160 per day

**Decision Variables:**
- x: integer, number of high-volume pipes (x >= 0)
- y: integer, number of low-volume pipes (y >= 8)

**Model:**
Minimize: x + y  
Subject to:
- 10,000x + 5,000y >= 150,000 [demand]
- 12x + 5y <= 160 [technicians]
- x <= 0.35(x + y) [at most 35% high-volume]
- y >= 8 [minimum low-volume]

**Solution:**  
Optimal: x = 5, y = 20  
Minimum total pipes: 25

**Implementation:**  
Modeled and solved as an Integer Linear Program (see 'pipe_ip_solver.py' for Pyomo/GLPK concrete implementation).

*Use as a template for similar resource allocation, mix-integer programming, or labor-constrained optimization problems.*
