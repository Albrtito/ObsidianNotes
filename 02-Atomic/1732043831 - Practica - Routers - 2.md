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
  subgraph SUCURSAL N
    R1[(R1)] --- eth0.1
    R1 --- eth0.2
    R1 --- eth0.3
    R2[(R2)] --- eth0.1 
    R2 --- eth0.2
    R2 --- eth0.3
    R3[(R3)] --- eth0.1
    R3 --- eth0.2
    R3 --- eth0.3
    R3 --- eth0.4
    Red Oficinas 1 --- eth1
    Red Oficinas 2 --- eth1
    Red Servidores --- hstOf11
    Red Servidores --- hstOf12
  end
  R100[(R100)] --- 10.0.100.0/24
  10.0.75.0/24 --- R1
  10.0.75.0/24 --- R2
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