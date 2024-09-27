---
aliases:
  - Packet switching
tags:
  - review
  - Networks
References: 
cssclasses:
---
# Packet switching

> [!NOTE] Definition: 
> Information on the internet is sent by hoping from one host to another until the target host is reached. Messages are not sent whole but broken down into smaller pieces, this process is called **packet switching**.  

+ An explanatory header is added to each of this packets by each of the network layers

This makes the network much quicker as **the links are being used constantly**. 

## Store and forward:
The transmission of packets between the routers is performed following an store and forward technique: **Entire packets must arrive in order for the packet to be sended to the next link**. 
+ Router must **wait** for all bits. 
This creates [[1727255580 - Loss and delay in Networks#Transmission delay|transmission delay]]. 


***