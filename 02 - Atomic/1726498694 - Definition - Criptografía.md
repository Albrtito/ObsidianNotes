---
aliases:
  - Definition - Criptografía
  - Criptografía
tags:
  - review
  - Cripto
References: 
cssclasses:
---
# Criptografía:
La definición moderna de criptografía incluye los tres objetivos de la seguridad informática ya [[1726234693 - Intro a la seguridad informática|mencionados]]: **Confidencialidad, Integridad y aviabilidad**

> [!NOTE] Definición:
> La criptografía es la disciplina que estudia los principios, métodos y medios de **transformar los datos para ocultar su significado**, garantizar su **integridad**, establecer su autenticidad y **prevenir** su **repudio** 
+ Cifrador: Aquella máquina que cifra el mensaje

**Cifrador:** Aquel que cifra el mensaje original utilizando una clave.
![[Screenshot 2024-09-13 at 3.58.36 PM.png]]
+ **k:** Clave
+ **C:** Mensaje cifrado

**Remarks:**
+ Cuando la clave del cifrado y la del descifrado es la misma se denomina **cifrado simétrico**. Cuando son dos claves diferentes lo llamamos **cifrado asimétrico**
	+ La criptografía asimétrica hace un **intercambio de claves en medio público de forma segura**. → En esto está lo importante. 
	  De esta forma podemos introducir el cripto sistemas.
+ A diferencia que en el cifrado, la codificación **no no necesita una clave.**

### Propiedades del cifrado: 
Definimos una serie de espacios y transformaciones de cada cifrado. 
**Espacio de mensajes:** Cantidad de mensajes que se pueden generar
**Espacio de cifrados:** Posibles cifrados que se pueden generar
**Espacio de claves:**
**Familia de transformaciones de cifrado:**
**Familia de transformaciones de descifrado:**

### Principios de Kerckhoff
+ **Computacionalmente seguro**
+ **Seguridad en la clave NO EN EL ALGORITMO**
	El desconocimiento de la clave hace que romper el algoritmo sea practicamente imposible. Con el conocimiento de la clave ha de ser muy fácil comunicar información.
	Conseguir que la única opción viable sea la fuerza bruta.
	
### Criptosistema:
![[Screenshot 2024-09-13 at 4.07.14 PM.png]]
#### Características del criptosistema:
1. Tipo de operación que realiza: **Sustituciones y transposiciones**
2. Número de claves usadas: 
	+ **Simétricos**: Tiene solo una clave → La clave es secreta
	+ **Asimétricos**: Tienen dos claves (una de cifrado y otra de descifrado) → La clave es pública
3. Tipo de procesamiento del texto en claro:
	+ Se va cifrando por bloques → **Bloques**
	+ Se cifra todo junto → **Flujo**
### Operaciones de sustitución y permutación: 
> **Bibliografía:** Claude Shanon. Communication theory of secrecy systems (1949)

Las técnicas matemáticas de cifrado que se usan aún hoy en día son las más básicas: 
+ **Sustitución:** Añade **confusión** mediante sustituyendo o modificando caracteres
+ **Transposición o permutación:** Redistribución de los caracteres sin modificación directa. A esto se le llama **difusión**
	+ Mismos elementos en posiciones diferentes
## Criptografía clásica:
Dividimos los métodos criptográficos clásicos por las operaciones de sustitución y transposición. 
+ **Transposición**: Divididos en:
	+ [[1726493957 - Transposición por grupos|Transposición por grupos]]
	+ [[1726494070 - Transposición por series|Transposición por series]]
	+ [[1726494186 - Transposición por columnas|Transposición por columnas]]
+ **Sustitución**: Divididos a su vez en: 
	+ Monoalfabeto:
		+ [[1726494310 - Sustitución monoalfabeto monográfica|Sustitución monoalfabeto monográfica]] 
		+ [[1726495455 - Sustitución monoalfabeta poligráfica|Sustitución monoalfabeta poligráfica]]
	+ Polialfabética:
		+ [[1726496164 - Sustitución polialfabética periódica|Sustitución polialfabética periódica]]
		+ [[1726497421 - Sustitución polialfabética no-periódica|Sustitución polialfabética no-periódica]]