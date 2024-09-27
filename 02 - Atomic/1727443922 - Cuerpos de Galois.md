---
aliases:
  - Cuerpos de Galois
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Cuerpos de Galois
Existe un cuerpo de Galois $CG(q^n)$ formado por polinomios a(x) de grado (n-1) o menos cuyos coeficientess $a_1 \in Z_q$ 
$$\boxed{ CG(q^n) \Rightarrow a(x) = a_{n-1}x^{n-1}+a_{n-2}x^{n-2} + ... + a_1x+ a_0 \mod p(x)}$$
+ $a_1 \in Z_q$ donde q es primo
+ $\mod p(x)$ es un polimonio de grado n y es un polinoio irreducible: Se suele utilizar $p(x) = x^n + x + 1: n = 1,2,3,4,5…$ 
Los cuerpos de Galois tienen **operaciones de suma, multiplicacion, división, etc…**


## En criptografía: 
Para usos criptográficos trataremos con un cuerpo de Galois en concreto: 
$$
CG(2^n)
$$
+ $a_i \in Z_2 = {0,1}$
+ Solemos representar este polinomio como: $a(x) \in CG(2^n)$ / $(a_{n-1}, a_{n-2}, …, a_1, a_0)$/ $(a_{n-1} a_{n-2} … a_1 a_0)$ 

Al utilizar este polinomio específico, obtendremos básicamente **strings de bits** con una longitud igual a n.

### Operaciones con el cuerpo $CG(2^n)$: 

> [!quote] Recuerda: 
> Como estamos en un cuerpo con módulo 2 todas las operaciones se hacen acorde. 
> 

**Remark:**
+ Esto lo que va a significar es que realizaremos operaciones binarias utilizando la representación binaria de los polinómios
#### Suma y resta:
+ **Suma:** Sumar es equivalente a realizar un **XOR**
$$
\boxed{
C = a + b = a_i \oplus b_i}
$$
#### Multiplicación: 
Habrá que utilizar el $\mod p(x)$ : 
$$
\boxed{C = a\cdot b , C = \sum_{i= 1}^n(a_i\cdot b)xî \mod p(x)}
$$
$$
a_i \cdot 
$$

***