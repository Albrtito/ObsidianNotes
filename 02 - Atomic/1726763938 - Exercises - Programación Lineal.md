---
aliases:
  - Exercises - Programación Lineal
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Exercises - Programación Lineal
## Resolución gráfica:
Una vez obtenidas las variables, función y restricciones podemos aplicar la resolución lineal para obtener la solución que maximiza/minimiza la función objetivo: 
1. **Identificación de la región factible** (S): Para esto usamos las restricciones establecidas para delimitar los posibles valores para nuestras variables, pintando el modelo gráficamente.
2. **Obtener los puntos extremos:** Estos puntos son **las esquinas de la región factible**
3. **Identificar la solución:** La solución será **uno de los puntos factibles**. Para identificar que punto factible es podemos utiliza dos métodos. 
	1. **Búsqueda del máximo** entre todos los puntos: Calcular el valor de cada uno de los puntos. Aplicar este valor a la función del problema y comparar entre el valor de la función para cada punto para obtener el máximo. 
	2. **Curvas/Rectas de Isobeneficio**: Obtener la función objetivo para un valor que cumpla con las restricciones. Hecho esto “alejar” esta función a través de rectas paralelas hasta identificar el punto factible con el que se obtiene el valor máximo de f.
### Problema 1:
La empresa UniZumo fabrica y distribuye zumos de piña en las presentaciones Néctar de Piña y Unizumo de Piña. Ambos zumos se fabrican a base de concentrado de piña, de modo que en cada litro de zumo hay un 20 % y un 50 % de concentrado respectivamente. Para la fabricación del año se dispone de 2,4 millones de litros de concentrado de piña y se ha pactado con los mayoristas un precio de 1,25 euros por tetra brik (con una capacidad de un litro) de Néctar de Piña y 2,05 euros por el de Unizumo de Piña, bajo la condición de que no se saquen al mercado más de 6 millones de litros de zumo. 
Se pide: 
1. Modelar el problema como un problema de Programación Lineal para obtener las cantidades de cada producto que UniZumo debe fabricar para maximizar los ingresos por ventas. 
2. Resolver gráficamente el problema. 
3. Representar el problema en forma estándar

**Variables:**
m.l → Millones de Litros
+ $x_1$: m.l. Néctar
+ $x_2$ : m.l. Unizumo
**Función:**
$$
f_o = \max z = 1.25 x_1 + 2.05 x_2
$$
**Restricciones:**
$$
\begin{gather}
0.2x_1 + 0.5x_2 \le 2.4\\\\
x_1 +x_2 \leq 6\\\\
x_1, x_2 \geq 0\\\\
x_1, x_2 \in \mathbb{N} \cup \{0\}
\end{gather}
$$

**Sistemas de ecuaciones:**
Se han de solucionar utilizando el **método de la matriz inversa**. 
$$
\begin{gather}
AX = b\\
X = A^{-1}b
\end{gather}
$$
+ Para ello debemos de calcular la matriz inversa. Lo haremos a través del siguiente método: 
$$
A^{-1} = \frac{(adj(A))^T}{det(A)}
$$

**Trabajo con números enteros y racionales:** 
Trabajaremos usando números racionales para **prevenir la pérdida de error**. 
> p.e: Usaremos $1 \over 5$ en vez de $0.2$

**Implementación de condicionales:**
>Si una variable toma un valor entonces la otra toma otro **en consecuencia**

**Representación en forma estandar:**
Parar representar un problema de forma estandar hemos de representar las desigualdades de las restricciones como igualdades en las que todos los valores de la parte derechas son positivos. 
+ Para esto introducimos **variables de holgura**
> p.e: Transformamos $0.2x_1 + 0.5x_2 \leq 2.4$ en $0.2x_1 + 0.5x_2 + x_3 = 2.4$. Dnd $x_3$ es la variable de holgura. 



