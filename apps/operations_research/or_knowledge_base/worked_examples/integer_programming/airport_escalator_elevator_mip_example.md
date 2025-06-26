# Airport Escalator/Elevator Capacity MINLP Example

## Problem Statement

An airport can either install escalators or elevators. 
- Each escalator transports 20 people per minute, using 5 units of space. 
- Each elevator transports 8 people per minute, using 2 units of space. 
- The airport must transport at least 400 people per minute.
- There must be at least three times as many escalators as elevators.
- At least 2 elevators must be installed.

**Objective**: Find the numbers of escalators (x) and elevators (y) to _minimize_ total space used.

## Mathematical Formulation

Let:
- x = number of escalators (integer ¡Ý 0)
- y = number of elevators (integer ¡Ý 2)

**Minimize:**  
    5x + 2y

**Subject to:**  
    20x + 8y ¡Ý 400  
    x ¡Ý 3y  
    y ¡Ý 2  
    x, y integer

## Pyomo MILP Implementation Example

## Proven Optimal Solution

- Escalators: 18
- Elevators: 5
- Minimal Space: **100 units**

----
_This example is useful for facility/component selection under space, ratio, and minimum/maximum constraints with integer decision variables._
