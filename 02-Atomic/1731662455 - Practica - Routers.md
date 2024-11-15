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



## Router configurations: 
The routers have several modes to work in: 
+ **Terminal mode:** The initial mode of the router 
+ **Configuration mode:** Mode to change things, accessed using `configure terminal` 
## First part: 
> RSC/S16_escenario_1

> [!check] MILESTONE 
>  Compruebe la conectividad entres las redes A y B del escenario, **haciendo un ping entre PCA y PCB**. Verifique con el comando traceroute las interfaces atravesadas por los paquetes que van de PCA a PCB.

### Assigned IP addresses: 
**RA:**
+ (NET A): eth0.0 
+ (NET C): eth0.1

**RB:**
+ (NET B): eth0.0
+ (NET C): eth0.1

**PCA:**
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
	# delete the address
	no ip address <address>
	# Repeat for all interfaces and routers
	
# PCA/PCB: Comprobar direcciones usando ip: 

	# Show ip config 
	ip addr show 
	# Eliminar una IP
	sudo ip addr del <addr> dev <interface_name>
	
```
***