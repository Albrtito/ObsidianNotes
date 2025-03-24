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






***