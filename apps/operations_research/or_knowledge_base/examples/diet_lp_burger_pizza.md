# Example Diet Optimization: Burgers and Pizza (Minimize Cholesterol)

**Problem Statement:**
A man needs at least 130 units of fat and 3000 calories daily.  
- Each burger: 10 fat, 300 cal, 12 cholesterol
- Each pizza slice: 8 fat, 250 cal, 10 cholesterol
- Must have at least twice as many slices of pizza as burgers (y >= 2x)

**Variables:**
x = burgers (integer >= 0)  
y = slices of pizza (integer >= 0)

**Objective:**
Minimize total cholesterol:   12x + 10y

**Constraints:**
10x + 8y >= 130         # Fat  
300x + 250y >= 3000     # Calories  
y >= 2x                 # Pizza/burger ratio  

**Optimal solution:**
x = 5, y = 10  
Objective value: 12*5 + 10*10 = 160 cholesterol  
All constraints satisfied.

**Model and solution implemented in Pyomo via algebraic_optimizer_agent.**
