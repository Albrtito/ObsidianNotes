---
aliases:
  - The network link layer
  - Link Layer
  - The link layer
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# The network link layer

> [!attention] Biblio reference: 
> The wifi is really compact in the UC3M course and given with LANs. We wont be seeing the whole WIFI chapter. 
> 

> [!NOTE] Definition (MAIN IDEA):  
> The link layer has the **responsability of transferring a datagram from one node to a physically adjacent node over a link**. 
> + Connect a ONE LINK HOP via some medium
>   
> Each link is different and therefore needs a different protocol. 

> [!example] Notation: 
>+ **host and routers = nodes:** From the link layer point of view all devices at the edges of the link are nodes and there are no differences between them. 
>+ **links:** The communication channels that connet adjacent nodes. There are severl types. 
>+ **packet → FRAME:** The packet of the link layer is a frame, it **encapsulates the network layer packet (datagram)**
>+ **MAC Addresses: Physical addresses: Link layer addresses:** The addresses used in the Link layer to identify hosts 
>+ **bitTime:** The time to transmit one bit


> [!bug] Problems: 
> The main problems of the link layer are: 
> 1. There are several link mediums through wich a packet can travel. Several protocols need to be used easily. Changing between protocols musnt be a problem 

## Link layer services: 
The link layer may provide some of the following services based on the different protocols and mediums used.
### Framing:

> [!NOTE] Def: 
>  The act of creating the link frame, is directly related to the protocol used.

#Duda : Porque el channel access protocol es algo dentro del servicio de framing?

Este servicio engloba: 
+ Creation of a **header and trailer**.
+ Use of a [[1732031831 - Link channel access protocols|Channel access protocol]]. 
+ Creation of a **MAC ADDRESS** 

 **Remarks:**
+ A trailer is something added **behind the data** instead of before it.
      
### Reliable delivery between ADJACENT NODES:

> Already know how to do this based on the [[1727176650 - Principles of reliable data transfer|Principles of reliable data transfer]]


This service comes with a question on why it is necessary.

> [!bug] Problem, question: 
> If TCP is reliable, why is important to have a reliable link layer protocol. 
> If the link is reliable, why use TCP or any other reliable transport layer protocol ?

> [!check] Solution:
> + The retransmission of TCP packets can be avoided with a reliable link layer. Instead of retransmitting through the whole network we just need to do it over one link. 
> + Maybe if we are sure that the link will allways be reliable, it makes no sense to implement TCP. The reality is that we wont be able to really know that for sure. So better implement TCP

### Half-Full Duplex channels:
5. **Half duples and full duplex protocols**: Ways of sending and recieving data over the same channel. 
	1. **Half duplex:** One is sending, the other cannot
	2. **Full duples:** Sending is permitted from both parts. 

### Other services:
1. **Flow control** 
2. **Error detection**
3. **Error correctoin**
## Implementation of the link layer: 
The link layer is implemented in each host.Each hosts needs an specific card(chip) in order to use each one of the protocols (wifi card, ethernet card…). 

## Multiple access protocols: 
We can define two different types of links: 
+ **point-to-point:** Point to point link between ethernet switches and a host.
  > A wire connecting one host to another
+ **broadcast** links
  > Wifi, signals, using air and similar mediums. 
  
In both types we’ll find problems with something we’ll call **collision**. 
Collisions happen when a node recieves two or more signals at the same time. 

In order to solve this the **multiple access protocols are used,** these protocols determine: 
+ How nodes hsare the chanell → When each node can transmit 
+ The protocols must **use the same channel that is being coordinated.** 

### Ideal framework: 
What would be the ideal multiple acces protocol? 
+ We define a multiple acces channel (MAC) with a rate R of bps. 
We would like that: 
1. When only one node wants to transmit it can send at rate R 
2. When M nodes want to transmit, each can send at average rate R/M. Distribution of the link over all nodes. 
3. There wont be a centralized entity that synchronises. There is a decentralized network of links. 
4. We would like for the protocol to be simple. 

### Types: 
+ **Channel partitioning:** We divide the channel into smaller pieces. Each node has a piece.
	+ There are no collisions in this method
  > A piece could be a t ime slot or a frequency. 

	 + Some examples are: [[1732020527 - Protocol - TDMA|TDMA]] and [[1732020800 - Protocol - FDMA|FDMA]]
	 + **Good** for high channel loads, **bad** for low channel loads

+ **Random access:** Channel does not divide or partition. 
	+ We need a way to **detect recover from collisions.**
	+ Some examples are: [[1732021285 - Protocol - ALOHA|ALOHA]], [[1732022695 - Protocol - CSMA-CD|CSMA]]
	+ Opposite from the channel partition: **Good for low** channel load, **bad for high** channel load. 

+ **Taking turns:** Nodes take turns. The nodes with more data take longer turns.
	+ 


***