---
aliases:
  - Comunicación y sincronización entre procesos
tags:
  - Distri
  - OS
References: 
cssclasses:
---
# Comunicación y sincronización entre procesos

## Conceptos básicos:

> [!NOTE] Sistema distribuido: 
> Sistema formado por rescursos (hardware y software) físicamente distribuidos y **conecctados a través de la red**.
> +  Se comunican a través de mensajes 
> + cooperan para realizar tareas. 


> [!NOTE] Programa vs Proceso: 
> **Programa:** Instrucciones 
> **Proceso:** Programa en ejecución 
> + Gestionado por el sistema operativo
> + Reside en la memoria principal
> + Relacionado jerárquicamente con otros procesos 


> [!NOTE] Thread | Hilo:  
> Programa en ejecución que comparte la imagen de memoria (y otras coass) con otros threads. 
> + Todo esto dentro de un proceso
> + Un proceso tiene **mínimo un hilo**
> 
> Cada hilo tiene:
> + Contador de programa, valor de registros
> + Pila propia 
> + Estado(ejecutando, listo, bloqueado)
>   
> El proceso contiene (información compartida entre hilos):
> + Espacio de memoria
> + Variables globales 
> + Ficheros abiertos, sockets
> + Procesos hijos 
> + Temporizadores ¡
> + Mutex/Semáforos

![[1739203641 - Comunicación y sincronización entre procesosj.png|center|500]]
Se utilizan los threads para paralelizar procesos










***