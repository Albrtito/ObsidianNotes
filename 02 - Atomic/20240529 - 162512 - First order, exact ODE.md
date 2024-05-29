---
aliases:
  - Exact ODE
  - First order, exact ODE
tags:
  - review
"References:": 
cssclasses:
---
# Exact ODEs:
Exact ODEs are those that can be written in the form: 

$$
\begin{gather}
M(x,u) + N(x,u)u' =0 \\
\text{and}\\
M(x,u) + N(x,u)u' = \frac{d}{dx}f(x,u(x)) = 0
\end{gather}
$$
And follow the **necessary condition:** 
$$
{\partial M\over \partial u} = {\partial N \over \partial x}
$$
**Remarks:**
+ [[20240528 - 110528 - Separable ODEs|Separable ODEs]] **are exact**: We can write them with the form: 
$$
M(x) + N(u)u' = 0
$$
## General form and solution:
The general solution for this type of equation is: 
$$
f(x,u(x)) = c
$$
This means that in order to find the solution we need to **find f(x,u(x))**

To find f we use [[Partial derivatives]]: 
1. 
