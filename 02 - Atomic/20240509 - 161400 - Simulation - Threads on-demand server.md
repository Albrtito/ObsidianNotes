---
aliases:
  - Simulation - Threads on-demand server
tags:
  - OS
"References:": 
cssclasses:
---
# Simulation of a threads on-demand server: 
This simulation is done using [[20240503 - 190310 -Semaphores Dijkstra method|Semaphores]].

**Remarks:**
+ Careful not to cause race conditions

One single thread is created in the main loop. This thread controls all the creation of other threads from that point forwards.