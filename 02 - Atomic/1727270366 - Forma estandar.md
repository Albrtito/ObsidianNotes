---
aliases:
  - Forma estandar
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Forma estandar

> [!NOTE] Problema estandar
> Un problema de programación lineal esta en forma estandar si: 
>+ Se busca **MAXIMIZAR o MINIMIZAR**
>+ Las restricciones son de **igualdad**
>$$Ax = b$$
>+ Variables → **≥ 0**
>+ Vector de recursos (b) → **≥ 0** 


## Transformaciones: 
Para transformar el problema a forma lineal realizamos las siguientes operaciones:
+ Para convertir una función de minimización en otra de maximización **multiplicamos por -1**
$$
\min z = c^TX \triangleq \max z' = -c^TX
$$[^1]

+ Cambiar de signo al vector de recursos es lo mismo que multiplicar por -1. Lo que le da la vuelta a la inequality.
+ Para convertir una igualdad en desigualdad debemos de **introducir una variable de holgura** (sumando o restando).
$$
\begin{gather}
\sum_{j=1}^{n}a_{ij}x_j \leq b_i  \triangleq \sum_{j=1}^{n}a_{ij}x_j + s_i = b_i\\
\sum_{j=1}^{n}a_{ij}x_j \geq b_i  \triangleq \sum_{j=1}^{n}a_{ij}x_j - s_i = b_i\\
\end{gather}
$$


Si una variable de decisión $x_i$ **puede tomar valores negativos** se pone entonces como la diferencia de dos variables no negativas restringidas: 
$$
x_i = x'_i − x'_i , x'_i , x ''_i ≥ 0
$$
***

[^1]: El símbolo de igualdad con el triángulo encima significa igual **por definición.** Es matemáticamente un **axioma.**