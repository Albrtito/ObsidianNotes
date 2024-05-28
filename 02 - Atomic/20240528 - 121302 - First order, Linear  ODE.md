---
aliases:
  - First order, Linear  ODE
tags:
  - review
  - DiffCalc
"References:": 
cssclasses:
---
# First order, linear ODE 
An ODE is linear and has order 1 when the largest derivative appearing in the relation is the first derivative and the largest order of the dependent variable y is equal to 1. 

## General form and solution:

This DE are of the form: 
$$
a_1(x)u' + a_0(x)u = F(x)
$$
+ Solution is the function u(x) or u.
**Where:**
+ $a_1(x)$ is a function of x multiplying the first derivative of u
+ $a_2(x)$ is a function of x multiplying the function u
+ F(x) is a function of x

**Remarks:**
+ When F(x) = 0 the DE is **homogeneous**

### General solution: 

1. First, solve the homogeneous equation (without F(x)). This solution is: 
   $$
   u_h(x) = e^{-g(x)}
   $$
   Where g(x) is equal to: 
   $$
   g(x) = \int^{}_{x}\frac{a_0(t)}{a_1(t)}dt
   $$
   