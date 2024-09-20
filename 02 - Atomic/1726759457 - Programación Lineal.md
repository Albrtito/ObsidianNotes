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
> + $c^T$: es el vector de coeficientes
> + $x$ : es el vector de variables/incognitas del problema
>
>Además, el problema define **restricciones que se aplican a las variables de la función.**

+ En resumen: Los problemas de programación lineal se definen con **variables, función y restricciones**


> [!done] Solución:
> La solución de un problema de progamación lineal se encuentra en el vector de variables que maximice/minimice la función objetivo.
> + La solución óptima puede ser única o no. En este segundo caso decimos que existen **soluciones óptimas alternativas**


Según la forma en la que se exprese la función y las restricciones podemos representar el problema de forma **canónica o de forma estandar**
## Forma canónica:
Un problema de programación lineal esta en forma canónica si: 
+ El objetivo/función busca **MAXIMIZAR**
+ Igualdades: **≤**
+ Variables: **≥ 0**
EL modelo se puede expresar de la siguiente forma:
$$
\begin{gather}
\text{Función:}\\
\max z = c^Tx\\\\
\text{Restricciones:}\\
Ax <= b\\\\
\text{Variables:}\\
x>= 0
\end{gather}
$$
+ c → Vector de costes/beneficios (A obtener/reducir)
+ b → Vector de recursos (Que delimitan)

Para transformar un modelo lineal a su forma canónica utilizamos las siguientes equivalencias:
### Transformaciones:
1. Un problema de minimización es equivalente al de maximización, **con un cambio de signo a f**
2. Para cambiar el sentido de una desigualdad multiplicamos por -1.
## Forma estandar:
Un problema de programación lineal esta en forma estandar si: 
+ Se busca **MAXIMIZAR o MINIMIZAR**
+ Las restricciones son de **igualdad**
+ Variables → **≥ 0**
+ Vector de recursos (b) → **≥ 0** 

### Transformaciones: 
+ Cambiar de signo al vector de recursos es lo mismo que multiplicar por -1. 
+ Para convertir una igualdad en desigualdad debemos de **introducir una variable de holgura** (sumando o restando).
$$

$$
## Resolución de problemas lineales: 
Los ejercicios de programación lineal se resuelven a trozos:
1. Primero se debe de [[1726759568 - Creación de modelos en programación lineal|crear un modelo]] que contenga la función objetivo, restriciones y variables. 
2. Una vez creado el modelo debemos de aplicar un método para resolverlo. 
	+ [[1726835656 - Method - Resolución gráfica de modelos lineales|Method - Resolución gráfica de modelos lineales]]
	+ 