---
aliases:
  - Theorem - Indicador de Euler
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Theorem - Indicador de Euler

> [!NOTE] Definition: 
> El indicador de euler da el número de elementos que tiene el conjunto reducido de restos de n.  
+ **Notation:** $\Phi (n)$ 
## Teorema de Euler: 
A la hora de calcular el indicador de euler de n podemos utilizar el teorema de euler:
$$
\boxed{a^\Phi(n)\mod n =1}
$$
Gracias a este teorema podemos deducir la siguiente expresión: 
$$
a^{-|} = a^{\Phi(n)-1} \mod n = 1
$$
+ Esta expresión nos permite **calcular el inverso de a mod n**[^1]
Si n es primo (p), todo se simplifica más aún (según la teoría del indicador de euler): 
$$
a^{-1} = a^{p-2} \mod p
$$


***

[^1]: [[Multiplicative inverse]]