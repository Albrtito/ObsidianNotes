---
aliases:
  - Forwarding function of the network layer
  - Forwarding
tags:
  - incomplete
References: 
cssclasses:
---
# The forwarding function the netwok layer:
> [!NOTE] Forwarding: 
>  Router local action of transferring a packet from input link intergace to the appropiate output link interface.

 + Takes place in **very short timespaces**. Needs to be done quickly as a lot of packets go through one router. 

## Forwarding tables:
Every network router has one forwarding table. These tables are use by the router to **know where each packet needs to be forwarded**. 
+ Data from the packet header is taken and used to index the table. 
+ These tables are **created by the [[1730567097 - The network layer control plane|Control plane]]**
***