Title: Allocating Funds with Weighted Average Risk Constraint

Problem Statement:
Given several investment/betting options, each with a potential payout per dollar and an associated chance of loss (risk), allocate a given budget among these options to maximize total expected payout. Constraint: the average risk of the total allocation (weighted by allocation) must not exceed a specified bound.

Mathematical Formulation:
Let there be n options. For each option i:
- x_i: allocation to option i (decision variable)
- r_i: risk (probability of losing money) for option i (parameter)
- p_i: payout per dollar for option i (parameter)

Objective:
maximize  sum_i p_i * x_i

Constraints:
1. Budget: sum_i x_i <= TotalBudget
2. Average risk: sum_i r_i * x_i / sum_i x_i <= risk_threshold (if allocation > 0; otherwise constraint is vacuously satisfied)
3. x_i >= 0 for all i

In code (Pyomo example):

from pyomo.environ import *
model = ConcreteModel()
options = [1,2,3]
payout = {1: 1.2, 2: 0.5, 3: 0.1}
risk = {1: 0.5, 2: 0.25, 3: 0.1}
budget = 100000
risk_limit = 0.3
model.x = Var(options, within=NonNegativeReals)

def total_bet(m):
    return sum(m.x[i] for i in options)
model.total_bet = Expression(rule=total_bet)

def avg_risk(m):
    if value(m.total_bet) == 0:
        return 0
    return sum(risk[i] * m.x[i] for i in options)/value(m.total_bet)
model.avg_risk = Expression(rule=avg_risk)

model.budget_constraint = Constraint(expr= model.total_bet <= budget)
def risk_constraint_rule(m):
    return sum(risk[i] * m.x[i] for i in options) <= risk_limit * (m.total_bet)
model.risk_constraint = Constraint(rule=risk_constraint_rule)

model.obj = Objective(expr=sum(payout[i] * model.x[i] for i in options), sense=maximize)

Insight:
- In this problem, any allocation to an option with per-dollar risk exceeding the specified risk threshold is excluded.
- Among remaining options, allocate as much as possible to the option(s) with highest payout per dollar, subject to the risk/budget constraints.

Typical applications: betting, portfolio allocation with average risk, resource allocation where an average quality/risk threshold must be met.
---
