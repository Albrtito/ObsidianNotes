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

## 1. Prove an inequality: 
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

\end{gather}
$$