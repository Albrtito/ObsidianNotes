---
aliases:
  - Problemas de búsqueda
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Problemas de búsqueda
#Duda: El espacio de estados es simplemente el modelo? Luego la resolución la realizamos con un algoritmos de búsqueda (de los que hay en tipos de algoritmos?)
## Modelado de un espacio de estados:
El modelado de problemas de búsqueda como un espacio de estados se basa en dos ideas fundamentales: 

1. Un posible conjunto de valores específicos para cada una  de mis variables es un estado que se representa en forma de **nodo**
2. Realizar un cambio para obtener un conjunto diferente es una operación, que se representa como **una arista**
+ Este modelado se explica en profundidad en su nota: [[1731507784 -  Busqueda modelando un espacio de estados|Modelado de un espacio de estados]]
+ Como resultado de este modelado **obtenemos un grafo**
##  Resolución
> [!attention] MAIN IDEA: 
> Dado el [[1731511534 - ADT - Graf|Grafo]] G(V,E) obtenido utilizamos un [[1732193365 - Algoritmos de busqueda|Algoritmo de busqueda]] para generar el árbol de búsqueda $T_G(s,t)$ que muestra el resultado del problema. 
> 

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