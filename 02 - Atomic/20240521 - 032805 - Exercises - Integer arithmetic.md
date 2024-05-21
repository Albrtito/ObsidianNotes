---
aliases:
  - Exercises - Integer arithmetic
tags:
  - review
  - Discrete
"References:": 
cssclasses:
  - page-manila
---
# Exercises - Integer arithmetics: 

## 12.1
Given a = 92 and b = 84, use Euclid’s algorithm to compute d = gcd(a, b), Find integers x, y ∈ Z such that ax + by = d.

gcd(92,84)  = gcd(84,8) = gcd(8,4) = gcd(4,0) = 4
This is equal to: 
$$
\begin{gather}
92 = 84\cdot1 + 8 \\
84 = 8 \cdot 10 + \boxed{4}\\
8 = 4\cdot 2 + 0
\end{gather}
$$
Then gcd(a,b) = 4

Going backwards:
$$
\begin{gather}
4 = 84 - 8 \cdot 10 \\
8 = 92 - 84\\
\Rightarrow\\
4 = 84 - (92-84) \cdot 10 = 11\cdot 84 - 10 \cdot 92
\end{gather}
$$
Then x = -10 and y = 11

## 12.2
The product of two natural numbers is 1260, and their lcm is 630. Find those numbers.
$$
a \cdot b = 1260
$$
$$
lcm(a,b) = 630
$$
We know that: 
$$
a \cdot b = gcd(a,b) \cdot lcm(a,b)
$$
Then: 
$$
1260 = 630 \cdot gcd(a,b)
$$
gcd(a,b) = 2

## 12.3
Positive divisors of the number ….


## 12.7
Integer solutions of Diophantine equations: 

1. 28 x + 36y = 44
	
	**Check possible solution**: If gcd(28,36)| 44
	gcd(28,36) = 4  and 4 | 44 => There is a  possible solution. 
	
	Get x y such as: 28 x + 36 y = 4
	
	**From Euclid’s theorem:** 
	$$
	\begin{gather}
	36 = 28 \cdot 1 + 8\\
	28 = 8 \cdot 3 + 4\\
	8 = 4 \cdot 2 + 0
	\end{gather}
	$$
	**Unrolling**: 
	$$
	\begin{gather}
	4 = 28 - 8\cdot 3\\
	8 = 36 - 28\\
	\Rightarrow\\
	4 = 28 - (36-28) \cdot 3 \Rightarrow 4 = 4\cdot 28 - 3 \cdot 36
	\end{gather}
	$$
	**Where** x = 4 ,  y = -3
	
	**Then**: 
	$$
	x_k = 4(11) + \frac{36k}{4} = 44 + 9k
	$$
	$$
	y_k = -3(11) + \frac{28k}{4} = -33 + 7k
	$$
2. 66x + 550y = 88

**Check possible solution:**
+ Get gcd(66,550)
$$
\begin{gather}
550 = 66 \cdot 8 + 22\\
66 = 22 \cdot 3 + 0
\end{gather}
$$
	gcd(66,550) = 22
	
+ Check that gcd(a,b) | 88 => True, as 22 | 88
+ Obtain a solution for x and y such as: 
$$
x\cdot a + y \cdot b = 22
$$
**Unroll Euclid’s (used for gcd)**
$$
\begin{gather}
22 = -8 \cdot 66 + 1\cdot 550
\end{gather}
$$
