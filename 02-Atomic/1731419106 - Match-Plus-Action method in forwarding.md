---
aliases:
  - Match-Plus-Action
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# Match-Plus-Action 
The match plus action process is performed inside the routers, it is an esential function of the data plane **in charge of finding where each datagram should be redirected by looking at the table**. 

We’ll look at the match-plus-action method for **generalised forwarding**. This method is ruled by the **OpenFlow** standard. 
## Flow tables:
The forwarding or flow tables contain the following fields for each entry:
+ **Set of header field values**: Prefix to match
+ **Set of counters:** Updated as packets are matched by the table entry. 
+ **Set of ac**
## Optimizing searching: 
> [!BUG] Problem: 
> The main problem when looking at a table is how long is it going to take. Input ports need to work blazingly fast and looking at a 4 million entry table is not feasable.
> 

> [!check] Solution: 
> The solution is to use **prefix-matching** to simplify all the probabilities into a few prefixes and output into link-interfaces based on this prefixes.
> 
+ If two prefixes math use **longgest-prefix matching**
+ This still needs to be done super fast. Spetial SRAM,DRAM,TCAM memory is used along with the latest search algorithms to return rows in **constant time.**
***