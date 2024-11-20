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
>  + La lista será **una cola**



***