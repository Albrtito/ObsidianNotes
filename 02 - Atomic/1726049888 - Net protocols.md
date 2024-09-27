---
aliases:
  - Net protocols
tags:
  - review
  - Networks
References: 
cssclasses:
sr-due: 2024-10-20
sr-interval: 23
sr-ease: 250
---
# Net protocols
When sending packages though the internet computers need to understand one another. This means **encoding the packages in the same way** as the one receiving them.
+ The [IETF](https://www.ietf.org/) defines public standard protocols.
**Remarks:**
+ Most protocols are public (TCP,IP) although anyone can develop a private protocol.

> [!NOTE] Definition(Kurose): 
> A protocol defines the ==format and the order== of messages exchanged between two or more communicating entities, as well as the actions taken on the transmission and/or receipt of a message or other event.
## Types based layer:
The internet is constructed as a layered architecture. For each of it’s layers there are several different protocols. 
### Transport protocols:
Two main protocols are used in this layer, TCP and UDP. 
+ [[1727428429 - Definition - UDP|UDP]]
+ [[1727428451 - Definition - TCP|TCP]]
We must also mention the [[1727429612 - Definition - TLS|TLS]] tools. Used to add a layer of security to the transport layer protocols. 