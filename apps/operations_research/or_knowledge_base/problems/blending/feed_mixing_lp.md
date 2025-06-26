# Animal Feed Mixing Linear Programming Problem

## Problem Statement
A farmer wants to mix Feed A and Feed B such that the mixture contains at least a minimum amount of protein and fat while minimizing cost.

- Feed A: $100/kg, 10 units protein, 8 units fat
- Feed B: $80/kg, 7 units protein, 15 units fat

Requirements:
- Mixture must have >= 30 units of protein.
- Mixture must have >= 50 units of fat.

## Mathematical Formulation

Let:
- x = kg of Feed A
- y = kg of Feed B

Minimize:  
    Cost = 100x + 80y

Subject to:
    10x + 7y >= 30   # Protein constraint
    8x + 15y >= 50   # Fat constraint
    x >= 0, y >= 0

## Pyomo Model

## Typical Optimal Result

- Minimum cost approx $327.66
- Feed A approx 1.06 kg
- Feed B approx 2.77 kg

This result ensures both nutrient requirements are met at minimum total feed cost.

## Applications

- Useful for diet problems, blending problems, cost minimization in food, agriculture, and manufacturing.
- The structure can be adapted/extended to more nutrients, feed types, or tighter/looser constraints as needed.
