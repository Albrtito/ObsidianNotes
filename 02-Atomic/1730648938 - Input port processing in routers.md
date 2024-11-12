---
aliases:
  - Input port processing in routers
  - Input port processing
tags:
  - Networks
  - incomplete
References: 
cssclasses:
---
# Input port processing:
Input ports must do the following actions, we’ll discuss each one of them below:

1. Lookup into the forwarding tables and send the packet into the switching fabric to the output port. This lookup is usually denoted as the abstraction **match plus action**
2. Physical and link layer processing.
3. Rewrite the packets header information
4. Update counters for network management.
## Lookup (match plus action):
+ Iput port processing solves the centralised processing botleneck in lookup by **copying the forwarding tables into each one of the input ports.** 

![[1730624725 - Routerj.png|center|500]]


> [!BUG] Problem: 
> The main problem when looking at a table is how long is it going to take. Input ports need to work blazingly fast and looking at a 4 million entry table is not feasable.
> 

> [!check] Solution: 
> The solution is to use **prefix-matching** to simplify all the probabilities into a few prefixes and output into link-interfaces based on this prefixes.
> 
+ If two prefixes math use **longgest-prefix matching**
+ This still needs to be done super fast. Spetial SRAM,DRAM,TCAM memory is used along with the latest search algorithms to return rows in **constant time.**


***