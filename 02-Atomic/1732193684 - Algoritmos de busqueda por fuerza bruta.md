---
aliases:
  - Algoritmos de busqueda por fuerza bruta
tags:
  - Heuri
  - review
References: 
cssclasses:
sr-due: 2024-11-22
sr-interval: 1
sr-ease: 230
---
# Algoritmos de busqueda por fuerza bruta

#Duda: Que pasaría si nuestro grafo no fuese simple? → Hay multiple edges
## Pseudocódigo:

> [!attention] Main idea:
> Este pseudocódigo recoge el algoritmo general de un algoritmo de búsqeuda por fuerza bruta 

1. Generar el estado inicial $S_0$ 
2. Expandir el primer nodo de la LISTA y añadir sus sucesores a LISTA. 
3. Si t$\in$ conjunto de sucessores, entonces **HALT**, en caso contrario **volvemos al caso 2**
## Implementaciones:
Tenemos dos formas de hacer búsqueda por fuerza bruta, hacerlo por **amplitud o por profundidad**
+ [[1732112181 - Algorithm - Primero en amplitud|Algorithm - Primero en amplitud]]
	+ Muy util **con transposiciones**
	+ Inutil sin transposiciones
+ [[1732114607 - Algorithm - Primero en profundidad|Algorithm - Primero en profundidad]]
	+ Muy útiles cuando **no hay transposiciones**
	+ Inutil con transposiciones

No obstante el algoritmo de primero en profundidad tiene el problema de no ser ni completo ni admisible, para obtener una variación de este algoritmo que sea tanto completo como admisible utilizamos el algoritmo:
+  [[1732116599 - Algorithm - Profundizacion iterativa|Algorithm - Profundizacion iterativa]]


***