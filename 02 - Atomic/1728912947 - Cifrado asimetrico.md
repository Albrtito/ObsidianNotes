---
aliases:
  - Cifrado asimetrico
tags:
  - Cripto
  - incomplete
References: 
cssclasses:
---
# Cifrado asimetrico


> [!quote] Remember: 
> Recordamos todas las bases de la aritmética modular para exponer la siguiente teoría del cifrado asimétrico:
> + [[20240520 - 171554 - Definition - Modular arithmetics - Multiplicative inverse of x|Modular arithmetics - Multiplicative inverse of x]]
> + [[20240520 - 173827 - Definition - Euler's totient function|Euler's totient function]]
> + [[20240519 - 232552 - Definition - Relatively prime numbers|Relatively prime numbers]]

## Básicos matemáticos: 
### Restos potenciales: 
Al igual que muchas otras propiedades, las potencias de un número a en módulo n se repetirán con un patron predecible.

Dados dos números coprimos existe **al menos un m tal que:**
$$a^m = 1 \mod n$$
Entonces: 
$$a^{\phi(n)} = 1 \mod n \rightarrow m = \phi(n)$$
+ Si existe más que un solo m, entoces m ha de ser divisor de $\phi(n)$

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

***
