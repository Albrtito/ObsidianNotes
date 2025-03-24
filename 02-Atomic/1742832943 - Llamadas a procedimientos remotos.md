---
aliases:
  - Llamadas a procedimientos remotos
  - Remote Procedure Calls
  - RPC
tags:
  - Distri
References: 
cssclasses:
---
# Llamadas a procedimientos remotos


> [!NOTE] Objetivo: 
> Poder programar lo distribuido como si no lo fuese.
> + Hacer la comunicación como si fuese un proceso local. Una vez que se llama a esa función local se realizará toda la logica de conexión distribuida internamente. 


> [!CHECK] Idea: 
>  Obtener el código del servidor automáticamente b asado en las interfaces del cliente. 
>  A esto se dedican los RPCs, simplifican todo lo que se haría con sockets para hacerlo internamente. 

## Uso de la RPC
Las RPC generan el código (stub) del cliente y servidor a partir de un archivo `.x`
+ Del lado del servidor se han de implementar las funciones definidas. 
+ Del lado del cliente se haran **llamadas al stub del cliente** que a su vez se encargará de hacer toda la comunicación con el servidor. 

**Remarks:**
+ El cliente es el activo, es el que activa la comunicación con el servidor 
+ El server es un proceso pasivo esperando requests. 
### Stubs:
Piezas de código que realizan la comunicación entre servidor y cliente. 
>Lo que durante los laboratorios de la asignatura han sido proxy.c y servidor.c 

+ Se encargan de hacer toda la convesrsión de parámetros para el uso de sockets. 
+ **Stub servidor:** Se encarga de registrar el servicio para que el cliente pueda buscarlo

## Características de RPC: 
1. Existen dos tipos de RPC: 
	+ **Síncronas** Petición y respuesta
	+ **Asíncronas:** Solo admiten peticiones. El cliente no espera una respuesta (no hay salida)
2. Utilizan un lenguade de definición de interfaces (IDL)
3. Generan los stubs
4. Funcionan basados en un protcolo de comunicación

## IDL:
> Lenguaje de Definicion de Interfaces

Requiere tres tipos de parámetros: 
1. de **entrada (in)**
2. de **salida (out)**
3. de **entrada/salida (inout)**

Para transferir estos parámetros hace falta **aplanar los datos**, esto significa pasarlos a texto, normalmente dentro de un esquema de representación de datos (XML, JSON, XDR …)


***