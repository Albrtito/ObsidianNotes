---
aliases:
  - The network stack
tags:
  - review
  - Networks
References: 
cssclasses:
---
# The network stack: 

> [!NOTE] Why layers? 
>  In order to organise the whole network. Split the network into smaller chunks of info. → **Modularization**
+ The layers are called an stack **because they are implemented as such:** Last in first out 
![[1726572508 - The network stack.png]]

From bottom to top, each layer offers a different service.:
**Physical:** The actual things we can touch → Hardware
**Link:** Data transfer between **neighboring network elements**
**Network:** Joining all the linked devices in the link layer (the glue to actually create the network)
4. **Transport:** Only exists in the end points/host systems. Adapts the service offered by the network layer to the specific needs os applications. How are we going to send the packages? How are they gonna be transported? → With protocols
5. [[1726574469 - Application layer|Application layer]]:Again, only exists in the endpoint devices. 

+ Layers 4 and 5 are only required to be implemented by any device with the need of using application services. 
+ **Routers:** Implement the first three layers
+ **Switches:** Implement the first two layers
+ When traveling through each layer, a **layer header** is added to the message. Each layer adds it’s own layer. (the physical layer does not add a header). 
	+ The completed message plus all the headers is called a **frame.** 
