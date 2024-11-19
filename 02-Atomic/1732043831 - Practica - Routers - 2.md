---
aliases:
  - Practica - Routers - 2
tags:
  - Networks
References: 
cssclasses:
---
# Practica - Routers - 2
For this practice we’ll use a **modified version** of the [[1730716899 - Practica - IP addressing|IP Address Assignment]], with small changes to the number of hosts required for each of the networks. 

## Requirements: 
1. **Office 1:** 100 hosts
2. **Office 3:** 25 hosts 
3. **Servers:** 10 hosts 
4. Ip addresses must be assigned optimizing the number of direcctions for each network 
### RIP Requirements:
1. RIP should not be used when no adjacent routers use RIP
2. Identify the initial router information 
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