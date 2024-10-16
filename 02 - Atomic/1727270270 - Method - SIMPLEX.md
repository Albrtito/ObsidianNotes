---
aliases:
  - Method - SIMPLEX
  - SIMPLEX
tags:
  - Heuri
  - incomplete
References: 
cssclasses:
---
## Pasos: 
1. Primera base será matriz identidad 
2. $x_b = B^{-1}b: z = C_B^T \cdot x_B$
   + $C_B^T$ : Sera la matriz de coefiientes de costes para la base B
     
3. Regla de entrada: Vamos a ver cual es la variable que más nos ayuda al entrar.
	+ Calcular la entrada de una nueva variable: $z_j - c_j$ → Entra $x_j$ con $z_j - c_j$ MENOR (más negativo)
	  $$z_j = C_B^Ty_j \rightarrow y_j = B^-a_j$$
	+ Si todas son positivas entonces **terminamos:**
		+ **Sol. Opt:** Todas las variables artificiales toman valor nulo. 
			+ **única:** Si ninguna es igual a 0
			+ **infinitas:** Si alguna es igual a 0
4. **Regla de salida:** Vamos a ver que variable sale: 
   $$ \min\{\frac{X_{B_i}}{y_{ji}}\}$$
# Method - SIMPLEX:

> [!NOTE] Definition: 
> El método simplex se usa para **econtrar soluciones a problemas lineales**. Para ello, recorre las aristas de la región de soluciones factibles buscando puntos que resuelvan el problema. 
> Una vez encontrado un punto comprueba si existe algún otro punto con el que se consiga una mejor solución (estamos maximizando), si existe lo busca, en caso contrario finaliza habiendo encontrado 

+ Si representásemos lo que hace el algoritmo en un plano bidimensional obtendríamos algo así. 
![[1727270270 - Method - SIMPLEXj.png|center|350]]

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


> [NOTE] Teorema: > Dada $\max z = C^Tx$,las soluciones, si las hay, están en puntos extremos de F: $Ax = b$ con $x\geq0$. 
## Paso a paso:

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
			$$z_2 - c_2 = C_B^Ty_2- C_2 = 3$$
			El mayor número negativo será -2 así que **incluimos a $x_1$ en la base** y pasamos al siguiente paso. 
			
	3. **Regla de salida**: 
			La base tiene que ser tridimensional, tenemos una columna de más. Vamos a averiguar que columna es la que nos quitamos. 

		  Ahora el problema aparece pq tenemos una base tridimensional igualada a otra cuatridimensional (hemos añadido a1)
		  $$a_3x_3 + a_4x_4 + a_5x_5 = a_3\hat x_3 + a_3\hat x_3 + a_3\hat x_3 + a_3\hat x_3 + a_1 \theta$$
		  Resolvemos la equación algebráica: 
		  $$ B_0 y_1 = a_1$$ 
			Y obtenemos la igualdad: 
			$$ \boxed{a_1 = a_3y_{11} + a_4y_{12} + a_5y_{13} }$$
			Lo que nos permite reformular utilizando la nueva definicón de a1:
			$$a_3x_3 + a_4x_4 + a_5x_5 = a_3(\hat x_3 + \theta y_{11}) + a_4(\hat x_4+ \theta y_{12})  + a_5(\hat x_5 + \theta y_{13})$$
			Que podemos simplificar como: 
			$$x_i = \hat x_i + \theta y_{ii'}$$
			Y de aquí obtenemos el cambio de valor para la variable de decisión: 
			
			$$\hat x_i =  x_i - \theta y_{ii'}$$
			Acotando este valor como **no-negativo** podemos obtener: 
			$$ \theta \leq \frac{x_i}{y_{ji`}}$$
			Entonces, si nuestra restricción es que las variables sean mayores de 0, al intentar sacar una variable podemos ver si la que quitamos nos crea un valor negativo y denegarla.
			La variable que tendremos que saar será con la que se obtenga: 
			$$min_{i\in B}\{\frac{x_i}{y_{ji'}}\}$$
			Mientras que sea **mayor o igual a 0**
		+ Si nos encontrásemos con un caso en el que todos los valores son negativos significaría que la región no esta acotada, esto simplemente no pasa con un buen modelo. Te faltan restricciones.
		  
			En el ejempo que estamos haciendo ahora mismo obtenemos: 
			$$min\{\frac{2}{-1}, \frac{4}{1},\frac{1}{1}\}$$
			**
			**SIGUIENTE ITERACIÓN**
			
			Tendrá que salir la variable $x_5$ de la base.
			La nueva base para la nueva iteración será: 
			$$ B_1 = \{x_1, x_3, x_4\} = \begin{pmatrix}
-1 &&1 &&0 \\ 1 && 0&& 1 \\ 1&& 0&& 0
\end{pmatrix} $$

			Calculamos la inversa y obtenemos el siguiente punto. 
			$$ B_1 ^- = $$ 
		Esto se repite → Ya copiado en el sucio. 
		
***