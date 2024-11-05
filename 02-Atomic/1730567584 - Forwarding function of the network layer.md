---
aliases:
  - Forwarding function of the network layer
  - Forwarding
  - switching
tags:
  - incomplete
References: 
cssclasses:
---
# The forwarding function the netwok layer:
> [!NOTE] Forwarding: 
>  Router local action of transferring a packet from input link intergace to the appropiate output link interface.

 + Takes place in **very short timespaces**. Needs to be done quickly as a lot of packets go through one router. 
 

> [!example] Dictionary: 
> + **switching** → Can be used interchangeably with forwarding 


## Forwarding tables:
Every network router has one forwarding table. These tables are use by the router to **know where each packet needs to be forwarded**. 
+ Data from the packet header is taken and used to index the table. 
+ These tables are **created by the [[1730567097 - The network layer control plane|Control plane]]**

## Destination-based forwarding:

> [!attention] MAIN IDEA: 
> Only the destination matters 


> [!NOTE] Intro(Analogy): 
> Each node sees the final destination of a packet and decides **towards where to send it only based on how to arrive to that destination**. 
> 
> If we used cars going though roundabouts with each roundabout having an entry booth the cars would tell the attendand where to go(final destination) and the attendand would just decide wich exit to take at that roundabout.


## Generalized forwarding:


> [!attention] MAIN IDEA: 
> A lot of factors matter, not only the destination

> [!NOTE] Intro(Analogy): 
>  Each node sees the final destination of the packet **along with a lot of other info** and decides where to send it based on an algorithm programmed into the router. 
>  
>  The cars that enter a roundabout not only tell the booth assistant where to go but also have some properties that allow them to use some exits or not (maybe older cars cannot use the fast highway). It can also happen that some cars are not allowed to used any of the exits.


***