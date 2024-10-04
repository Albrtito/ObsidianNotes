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

> [!NOTE]  Definition:
>  TCP is a connection oriented **internet transport protocol** that offers **reliable transmission**[^2] of data between sender and reciever.

+ Works with **one-to-one**: One sender to one reciever
+ Data arrives **ordered and whole**
+ Offers **congestion control**[^1]
+ Offers **flow control** 
+ Requires to **set up the connection** → [[1728042156 - The three way handshake|The three way handshake]]

![[1727428451 - Definition - TCPj.png]]

## Sequence numbering:
TCP has a **wierd way of numbering packets**. Based on the [[1727187791 - Method - RDT Sliding window|Method - RDT Sliding window]] we can say that for any sliding window with value n we’ll **need at least 2n sequence numbers to prevent any type of erros.**

TCP does not use this 2n sequence numbers but instead uses the **number of the first byte of the package** to number the whole packet. 


#Duda: Are we, at any point, reusing the byte numbers? If a message has to many bytes 


## Properties:

+ The TCP protocol must control the flow of data so that there are less packages being sent but sent constantly. This is because **for each package a frame will be created**. This frame has some size.
	+ This tradeof is solved by only allowing one **small package in flight**, the rest of packages in the window must be bigger than the minimun stablished size. 

+ **Bi-Directional flow of data**: The data will be composed of two unidirectional flows. Meaning both hosts can **act as both reciever and sender**.
  Therefore we need to create **two different sequence number spaces**. One for each sender.
	+ Because both hosta are going to send data, the **acks will be carried within the data sent as response**, this is called **PIGGYBACKING**

+ **Cummulative ACKS:** Each ack not only says that the last package was correct. It also says that **all packages till that point where recieved correctly**.

+ **Out of order packages are stored**
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
 

## ACK Generation: 
Right now the protocol reacts with a large waiting time (4 times the deviation). If we send 4 packages and the second one is lost, then the reaction to send the again the second package wont arrive until we have recieved the acks for all 4 packages (or not). 
We would like to ackt in one RTT time. In order to do so we’ll **tolerate up to three duplicate acks**. 
+ Once we have recieved **more than three duplicated ack** we’ll assume that it is a loss package and retransmit right away. 

***

[^1]: [[1728027800 - Network congestion|Congestion control]]
[^2]: When explaining the workings of TCP we begin by assuming that the [[1727176650 - Principles of reliable data transfer|Principles of reliable data transfer]] are known, and the methods used for it are to.