---
aliases:
  - TCP
  - Definition - TCP
tags:
  - review
  - Networks
References: 
cssclasses:
sr-due: 2024-10-06
sr-interval: 6
sr-ease: 230
---
# TCP
#Duda: Differencia entre internet transport protocol and internet transport protocol service.

> [!NOTE]  Definition:
>  TCP is an **internet transport protocol service** that offers **reliable transmission** of data between sender and reciever.

**Remarks:**
+ **Reliable transport**
+ **Flow and congestion control**
+ **NO** 
	+ timing
	+ security 
	+ minimum throguhput
+ Requires for the server and the client to **set up the connection** (==Three-way handshake)==
## Properties:

+ The TCP protocol must control the flow of data so that there are less packages being sent but sent constantly. This is because **for each package a frame will be created**. This frame has some size.
	+ This tradeof is solved by only allowing one **small package in flight**, the rest of packages in the window must be bigger than the minimun stablished size. 

+ **Bi-Directional flow of data**: The data will be composed of two unidirectional flows. Meaning both hosts can **act as both reciever and sender**.
  Therefore we need to create **two different sequence number spaces**. One for each sender.

+ **Cummulative ACKS:** Each ack not only says that the last package was correct. It also says that **all packages till that point where recieved correctly**.

## TCP segment:

***