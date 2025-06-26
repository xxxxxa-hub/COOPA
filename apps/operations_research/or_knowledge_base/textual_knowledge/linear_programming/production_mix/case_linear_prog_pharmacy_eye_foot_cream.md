# Case Study: Minimizing Machine Hours for Pharmacy Cream Production (LP)

## Problem Statement

A pharmacy produces eye cream and foot cream using two machines:
- **Machine 1**: Produces 30 ml/hour eye cream, 60 ml/hour foot cream, uses 20 ml/hour distilled water.
- **Machine 2**: Produces 45 ml/hour eye cream, 30 ml/hour foot cream, uses 15 ml/hour distilled water.

Constraints:
- Max available distilled water: 1200 ml.
- Must produce at least 1300 ml eye cream, 1500 ml foot cream.

## Linear Programming Formulation

**Variables:**
- t1: Hours machine 1 is run (continuous, t1 >= 0)
- t2: Hours machine 2 is run (continuous, t2 >= 0)

**Objective:**
Minimize total machine running time:  
minimize: t1 + t2

**Constraints:**
- 30*t1 + 45*t2 >= 1300  (eye cream requirement)
- 60*t1 + 30*t2 >= 1500  (foot cream requirement)
- 20*t1 + 15*t2 <= 1200  (distilled water)

## Implementation Tip

This problem is a standard LP and can be solved by algebraic solvers (e.g., Pyomo+GLPK). Model as continuous variables; all coefficients are positive. Useful template for production planning under multi-constraint bottlenecks.
