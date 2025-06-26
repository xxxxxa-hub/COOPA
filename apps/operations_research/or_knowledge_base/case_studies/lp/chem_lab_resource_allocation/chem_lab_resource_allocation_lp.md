# Chemistry Lab Resource Allocation Linear Program (Degenerate Solution Example)

## Problem Statement
A chemistry teacher plans to run two different experiments (experiment 1 and experiment 2), each consuming red and blue liquids and producing green gas and smelly gas, under the following constraints:
- Each experiment 1: Uses 3 units red, 4 units blue, produces 5 units green gas, 1 unit smelly gas.
- Each experiment 2: Uses 5 units red, 3 units blue, produces 6 units green gas, 2 units smelly gas.
- Resource limits: **80 red**, **70 blue**, **smelly gas at most 10 units** total.
- Objective: Maximize total green gas produced, i.e., maximize `5*x1 + 6*x2`
- Variables: x1 = count of experiment 1 (continuous, >=0); x2 = count of experiment 2 (continuous, >=0).
- Algebraic model:
    1. 3x1 + 5x2 <= 80      (Red liquid constraint)
    2. 4x1 + 3x2 <= 70      (Blue liquid constraint)
    3. 1x1 + 2x2 <= 10      (Smelly gas constraint)
    4. x1, x2 >= 0

## Key Lesson
With the given (very tight) smelly gas constraint, the LP admits only the trivial solution x1 = x2 = 0, i.e., **maximum green gas possible is 0**.

## Reference code
See `green_gas_pyomo_model.py` for Pyomo implementation.
