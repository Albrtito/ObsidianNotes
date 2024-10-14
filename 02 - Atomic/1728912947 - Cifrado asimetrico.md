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
+ 
Hablamso entonces de **ORDENES GAUSIANOS**. El orden gausiano de a respecto a un módulo n será denominado como w y seguirá la definición expuesta más arriba:
$$ a^w = 1 \mod n$$
$$w = \text{orden}(a,n)$$

+ Si el gausiano de un número a es igual a $\phi(n)$ entonces se le llama **generador o raiz primitiva** debido a que es campaz de **generar TODO EL CONJUNTO DE RESTOS de n**. 

### Logaritmos discretos:
…

## Modelo de criptosistema asimétrico: 
Cada cliente tendrá un par de claves, una **privada y otr pública.** La clave privada será la inversa de la pública. 
+ Para poder calcular facilmente la inversa se tiene un “secreto” de forma privada
+ Como estoy calculando dos claves que realmente son inversas entre ellas, puedo usar cualquiera de las dos como la otra. Se elige de forma arbitararia(o no) cual es cual. 
z
***
