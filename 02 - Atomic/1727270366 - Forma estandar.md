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
>+ Variables → **≥ 0**
>+ Vector de recursos (b) → **≥ 0** 


## Transformaciones: 
Para transformar el problema a forma lineal realizamos las siguientes operaciones:

+ Cambiar de signo al vector de recursos es lo mismo que multiplicar por -1. 
+ Para convertir una igualdad en desigualdad debemos de **introducir una variable de holgura** (sumando o restando).
$$
\begin{gather}
\sum_{j=1}^{n}a_{ij}x_j \leq b_1  \triangleq \sum_{j=1}^{n}a_{ij}x_j + s_i = b_1\\
\sum_{j=1}^{n}a_{ij}x_j \geq b_1  \triangleq \sum_{j=1}^{n}a_{ij}x_j - s_i = b_1\\
\end{gather}
$$
Si una variable de decisi´on xi no est´a restringida se pone entonces como la diferencia de dos variables no negativas restringidas: 
$$
x_i = x'_i − x'_i , x'_i , x ''_i ≥ 0
$$
***