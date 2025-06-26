# Farmer Crop Allocation Linear Program

## Problem Description
A farmer must decide how many acres of turnips (x1) and pumpkins (x2) to plant, to maximize revenue given constraints on land, watering time, and pesticide budget.

### Data
- Land available: 500 acres
- Watering time available: 40,000 min
- Pesticide budget: $34,000

#### Crop Requirements per Acre
| Crop     | Watering (min) | Pesticide ($) | Revenue ($) |
|----------|----------------|---------------|-------------|
| Turnips  | 50             | 80            | 300         |
| Pumpkins | 90             | 50            | 450         |

## Model Formulation

**Variables:**
- x1: acres of turnips (continuous, >= 0)
- x2: acres of pumpkins (continuous, >= 0)

**Objective:**  
Maximize total revenue  
`max 300*x1 + 450*x2`

**Constraints:**  
- x1 + x2 <= 500 (land)
- 50*x1 + 90*x2 <= 40,000 (watering)
- 80*x1 + 50*x2 <= 34,000 (pesticide)
- x1, x2 >= 0

## Optimal Solution (solved via Pyomo/IPOPT or similar)
- x1 (turnips): 125.0
- x2 (pumpkins): 375.0
- Maximum revenue: **$206,250**

- Binding constraints at optimality: Land, Watering
- Pesticide constraint not binding at optimum.

## Reuse
This model template applies to any two-crop (or two-product) allocation problem with additive resource constraints and linear objective.

---

**Keywords:** crop allocation, farm, LP, Pyomo, binding constraint, example solution, agricultural planning, resource allocation, linear programming

**Index categories:** agricultural planning, resource allocation, linear programming
