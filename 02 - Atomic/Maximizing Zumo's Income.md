---
aliases:
  - Exercises - Programación Lineal
  - Ejercicios programación lineal
tags:
  - review
  - Heuri
References: https://aulaglobal.uc3m.es/pluginfile.php/7298887/mod_resource/content/2/enunciados_representacion_lp.pdf
cssclasses:
---
# Exercises - Programación Lineal
## Problema 1:
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
