---
aliases:
  - Intro a la seguridad informática
tags:
  - review
  - Cripto
References: https://aulaglobal.uc3m.es/pluginfile.php/7291371/mod_resource/content/1/M1_Intro_Ciber_Cifrado_2425.pdf
cssclasses:
---
# Intro a la seguridad informática 
## Objetivos de seguridad:
Los objetivos de seguridad se dividen en lo que llamamos la **triada CIA**: (CIA Triad)
![[Screenshot 2024-09-16 at 3.12.04 PM.png]]

**Remarks:**
 + Estos objetivos se han de cumplir en cualquier proyecto
+ El objetivo se satisface a través de servicios. A su vez, el servicio cumple con la implementación de un mecanismo.
## Amenazas y medidas: 
### Tipos de amenazas:
Clasificamos las amenazas en 4 tipos: 
1. **Interceptación:** Escuchar lo que se esta diciendo a través de un medio de comunicación
2. **Interrupción**: 
3. **Modificación:**
4. **Generación:**
### Tipos de medidas:
Podemos clasificar las medidas de seguridad que se aplican para proteger un sistema según diferentes criterios. 

**Según activación:**
+ **Prevención**: 
+ **Detección**:
+ **Respuesta**:

**Según el tipo:**
+ **Medidas físicas:** Hay que proteger el hardware ademas del software. 
+ **Técnicas:** Cifrados
+ **Administrativas:** 
+ **Legales:** Medidas aplicadas en la ley. En España tenemos la LOPD (Ley Orgánica de Protección de Datos)
## Cripto y cifrado: 
La definición moderna incluye los tres objetivos de la seguridad informática: **Confidencialidad, Integridad y aviabilidad**

> [!NOTE] Definición:
> La criptografía es la disciplina que estudia los principios, métodos y medios de **transformar los datos para ocultar su significado**, garantizar su **integridad**, establecer su autenticidad y **prevenir** su **repudio** 
#Duda: Diferencia entre codificador y cifrador?

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

### Principios de Kerckhoffs
+ **Computacionalmente seguro**
+ **Seguridad en la clave NO EN EL ALGORITMO**
	El desconocimiento de la clave hace que romper el algoritmo sea practicamente imposible. Con el conocimiento de la clave ha de ser muy fácil comunicar información.
	Conseguir que la única opción viable sea la fuerza bruta.
	
### Criptosistema:
![[Screenshot 2024-09-13 at 4.07.14 PM.png]]
#### Características del criptosistema:

### Operaciones de sustitución y permutación: 
> **Bibliografía:** Claude Shanon. Communication theory of secrecy systems (1949)
Las técnicas matemáticas de cifrado que se usan aún hoy en día son las más básicas: 
+ **Sustitución:** Añade **confusión** mediante sustituyendo o modificando caracteres
+ **Transposición o permutación:** Redistribución de los caracteres sin modificación directa. A esto se le llama **difusión**
	+ Mismos elementos en posiciones diferentes
