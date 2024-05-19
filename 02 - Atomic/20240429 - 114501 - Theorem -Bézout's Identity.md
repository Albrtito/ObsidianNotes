---
aliases:
  - Bézout's Identity
tags:
  - Discrete
  - review
"References:": 
cssclasses:
sr-due: 2024-05-20
sr-interval: 1
sr-ease: 210
---


> [!NOTE] Theorem:
> IF a and b are: 
> + Two integers
> + Not simultaneously zero
> **THEN:**
> Exists integers u and w such that: 
> $$ 
> gcd(a,b)= a \cdot u + b\cdot w
> $$

**Remarks:**
+ The proof of this theorem is given by “unrolling” the steps of [[20240519 - 233523 - Algorithm - Euclid's algorithm|Euclid's algorithm]]. 
![[Screenshot 2024-05-19 at 23.53.57.png]]

+ The Bézout’s identity does **not imply that the integers u and v are unique**

From this identity we obtain the following theorems: 

> [!NOTE] Theorem: 
> Let a and b be two integers not simultaneously zero with gcd(a,b) = d. 
> An integer c can be written in the form: a\cdot x + b\cdot y 
