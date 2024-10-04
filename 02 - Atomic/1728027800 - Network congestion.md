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
   We can also use **packet loses**, it is easier altough most mechanisms are complex and use the RTT.
2. **A way of changing the flow:** Just change the size of the window

We’ll use packet losses and apply the AIMD method:

> [!attention] IDEA: 
> We aim to create congestion until we create the congestion, this way we can reach better average time. 
> AIMD: 
> + **A**ditive **I**ncrease
> + **M**ultiplicative **D**ecrease: 
> 	We dont only want to decrease the flow, we also **need to drain the buffer** 

+ **Base case:** Lets start with the basic cases: Once we sent a window of n we get n acks, the: 
1. We can send again the **same number of packets** 
2. We can send an **increased amount of packets** → We’ll do this so that if later we reach a congestion it is with a bigger amount of packets.
+ **Packets lost cases:** If we dont get the acks → **Packet loses**
1. Send a lot of less packets, not only to decrease the flow but enougth to **drain the buffers**. → Divide the window by 2. (Cut it in half)

### Cons: 

**What to do when starting a new flow?:** 
1. We can start really conservative, **start with a window of 1**. 
   But one is to little, we’ll be incrementing for forever
2. Estimate an RTT based on the speed of the link we have. 
   But this is to much, se can disturb other users. 
**Solution:** We’ll perform an exponential incrementation. Start with 1 packet and double it each time. 1-2-4-8 -..-. We call this method **slow start**


### Detection of the packet loss: 
We an detect loss packets in two different ways, one of them is by **duplicate acks** and the other is **packet timeouts**. We’ll react differently in each case:

+ Dup


***
