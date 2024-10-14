---
aliases:
  - Restos potenciales
tags:
  - review
  - Discrete
  - Cripto
References: 
cssclasses:
---
# Restos potenciales

> [!NOTE] Defintion: 
> Los restos potenciales de un número a en módulo n son aquel conjunto de soluciones a las potencias de a módulo n. 
> $$ \{a^0, a^1, a^2, a^3,...a^{n-1}\} \mod n$$
> 
> + Solo tendrémos hasta el elemento $a^{n-1}$ puesto a que pasado este el resultado de los módulos se repetirá. (se pueden agrupar en grupos de n a’s)
## Matemáticamente:

**Dados dos números coprimos ( a y n) existe al menos un m tal que:**
$$a^m = 1 \mod n$$
**Entonces**: 
$$a^{\phi(n)} = 1 \mod n \rightarrow m = \phi(n)$$
+ Si existe más que un solo m, entoces m ha de ser divisor de $\phi(n)$


***
