---
aliases:
  - Partial derivatives
tags:
  - Calc
  - DiffCalc
  - review
"References:": 
cssclasses:
---
# Partial derivatives
In single variable calculus the derivative is defined as the rate of change in the function for changes in the independent variable: 
$$
df\over dx
$$
This same expression could also be applied to multi-variable functions, for example, for the function: 
$$
f(x,y)
$$
If we compute: 
$$
df\over dx
$$
We are studying the changes in f for variations in x. However we are not taking into account changes in y, another independent variable introduced. We could see that the changes in f for variations in y are given by the following expression: 
$$
df\over dy
$$
However this same thing happens, now we do not take into account changes in x.

In order to represent both changes we use the partial derivatives.
This derivatives have the same meaning that the ordinary ones, however use different symbolisation:

This would be the partial derivative of f with respect to x: The result would be the same as the derivative of f wrt to x. However with this notation we know that f is a multivariable function.
$$
\delta f\over \delta x
$$

> [!NOTE] Definition:
> For the function: 
> $$
> f(x_1,x_2,x_3,...,x_n)
> $$
> It’s partial derivatives are: 
> $$
>  


### Example: 
Given a function f with two independent variables:
$$
f(x,y) = 2x^2 + 3y^4x 
$$
Partial derivative for x
$$
{\delta f\over \delta x} = 4x + 3y^4 
$$
Partial derivative for y
$$
{\delta f\over \delta y} = 12y^3x
$$