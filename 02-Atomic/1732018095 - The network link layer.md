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
> + Connect a ONE LINK HOP
>   
> Each link is different and therefore needs a different protocol. 

> [!example] Notation: 
> **host and routers = nodes:** From the link layer point of view all devices at the edges of the link are nodes and there are no differences between them. 
> **links:** The communication channels that connet adjacent nodes. There are severl types. 
> **packet → FRAME:** The packet of the link layer is a frame, it **encapsulates the network layer packet (datagram)**
>**MAC Addresses: Physical addresses: Link layer addresses:** The addresses used in the Link layer to identify hosts 

## Link layer services: 
1. **Framing:** 
  + The encapsulation of the datagram into a frame. A **header and trailer are added** 
  + Mediación / organisation of the used medium in shared channels 
  + **MAC address** usage to identifiaction of hosts
2. **Reliable delivery between ADJACENT NODES:** 

> [!bug] Problem, question: 
> If TCP is reliable, why is important to have a reliable link layer protocol. 
> If the link is reliable, why use TCP or any other reliable transport layer protocol ?

> [!check] Solution:
> + The retransmission of TCP packets can be avoided with a reliable link layer. Instead of retransmitting through the whole network we just need to do it over one link. 
> + Maybe if we are sure that the link will allways be reliable, it makes no sense to implement TCP. The reality is that we wont be able to really know that for sure. So better implement TCP


3. **Flow control:** 
4. **Error detection**
5. **Error correctoin**
6. **Half duples and full duplex protocols**: Ways of sending and recieving data over the same channel. 
	1. **Half duplex:** One is sending, the other cannot
	2. **Full duples:** Sendi
***