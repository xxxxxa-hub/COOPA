# Ad Campaign MILP Example: Streaming Platforms Audience Maximization

## Problem Summary
A food company wants to maximize its total advertising audience by purchasing commercials across three streaming platforms (Pi TV, Beta Video, Gamma Live), each with different costs, reach, and placement requirements.

## Decision Variables
- x1: Number of Pi TV commercials (integer, >= 0)
- x2: Number of Beta Video commercials (integer, >= 0)
- x3: Number of Gamma Live commercials (integer, >= 0)

## Data
| Platform     | Cost per Commercial | Audience per Commercial | Limits             |
|--------------|--------------------|------------------------|--------------------|
| Pi TV        | $1200              | 2,000                  | >= 20% of all slots |
| Beta Video   | $2000              | 5,000                  | <= 8 commercials    |
| Gamma Live   | $4000              | 9,000                  | <= 1/3 of all slots |

Weekly budget: $20,000

## Mathematical Formulation

**Objective:**  
Maximize total audience:  
`Maximize 2000*x1 + 5000*x2 + 9000*x3`

**Constraints:**
- Budget: `1200*x1 + 2000*x2 + 4000*x3 <= 20000`
- Beta Video: `x2 <= 8`
- Gamma Live share: `x3 <= (1/3)*(x1 + x2 + x3)`
- Pi TV share: `x1 >= 0.2*(x1 + x2 + x3)`
- Non-negativity & integrality: `x1, x2, x3 >= 0` and integers

### Linearized Share Constraints (for MILP)
Let S = x1 + x2 + x3 (total commercials):

- Gamma Live: `x3 <= (1/3)S` -> `3x3 <= S` -> `2x3 - x1 - x2 <= 0`
- Pi TV: `x1 >= 0.2S` -> `5x1 >= S` -> `4x1 - x2 - x3 >= 0`

## Optimal Solution (via MILP solvers, e.g., Pyomo+GLPK)
- x1 (Pi TV): 3
- x2 (Beta Video): 8
- x3 (Gamma Live): 0
- Max audience: **46,000**

**All constraints are tight or satisfied. Gamma Live is not chosen due to cost and other share constraints.**

## Pyomo Modeling Comments
- Use integer variables and linearized constraints for share/fraction.
- Budget and slot constraints simply model as inequalities.
- Solution achieved using MILP solver (GLPK).
