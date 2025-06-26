# Factory Production Time Minimization (LP Example)

## Problem Statement
A pharmacy operates two factories producing acne and anti-bacterial creams using a base gel resource. Each factory has a distinct production rate and base gel consumption per hour. The pharmacy must meet minimum production requirements under a gel resource cap, with the objective of minimizing combined operating hours.

### Variables:
x1 = hours for Factory 1; x2 = hours for Factory 2

### Data:
- Factory 1: 12 acne cream/hr, 15 anti-bacterial cream/hr, 30 base gel/hr
- Factory 2: 20 acne cream/hr, 10 anti-bacterial cream/hr, 45 base gel/hr
- Max gel: 5000
- Min acne cream: 800
- Min anti-bacterial cream: 1000

### Mathematical Model:
Minimize: x1 + x2

Subject to:
12*x1 + 20*x2 >= 800    # Acne cream constraint
15*x1 + 10*x2 >= 1000   # Anti-bacterial cream constraint
30*x1 + 45*x2 <= 5000   # Base gel constraint
x1 >= 0, x2 >= 0

### Optimal Solution:
Min total time (rounded): 66.67 hours (x1=66.67, x2=0)
All requirements and constraints satisfied.

### Reference:
Pyomo code in working directory: factory_lp_solver.py (callable as solve_factory_lp).
