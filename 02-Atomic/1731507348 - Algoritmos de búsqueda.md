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

> [!NOTE] Utilidades: 
> Dado un grafo G(V,E) utilizamos un algoritmo de búsqueda para generar el árbol de búsqueda $T_G(s,t)$
> 
## Propiedades: 
+ **Completitud:** Un algoritmo de búsqueda es completo si **garantiza que encontrará una solución** dada que exista alguna. #Duda: Aunq esta solución se pueda dar en tiempo infinito
+ **Admisibilidad:** Si garantiza que encontrará una solución óptima dado a que exista alguna. 
	+ Si un algoritmo es **admisible es necesariamente completo**


+ [[1731507784 - Algorithm - Busqueda espacio de estados|Algorithm - Busqueda espacio de estados]]

## Algoritmos de búsqueda por fuerza bruta: 

> [!attention] Remarks: 
> + **Generar = Usar memoria** : Siempre que generamos algun dato estamos utilizando memoria para ello, guardamos ese dato en algún sito. 

### Pseudocódigo:
1. Generar el estado inicial $S_0$ 
2. Expandir el primer nodo de la LISTA y añadir sus sucesores a LISTA. 
3. Si t$\in$ conjunto de sucessores, entonces **HALT**, en caso contrario **volvemos al caso 2**
### Implementaciones:
+ [[1732112181 - Algorithm - Primero en amplitud|Algorithm - Primero en amplitud]]



***