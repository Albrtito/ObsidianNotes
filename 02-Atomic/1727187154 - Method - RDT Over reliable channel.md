---
aliases:
  - Method - RDT Over reliable channel
tags:
  - review
  - Networks
References: 
cssclasses:
sr-due: 2024-12-06
sr-interval: 53
sr-ease: 290
---
# Method - RDT Over reliable channel

> [!NOTE] Implementation:
>  There is not much to say about this implementation. If the channel is reliable, then there is no problem at all, no errors, no loss, no noting. 
>  **In a perfect world this is just it** 

The FSM implementations are really simple. 
+ Wait for a call (package arrives, package is needed) then perform actions.
![[1727187154 - Method - RDT Over reliable channel.png]]
***