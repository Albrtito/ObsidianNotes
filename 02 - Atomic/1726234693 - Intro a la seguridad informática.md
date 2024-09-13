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
## Clasificación de las medidas de seguridad: 
Podemos clasificar las medidas de seguridad que se aplican para proteger un sistema según diferentes criterios. 

**Según activación:**
+ Prevención: 
+ Detección:
+ Respuesta:

**Según el tipo:**
+ Medidas físicas: Hay que proteger el hardware ademas del software. 
+ Técnicas: Cifrados
+ Administrativas: 
+ Legales: Medidas aplicadas en la ley. En España tenemos la LOPD (Ley Orgánica de Protección de Datos)
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

### Criptosistema:
![[Screenshot 2024-09-13 at 4.07.14 PM.png]]
#### Características del criptosistema:

### Operaciones de sustitución y permutación: 
