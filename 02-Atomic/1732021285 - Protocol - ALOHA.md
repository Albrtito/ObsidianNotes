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
+ Clock synchronisation is really hard to do. 

### What is the efficiency of this systems?
With a **huge number of hosts** we’ll have a value for p = 37%. This value will transform into: 
+ 37% of the channel will be used. 
+ 37% of the channel wil be empty. 
+ 26% of the time there will be collisions. 

For an small (or any arbitrary) number of host, the **best value for p will be:**
 $$
 p = 1/N
 $$
 + Where N is the number of hosts in the system. 

## PURE (Unslotted) ALOHA: 
In order to solve the problem of clock synchronisation we delete the slots. 
+ This means that collisions can also happen if someone is in the middle of the transmission. 
+ Any frame that is send will collide with other frames that are send in the interval $[t_0 -1, t_0 + 1]$. There will be collision with any system that transmit
	+ This after all means that **the number of collisions rises.**

***