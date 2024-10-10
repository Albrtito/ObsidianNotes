---
aliases:
  - Ejemplos SIMPLEX
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Ejemplos SIMPLEX

## Prueba evaluación 30min: 
### Modelado:
**Función objetivo:**
$$ \min z = x_1 + x_2$$
**Variables:**
$x_1 : \text{H. Primer trabajo}$
$x_2: \text{h. Segundo trabajo}$

**Restricciones:**
$\text{1) } 20 \geq x_1 + x_2$
$\text{2) } x_1 \leq x_2$
$\text{3) }150 \leq x_1\cdot 15  +  x_2\cdot 10$

**Representación en forma canónica:**
$$
\begin{gather}
\text{Función objetivo: }\\
\max z' = -x_1 - x_2\\\\

\text{Restricciones:}\\\\
 20 \leq x_1 + x_2\\\\
 0\leq x_2-x_1\\\\
150 \leq x_1\cdot 15  +  x_2\cdot 10\\\\
xi\geq 0
\end{gather}
$$
### Resolución gráfica:
1. **Obtenemos la región factible**
![[1728047794 - Ejemplos SIMPLEXj.png]]

2. **Obtenemmos el valor de -x-y para un z arbitrario y comprobamos:**
	1. En este caso hemos comprobado con z = -10. 

![[1728047794 - Ejemplos SIMPLEXj-1.png]]
3. **Vemos que la solución es el punto: (10,0)**
   
   Entonces nuestra solución que minimiza las horas  será:
   $x_1 = 10$ , $x_2 = 0$ 
***

