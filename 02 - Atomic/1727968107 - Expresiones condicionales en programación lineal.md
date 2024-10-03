---
aliases:
  - Expresiones condicionales en programación lineal
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Expresiones condicionales en programación lineal


> [!NOTE] Definition: 
> Cuando nos encontramos con expresiones del tipo: 
> 
> > **Si variable1 es mayore que 20 entonces pasa algo**
>
> tenemos ante nosotros una **expresión condicional.** 

> p.e: $$x_2 \geq 20 \Leftrightarrow \text{Comprar aparato}$$


> [!Check] Solution: 
> La solución es utilizar el método de **big-M** para definir una solución.

> p.e: (En el caso anterior): Creamos la siguiente restricción:
> $$ 20 \leq x_2 + M(1 - b)$$
> M : **Constante = $\infty$**



**Remarks:**
Con estas restricciones tenemos que asegurarnos de que todos los casos se cumplen. 
> p.e: (Siguiendo con el ejemplo):
> Debemos de satisfacer cuatro casos: 
> 1. $x_2 \geq 20 \rightarrow b = 1$
> 2. $b = 1 \rightarrow x_2 \geq 20$
> 3. $x_2 < 20 \rightarrow b = 0$
> 4. $b = 0 \rightarrow x_2 < 20$





***
