---
aliases:
  - Algoritmos de búsqueda
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Algoritmos de búsqueda

> [!NOTE] Intro:  
> Los algoritmos de búsqueda resuelven de forma eficiente aquellos problemas con conplejidad exponencial. 

## Modelado con espacio de estados:
El modelado de problemas de búsqueda con espacio de estados se basa en dos ideas fundamentales: 

1. Un posible conjunto de valores específicos para cada una  de mis variables es un estado que se representa en forma de **nodo**
2. Realizar un cambio para obtener un conjunto diferente es una operación, que se representa como **una arista**
+ Este modelado se explica en profundidad en su nota: [[]]

> [!NOTE] Modelado: 
> Dado el [[1731511534 - ADT - Graf|Grafo]] G(V,E) obtenido utilizamos un algoritmo de búsqueda para generar el árbol de búsqueda $T_G(s,t)$
> 
## Propiedades: 
Evaluamos un algorimo de busqueda analizando su completitud y admisibilidad.

+ **Completitud:** Un algoritmo de búsqueda es completo si **garantiza que encontrará una solución** dada que exista alguna. #Duda: Aunq esta solución se pueda dar en tiempo infinito
+ **Admisibilidad:** Si garantiza que encontrará una solución óptima dado a que exista alguna. 
	+ Si un algoritmo es **admisible es necesariamente completo**


+ [[1731507784 - Algorithm - Busqueda espacio de estados|Algorithm - Busqueda espacio de estados]]

## Algoritmos de búsqueda por fuerza bruta: 

> [!attention] Remarks: 
> + **Generar = Usar memoria** : Siempre que generamos algun dato estamos utilizando memoria para ello, guardamos ese dato en algún sito. 
> + **Eliminar de la lista = Dejar de usar memoria**: 


#Duda: Que pasaría si nuestro grafo no fuese simple? → Hay multiple edges
### Pseudocódigo:

> [!attention] Main idea:
> Este pseudocódigo recoge el algoritmo general de un algoritmo de búsqeuda por fuerza bruta 

1. Generar el estado inicial $S_0$ 
2. Expandir el primer nodo de la LISTA y añadir sus sucesores a LISTA. 
3. Si t$\in$ conjunto de sucessores, entonces **HALT**, en caso contrario **volvemos al caso 2**
### Implementaciones:
Tenemos dos formas de hacer búsqueda por fuerza bruta, hacerlo por **amplitud o por profundidad**
+ [[1732112181 - Algorithm - Primero en amplitud|Algorithm - Primero en amplitud]]
	+ Muy util **con transposiciones**
	+ Inutil sin transposiciones
+ [[1732114607 - Algorithm - Primero en profundidad|Algorithm - Primero en profundidad]]
	+ Muy útiles cuando **no hay transposiciones**
	+ Inutil con transposiciones

No obstante el algoritmo de primero en profundidad tiene el problema de no ser ni completo ni admisible, para obtener una variación de este algoritmo que sea tanto completo como admisible utilizamos el algoritmo: [[1732116599 - Algorithm - Profundizacion iterativa|Algorithm - Profundizacion iterativa]]



***