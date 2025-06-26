# Chicken Transport Integer Programming Model (Operations Research Example)

**Problem context:**  
A chicken farmer must transport 1200 chickens using two kinds of vehicles: buses and cars. Each bus trip can carry 100 chickens (with a 2 hour duration per trip, and up to 10 trips allowed), while each car trip can carry 40 chickens (1.5 hours per trip). Importantly, at least 60% of the *total* trips must be by car. The goal is to minimize the total time required to move all chickens.

**Variables:**  
- x: Number of bus trips (integer, 0 <= x <= 10)  
- y: Number of car trips (integer, y >= 0)

**Objective:**  
Minimize total transport time: total_time = 2x + 1.5y

**Constraints:**  
- 100x + 40y >= 1200   (must transport all chickens)
- x <= 10              (maximum bus trips)
- y >= 1.5x            (at least 60% of all trips must be by car)
- x, y are non-negative integers

**Modeling notes:**  
- Model implemented in Pyomo, an optimization framework for Python, utilizing the GLPK solver.  
- All data values are parameterized for clarity and potential flexibility.  
- Uses integer programming features of Pyomo, and solution result values are extracted using value().

**Optimal solution:**  
- Minimal total time: 33.5 hours  
- Optimal number of trips: Bus trips (x) = 7, Car trips (y) = 13

**Reference implementation:**  
See Python model file: `transport_ip_model.py` (Pyomo) for concrete implementation.

**Keywords:** integer programming, Pyomo, transportation, constraints, car/bus allocation, operations research, trip optimization

---
*This entry summarizes a classic transportation integer programming model, grouped under code_examples/ for applied Pyomo models with clear vehicle, ratio, and time constraints. For related models, see also 'knowledgeboat_fish_transport_20250519.md' (boat/fish), 'helicopter_car_transport_optimize.py' (helicopter/car), and 'benchmarks/integer_transport/knowledgebase_transport_plane_truck_ILP.md' (plane/truck variant).*
