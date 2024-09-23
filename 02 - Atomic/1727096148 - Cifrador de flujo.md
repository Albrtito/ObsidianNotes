---
aliases:
  - Cifrador de flujo
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Cifrador de flujo

> [!NOTE] Definición: 
> Los cifradores de flujo cifran el **mensaje(M) byte|bit per byte|bit**. Utilizan una **serie cifrante (K)**. Cada elemento de la serie cifra un byte|bit. 
> $$M = m_1, m_2, m_3,m_4...$$
> $$K = k_1, k_2, k_3,k_4..$$
> + $m_i$ se cifra con $k_i$
> + La serie cifrante (K) es **idealmente infinita y aleatoria**

**Remarks:**
+ Es imposible generar una serie infinitamente aleatoria con el uso de ordenadores → Se utilizan series **pseudoaleatorias** generadas por PRNGs 
## Tipos: 
AL ser un método de criptación síncrono, los cifradores de emisor y receptor han de ser capaces de **intercambiar la clave** cifrante. Cuando este intercambio se realiza de forma **externa será un sistema síncrono**, mientras que si se realiza de forma **automática será un sistema autosíncrono** 

+ #Duda: Diferencias en la generación de la serie cifrante para cada uno de los casos

## Pros&Cons:
+ Cifrado muy rápido
+ Los errores no se propagan (Cifrado uno a uno)

+ Poca difusión
+ No se puede generar aleatoriedad
+ Problemas al reutilizar la clave. 
	Se pueden realizar ataques sabiendo solo parte del sistema:
	1. **Ataque con texto original conocido:** Obtener K teniendo M yC
	2. **Ataque solo al criptograma:** Usando dos trozos diferentes de la clave. 
***