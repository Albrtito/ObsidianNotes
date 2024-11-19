---
aliases:
  - Protocol - CSMA
  - CSMA
  - CSMA/CD
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# Protocol - CSMA
CSMA is a link layer protocol using random access in order to solve a multiple access network. It takes the [[1732021285 - Protocol - ALOHA|ALOHA]] protocol and solves the problems that occur with pure aloha. 

## Changes made to ALOHA: 
### CSMA:
+ If someone is in the channel, just dont transmit. 

### CSMA/CD:
Add **collision detection:** Reduce the time wasted in collisions. 
+ If a node detects a collision while it is transmitting, it’ll stop. 
+ 
***