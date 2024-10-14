---
aliases:
  - Cifrado asimetrico
tags:
  - Cripto
References: 
cssclasses:
---
# Cifrado asimetrico

> [!quote] Remember: 
> Recordamos todas las bases de la aritmética modular para exponer la siguiente teoría del cifrado asimétrico:
> + [[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]
> + [[1727100415 - Theorem - Indicador de Euler|Theorem - Indicador de Euler]]
> + [[20240519 - 232552 - Definition - Relatively prime numbers|Relatively prime numbers]]

## Más bases matemáticas: 
+ [[1728916836 - Restos potenciales|Restos potenciales]]
+ [[1728917414 - Orden gaussiano|Orden gaussiano]]

### [[1728919808 - Logaritmos discretos|Logaritmos discretos]]

> [!attention] IMPORTANTE:
> Los logaritmos discretos son **lo que hace que podamos cifrar de forma pública**. 
> Para una equacion basada en uno de estos algoritmos:
> $$
> x = log_a b \mod n
> $$
> + x será igual al número que tenemos que elevar a para que de b. 
>   **LA UNICA FORMA DE ENCONTRARLO ES BUSCAR LOS POSIBLES VALORES DE A**

 
  **Remarks:**
  No solo tenemos esta propiedad sino que además se cumple: 

+ **Si a es una raiz primitiva de n, el logarimo siempre existe, x existe**. 


## Modelo de los criptosistemas asimétricos:

> [!BUG]  Problema:
> El problema que nos encontramos en el cifrado simétrico es que **el intercambio de claves se ha de hacer por un medio seguro**.

> [!check] Solución: 
> Contents
 

Cada cliente tendrá un par de claves, una **privada y otr pública.** La clave privada será la inversa de la pública. 
+ Para poder calcular facilmente la inversa se tiene un “secreto” de forma privada
+ Como estoy calculando dos claves que realmente son inversas entre ellas, puedo usar cualquiera de las dos como la otra. Se elige de forma arbitararia(o no) cual es cual. 
z
***
