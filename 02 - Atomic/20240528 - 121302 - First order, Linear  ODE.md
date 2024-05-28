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
The method is based on finding the solution for the homogeneous and then for the particular equation
1. First, solve the homogeneous equation (without F(x)). This solution is: 
$$
\begin{gather}
a_1\frac{du}{dx} + a_0 u = 0\\
\frac{du}{dx} = -\frac{a_0u}{a_1}\\
\frac{du}{u} = -\frac{a_0dx}{a1}\\
\int \frac{1}{u} du = \int -\frac{a_0}{a1} dx\\
\ln|u| = \int -\frac{a_o}{a_1}dx\\
\boxed{u_h = e^{\int-\frac{a_o}{a_1}dx}}
\end{gather}
$$

We simplify calling g(x) to:

$$
g(x) = \int^{}_{x}\frac{a_0(t)}{a_1(t)}dt
$$
 2. We can create a relation between this new solution we have found for the homogeneous and F(x) in order to find a **solution to the particular form** #Duda WHAT?
$$
\left[e^{g(x)} u\right]^{\prime}=\frac{F(x) e^{g(x)}}{a_1(x)}
$$
This expression can be simplified by direct integration: 
**Note:** $[e^{g(x)}u]'$ is **all** derived. Then an integer just removes the derivative leaving $e^{g(x)}u$
$$
e^{g(x)} u_p=\int^x \frac{F(x) e^{g(x)}}{a_1(x)}
$$
Simplified: 
$$
 u_p=e^{-g(x)}\int^x e^{g(x)}\frac{F(x) }{a_1(x)}
$$
Because we know the value of $e^{g(x)}$ already we have obtained the particular form.

 3. The final **general solution is given based on the principle of superposition** (sum of both homogeneous and particular parts)
**Note:**
 + The homogeneous equation is multiplied by a constant (A) that will appear from integration of g(x). (it’ll be some e to some constant) 
$$
u(x) = u_h + u_p
$$
$$
u(x) = Ae^{g(x)} + e^{-g(x)}\int^x e^{g(x)}\frac{F(x) }{a_1(x)}
$$

**Remark:**
+ The value: $e^{g(x)}\over a_1(x)$ is called **integrating factor** because it reduces the non-homogeneous part in order to solve by direct integration. #Duda : Same as last one in this same document. 
+ This solution is also true for an ODE of n-th order 

## Solved examples: 
