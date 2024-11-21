---
aliases:
  - Modelado de un espacio de estados
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Modelado de un espacio de estados

> [!attention] Pregunta de examen:
> En el examen habrá seguro una **modelización de un problmea de búsqueda con espacios de estado**. 
> 

Modelar un problema de búsqueda con espacio de estados nos permite **obtener un grafo que reprsenta el problema **
1. Modelado del problema en forma de grafo, obteniendo los estados y operadores 
2. Obtener un **arbol de búsqueda** con todos los caminos posibles en el grafo empezando en el estado inicial. Este algoritmo se genera **utilizando algoritmos de búsqueda**
3. Analizar el arbol para obtener soluciones

> [!example] Nomenglatura y definiciones: 
> + **Estados:** configuraciones posibles del problema. Representan información **estática**
> 
> + **Operadores:** Transitar entre los estados. 
> 
> + **Vista estática del problema:** La estructura que tienen los estados del problema y la información que en ellos se presenta.
> 
> + **Espacio de problemas:**
> 	+ **Espacio de estados**: Un grafo: G(V,E)
> 	+ **Un estado inicial**, s: 
> 	+ **Min un estado final**, t: Se pueden definir explicitamente o implicitamente. La definición explicita apunta a problemas de **optimización** y la definición implícidta a problemas de **decibilidad.**
> + **Solución:** La solución contiene un conjunto de operadores(transformaciones), en orden, que transforman el estado inicial al final. Esto se ve **representado como un camino en el grafo**

## Representación gráfica: 
Se pueden representar los estaos y operadores como un [[1731511534 - ADT - Graf|Grafo]] en el que los **nodos serán estados** y las **aristas serán los operadores.** 

> [!NOTE] : 
> + **Vertice:** Un vertice en un grafo es  representa un estado del problema → [[1731507784 -  Busqueda modelando un espacio de estados|Algorithm - Busqueda espacio de estados]]

En esta representación también observamos que las **restricciones se ven representadas como los caminos que no se pueden realizar.**
+ Si no puedo llegar a un nodo desde otro tendremos una restricción. 
## Árboles de decibilidad:
Definimos dos factores de importancia de los árboles de decibilidad:
1.  factor de ramificación: Lo ancho que puede llegar a ser el arbol (anchura max)
2. factor de profundidad: Lo alto que puede llegar a ser el arbol. 

 




***