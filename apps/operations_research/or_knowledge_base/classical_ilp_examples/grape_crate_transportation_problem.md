## Classic ILP: Grape Crate Transportation Problem

**Problem statement:**  
A grape farmer transports grapes using small crates (200 per crate) and large crates (500 per crate). The following constraints apply:  
- At least 3 times as many small crates as large crates (s >= 3*l)
- Maximum 100 small crates (s <= 100)
- Maximum 50 large crates (l <= 50)
- No more than 60 crates total (s + l <= 60)
- At least 10 large crates (l >= 10)
- s, l integer and >= 0

**Objective:**  
Maximize 200*s + 500*l

**Solution:**  
Optimal number of grapes transported: 11000  
Optimal variables: s=30, l=10

**References:**  
- Pyomo model: grape_ilp_model.py
