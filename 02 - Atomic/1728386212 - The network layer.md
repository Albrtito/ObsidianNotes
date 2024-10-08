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
Within the network layer there are three types of protocols: 
+ Routing and forwarding
+ [[1728390442 - IP Protocol|IP Protocol]] 
+ ICMP protocol 
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

+ **Memory switching:** The **initial architecture of routers**, used in the first generations. 
  The router saves all into memory where the CPU controls where the output goes.
  
+ **Bus switching:** Add some processing capability to each input port. 
  Each packet is moved through the system bus once the processing is done in the input port. But the bus **can only be used one packet at a time.** 

+ **Interconnection network switching:** Creation of several interconnected buses within the router. Each packet can take several routes. 
  > An small telephone network inside each router. 
  
### Iput port queuing:
We can see a clear queue form when the bus has to send a packet, at this moment ports need to wait and generate a queue. 

**To solve the queue issue we impose**
+ Bus needs to have an speed **at least equal to the sum of all port speeds**

### Output port queuing:
An output queue can be generated if there is **concentration of traffic in only one port.** 

We could impose that each output port had the same speed as the bus, however this is not reasonable as we part from the assumption that the input and outpus peeds must be equal. 
+ **These are the queues we end up whith when talking about [[1727255580 - Loss and delay in Networks|Loss and delay in Networks]]**

This queues will be the one **dropping packets**. This is called **buffer management**. 
#### Buffer management:
The buffer management occupies of selecting the packets that will be dropped. There are several ways of dropping packets, this ways try to follow the principle: 
	**IF packets are dropped once the buffer is full, a lot of packets will be dropped and services like TCP will haveno other choice than to go to slow start..**

+ **tail drop:** Drops everything once full → Really bad for TCP
+ **priority:** Drops given some probability (small), only drop some packets **before the buffer is full**. 
+ **marking:** Mark packets to signal congestion 

#### Packet scheduling:
Decide wich packet so send next on linnk, there are several methods as in every OS[^1]. 
+ **FIFO**
+ priority
+ round robin
+ weighted fair queueing

***

[^1]: [[20240411 - 132633 - Intro to processes|Intro to processes]]