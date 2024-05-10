---
aliases:
  - Server concurrency
tags:
  - OS
  - incomplete
"References:": 
cssclasses:
---

# Server concurrency: 

## Simulations: 
These practical simulation examples are based on the following video of the OS UC3M course: [Video](https://eu-lti.bbcollab.com/collab/ui/session/playback). This video goes through the theory while creating prototypes of servers based on the types discussed below. 

## Generic server structure: 
Any server contains an infinite loop with three blocks. 

…→Request **reception** → Request **processing** → Reply **sending** → …

Once the sending is finished the server goes back to waiting for reception

**Remarks:**
+ When processing the **importance lies in the CPU time** 

## Types of servers: 

### Process-based server:
This types of servers create a child process each time a request arrives. The child process performs the request processing while the parent process waits for the next request. 
+ This solves the problem of several requests arriving together or processing processes at the same time.
#### Problems: 
+ **Creation of processes** with fork **takes time**: 
	+ A new process must be started for each incoming request
	+ A process is terminated for each served request
This means an **excessive use of resources**

+ No admission control
	+ Problems with quality

#### Simulations: 
![Implementation-Process based server](20240509%20-%20155121%20-%20Simulation%20-%20Process%20based%20server.md)




### Thread server:
The thread per-request solution focusses on creating a new thread each time a request is received. This creation of threads can be done in two ways: 

+ **On-demand threads:** Create a new thread every time a request is received. 
+ **Thread pool**: Create a **fixed number of threads** from the beginning. Each time a request is received a **free thread is assigned to the request**
	+ Use a **request queue.**

**Remarks:** The last methods (thread pool) is the generalised one and how nowadays (2024-05-09) the servers work. 
#### Thread-per request:
##### Problems: 
+ Although creation of threads has a lower cost than processes, it still has a cost. And creating and deleting threads all the time is not ideal
+ Control of resources. What if many request arrive, if we start creating more and more threads it ends up needing to many resources
##### Method:
+ One receiver thread receives request.
+ If a request arrives, a new thread is created and a copy of the request is passed to the new created thread
	+ **Must be a copy of the request**

##### Simulation:
![Simulation - Threads on-demand server](20240509%20-%20161400%20-%20Simulation%20-%20Threads%20on-demand%20server.md)





#### Thread pool server: 
+ Threads are created at startup to run a service. 
+ A queue of pending request is created to feed the threads. 
+ All threads wait until some request is in the queue.
##### Simulation:
![Simulation - Thread Pool Server](20240509%20-%20191823%20-%20Simulation%20-%20Thread%20Pool%20Server.md)