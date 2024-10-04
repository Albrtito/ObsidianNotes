---
aliases:
  - The three way handshake
tags:
  - review
  - Networks
References: 
cssclasses:
---
# The three way handshake

#Duda: Why won’t the two way handshake work?

> [!NOTE] Definition: 
> The three way handshake is the way of stablishing communicatoin in TCP. Used to agree on the **initial sequence numbers**


1. **First message (hostA → hostB)**: 
   + Chooses the initial sequence number x (for itself) and sends it
   + Uses the **SYN** flag

2. **Second message (hostB → hostA):**
   + Chooses initial sequence number y (for itself) and sends it
   + Sends **SYN** and **ACK** flags. 
***
