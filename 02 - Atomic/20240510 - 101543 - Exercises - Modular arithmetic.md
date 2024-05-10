---
aliases:
  - Exercises - Modular arithmetic
tags:
  - Discrete
"References:": 
cssclasses:
  - page-manila
---
# Exercises - Modular arithmetic: 
## 12.1: 
Given a = 92 and b = 84, use Euclid’s algorithm to compute d = gcd(a, b), Find integers x, y ∈ Z such that ax + by = d.

a = 92
b = 84
1. gcd(92,84) = d => gcd(92,84) = gcd(84,8) = gcd(8,4) = gcd(4,0) = 4
	$$
	\begin{gather}
	92 = 1\cdot 84 + 8 \Rightarrow 8 = 92 - 84\\
	84 = 10\cdot 8 + 4 \Rightarrow 4 = 84 - 10\cdot 8\\
	8 = 2 \cdot 4 + 0
	\end{gather}
	$$
+ 4 = d
2. Finc x, y $\in$ >; 
	+ ax + by = d
	$$
	4 = -10 \cdot 92 + 8 \cdot 11 \rightarrow x = -10, y = 11
	$$

## 12.7: Diophantine
Find the integer solutions of the Diophantine equations: 
1. 28x + 36y = 44. 
2. 66x + 550y = 88.

**Solving:**
1. Solve the first equation:
	i. Find greatest common divisor of 28 and 36. 
	+ gcd(28, 36) = gcd(7\*4, 6\*4) = 4

	ii. Because 4 | 44 => There is a solution
	
	iii. We can simplify the equation by dividing by 4. Obtaining: 7x + 9x = 11
	
	iv. Euclid’s algorithm??
	$$
		\begin{gather}
		9 = 7 * 1 + 2 \Rightarrow 2 = 9 - 7\\
		7 = 3 * 2 + 1\\
		2 = 2 * 1 + 0
		\end{gather}
	$$
		Then: 
		

   
   