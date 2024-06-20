---
aliases:
  - Method - Partial Fractions
  - Partial Fractions
tags:
  - review
  - CalcI
  - DiffCalc
"References:": 
cssclasses:
---
# Partial fractions:
The partial fraction method is used to **decompose**fractions into **sums of simpler** rational functions. The objective is to rewrite expressions such as: 
$$
\frac{3x}{x^2 -x -2}
$$
by partitioning them into smaller fractions based on the decomposition of the denominator by it’s rots. For the previous example we would obtain something such as: 
$$
\frac{1}{x +1} + \frac{2}{x -2}
$$
## Method:

**CONDITION:**
This method is used for fractions such as: 
$$
\frac{P(x)}{Q(x)}
$$
There are two variations of the method:

There’ll be two different possibilities whether: 
1.  $\deg(P(x)) < \deg(Q(x))$ 
2. $\deg(P(x)) > \deg(Q(x))$ 

### For deg(P(x)) < deg(Q(x))
Perform [[20240620 - 172412 - Method - Polynomial long division|Polynomial long division]] in order to restructure the polynomic fraction.

### For deg(P(x)) > deg(Q(x))

1. Rationalise Q(x) into it’s factors. 
2. Write an equality such as: 
$$
\frac{P(x)}{Q(x)} = \frac{A}{F_1(x)} +\frac{B}{F_2(x)} + ... + \frac{N}{F_n(x)} 
$$
