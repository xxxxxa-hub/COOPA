# Minimum Transportation Units Problem with Proportional Constraints (Trains & Trams Example)

## Summary
This example demonstrates how integer programming can be used to minimize the number of transportation units (such as trains and trams), each with distinct capacities, to meet an overall transport demand. Unlike standard transport unit minimization models, this problem features a proportionality constraint requiring a minimum ratio between the numbers of different vehicle types.

---
### Problem Statement
Minimize the total number of trains and trams needed, where:
- Each train can transport 120 people per hour.
- Each tram can transport 30 people per hour.
- The company must transport at least 600 people per hour.
- The number of trams must be at least twice the number of trains.
- All decision variables are non-negative integers.

---
#### Mathematical Model
Let **x** = number of trains (integer >= 0)
Let **y** = number of trams  (integer >= 0)

Objective:
  Minimize x + y

Subject to:
  120x + 30y >= 600
  y >= 2x
  x, y >= 0 and integer

---
#### Best Practice
This problem is modeled and solved in Python using Pyomo. Features of the provided implementation:
- Clear mathematical formulation with variable, objective, and constraint definitions
- Solver output and variable reporting
- Inline comments to explain model structure

**File Reference:** [transportation_optimizer.py](../../code_examples/Transportation/Resource_Allocation/Integer_Programming/transportation_optimizer.py)

---
#### Applications
This structure is widely applicable beyond multimodal transport:
- Multimodal transport network planning
- Production or machine scheduling where a certain mix is required
- Resource allocation or blending where proportional or regulatory constraints exist

#### Adaptable Parameters
- Vehicle (or resource) capacities
- Minimum total demand to be met
- Proportionality constants, e.g., how many trams per train

---
#### Related Knowledge
- Integer programming formulations for transportation and resource allocation
- Proportional or mix constraints in linear/integer programming
- Blending and minimum-resource selection problems

#### See Also
- [cart_optimization_model.py](cart_optimization_model.py)
- [carts_and_horses_integer_programming.md](carts_and_horses_integer_programming.md)
- [transport_optimizer.py](transport_optimizer.py)

---
*For code, see* [transportation_optimizer.py](../../code_examples/Transportation/Resource_Allocation/Integer_Programming/transportation_optimizer.py) *in the code_examples folder.*
