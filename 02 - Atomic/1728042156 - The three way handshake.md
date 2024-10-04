---
aliases:
  - The three way handshake
tags:
  - review
  - Networks
References: 
cssclasses:
sr-due: 2024-10-05
sr-interval: 1
sr-ease: 228
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
   + Sends **SYN** and **ACK** flags. (only ACK also suffices)

3. **Third message: (hostA → hostB)**:
   + **ACK** for the last message.

4. Start the communication
***
