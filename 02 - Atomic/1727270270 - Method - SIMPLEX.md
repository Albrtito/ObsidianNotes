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


## Ejemplo práctico: 
$$
\begin{gather}
\max z = 2x_1 - 3x_2\\\\
\text{Restricciones:}\\
-x_1 + x_2 \leq 2\\
x_1 + x_2 \leq 4\\
x_1 - 2x_2 \leq 1\\
x\geq 0
\end{gather}
$$
**Método gráfico:**
Se dibuja cada una de las restricciones y se encuentran los puntos extremos de la región factible. 

**SIMPLEX:**
1. Pasar el problema a forma estandar: Hemos de sumar **variables de holgura** para cada una de las restricciones:
$$
\begin{gather}
\text{Restricciones:}\\
-x_1 + x_2 + x_3 = 2\\
x_1 + x_2 +  x_4 = 4\\
x_1 - 2x_2 + x_5 = 1\\
x\geq 0
\end{gather}
$$
+ A la hora de realizar este tipo de ejercicios, **separar por columnas para evitar errores.**
+ Las variables que “nos importan” son $x_1$ y $x_2$. El resto son variables de holgura, auxiliares, útiles solo para la resolución.

2. Empezamos a iterar:
	+ Iteración #0: Cálculo de una solución **básica factible inicial**. 
	1. **Cálculo de las variables básicas:** Para la base $B_0 = I_{3x3}$  serán $x_3, x_4, x_5$, de tal forma que: $x_B = B^-b = I_3^-b = (2,4,1)^T$
		Entonces: 
		$$ z_{B_0} = C_{B_0}^T X_{B_0} = (0,0,0)(2,4,1)^T = 0$$
		**Remarks:** Estamos haciendo que las variables $x_1 y x_2$ sean 0 de forma manual. 

		Este primer punto que hemos encontrado será la **primera solución del problema lineal**. Esta solución estará en el punto: (0,0,2,4,1), aunq para obtener la solución bidimensional solo nos quedamos con las primeras dos. Obteniendo (0,0)

	2. **Regla de entrada:** 
		+ Utilizamos el subindice i para referirnos a las variables básicas. Mientras que se usa el subindice j para las variables nuevas que entren.
		  
		  La forma en la que estamos calculando la función objetivo (su valor) es la siguiente. 
		  $$ z = \sum_{i\in B} C_i X_i$$
		  En el paso uno las nuevas variables eran 0 y no teníamos que tenerlas en cuenta.
		  Ahora introducimos una variable no básica/nueva.
		  $$ z = \sum_{i\in B} C_i \hat X_i + c_j \sigma $$
		  + **sigma:** Es la variable nueva. 
		  + $c_j$: Es el coeficiente de la variable nueva
		  El valor de las variables básicas cambia, se **acomodan**. Por eso lleva el sombrerito. Podemos obtener el nuevo valor de las variables básicas. 
		  $$ \boxed{\hat x_i. = x_i - \sigma y_{ji'}}$$
		  Operamos: 
			…
			$$z - \sigma(z_j - c_j)$$
			A esto lo llamamos el **coste reducido**. En este caso queremos minimizar así que trateremos de encontrar el máximo valor negativo del coste reducido. 
			Tenemos dos opciones, una por variable nueva: 
			$$z_1 - c_1 = C_B^Ty_1 - C_1 = -2$$
		  
***