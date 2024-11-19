---
aliases:
  - Protocol - ALOHA
  - ALOHA
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# Protocol - ALOHA
ALOHA is a link layer random access protocol for multiple channel access. 

## Slotted ALOHA: Time slots
This protocol takes into account the followint **assumptions** (rules so that everyone is playing with the same idea in mind): 

+ All frames have the same size
+ Time is divided into slots, each slot has the lenght equal to the time required to transmit 1 frame. 
	+ Everyone can use the slots, however u need to transmit **at the beginning of the slot**
+ Nodes are somehow synchronized 
+ The collision is detected by every node in the system. 

What happens with collisions? 
If there is a collision, **each node that collided retransmits with a probability p**. 
+ P is obtained randomly. The probability of collisions will change with a direct relation to P. The higher the P, the higher the probability of collisions. 

## PROS and CONS: 

**PROS:** 
+ With an small load, the channel can be used with little to none problems. 
+ Decentralization, only clocks are needed
+ Really simple. 

**CONS:**
+ Collisions = wasting slots

### What is the efficiency of this systems?

***