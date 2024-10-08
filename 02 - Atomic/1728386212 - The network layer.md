---
aliases:
  - The network layer
  - Network layer
tags:
  - review
  - Networks
References: 
cssclasses:
---
# The network layer

## The two network layer functions: 
The network layer occupies itself of two main task, these are: 

+ **Forwarding:** moving packets from a routers input link to the appropiate router output link
+ **routing:** Determine **which route to take in order to arrive at the destination point**. 
  In order to perform this function we use routing algorithms. 

## Data and control plane: 
+ **Data plane:** How are packets going to be forwarded. 
  The **forwarding is a data plane function**
+ **Control pane:**: The layer from a **network-wide logic**. The control plane is made out of traffic needed to make the network work. 
  The setting of this plane can be done in one of two ways: 
  1. Traditional routing algorithms **implemented** **in the routers**
     + **Manually:** Each router is set up manually. Tedious and only can be done in small setups
     + **Per router:** Each router discovers the network topology, then applies an algorithm. 
 2. **Software-Defined networking(SDN):** Configured in servers, not in routers.
	 + Not ideal for the whole internet but small networks are using it
	 + One server performs the computing and then pushes to the routers

## Service models:
+ These are [[1728387775 - Best effort services|best-effort services]] so that all the reliability is **implemented in the endpoints → TCP**
## Router architecture: 

![[1728386212 - The network layerj.png|center|500]]

+ high-speed switching fabric: Connects all the input to the output

### Input port functions: 
![[1728386212 - The network layerj-2.png|center|500]]

### Switching fabrics:
In order to move the data from one input port to an oputput port we can use different **types of switching fabrics**

+ **Memory switching:** 
***
