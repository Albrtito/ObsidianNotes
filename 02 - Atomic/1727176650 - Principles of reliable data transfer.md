---
aliases:
  - Principles of reliable data transfer
tags:
  - review
  - Networks
References: 
cssclasses:
---
# Principles of reliable data transfer
The problem lies on how to transfer data reliablely using an unreliable channel. 

**Interfaces:**

> [!NOTE] Definitions: 
> + **rdt_send()**: Function used to send data over a reliable channel
> + **udt_send()**: Function used to send data over an unreliable channel
> + **rdt_rcv()** : Function used to receive reliable data
> + **deliver_data**(): Function that delivers the data to the app.

+ **Only unidirectional data transfer:** This implementation will be based on a systen where ther is only one sender and one reciever. This means that there cannot be any message sent by the reciever. If we wanted to implement it the other way around we would just do it as a new implementation. 

+ We assure a reliable transmission of data. We **do not assure a reliable transmission of the acknowledgment packages.** 
## Channel with bit errors: 
+ Using error detection methods such as the **checksum**. 
	+ IF there where an error, drop it, ask for it and send it again.

The cycle of sending-recieving messages goes: 
$$
\text{sent package → recieved → dropped/kept → positive/negative acknowledge }
$$

+ With a positive acknowledgement: Send next one
+ With a negative acknowledgment: Resend last one

We can define this cycle as two FSMs in the following ways:

The FSM of the sender:
	![[Screenshot 2024-09-24 at 1.35.21 PM.png|640]]
The FSM of the receiver:
	![[Screenshot 2024-09-24 at 1.38.16 PM.png|640]]

**PROBLEM:** This method does not take into account that there **may be an error in the acknowledgment packages.** 
+ Adding a checksum for this package does not solve anything due to a repeating creation of vulnerable packages. “The acknowledgment of the acknowledgment”
 
+ With an optimistic implentation of the sender the packages may be lost. Transforming data corruption into data loss. This is not reliable
+ With a pesimistic implementation of the sender, the packages may be send twice (duplicated). Is duplication equal to **no data loss**? Nop, this isn’t acceptable or reliable. However it is a problem that **can be fixed** once recieved the packages by **numbering the packages (sequence number)**. 
  When the reciever gets a duplicated package it drops it by checking the sequence number and **sends a positive acknowledgment** 


> [!TIP] stop and wait  
> This type of transmission transmits ordered pck. Then the idea is: 
> 1. Sender sends
> 2. Sender waits for response

### Complete FSMs: 
+ Sender an receiver need to know how many packages there are and how are they numbered → Checking for duplicates. 
  Given the delteion of the NAK there can be only two numberings of the package.Alternating betwen those is enought.
+ There is only a need for two flags → **ACK and NAK** (positive/negative acknowledgment)
**Sender:**
	![[Screenshot 2024-09-24 at 1.54.39 PM.png]]
**Receiver:**
	![[Screenshot 2024-09-24 at 1.55.20 PM.png]]

### Getting rid of the NAK:
+ Only have positive ack with the sequence number of the ack pck.
The receiver will generate an **ACK package with the sequence number of the last package it recieved ok**.
+ This way we get rid of the NaK
> f.e: 
> 1. Sender sends pck sequence number 0
> 2. Receiver says ack 0
> 3. Sender send pck sequence number 1
> 4. Receiver says ack 0 → This is a negative acknowledgment of pck 1

## Channel with errors and loss:
In a channel with losses, the previous designed mechanism will **get stuck** waiting for **some packages that never arrive.**
+  **Solution:** Include a timer

Once the package is send a timer starts, when the timer ends, the sender asumes that the package has been lost **and retransmits it**. 
+ Duplicate packages can be generated → We already have sequence numbers to deal with this. 
+ The timer waits for **exactly 1 RTT** (Round Trip Time)
	+ To compute the RTT we can check the history of packages sent and how long they took. **However the only variable that will change the RTT is the queueing delay**. This means that the last package wont be a good prediction of the next one. 
	+ Because it is an estimation. The RTT will be wrong some times. 
+ For the first package: Either be very agressive and start sending with small RTT untill there is a response, or be loose and set a long RTT. THe thing is we need that first response to estimate a better RTT.
+ We say that packages are retransmitted, however ack packages are **never retransmitted** but send again for a retransmitted package.
### Complete FSMs:
**Sender:**
	![[1727176650 - Principles of reliable data transfer.png]]
**Receiver:**
+ Is unchanged with respect to the last model 

