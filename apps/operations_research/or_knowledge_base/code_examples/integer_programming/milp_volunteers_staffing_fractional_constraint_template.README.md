# MILP Volunteers/Staffing Fractional Constraint Template (Pyomo)

## Description
This code template provides a Pyomo-based Mixed Integer Linear Program (MILP) for optimizing volunteer/staff allocation with integer constraints and ratio-based (fractional) restrictions between staff categories. The primary example maximizes deliverables (gifts) subject to cost, integer, minimum, and ratio/percentage constraints. Typical use cases include:
- Staffing and volunteer assignment in nonprofits and operations research.
- Problems where you must limit or guarantee the proportion of a staff type (e.g., no more than 30% seasonal).
- Incorporation of budget (points/cost) constraints and minimum full-time staffing.

## Features
- Integer variables for seasonal (s) and full-time (f) volunteers.
- Points/cost budget constraint.
- Minimum full-time volunteer constraint.
- Ratio constraint (e.g., s/(s+f) <= alpha) linearized for MILP: (1-alpha)s <= alpha f.
- Example linearization for alpha = 0.3: 7s <= 3f.
- Demonstrates solution extraction and verifying constraints after solve.

## Usage
- Start from this template for any MILP staff/resource allocation in which you need integer staffing variables and ratio/fraction/proportion requirements.
- Adapt constraints and variable names to new domains (healthcare, education, disaster logistics, etc.).

## Reference location:
- code_examples/integer_programming/milp_volunteers_staffing_fractional_constraint_template.py

## Related examples:
- code_examples/workforce_sizing_MILP_pyomo_snow_removal.md  (crew sizing, shift and budget)
- code_examples/integer_programming/integer_vehicle_problem_corn_transport.py

---

Store this file as a template for solving future MILP staff, volunteer, or team allocation problems with integer constraints and percent/ratio restrictions.