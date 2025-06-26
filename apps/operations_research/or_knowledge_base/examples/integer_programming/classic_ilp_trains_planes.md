# Max Profit for Trains and Planes (Integer Linear Programming Example)

**Problem Statement:**  
A hobbyist makes model trains and planes using wood and paint.  
- A train requires 3 units wood, 3 units paint; profit $8  
- A plane requires 4 units wood, 2 units paint; profit $10  
- Total wood: 120 units; total paint: 90 units  
- Variables: x1 = trains (integer), x2 = planes (integer)  
- Constraints:  
  - 3x1 + 4x2 <= 120  
  - 3x1 + 2x2 <= 90  
  - x1, x2 >= 0

**Model (Pyomo, Integer):**

**Optimal Solution:**  
- Make 20 trains, 15 planes for maximum profit = $310.

**Keywords:**  
production planning, ILP, two-resource, integer variables, pyomo, maximal profit, example
