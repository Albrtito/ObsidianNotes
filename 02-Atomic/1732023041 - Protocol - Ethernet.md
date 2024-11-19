---
aliases:
  - Protocol - Ethernet
  - Ethernet
tags:
  - incomplete
  - Networks
References: 
cssclasses:
---
# Protocol - Ethernet
The Ethernet protocol is a link layer protocol that uses a random access implementation based on [[1732022695 - Protocol - CSMA-CD|CSMA/CD]] protocol. 

**Remarks:**
+ The ethernet link card that a host has is called NIC
## Steps: 
**Sending data:**
1. NIC recieves tha datagram, creates the frame
2. NIC **senses channel:**
   + **Empty channel:** Start frame transmission 
   + **Busy channel:** Wait for empty channel 
3. Wait untill the transmission is finalized (the whole frame is send): 
	+ **There is no collision while sending:** Nice, the frame was sent
	+ **There is a collision:** Abort and send a jam signal (saying, I stopped because a collision was sensed)
		+ Enter an **binary exponential backoff**. Based on a probability, a retransmission will happen. 
   * 
***