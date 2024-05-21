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
a \cdot b = 
$$
