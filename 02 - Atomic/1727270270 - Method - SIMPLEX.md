---
aliases:
  - Method - SIMPLEX
  - SIMPLEX
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Method - SIMPLEX
Lo primero que hemos de realizar es **transcribir la tarea de programación lineal a [[1727270366 - Forma estandar|Forma estandar]]**

+ Un vector X que resuelve Ax = b se llama solución
+ Un vector X ≥ 0 que resuelve Ax = b se llama **solución factible**. 
+ Un vector $X_B \geq 0$ que resuelve $B_{mxm}X_B=b$ se llama **solución factible básica.**
	+ Entonces podemos convertir la forma que usábamos: $z = C^T X$  en: $z = C_B^TX_B$
+ Decimos que $X^*$ es una solución factible, básica y óptima. Si y solo si:
$$C_B^TX^* \geq C_B^TX, \forall x \in F$$
+ Resolución usando de sistemas algebráicos usando la inversa:
$$
Ax_A = b \Rightarrow x_A= A^{-1}b
$$
	+ Entonces la única condición que ha de haber para que un sistema algebráico tenga solución será que **sea invertible**.
	+ Hacer cambios en el vector de coeficientes b de un sistema que tiene solución no altera ese aspecto del sistema. Seguirá teniendo solución.

> [!NOTE] Teorema: 
> Dada $\max z = C^Tx$,las soluciones, si las hay, están en puntos extremos de F: $Ax = b$ con $x\geq0$. 


***