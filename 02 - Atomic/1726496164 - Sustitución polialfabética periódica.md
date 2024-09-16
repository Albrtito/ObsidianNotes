---
aliases:
  - Sustitución polialfabética periódica
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Sustitución polialfabética periódica.

> [!NOTE] Definición: 
> Decimos que algo es **polialfabético** cuando el alfabeto cifrado generado no es isomorfo al alfabeto original.
> Cuando los alfabetos que utilizamos **se repiten** de forma periódica lo llamamos sustitución poli periódica. 

Dividimos entre la creación de alfabetos lineales y alfabetos progresivos:
## Alfabetos lineales:
Definimos la sustitución de las siguiente forma:
$$
E(m_j) = (m_j + k_{(j \mod m)}\mod n)
$$
+ Estos alfabetos son lineales
+ p.e: Si a cada letra del abecedario le doy una constante $b_i$ y hago una [[1726494310 - Sustitución monoalfabeto monográfica|Sustitución monoalfabeto monográfica]] para cada una de ellas. Estoy generando un alfabeto nuevo por cada uno de los grafos.
## Alfabetos progresivos: 

> [!NOTE] Alfabeto progresivo: 
> Esto quiere decir que cada nuevo grafo cifrado **depende del anterior grafo**. (El nuevo alfabeto depende de algo anterior)

+ p.e: La máquina enigma
