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
	+ Because both hosta are going to send data, the **acks will be carried within the data sent as response**, this is called **PIGGYBACKING**

+ **Cummulative ACKS:** Each ack not only says that the last package was correct. It also says that **all packages till that point where recieved correctly**.

## TCP segment:
+ **Sequence number of the package:** Given by the sequence number of the first byte. This is because all bytes are numbered. 
+ **Sequence number of the ack:** The acknowledgement package has the number of the **package it is waiting go recieve**. Ack number = expected sequence number

## Echoes: 
Resend of the last package with the same data. To assure that the data has been recieved. 

## Round Trip Time(RTT):
+ Associate a timer to the **oldest package being sent** (without a recieved ack)

It is better to set a **longer RTT** because then we’ll only be waiting longer for packets that get lost or corrupted. This is why we **wont try to get an exact value for the RTT but we’ll try to macke overestimate**

### Estimation of the RTT:
Eestimating based on the last sent package is a really bad idea because the **variabilty between packages is huge.** A best estimation will be: 
$$
EstimatedRTT = (1-\alpha) \cdot EstimatedRTT + \alpha \cdot SampleRTT
$$
+ This formula makes it so the weight of one particular sample **decreases exponentialy over time**. 
+ We compute the average of the last n samples with a decreasing weight for each previous sample. 
+ The changes in alpha give out how much weight we give to previous samples. 

**Problem:** However the estimation of the RTT is a bad value to use as actual RTT **because we are not overshooting**. 

**Solution:** Create the overshoot with a security margin using the **variance(deviation)** of the estimated value. 
$$
DevRTT = (1-\beta)\cdot DevRTT + \beta|SampleRTT - EstimatedRTT|
$$
## Timeout interval: 
Using what we have just explained about RTT, we use that data to compute the timout intervals for timers sending the oldest package:

Finally, the gloval timeout interval will be: 
$$
\boxed{TimeoutInterval = EstimatedRTT + 4\cdot DevRTT}
$$
## Sender&Reciever:
 

***