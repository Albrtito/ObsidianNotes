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
long fibonacci aux(int n) {
  if (f[n] == UNKNOWN)
    f[n] = fibonacci aux(n - 1) + fibonacci aux(n - 2);
  return f[n];
}
long fibonacci 1(int n) {
  int i;
  f[0] = 0;
  f[1] = 1;
  for (i = 2; i≤n; f[i++] = UNKNOWN)
    ;
  return fibonacci aux(n);
}
```

