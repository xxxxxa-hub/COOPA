# Mask Box Shipping Integer Programming Example

**Problem Statement:**
A mask making company ships masks to their stores using small and large boxes. A small box holds 25 masks, a large box holds 45 masks. There must be at least three times as many small boxes as large boxes, at least 5 large boxes must be used, and at least 750 masks must be shipped. Minimize the total number of boxes.

**Integer Programming Formulation:**
Let s = small boxes, l = large boxes (integers, >= 0):

- Minimize:   s + l  
- Subject to:  
    - 25s + 45l >= 750  (minimum masks shipped)  
    - s >= 3l            (stacking/stocking business rule)  
    - l >= 5             (minimum large boxes)  
    - s, l integers >= 0  

**Optimal Solution:**  
s = 20, l = 6, total boxes = 26
