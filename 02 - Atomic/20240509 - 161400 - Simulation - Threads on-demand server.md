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

One single thread is created in the main loop. This thread controls all the creation of other threads from that point forwards. This master thread is based on the receiver function.

## Functions: 

**Main:** 
The main function creates the receiver and initialises all the semaphores, etc. It also computes the time it takes the server each request. 

**Receiver:**
This acts as a master thread. It receives all the request and creates threads to manage the received requests. It uses the semaphore sparam to wait for the just created thread to copy the pointer to the request so it can keep using it’s pointer r. 
Finally i