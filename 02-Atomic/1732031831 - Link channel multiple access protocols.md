---
aliases:
  - Link channel access protocols
  - Channel access protocols
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# Link channel multiple access protocols

The link layer must decide how each channel is accesed, not all channels provide bowth ways connecttion, not only that but most of the channels must provide an operating window for tons of hosts and must manage that. These protocols are used to figure out how 
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