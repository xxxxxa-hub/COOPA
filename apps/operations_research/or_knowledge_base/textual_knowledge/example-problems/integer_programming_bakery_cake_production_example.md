**Title:** Bakery Cake Production Integer Programming Example

**Problem Statement:**
A bakery has 20,000 grams of batter and 14,000 grams of milk to make crepe cakes, sponge cakes, and birthday cakes.
- Crepe cake: needs 400g batter, 200g milk, $12 profit
- Sponge cake: needs 500g batter, 300g milk, $10 profit
- Birthday cake: needs 450g batter, 350g milk, $15 profit

How many of each cake should be made to maximize profit? Variables must be non-negative integers.

**Mathematical Model:**
Let x1 = crepe cakes, x2 = sponge cakes, x3 = birthday cakes.

Maximize: 12*x1 + 10*x2 + 15*x3

Subject to:
- 400*x1 + 500*x2 + 450*x3 <= 20000     (batter constraint)
- 200*x1 + 300*x2 + 350*x3 <= 14000     (milk constraint)
- x1, x2, x3 >= 0 and integer

**Optimal Solution:**
- Crepe cakes: 14
- Sponge cakes: 0
- Birthday cakes: 32
- Maximum profit: $648

**Interpretation:**
- The optimal production plan uses all available resources and produces 14 crepe cakes and 32 birthday cakes for a profit of $648.
