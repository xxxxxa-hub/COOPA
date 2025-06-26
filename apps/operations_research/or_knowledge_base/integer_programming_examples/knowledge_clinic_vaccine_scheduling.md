
# Clinic Vaccine Scheduling: Integer Linear Programming Example

## Problem Description

A clinic administers two vaccines: pills (10 min/admin) and shots (20 min/admin). The clinic must:
- Deliver at least 3 times as many shots as pills
- Administer at least 30 pill vaccines
- Administer the maximum total number of vaccines in 10,000 minutes

## Mathematical Model

Let:
- x = number of pill vaccines (integer)
- y = number of shot vaccines (integer)

Objective:
- Maximize x + y (total vaccinated)

Subject to:
- 10x + 20y ¡Ü 10000  (total time constraint)
- y ¡Ý 3x  (at least 3x as many shots as pills)
- x ¡Ý 30  (at least 30 pills)
- x, y ¡Ý 0 and integer

## Optimal Solution

- Maximum patients vaccinated: 571
- Pills administered: x = 142
- Shots administered: y = 429

Solution satisfies all constraints and fully utilizes the time budget.

## Model Implementation

A Pyomo+GLPK Python model solving this is saved as: `max_vaccination_ilp.py`.
The model defines variables, constraints, and objective as above.

---

For similar integer LP scheduling/resource allocation problems, use variables with appropriate bounds, linear constraints, and integer domains.
