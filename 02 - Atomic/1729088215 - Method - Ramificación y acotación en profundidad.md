---
aliases:
  - Method - Ramificación y acotación en profundidad
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Method - Ramificación y acotación en profundidad

> [!Attention] Examen: 
> En ejercicios de examen se suele preguntar como: Resolver con variables cumpliendo condiciones de integridad → Quiere decir que son enteras 

## Pasos:

Cuando tenemos que resolver un problmea lineal buscando únicamente números enteros realizamos el siguiente algoritmo, conceptualmente se hace lo siguiente. 

+ Inicializamos la variable B (valor de la función objetivo en la solución encontrada) a $-\infty$

1. Se resuelve el simplex para la región, esperando que alguna solución de las que tengamos sea entera. 
   + **Si $x^* \in \mathbb{N}$, HALT
2. En el caso de que la solución factible no sea entera, reducimos el conjunto factible a dos subconjuntos. La división la hacemos sobre una de las variables → Aquí hay varios métodos para hacerlo.  
   **
3. Volvemos a calcular el simplex en **cada uno de los dos conjuntos** y vemos si alguno de ellos es entero, repetimos ramificando, ahora repetmos el segundo paso para cada uno de los subconjuntos.
   
   **Calculamos $z_{F_i} \forall F_i$:** Donde F es una región factible de las que hemos partido. 
   Podemos ver varios casos una vez calculamos la solución a la función objetivo en la región factible:
   
	+ Si una de las dos regiones esta vacía no buscamos en ella. **Esto puede ocurrir pq las restricciones se contradigan entre ellas**
   + $x_{F_i} \in \mathbb{N} \land z_{F_i} > B$ $B \leftarrow z_{F_i}$ 
   + $z_{F_i} \leq B$


***
