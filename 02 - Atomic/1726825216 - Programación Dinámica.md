---
aliases:
  - Programación Dinámica
tags:
  - review
References: https://aulaglobal.uc3m.es/pluginfile.php/7277686/mod_resource/content/3/dynamic_programming.pdf
cssclasses:
---
# Programación Dinámica

> [!NOTE] Definición: 
> La programación dinámica es una **técnica bottom-up** en la que se **guardan resultados intermedios** para luego reusarse durante la resolución de un problema. 
+ Util cuando podemos obtener **subproblemas ordenados**. 
La técnica se puede descomponer en los siguientes pasos: 
1. **Descomponer el problema** en subproblemas similares
2. Definir recursivamente la solución óptima del problema → #Duda: QUE?
3. Calcular los subproblemas de abajo hacia arriba 
4. Calcular la solución global usando los resultados intermedios

## Ejemplos: 
### Serie de fibonacci: 
Usando la implementación básica: 
+ **Implementación básica:**
	```c
	long fibonacci_0 (int n)
	{
	if (n == 0) return 0;
	if (n == 1) return 1;
	return fibonacci_0(n-1) + fibonacci_0(n-2);
	}
	```
+ Evaluamos casos más de una vez, por ejemplo, para F(4) se evalúan F(4-1) y F(4-2) que a su vez vuelven a evaluar F(4-2). 
+ La cantidad de evaluaciones es **exponencial**. 

Podemos utilizar programación dinámica para resolver este problema, **almacenando valores intermedios**. 
+ **Implementación almacenando valores:**
	```c
	list f;
	long fibonacci_aux (int n) {
	  if (f[n] == UNKNOWN)
	    f[n] = fibonacci aux(n - 1) + fibonacci aux(n - 2);
	  return f[n];
	}
	long fibonacci_1 (int n) {
	  int i;
	  f[0] = 0;
	  f[1] = 1;
	  for (i = 2; i≤n; f[i++] = UNKNOWN)
	    ;
	  return fibonacci aux(n);
	}
	```
+ Tenemos una tabla/lista de valores f en la que guardamos el valor de la serie fibonacci para cada n. 
+ Comprobamos si sabemos ya el valor para fibonacci(n) para no volver a calcularlo. 

Se puede optimizar aún más con programación dinámica, sin necesidad de usar siquiera una tabla o recursividad. 
+ **Implementación usando programación dinámica:**
	```c
	long fibonacci_2 (int n)
	{
		int i,z;
		int x = 0;
		int y = 1;
		if (n<2)
			return n
		for (i =2; i<= n; i++)
		{
			z = x + y;
			x = y;
			y = z; 
		}
		return z;
	}
	```
+ En vez de calcular cada valor “hacia abajo” lo hacemos de abajo hacia arriba. Vamos calculando valores empezando desde los dos primeros (0 y 1) hasta que llegamos al valor deseado. 

### All-pairs shortest-path
Dado un grafo G(V,E), obtener el coste del camino más corte entre todos los pares de vértices i y j, D(i,j). 
