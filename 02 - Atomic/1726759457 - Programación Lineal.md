---
aliases:
  - Programación Lineal
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Programación Lineal

> [!NOTE] Intro:
> La programación lineal tiene como objetivo la resolución de problemas que pueden ser expresados como **una relación lineal entre sus variables**, namely, que tienen una forma tal que: 
> $$
> f: (\max/\min) z = c^Tx
> $$
> Donde: 
> + z : es el valor a maximizar/minimizar
> + $c^T$: es el vector de coeficientes(racionales), transpuesto para que la multiplicación sea posible.
> + $x$ : es el vector de variables/incognitas del problema
>
>Además, el problema define **restricciones que se aplican a las variables de la función.**

+ En resumen: Los problemas de programación lineal se definen con **variables, función y restricciones**


> [!done] Solución:
> La solución de un problema de progamación lineal se encuentra en el vector de variables que maximice/minimice la función objetivo y cumpla con las restricciones.
> + La solución óptima puede ser única o no. En este segundo caso decimos que existen **soluciones óptimas alternativas**
+ Puede **no existir ninguna solución**


## Formas de programación lineal:
Según la forma en la que se exprese la función y las restricciones podemos representar el problema de forma **canónica o de forma estandar**
+ [[1727270318 - Forma canónica|Forma canónica]]
+ [[1727270366 - Forma estandar|Forma estandar]]
## Resolución de problemas lineales: 
Los ejercicios de programación lineal se resuelven a trozos:
1. Primero se debe de [[1726759568 - Creación de modelos en programación lineal|crear un modelo]] que contenga la función objetivo, restriciones y variables. 
2. Una vez creado el modelo debemos de aplicar un método para resolverlo. 
	+ [[1726835656 - Method - Resolución gráfica de modelos lineales|Method - Resolución gráfica de modelos lineales]]
	+ [[1727270270 - Method - SIMPLEX|SIMPLEX]]
