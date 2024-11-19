---
aliases:
  - Practica - Routers - 2
tags:
  - Networks
References: 
cssclasses:
---
# Practica - Routers - 2
# Topología de Red RYSCA/p_encam_a

```mermaid
graph TD
subgraph ide1 [10.0.0.0/24]
R100
R4
R100 --- R4
subgraph ide2 [10.0.75.0/24]
R1
R2
R3
R4
end
end


  ```
  
## Tablas de Enrutamiento

### Router R1
| Destino       | Siguiente Salto        | Interfaz |
| ------------- | ---------------------- | -------- |
| 10.0.75.0/24  | Directamente conectado | eth0.2   |
| 10.0.75.0/24  | Directamente conectado | eth0.3   |
| 10.0.0.0/24   | eth0.1                 | -        |
| 10.0.100.0/24 | R100                   | -        |

### Router R2
| Destino | Siguiente Salto | Interfaz |
| ------- | -------------- | -------- |
| 10.0.75.0/24 | Directamente conectado | eth0.1 |
| 10.0.75.0/24 | Directamente conectado | eth0.3 |
| 10.0.0.0/24 | eth0.1 | - |
| 10.0.100.0/24 | R100 | - |

### Router R3
| Destino | Siguiente Salto | Interfaz |
| ------- | -------------- | -------- |
| 10.0.75.0/24 | Directamente conectado | eth0.1 |
| 10.0.75.0/24 | Directamente conectado | eth0.2 |
| 10.0.75.0/24 | Directamente conectado | eth0.3 |
| 10.0.0.0/24 | eth0.4 | - |
| 10.0.100.0/24 | R100 | - |

### Router R100
| Destino | Siguiente Salto | Interfaz |
| ------- | -------------- | -------- |
| 10.0.75.0/24 | R1, R2 | - |
| 10.0.0.0/24 | Directamente conectado | - |
***