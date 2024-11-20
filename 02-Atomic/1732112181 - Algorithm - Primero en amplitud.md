---
aliases:
  - Algorithm - Primero en amplitud
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Algorithm - Primero en amplitud

> [!NOTE] Intro: 
>  Nunca expande un nodo a profundidad d hasta que no ha expandido todos a la profundidad (d-1). 
>  > Se va buscando **por capas**, primero a profundad 1, luego 2, 3, 4 …
>  
## Pseudocódigo: 
1. Genera el nodo original y guárdalo en la lista 
2. Expandir el primer nodo de la lista. Al expandir lo eliminamos de la lista. 
	+ Obtener sus sucesores y append to the list 
	+ Esta la meta entre los sucesores?
		+ SI: **HALT**
		+ No:**Vuelvo al paso 2**


> [!attention] Remark: 
>  + La lista será **una cola**, **LIFO** (Last in first out)

## Propiedades: 

**Admisibilidad y completitud:**
+ Este algoritmo será **completo** pues siempre encontrara una solución 
+ El algorimo será **admisible** si y solo si **todos los operadores tienen el mismo coste**

**Remarks:**
+ Al encontraruna solución a este algoritmo a profundad d, se asegura que **no existe ningua solución a profundidad menor que d** puesto que todos los nodos a menor profundidad ya se han analizado. 

## Eficiencia: 
### Tiempo: 
El tiempo de ejecución de este algoritmo se guía por el **tiempo requerido para expandir un nodo**. 

Si llamamos d al **left most** nodo en de máxima profundidad p. Este será el mejor caso dentro de todos los peores casos con los que nos podemos encontrar. 
Para generar este nod d 
### Memoria: 
***