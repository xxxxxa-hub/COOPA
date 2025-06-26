# Newspaper Delivery Dogs: Integer Linear Programming Formulation

## Problem Statement
A training school allocates labradors and golden retrievers (dogs) to deliver newspapers, maximizing total deliveries subject to limited 'bone treat' resource and proportion constraints:
- A labrador delivers 7 newspapers at a time, needs 5 treats.
- A golden retriever delivers 10 newspapers at a time, needs 6 treats.
- 1500 treats available; at least 50 goldens; at most 60% of all dogs can be labradors.

## Mathematical Formulation
Let L = number of labradors, G = number of golden retrievers (both integers, L >= 0, G >= 50):

Maximize:  
    7*L + 10*G

Subject to:  
    5*L + 6*G <= 1500            (treat resource constraint)  
    G >= 50                      (minimum golden retrievers)  
    L >= 0                       (non-negativity)  
    2L <= 3G                     (at most 60% labradors, i.e., L/(L+G) <= 0.6)

## Modeling Notes
- The ratio constraint for 'no more than 60% labradors' can be algebraically rewritten as:  
    L <= 0.6*(L + G)  =>  2L <= 3G (for integer variables)
- Sometimes Pyomo or MIP solvers may incorrectly report such models as infeasible. If this happens, use brute force or enumeration if variable bounds are small.

## Optimal Solution (for problem data above)
Optimal: L = 0, G = 250  
Max newspapers delivered: 2500  
All resources should be allocated to golden retrievers; labrador usage would reduce the objective.

## File Reference
The Pyomo script solving this is named: labrador_golden_optimizer.py

## Lessons Learned
- Ratio constraints in integer programming may require rescaling/rewriting for solver compatibility.
- Try explicit enumeration if solver returns infeasible, as feasible integer solutions may exist.
