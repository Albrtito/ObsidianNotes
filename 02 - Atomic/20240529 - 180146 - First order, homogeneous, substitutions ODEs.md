---
aliases:
  - First order, homogeneous, substitutions ODEs
  - Homogeneous, substitutions ODEs
tags:
  - review
  - DiffCalc
"References:": 
cssclasses:
sr-due: 2024-06-04
sr-interval: 1
sr-ease: 210
---
# First order, homogeneous, substitutions ODEs
Sometimes we can use an [[20240529 - 135228 - Method - u-substitution|u-substitution]] in order to transform an ODE to a form that we know and can solve. 
There are several known substitutions.

During the DiffCalc course we’ll only look at x/u substitutions.
## x/y Substitutions:

This kind of ODEs are those that can be solved by using a **change of variable**:
u → x/u or u → u/x 

### General form and solution:

All homogeneous non lineal first order ODEs have the following general form: 
$$
M(x,u) + N(x,u)u' = 0
$$

Those that can be solved with an x/u substitution must comply with the following **condition**: 
$$
\begin{gather}
{du\over dx} = u' = F(x/u) \\
\text{or}\\
{du\over dx} = u' = F(u/x) \\
\end{gather}
$$
In order to check that the condition holds, rearrange the equation for u’. 

Once checked that the condition holds we can apply [[20240529 - 135228 - Method - u-substitution|u-substitution]] with the following changes:

**Introduce y:** 
+ y = x/u 
+ y = u/x

Finally, the new ODE is [[20240528 - 110528 - Separable ODEs|Separable ODEs]], and therefore solvable.
