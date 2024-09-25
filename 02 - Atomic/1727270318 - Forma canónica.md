---
aliases:
  - Forma canónica
tags:
  - review
  - Heuri
References: 
cssclasses:
---
# Forma canónica

Un problema de programación lineal esta en forma canónica si: 
+ El objetivo/función busca **MAXIMIZAR**
+ Igualdades: **≤**
+ Variables: **≥ 0**
EL modelo se puede expresar de la siguiente forma:
$$
\begin{gather}
\text{Función:}\\
\max z = c^Tx\\\\
\text{Restricciones:}\\
Ax <= b\\\\
\text{Variables:}\\
x>= 0
\end{gather}
$$
+ c → Vector de costes/beneficios (A obtener/reducir)
+ b → Vector de recursos (Que delimitan)

Para transformar un modelo lineal a su forma canónica utilizamos las siguientes equivalencias:
## Transformaciones:
1. Un problema de minimización es equivalente al de maximización, **con un cambio de signo a f**
2. Para cambiar el sentido de una desigualdad multiplicamos por -1.

***