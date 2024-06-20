---
aliases:
  - Improper Integrals
Date: 2024-03-12
tags:
  - review
  - DiffCalc
  - CalcI
"References:": 
sr-due: 2024-06-24
sr-interval: 28
sr-ease: 230
---
# Improper Integrals
Improper integrals are those integrals defined on an **infinite interval**. There are different improper integrals of **first kind**: 
$$
\begin{align}
&1. \int_a ^\infty f(x) dx = \lim_{N \rightarrow \infty} \int_a^N f(x)dx\\\\
&2. \int_\infty ^b f(x) dx = \lim_{N \rightarrow \infty} \int_{-N}^b f(x)dx\\\\
&3. \int^\infty_{-\infty} f(x) dx = \int_{-infty}^a f(x) dx + \int^\infty _a f(x)dx : a \in \mathbb R
\end{align}
$$

Based on the solution of this limits we can say that there is (or not) a solution to the integral: 
+ The limit **converges** => There is a solution
+ The limit **diverges** => There is no solution

> [!NOTE] Theorem
> An improper integral is always of the form: 
$$
> \int_a^\inf h(t)dt = lim_{A\rightarrow \inf} \int_a^A h(t) dt
$$

+ Integral can go to 0, inf, a number, or nowhere

> [!NOTE] Theorem 
> If the integral $\int_a^A h(t) dt$ exist for each a, A>a and the limit also exist, the improper integral **converges**

