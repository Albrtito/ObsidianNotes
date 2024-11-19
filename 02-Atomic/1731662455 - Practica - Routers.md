---
aliases:
  - Practica - Routers
tags:
  - Networks
References: 
cssclasses:
---
# Practica - Routers


> [!attention] CAREFUL: 
> Collection of things to be careful about:
> + Allways run the `ping` command with the `-c4` flag. Else the ping will be eternal and a `ctrl-c` would need to be used. This can fuck thigs up. 
> + Never leave a router in configuration mode
> + All addresses must be given in [[1730832772 - CIDR Notation|CIDR]] notation. Even if the whole 32 bits are significant → ex: `123.23.23.2/32` 
> + Aunq el código tenga comentarios no se pueden añadir si son de linea

## Dudas: 
#Duda: Pq necesito hacer las rutas para que el ping me funcione?



## Router configurations: 
The routers have several modes to work in: 
+ **Terminal mode:** The initial mode of the router 
+ **Configuration mode:** Mode to change things, accessed using `configure terminal` 
## First part: 
> RSC/S16_escenario_1

> [!check] MILESTONE 
>  Compruebe la conectividad entres las redes A y B del escenario, **haciendo un ping entre PCA y PCB**. Verifique con el comando traceroute las interfaces atravesadas por los paquetes que van de PCA a PCB.

### Assigned IP addresses and interfaces:
> Subnet mask NET A: `172.16.75.0/25` 
> Subnet mask NET B: `172.16.76.0/25` 
> Subnet mask NET C (ROUTERS): `172.16.0.0/30` 


**RA:**
+ (NET A): eth0.0 → `172.16.75.1` 
+ (NET C): eth0.1 → `172.16.0.1` 

**RB:**
+ (NET B): eth0.0 → `172.16.76.1`
+ (NET C): eth0.1 → `172.16.0.2` 

**PCA:** 
+ (NET A): eth1 → `172.16.75.2` 

**PCB:**
+ (NET B): eth1 → `172.16.76.2`

### Routing tables: 

#### RA:

| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.76.0/24 | RB       | eth0.1    |
| 172.16.75.2    | PCA      | eth0.0    |
| 172.16.0.2     | RB       | eth0.1    |
#### RB:


| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.76.2    | PCB      | eth0.0    |
| 172.16.75.0/24 | RA       | eth0.1    |
| 172.16.0.1     | RA       | eth0.1    |
#### PCA:


| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.75.0/24 | RA       | eth1      |
| 172.16.76.0/24 | RB       | eth1      |
#### PCA:


| TO             | NEXT_HOP | INTERFACE |
| -------------- | -------- | --------- |
| 172.16.76.0/24 | RB       | eth1      |
| 172.16.75.0/24 | RB       | eth1      |


### INPUTTED CODE: 
**Removing IPv4 addresses from routes:**
```sh
# Los comandos de este lab son (para cada router): 
config terminal
interface eth0.0
no ip address 192.168.0.1/24
exit
interface eth0.1
no ip address 192.168.1.1/24
exit
interface eth0.2
no ip address 192.168.2.1/24
exit 
interface eth0.3 
no ip address 192.168.3.1/24

exit
interface eth0.4
no ip address 192.168.4.1/24
exit
interface wlan0
no ip address 192.168.5.1/24
exit 
exit
```

**Removing IP addresses from PCs,  adding new ones and default gateways **
```sh
# Los comandos de este lab son: (Ejecutar según que linea en cada PC)
	#PCA
	
	#Eliminamos el address de la interfaz eth1 para PCA
	sudo ip addr del 192.100.100.101/24 dev eth1
	sudo ip addr flush dev eth1
	
	#Añadimos la dirección adecuada en el PCA
	sudo ip  addr add  172.16.75.10/25 dev eth1
	# Configuramos el default gateway por el router RA
	sudo ip route add default via 172.16.75.2 dev eth1


	#PCB
	
	#Eliminamos el address de la interfaz eth1 para PCB
	sudo ip addr del 192.100.100.102/24 dev eth1
	sudo ip addr flush dev eth1
	
	#Añadimos la dirección adecuada en el PCB
	sudo ip addr add  172.16.76.10/25 dev eth1
	# Configuramos el default gateway por el router RB
	sudo ip route add default via 172.16.76.2 dev eth1
	

```

**Assigning IP addresses to the routers:**
```sh
# Los comandos de esta parte son: (Ejecutar según que linea para cada router)
	# Para RA en NET A
	config terminal
	interface eth0.0
	ip address 172.16.75.2/25
	exit
	
	# Para RA en NET C
	interface eth0.1
	ip address 172.16.0.1/30
	exit 
	exit


	# Para RB en NET B
	config terminal 
	interface eth0.0
	ip address 172.16.76.2/25
	exit
	
	# Para RB en NET C
	interface eth0.1
	ip address 172.16.0.2/30
	exit
	exit
```

**Create the routes between the networks:**
+ In the routers:
```sh
# From RA send to NET B
	config term
	ip route 172.16.76.0/25 172.16.0.2
	exit
	
# From RB send to NET A
	config term 
	ip route 172.16.75.0/25 172.16.0.1
	exit
```

***