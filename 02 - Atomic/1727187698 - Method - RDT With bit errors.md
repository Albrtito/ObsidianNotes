---
aliases:
  - Method - RDT With bit errors
tags:
  - review
"References":
cssclasses:
---
# Method - RDT With bit errors

> [!BUG] PROBLEMS: 
> 1. Bits may be flipped (erros) in trasfer
> 2. 

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


***