---
aliases:
  - Methods for solving limits
tags:
  - review
"References:": 
cssclasses:
---
# Methods for solving limits:

## Theorems: 
List of useful theorems for limit solving: 
$$
lim_{x\rightarrow x_0} f(x)
$$
+ **If you can find a function g(x) and h(x):** g(x) ≤ f(x) ≤ h(x) then: [[20240605 - 171939 - Theorem - Sandwich lemma|Sandwich lemma]]
+ [[20240605 - 175232 - Theorem - Exponential limits|Exponential limits]]
## Limits at infty:

For solving limits at infty we can use several methods and strategies. Of course, because Calculus is just a bunch of happy ideas very smart people had to ruin the life of the student these are just some suggestions that could work. Who knows what ur dealing with!

1. **Look for common factors**
**f.e:** See here that after removing (x-3) we can compute the limit
$$
\begin{aligned}\lim_{x\to3}\frac{x^2-9}{x^2-5x+6}=\lim_{x\to3}\frac{x+3}{x-2}=6.\end{aligned}
$$

2. **Divide by the greatest term**
**f.e:** See here that after dividing by x we get a limit that can be computed. However note that this computation can be also computed based on what is explained in [[#Polynomial quotients]]  
$$
\lim_{x\to\infty}\frac{x+3}{x-4}=\lim_{x\to\infty}\frac{1+3/x}{1-4/x}=1.
$$

3. **Use the conjugate**
**f.e:** When having roots, it is reliable to say that in most cases the solution goes towards conjugates. 
$$
\lim\limits_{x\to\infty}\left(\sqrt{x+1}-\sqrt{x}\right)=\lim\limits_{x\to\infty}\frac{1}{\sqrt{x+1}+\sqrt{x}}=0.
$$

### Polynomial quotients: