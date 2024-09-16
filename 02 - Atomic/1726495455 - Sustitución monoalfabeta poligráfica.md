---
aliases:
  - Sustitución monoalfabeta poligráfica
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Sustitución mono-alfabeta poligráfica

> [!NOTE] Definición:
> **Poligráfica:** Debido a que sustituye los grafos en grupos de más de uno. 
> 

## Cifrador de PLAYFAIR:
## Cifrador de HILL:
Utiliza multiplicación por matrices: 
+ La matriz es la clave. Es una matriz cuadrada de n x n. El texto se divide en grupos de n elementos. Se aplican caracteres de relleno (si el texto no se divide exactamente en grupos de n)
+ Estos grupos se interpretan como vectores
+ Se multiplica cada vector por la matriz. Obteniendo un nuevo vector. Los nuevos valores están cifrados con la clave (matriz).
