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
+ 