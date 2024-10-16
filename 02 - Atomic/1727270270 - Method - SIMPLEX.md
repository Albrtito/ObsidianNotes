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

# Method - SIMPLEX:

> [!NOTE] Definition: 
> El método simplex se usa para **econtrar soluciones a problemas lineales**. Para ello, recorre las aristas de la región de soluciones factibles buscando puntos que resuelvan el problema. 
> Una vez encontrado un punto comprueba si existe algún otro punto con el que se consiga una mejor solución (la solución será un valor mayor para la función objetivo), si existe lo busca, en caso contrario finaliza habiendo encontrado 

+ Si representásemos lo que hace el algoritmo en un plano bidimensional obtendríamos algo así. 
![[1727270270 - Method - SIMPLEXj.png|center|350]]

> [!quote] Remember: 
> Recordemos que un problema lineal en forma estandar está definido de la siguiente forma:
> $$\begin{gather}
> f: \max z = C^T x\\\\
> \text{sujeto a: } Ax = b\\\\
> \text{con: } x \geq 0
\end{gather}
$$

## Nomenglatura:
Las nomenglatura básica del simplesx, para no perderse entre tanto vector, matriz y algebra.

+ **z:** Valor de la función objetivo. **z’** es lo mismo pero teniendo en cuenta que ha sido transformada de minimización a maximización.
+ **x** → **Vector**: Vector de incógnitas/variables, al darle valor a estas incógnitas/variable encontramos posibles soluciones.
+ **$C^T$ → Vector**: Vector de coeficientes de las incógnitas/variables. Se transpone para que se obtenga una solución no vectorial (z).
+ **A → Matriz:** Matriz de costes. Creada por los coeficientes de cada variable en cada una de las restricciones.

  >ej: Para un problema con restricciones
  > $$\begin{gather} x_1 + x_2 + 4x_3 = 2 \\ 2x_1 -3x_2 + x_3 = 3\end{gather}$$
  > Tendremos la matriz A: 
 >$$ \begin{pmatrix} 1 & 1 & 4 \\ 2 & -3 & 1\end{pmatrix}$$
  
  
+ **$B_i$ → Base(Matriz)**: Base que se usa en la iteración i del simplex. Compuesta por  coeficientes de las variables en la matriz de costes(A)

  > ej: (Siguiendo con el ejemplo anterior) Una base creada por las variables $x_1$ y $x_3$ sería:
>$$B = \begin{pmatrix} 1 & 4 \\ 2 & 1\end{pmatrix}$$
  
  
+ **$C_{B_i}$ → Vector**: Vector de coeficientes reducido, solo tendrá aquellos coeficientes de las variables que componen la base $B_i$.
	+ $C_B^T$ → **Vector:** Este mismo vector pero transpuesto
+ **b → Vector:** Vector de recursos. 
+ **$x^*$ → Vector:** Solució factible del problema


## Pasos:
1. Definimos una base con la que realizar la iteración. 
   + En la **primera iteración** escogeremos las variables que permitan crear la **matriz identidad** como base. 
     + Si no existen estas variables **crearemos una variable artificial que permita la creación de la identidad**. Esta variable artificial tendra un coeficiente negativo y suficientemente grande (al menos igual a la suma de todos los coficientes de las incógnitas.)

2. Calculamos el valor de la función objetivo para esa base. 
   1. Calcular el **valor de cada incógnita como el vector $x_B$:** Estos valores serán una **solución factible** 
      $$ x_B = B^-b$$
      - **Remark:** Las variables que no aparezcan en la base tomarán un valor de 0.
	2. Calcular el **valor de la función objetivo:**
	   $$z = C_B^T \cdot x_B$$
	   
2. **Regla de entrada:** En este paso calcularemos cual de las variables que no se encuentra en la base aporta mas entrando en ella. Esto lo sabremos calculando:
   $$\min \{z_j-C_j\}$$
   + Donde: 
	  $$z_j = C_B^Ty_j \rightarrow y_j = B^-A_j$$
   Entonces la j para la que se obtenga el minimo valor de esta expresión será el índice de la variable que entra $x_j$
   + Probamos **solo con las variables que no están ya dentro de la base**
   + **Una variable que acaba de salir no va a volver a entrar,** pero podemos calcular igualmente el valor de la exprsión para asegurarnos de que da positivo. (si da positivo significa que estamos haciendo las cosas bien)

	**CONICIÓN PARA IR AL PASO 3:**
	+ **HALT:** Si todas las variables toman valores positivos la solución actual será la final y óptima. En este caso también se ha de cumplir que.
		+ **Todas las variables artificiales toman valor 0**
		  
	+ **CONTINUE:** En cuanto una de las variables tome valor negativo pasamos al paso 3

3. **Regla de salida:** En este paso calculamos que variable de las que están en la base tiene que salir para que la variable que encontramos en el paso 2 entre. Saldrá la variable que cumpla: 
   $$ \min\{\frac{x_{i}}{y_{ji'}}\} \forall i \in B$$
   + Aquí $y_{ji}$ se refiere a la posición i (incrementando empezando en 1, por eso lleva la prima) del vector $y_j$ calculado en el paso 2
   + $x_i$ será el valor de la incognita para la solución factible prop

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