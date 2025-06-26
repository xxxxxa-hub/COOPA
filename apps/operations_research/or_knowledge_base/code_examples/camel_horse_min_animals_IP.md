# Camel and Horse Minimum Animal IP Example

## Problem (from Middle East Delivery Problem)

A company delivers packages to customers using camels and horses.
- Each camel carries 50 packages; each horse 60.
- Camel needs 20 units of food; horse 30.
- Must deliver at least 1000 packages; available food is 450 units.
- Horses cannot exceed number of camels.
- Minimize the total number of animals.

## Variables
- x: integer, number of camels
- y: integer, number of horses

## Model

- Minimize x + y
- Subject to:
    - 50x + 60y >= 1000    (Package constraint)
    - 20x + 30y <= 450     (Food constraint)
    - y <= x               (Horse <= Camel)
    - x, y >= 0, integer

## Solution

- x = 12, y = 7
- Minimum animals = 19
- Constraints are exactly satisfied:
    - Packages: 1020 >= 1000
    - Food: 450 <= 450
    - Horses <= Camels

## Pyomo Implementation

See the associated Python file.