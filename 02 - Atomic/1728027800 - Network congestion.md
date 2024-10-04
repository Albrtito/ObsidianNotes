---
aliases:
  - Network congestion
  - Congestion control
tags:
  - review
References: 
cssclasses:
---
# Network congestion

## TCP Congestion control: AIMD
We can use the number of packets (n) sent in a window to control the flow sent into the network. **Change the flow of the packets to control congestions**

For this we need to pieces: 
1. **A congestion signal:** A way of telling the sender there has been a congestion
   We can know this by **looking at the RTT**, this is because the only delay that can change is the **queueing delay** → Congestion. 
   We can also use **packet loses**, it is easier altough mo
2. **A way of changing the flow:** Just change the size of the window


***
