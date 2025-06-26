
# Dim Sum Restaurant Refill Minimization Problem

## Problem Description

A dim sum restaurant operates delivery by cart ('x' servers) and by hand ('y' servers). Each server interacts with a set number of customers per hour and requires a certain number of refills per hour. The restaurant must meet a minimum number of customer interactions per hour, meet a minimum share of cart deliveries, and ensure at least a certain number of hand servers for direct service. The objective is to minimize total refills per hour.

## Algebraic Model

- Let x = number of servers delivering by cart (integer, >= 0)
- Let y = number of servers delivering by hand (integer, >= min_hand)

### Objective
Minimize: 5x + 20y

### Constraints
1. 70x + 85y >= 4000                   (Minimum required customer interactions)
2. x >= 0.7 * (x + y)                  (At least 70% of servers are by cart)
3. y >= 3                              (At least 3 by hand)
4. x, y >= 0, integer

#### Integer-Linear Transformation for Cart Share Constraint

x >= 0.7*(x + y)  
=> x >= 0.7x + 0.7y  
=> x - 0.7x >= 0.7y  
=> 0.3x >= 0.7y  
=> 3x >= 7y

## Typical parameter values

- cart: 70 interactions/server/hr, 5 refills/server/hr
- hand: 85 interactions/server/hr, 20 refills/server/hr
- interactions required: 4000/hr
- cart must be at least 70% of servers
- hand servers at least 3

## Sample optimal solution (using GLPK on small scale)

- x = 54, y = 3 (54 cart, 3 hand)
- Total interactions: 4035
- Total refills per hour: 330
- All constraints satisfied

## Tags

minimize refills, integer programming, restaurant optimization, staff scheduling, MILP



---
**Tags:** MILP, staff optimization, refills minimization

**Section:** Restaurant and service staff scheduling problems
---

This file contains a comprehensive description, algebraic model, parameter values, algebraic insight (especially on integer-linearization of percentage constraints), and an optimal solution example for the dim sum restaurant refill minimization problem. It is provided as a resource for researchers and practitioners interested in staff scheduling, refills minimization, and MILP applications in restaurant operations.
