---
aliases:
  - Exercises - Programación Lineal
  - Ejercicios programación lineal
tags:
  - review
  - Heuri
References: https://aulaglobal.uc3m.es/pluginfile.php/7298887/mod_resource/content/2/enunciados_representacion_lp.pdf
cssclasses:
sr-due: 2024-10-19
sr-interval: 3
sr-ease: 210
---
# Ejercicios - Programación Lineal

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



## Tips: 
+ Cuidado con **unidades horarias** pues no se representan los minutos como porcentajes como en otros casos.  
	  → Calcular la equación en minutos o en horas
+ Para ejercicios con expresiones condicionales ver [[1727968107 - Expresiones condicionales en programación lineal|Expresiones condicionales en programación lineal]]
