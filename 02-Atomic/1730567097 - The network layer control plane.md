---
aliases:
  - The network layer control plane
  - Control plane
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# The network layer control plane
The control plane is the one that does all the **processing and thinking of the whole network layer**. This processing is done in the form of [[1730567598 - Routing function of the network layer|Routing]] functions. 

> [!ATTENTION] KEY IDEA: 
> This routing functions need to be implemented in some way that **takes information from all routers** to know who are they connected with and the paths that they use (routing tables). 

## Traditional approach: 
The traditional approach is to have a **routing algorithm inside each router**.
>This idea could be compared to having a human operator at each router deciding where to send packages. It would need to have some communication with the nearest operators

+ Requires that routers **talk to each other** this is done using **routing message**. 
## SDN(Software Define Networking) Approach: 
Instead of having each router implementing the functions have a **general routing component** that does all the routing for all routers and then sends this information to each of them. 



***