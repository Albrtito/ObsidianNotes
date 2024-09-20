---
aliases:
  - Criptosistemas clásicos
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Criptosistemas clásicos
**Referencias:**[Recurso web: Cifrar mensajes con cifradores clásicos](https://www.cryptool.org/en/cto/)

Según si se basan en la transposición o en la sustitución[^1].
## Sistemas de transposición:
+ **Por grupos**
+ **Por series**
+ **Por columnas**
## Sistemas de sustitución:
Necesitamos conocer el concepto de sustitución monoalfabética, polialfabética, monográfica y poligráfica

> [!NOTE] Definición:
> **Poligráfica/Monográfica:** Debido a que sustituye los grafos individualmente(Mono) o en grupos(Poli).

> [!NOTE] Definición:
> **Monoalfabética/Polialfabética:** Respecto al n**úmero de alfabetos criptados** que se crean. 
> + Mono → Uno
> + Poli→ Más de uno

### Monoalfabéticas:
 Cifrador de PLAYFAIR:
 **Cifrador de HILL:**
Utiliza multiplicación por matrices: 
+ La matriz es la clave. Es una matriz cuadrada de n x n. El texto se divide en grupos de n elementos. Se aplican caracteres de relleno (si el texto no se divide exactamente en grupos de n)
+ Estos grupos se interpretan como vectores
+ Se multiplica cada vector por la matriz. Obteniendo un nuevo vector. Los nuevos valores están cifrados con la clave (matriz).

		+ [[1726494310 - Sustitución monoalfabeto monográfica|Sustitución monoalfabeto monográfica]] 
		+ [[1726495455 - Sustitución monoalfabeta poligráfica|Sustitución monoalfabeta poligráfica]]
	+ Polialfabética:
		+ [[1726496164 - Sustitución polialfabética periódica|Sustitución polialfabética periódica]]
		+ [[1726497421 - Sustitución polialfabética no-periódica|Sustitución polialfabética no-periódica]]
***
[^1]: [[1726520589 - Definition - Criptosistema#Técnicas matemáticas de cifrado]]
