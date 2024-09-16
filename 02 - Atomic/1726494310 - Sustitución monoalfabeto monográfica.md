---
aliases:
  - Sustitución monoalfabeto monográfica
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Sustitución mono-alfabeta monográfica

> [!NOTE] Definición: 
> **Monográfica:** Debido a que sustituye los grafos de uno en uno. Un carácter de texto-claro por 1 carácter de texto-cifrado
> **Mono-alfabética:** Solo existe **un alfabeto transformado** (ver ejemplo cesar)

## Cifrador de desplazamiento puro(ROT):
Es aquel cifrador que utiliza una función del tipo: 
$$
C_i = (m_i \pm b) \mod n
$$
+ b: Constante de desplazamiento. (Sería la clave del sistema)
**Remarks:**
+ ROT → Rotación

**El cifrador Cesar:**
Un ejemplo de este cifrado sería el **cifrado cesar**, que **desplaza** el grafo dentro del alfabeto una cantidad de posiciones. 
En este tipo de cifrado cada grafo **siempre se sustituye** por el mismo grafo-cifrado. → Solo hay un alfabeto transformado (**Mono-alfabetismo**)

## Cifrador de decimación pura:
Es aquel que utiliza una multiplicación para variar el alfabeto y transformarlo en un alfabeto cifrado. 
$$
C_i = (a \times m_i) \mod n
$$
+ a: Clave de cifrado. Constante de decimación

### Cifrador por sustitución afín:
Unión de desplazamiento y decimación.
## Problemitas: 
Si creamos un histograma con la probabilidad de aparición de cada una de los grafos en un alfabeto. Aún después de haber realizado la sustitución, las probabilidades se mantienen.