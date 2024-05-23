---
aliases:
  - Modular arithmetics - Multiplicative inverse of x
  - Definition - Modular arithmetics - Multiplicative inverse of x
tags:
  - Discrete
"References:": 
cssclasses:
---
# Multiplicative inverse of x in modular arithmetics: 


> [!NOTE] Definition: Multiplicative inverse 
> The multiplicative inverse y of an integer x in $Z_m$ is such as: 
> $$
> x \cdot y = 1 \mod m
> $$ 
> 

**Remarks:**
+ In modular arithmetics, there **does not exist in general** the multiplicative inverse of an integer x.
## Properties:
Even if there is no multiplicative inverse in most cases, two properties hold, **although not in general in $Z_m$**

1. **Cancellation law:** 
	**IF:**$x \not = 0$ and $x\cdot y = c \cdot z$ **THEN:** y = z
		
2. **IF:** $x\cdot y = 0$ **THEN:** x = 0 | y = 0

## Unit modulo:

> [!NOTE] Definition: Unit modulo
>  We say an element x in Zm is unit modulo if it has a multiplicative inverse modulo m.
>  
>  **Then:** This multiplicative inverse r is **unique** and it is denoted by: 
>  $$
>  r^{-1}
>  $$


## Invertible elements: 

> [!NOTE] Theorem: Invertible elements:
> An element r in Zm is invertible if it has a multiplicative inverse. **THEN:** r and m are relatively primes

## Invertibility of with prime numbers
**Remember:** [[20240429 - 111500 - Prime numbers|Prime numbers]]
For a congruence relation defined over the modulus of a prime number p. **THEN:** Every non-zero element of $\mathbb{Z}_p$ is invertible and the following properties follow: 
+ $\mathbb{Z}_p$ is a field like $(\mathbb{R}, + ,\cdot)$
+ **IF:** m = p $\cdot$ q (m is composite) **THEN:** There are divisors of zero in Zm and Zm is **a ring with divisors of zero** 
 #Duda : Divisors of zero and what the hell is a ring.

## Eulers totient function:

