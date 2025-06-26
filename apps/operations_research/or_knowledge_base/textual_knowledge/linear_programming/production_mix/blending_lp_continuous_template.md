# Linear Programming Template: Blending/Resource Allocation (Continuous Variables)

## Problem Structure

A typical problem instance:
- Objective: Maximize (or minimize) total profit/revenue/cost by determining continuous quantities of multiple products/processes.
- Decision Variables: Continuous quantities (e.g., tanks produced, product mix).
- Each product/process consumes several resources (compounds, materials), each bounded above by their availability.
- Each product/process provides specific (possibly different) per-unit profit/revenue/cost.

## Mathematical Formulation

Let:
- x_i = quantity (continuous) of product/process i to produce/process.

Maximize:  
$\sum_{i} c_i x_i$  
where $c_i$ = profit/revenue/cost per unit of i.

Subject to, for each resource j:  
$\sum_{i} a_{ji} x_i \leq b_j$  
where $a_{ji}$ = units of resource j required per unit of i, $b_j$ = total available units of resource j.

And  
$x_i \geq 0 \ \forall i$

## Example

**Maple Oil Blending:**

Variables:
- x1 = tanks light oil
- x2 = tanks non-sticky oil
- x3 = tanks heavy oil

Objective:  
Maximize $550x_1 + 750x_2 + 950x_3$

Constraints:
- $3x_1 + 6x_2 + 9x_3 \leq 250$ (compound A)
- $3x_1 + 2x_2 + 3x_3 \leq 150$ (compound B)
- $x_1, x_2, x_3 \geq 0$

## Solution Agent

This template was solved using the `algebraic_optimizer_agent` (Pyomo/GLPK). See the referenced code and the problem statement embedded above for direct reuse.

## Reference Python Model

Original Pyomo code saved as: `mapleoil_lp_model.py`

---

_Use this template as a starting point for blend/resource allocation problems involving continuous decisions and linear constraints/objectives._
