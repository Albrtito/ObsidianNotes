---
aliases:
  - Algorithm - Busqueda espacio de estados
tags:
  - incomplete
  - Heuri
References: 
cssclasses:
---
# Algorithm - Busqueda espacio de estados

> [!attention] Pregunta de examen:
> En el examen habrá seguro una **modelización de un problmea de búsqueda con espacios de estado**. 
> 


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
Se pueden representar los estaos y operadores como un [[1731511534 - Graf Data sctructure|Grafo]] en el que los **nodos serán estasdos** y las **aristas serán los operadores.** 

En esta representación también observamos que las **restricciones se ven representadas como los caminos que no se pueden realizar.**
+ Si no puedo llegar a un nodo desde otro tendremos una restricción. 


***