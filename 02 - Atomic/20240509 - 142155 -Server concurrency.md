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

## Implementations: 
These practical implementation examples are based on the following video of the OS UC3M course: [Video](https://eu-lti.bbcollab.com/collab/ui/session/playback). This video goes through the theory while creating prototypes of servers based on the types discussed below. 

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
+ **Creation of processes** with fork t**akes time**: 
	+ A new process must be started for each incoming request
	+ A process is terminated for each served request
This means an **excessive use of resoureces**

+ No admission control
	+ Problems with quality

#### Implementation: 
![[20240509 - 155121 - Simulation - Process based server|Implementation-Process based server]]




### Thread-per request server:
The thread per-request solution focusses on creating a new thread each time a request is received. This creation of threads can be done in two ways: 

+ **On-demand threads:** Create a new thread every time a request is received. 
+ **Thread pool**: Create a **fixed number of threads** from the beggining



