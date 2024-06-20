---
aliases:
  - Taylor Polynomial
tags:
  - review
"References:":
  - https://www.youtube.com/watch?v=8SsC5st4LnI
  - https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=1s
  - "[[Calc_Theory_Taylor.pdf]]"
cssclasses:
---
# Taylor polynomial 
Taylor polynomial is used to **approximate a function near a given point using a polynomial**

**NOTE:** Remark that is an approximation **near a given point** → Remember this for limits


> [!NOTE] Definition: General form: 
> We define the Taylor polynomial of **degree n of f** near the point $x_0$ as:
> $$
P_{n,x_0}f(x) = \sum_{k = 0}^{n}\frac{f^{k)}(x_0)}{k!} (x-x_0)^k
> $$

**Remarks:**
+ When the point $x_0 = 0$ then the taylor polynomial is known as **McLaurin polynomial**
+ The following list compiles the basic taylor and McLaurin polynomials: [[20240620 - 160937 - Main Taylor Polynomials|Main Taylor Polynomials]]


> [!NOTE] Theorem:  
> If f and its derivatives up to order n exists at $x_0$, then:
> $$
> lim_{x \rightarrow x_0} \frac{f(x)-P_{n,x_0}f(x)}{(x-x_0)^n} = 0
> $$
> 

This means that the taylor polynomial gives out a **better approximation** the closer it is to the point $x_0$

## Usage of small-o
With taylor polynomials the [[20240620 - 162021 - Definition - small-o|small-o]] definition is used to gat
