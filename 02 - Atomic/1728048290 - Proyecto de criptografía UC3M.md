---
aliases:
  - Proyecto de criptografía UC3M
tags:
  - Cripto
References: 
cssclasses:
---
# Proyecto de criptografía UC3M

> [!attention]  **REQUISITOS:**
> 1. Se ha de tener contraseñas guardadas con gestiones hash. **Como mínimo** han de ser contraseñas que **el usuario conoce**
> 2. El intercambio de información ha de estar cifrado.
> 3. Debemos de comprobar que el mensaje ha llegado integro. → `fernet`

## Librerías a usar:
+ [pyca/Cryptography](https://cryptography.io/en/latest/)
+ [PyCrypto](https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/)

## Funciones: 

+ `fernet`: Con esta función no solo se cifra el mensaje sino que también se autentifica. 
  **Remark:** Si la usamos, explicar pq lo hacemos.

+ `HMAC`: 

## Contraseñas:
Tenemos distintos **tipos de contraseñas:**

1. A través de algo que el usuario conoce (contraseña)
2. A través de algo que el usuario tiene (tokens)
   + A día de hoy esto se da con otro dispositivo conocido
3. A través de cosas biométricas
4. Alguna mezcla de las anteriores

### Gestión de contraseñas: 

+ Para **almacenar contraseñas se utilizarán funciones hash**. Estas son funciones irreversibles. Solo obtenemos el mismo resultado con la contraseña. 
	> Utilizar función hash sha256
+ **Caducidad de contraseñas:** Cada cierto tiempo se pueden volver a pedir las contraseñas. 



***
