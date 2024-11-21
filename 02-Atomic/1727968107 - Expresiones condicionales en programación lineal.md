---
aliases:
  - Expresiones condicionales en programación lineal
tags:
  - review
  - Heuri
References: 
cssclasses:
sr-due: 2024-11-22
sr-interval: 1
sr-ease: 130
---
# Expresiones condicionales en programación lineal
#Duda: La nota entera

> [!NOTE] Definition: 
> Cuando nos encontramos con expresiones del tipo: 
> 
> > **Si variable1 es mayor que 20 entonces pasa algo**
>
> tenemos ante nosotros una **expresión condicional.** 

> p.e: $$x_2 \geq 20 \Leftrightarrow \text{Comprar aparato}$$


> [!Check] Solution: 
> La solución es utilizar el método de **big-M** para definir una solución.

> p.e: (En el caso anterior): Creamos la siguiente restricción:
> $$ 20 \leq x_2 + M(1 - b)$$
> M : **Constante = $\infty$**

+ Vemos en remarks que esta restricción no es suficiente

**Remarks:**
Con estas restricciones tenemos que asegurarnos de que todos los casos se cumplen. 
> p.e: (Siguiendo con el ejemplo):
> Debemos de satisfacer cuatro casos: 
> 1. $x_2 \geq 20 \rightarrow b = 1$
> 2. $b = 1 \rightarrow x_2 \geq 20$
> 3. $x_2 < 20 \rightarrow b = 0$
> 4. $b = 0 \rightarrow x_2 < 20$

+ Solo las restricciones 2 y 3 se cumplen con la primera restricción que hemos dado. Para solucionarlo introducioms una nueva restricción: 

> p.e: (Siguiendo con el ejemplo anterior):
> Introducimos una nueva restricción 
> $$x_2 \leq 19 + Mb$$
> Con esta nueva restricción **los dos casos (el 1 y 4) que antes no satisfacían ahora satisfacen.**
> 




***
