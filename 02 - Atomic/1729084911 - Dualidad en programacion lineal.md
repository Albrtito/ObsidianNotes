---
aliases:
  - Dualidad en programacion lineal
tags:
  - Heuri
  - incomplete
References: 
cssclasses:
---
# Dualidad en programacion lineal
Existe algún problema en programación lineal relacionado directamente con el problema que se esta intentando resolver. 

Definimos la **forma simétrica de un problema de programación lineal** igual que la forma canónica: [[1727270318 - Forma canónica|Forma simétrica]] 
+ La simétrica y la canónica son la misma

Llamamos **forma primal** al problema original del que se obtendra finalmente la forma dual. 
Entonces podemos definir la **forma dual de un problema de programación lineal como:**


> [!ATTENTION] Examen: 
> + En los examenes se suele pedir esto como **la contribución por unidad de recurso de la función objetivo**
>   
> + Cuando en examen se pregunta por un análisis de estos problemas (y en general para dar un informe de un problema de este estilo) se han de dar indiscutiblemente las siguientes respuestas: [[1729087121 - Creación de informes en programación lineal|Creación de informes en programación lineal]]
>   

## Forma dual:
+ Las inequaciones cambian de lado (menor o igual a mayor o igual)
+ Se transpone la matriz de coeficientes
+ Se cambia el vector de coeficientes de la función objetivo por el vector de recursos

**Remarks:**
+ Si el primal tiene una solución correspondiente a la base B, entonces $x’^{*^T} = C_B^t B^-$ 
  Esto quiere decir que no hace falta que recalculemos todo, al estar unidos podemos obtener directamente el problema.La solución del dual se calcula directamente desde la solución del primal. 
  + C → El vector de coeficientes de la base
  + B → La base de la última iteración 

+ La solución óptima de la variable global i’esima: $X_i’^*$ es **la contribución por cantidad de recurso al crecimiento de la función objetivo**. Es decir, nos da información de como crecerá la función objetivo cuando modifiquemos nuestras variables.
## Ejemplo: 
Dado el siguiente modelo de un problema de programación lineal (**forma primal**)
$$
\begin{gather}
\max z. = 3x_1 + -2x_2\\
4x_1 - 2x_2 \leq 2\\
5x_1 + 2x_2 \leq 3\\
x \geq 0
\end{gather}
$$


Para obtener su forma dual realizamos: (esto no esta terminado)
$$
\begin{gather}
\min z. = 3x_1 + -2x_2\\
+4x_1  -2x_2 \leq 3\\
+5x_1  +2x_2 \leq -2\\
x \geq 0
\end{gather}
$$
***
