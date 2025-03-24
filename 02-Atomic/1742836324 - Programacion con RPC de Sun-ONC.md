---
aliases:
  - Programacion con RPC de Sun-ONC
tags:
References:
cssclasses:
---
# Programacion con RPC de Sun-ONC
+ [[1742836514 - Definicion de interfaces con RPCs|Definicion de interfaces con RPCs]]

Para saber si se ha registrado conrrectamente el servidor utilizar: 
```
rpcinfo -p ipAddress
```

Usando rpcgen:
 ![[1742836324 - Programacion con RPC de Sun-ONCj.png]]
+ Usar flag -M para generar stubs multi-thread. También las flags -a y -N 
+ Solo hay que cambiar el archivo suma_server.c generado para el código. No hay que tocar ninguno de los archivos naranjas. 

## Makefile:


> [!attention] Cuidado con el clean del makefile
> Pq borra todo, todos los archivos creados por el RPC también. 
> Una vez que se crean los archivos con el RPC no volver a generarlo. (vas a perder todo lo que has hecho si lo haces) 





***