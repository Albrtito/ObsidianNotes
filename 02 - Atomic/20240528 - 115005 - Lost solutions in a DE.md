---
aliases:
  - Lost solutions in a DE
tags:
  - review
  - DiffCalc
"References:": 
cssclasses:
sr-due: 2024-06-06
sr-interval: 3
sr-ease: 252
---
# Lost solutions in a DE
When solving DEs, there is a chance that the Differential Equation expression is not valid for some value of y when using some method to obtain a solution to the DE.

## Separable DEs:

For example, if we have the following separable ODE: 
$$
\frac{dy}{(1-y)^2} = 2x dx
$$
+ We know that y ≠ 1 , to divide by something different from 0.
+ 
Because of this new rule we don’t take into account a possible solution for y: y(x) = 1
**This solution is a lost solution.** 

**In general:** 
Given a separable equation of the form:
$$
y' =  f(x)g(y)
$$
**All roots of g(y) are lost solutions.**