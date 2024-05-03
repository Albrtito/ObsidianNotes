---
aliases:
  - Process Synchronisation
tags:
  - review
  - OS
"References:": 
cssclasses:
---

# Process synchronisation:
## Communication mechanisms: 
How can we transfer information between two processes, there exists several mechanisms to do so: 
+ Files 
+ Pipes(pipes, FIFOs)
+ Shared memory variables
+ Message passing 

During the OS course we’ll work with **shared memory variables**
## Synchronisation mechanisms: 
Synchronisation between processes is the concept of managing how the processes share information between one another so there are no conflicts and the information is not changed in non-intended ways.

Synchronisation mechanisms **allow to enforce that a process stops its execution until an event happens in some other process**

In order to synchronise processes we use services provided by the OS such as: 
+ Semaphores 
+ Mutex and condition variables
During the OS course we’ll focus on those two with an entasis on mutex and condition variables as semaphores can be to fixed to models. 
These methods are based on the concept of how synchronization operations must be **atomic**. 