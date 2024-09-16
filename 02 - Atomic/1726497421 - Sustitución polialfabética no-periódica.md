---
aliases:
  - Sustitución polialfabética no-periódica
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Sustitución polialfabética no-periódica
Los alfabetos no se repiten más que de manera aleatoria. Esto se consigue a través del método de Vernam. 

## Vernam: 
Uso de una puerta XOR para comparar la clave con el mensaje y generar el cifrado. 
+ Este cifrador es **incondicionalmente seguro** si: La clave es realmente aleatoria, se usa una sola vez y es de longitud igual o mayor que M.
**Problema:** No se puede implementar pues no se pueden generar claves aleatorias. Solo somos capaces de generar número **pseudoaleatorio**
![[Screenshot 2024-09-16 at 7.13.37 PM.png]]
