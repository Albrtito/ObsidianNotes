---
aliases:
  - Application layer
tags:
  - review
  - Networks
References: "[[Net_References_s2_1.pdf]]"
cssclasses:
---
# Application layer

> [!Quote] Remember: 
> In any network, the aplicatinos that send messages through the network are called **distributed**. 

The **architecture of the application can be one of two types:**

Server - Client
1. **Server:** Where some common info is. It has a permanent place (permanent IP) and sends info to all the clients. 
2. **Clients:** The clients communicate with the server and not with each other. Do not need to be connected all the time

Peer-Peer: 
The peer to peer architecture uses a direct connection between hosts instead of a server-host connection. 
+ There is **no server**
+ There is a service for service mindset. (Bit-Torrent)
+ Peers are **intermittently connected**

## Communication of processes: 
Each application can be composed of one or more processes, this processes can communciate (send messages) with other processes 
