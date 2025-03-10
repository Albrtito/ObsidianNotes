---
aliases:
  - Servicios distribuidos
tags:
  - Distri
References: 
cssclasses:
---
# Servicios distribuidos

> [!BUG] Problemas en la sincronización de los servicios distri: 
> + Uno de los grandes problemas con los que nos encontramos en los sistemas distribuidos es la **ausencia de un reloj común** para sincronizar los procesos. 
>+ La información relevante esta distribuida “puedo no tenerla yo”
> 

Dados dos procesos en un servicio distribuido se puede decir que: 
+ Son concurrentes o que un ocurre antes que otro. 
Esto se ve a través de los diagramas de espacio-tiempo:
![[1741624225 - Servicios distribuidosj.png]]

Un modelo distribuido puede ser **asíncrono o síncrono:**
+ **Asíncronos:** Aquellos en los que **no hay reloj común.**
	+ No suponemoss nada sobre la velocidad de un proceso
	+ Canales fiables sin límietes: Hay latencia sin límite
	+ Comunicación entre procesos es la única forma de sincronización. 

Los problemas que tenemos en estos casos son de reloj y lo solucionamos aplicando otras técnicas para crear relojes. 

## Tiempo en el sistema linux:
Par obtener el tiempo actual en unsistema linux podemos utilizar. 
+`clock_realtime` : Obtiene le código actualizándolo 
+`clock_monotonic` : Obtiene el código sin actualizar (el código de la máquina.)

## Sincronización de relojes físicos: 
Para un sistema distribuido **cad nodo posee un reloj físico NO SINCRONIZADO.**

***