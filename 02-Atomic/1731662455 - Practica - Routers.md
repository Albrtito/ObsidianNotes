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
> Subnmet mask NET B: `172.16.76.0/25` 


**RA:**
+ (NET A): eth0.0 → `172.16.75.1` 
+ (NET C): eth0.1

**RB:**
+ (NET B): eth0.0
+ (NET C): eth0.1

**PCA:** `172.16.75.2`
+ (NET A): eth1 

**PCB:**
+ (NET B): eth1
### CODE: 
```bash
# RA/RB: Eliminar las direcciones de eth0.0 a eth0.4 y wlan0
	# Check the interfaces data in terminal mode:
	show interface eth0.0 
	show interface eth0.1 
	show interface eth0.2
	show interface eth0.3 
	show interface eth0.4
	# Do for RA and RB
	# Now delete those IP addresses in configuration
	# Enter conf mode with: 
	configure terminal 
	# enter an interface 
	interface <name>
	# delete the address. 
	no ip address <address>
	# IP6 should not be necessary, the command is:
	no ip6 address <address> 
	# Repeat for all interfaces and routers
	
# PCA/PCB: Comprobar direcciones usando ip: 
	# Show ip config 
	ip addr show 
	# Eliminar una IP
	sudo ip addr del <addr> dev <interface_name>
	# Añadir una nueva IP
	sudo ip addr add  <addr> dev <interface_name>

# RA/RB: Añadir una nueva dirección IP
	config terminal
	ip address <address> # Address in CIDR notation
	
```

#### INPUTTED CODE: 
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

**Removing IP addresses from PCs**
```sh
# Los comandos de este lab son: (Ejecutar según que linea en cada PC)
	# Eliminamos el address de la interfaz eth1 para PCA
	sudo ip addr del 192.100.100.101/24 dev eth1
	# Eliminamos el address de la interfaz eth1 para PCA
	sudo ip addr del 192.100.100.102/24 dev eth1
	# Añadimos la dirección adecuada en el PCA
	sudo ip addr add  172.16.75.2 dev eth1
```

**Adding IP addresses to the routers:**
```sh
# Los comandos de esta parte son: (Ejecutar según que linea para cada router)
	# Para RA
	config terminal
	ip address 172.16.75.1/32
	exit
	# Para RB
	config terminal 
	ip address 172.16.76.1/32
	exit
```
***