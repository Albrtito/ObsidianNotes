---
aliases:
  - Exercises - Real Variable functions
tags:
  - review
  - CalcI
"References:":
  - "[[20240602 - 172958 - Real variable functions|Real variable functions]]"
cssclasses:
  - page-manila
---
# Exercises - Real variable functions. 

Collection of solving methods for exercises provided in UC3M calculus course. 

## Prove an inequality: 
Given:
$$
0< a < b: k > 0
$$
Prove:
$$
a < \sqrt{ab} < \frac{a+ b}{2} < b
$$
**Methods:**
Either go backwards or forwards. Backwards means start in the inequality to prove and end in some given fact or basic statement.

f.e: Go forwards: 
$$
\begin{gather}
a < b \\
a \cdot a < a \cdot b \\
a^2 < ab \Rightarrow \boxed{a < \sqrt{ab}}
\end{gather}
$$
f.e: Go backwards:
$$
\begin{gather}
\sqrt{ab}< \frac{a+b}{2}\\
2\sqrt{ab} < a + b \\
ab < \frac{(a+b)^2}{4}\\
ab < \frac{a^2 + b^2 + 2ab}{4}\\
0 < -2ab + a^2 + b^2\\
\boxed{0 < (a-b)^2 : a \not = b}
\end{gather}
$$

## Prove that some formula is multiple of m.

Basic method with this types of exercises is to first of all factor the relation. 
f.e: Given $n^2-n$ first obtain: $n(n-1)$

Once factored, reason what types of multiples those factors must be. For this last example, either n or n-1 must be even. Therefore $n^2 - n$ must be even. 

For composite numbers, find it’s decomposition in some of it’s multiples: 

### 2.3: Given $n^2-1$ with n odd, prove that it is multiple of 8: 
$$
n^2 - 1 = (n-1)(n+1)
$$
If n is odd both factors must be even. One multiple of 2 and the other multiple of 4. From this we get 8. 

### 5.1: $n\in N$ $10 ^n - 1$ => Multiple of 9


