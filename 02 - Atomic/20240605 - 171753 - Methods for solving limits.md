---
aliases:
  - Methods for solving limits
tags:
  - review
  - CalcI
"References:": 
cssclasses:
---
# Methods for solving limits:

## Theorems: 
List of useful theorems for limit solving: 
$$
lim_{x\rightarrow x_0} f(x)
$$
1. **If you can find a function g(x) and h(x):** g(x) ≤ f(x) ≤ h(x) then:
   
    → [[20240605 - 171939 - Theorem - Sandwich lemma|Sandwich lemma]]
  
2. For limits such as:
	$$\lim_{x\rightarrow \alpha} 1^{\infty /-\infty}$$
	→ [[20240605 - 175232 - Theorem - Exponential limits|Exponential limits]] 

## For limits at infty:

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
For limits such as: 
$$
\begin{gather}
\lim_{x\rightarrow x_0} f(x): \\ f(x) = \frac{P_1(x)}{P_2(x)} =\frac{a_0+xa_1+x^2a_2...+ x^na_n}{a_0+xa_1+x^2a_2...+ x^na_n}
\end{gather}
$$

There are three posible casos based on the **maximum degree of x in P1 and P2**: 

1. If the max degree of x in P1 is greater than the one in P2 then **the limit goes to infinity**
   $$
   Max(P_1) > Max(P_2) \Rightarrow \infty
   $$
   
   The idea is that the part above grows larger than the one below. Then it goes to infty before being able to be divided by anything. 
   
   f.e: 
	   $$
	   \lim_{x\rightarrow x_0} \frac{x^2+2}{x} = \infty
	   $$

2. If the degree of x in P2 is greater than the one in P1 then **the limit goes to 0**
   
   Same idea, but if the part below goes to infinity first, then it is division by infinity → 0 
   $$
   Max(P_2) > Max(P_1) \Rightarrow 0
   $$
   f.e: 
   $$
	   \lim_{x\rightarrow x_0} \frac{x}{x^2 + 2} = 0
	$$

3. If the degree of x in P2 is equal to the one in P1 then:
   **The limit is equal to the division of both coefficients of**: $x^{\text{maxDegree}}$
   
   f.e: 
	   $$
	   \lim_{x\rightarrow x_0} \frac{4x^2}{x^2 + 2} = \frac{4}{1} = 4
	   $$
	   
	   