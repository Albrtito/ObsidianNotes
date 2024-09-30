---
aliases:
  - Sustitución polialfabética no-periódica
  - Método de Vernam
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Sustitución polialfabética no-periódica

> [!NOTE] Definición: 
> Los alfabetos creados son aleatorios. Esto se consigue a través del método de Vernam. 

## Vernam: 
**Uso de una puerta XOR para comparar la clave con el mensaje y generar el cifrado.** 

+ Este cifrador es **incondicionalmente seguro** si: La clave es realmente aleatoria, se usa una sola vez y es de longitud igual o mayor que M.

> [!BUG] Problema: 
> Este meétodo es **imposible de implementar**, pues para ser completamente seguro necesitamos 


**Problema:** No se puede implementar pues no se pueden generar claves aleatorias. Solo somos capaces de generar número **pseudoaleatorio**
![[Screenshot 2024-09-16 at 7.13.37 PM.png]]
