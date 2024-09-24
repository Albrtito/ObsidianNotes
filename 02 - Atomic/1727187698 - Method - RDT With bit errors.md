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

**Solution:**
In order to recover from this problem we can use the [[1727177356 - Method - Checksum|checksum]] method. **Once the receiver gets a package it checks if there has been any errors.**
## Acknowledgment packages: ACKs/NAKs
Once the reciever checks if the package has been corrupted it sends a package that tells it to the sender. These packages are **acknowledgment packages**. 

There are two of them: 
+ **ACK:** Afirmative acknowledgement. Nice, everything ok
+ **NAK**: Negative acknowledgement. The package had corruption

Then, for each package that is send triggers the following cycle:
$$
\boxed{\text{sent package → recieved → dropped/kept → positive/negative acknowledge }}
$$

Once the **cycle finishes**(recieved ACK or NAK) the sender can do one of two things:

+ With a **positive** acknowledgement: **Send next one**
+ With a **negative** acknowledgment: **Resend last one**
### States of the sender/reciever:
IF we wante to apply this acknowledgment in the previous state machine (the one with no problems in the medium):
+ We add the states for waiting for  the ACKs and NAKs in the **sender**
+ Add the sending of ACKs and NAKs in the **receiver** **based on the corruption** in the message

### Reliability of the acknowledgment pck’s:
> [!BUG] PROBLEM: 
> This method does not take into account that there **may be an error in the acknowledgment packages.**

+ Adding a checksum for this package does not solve anything due to a repeating creation of vulnerable packages. **“The acknowledgment of the acknowledgment of the acknowledgedment of the acknowledgment is vulnerable”**

**The solution:**
Instead of reasking for an acknowledgment of the corrupted acknowledgment, **if the PCK is corrupted we assume that it said NAK** (pesimistic sender) and send that same package again.

+ With an optimistic implentation (corrupted packages are assumed as ACK) we transform data corruption into data loss. **This is not reliable**

+ The retransmission of a package that may not have been corrupted could turn into duplication errors: 
	$$
		\boxed{\text{Is duplication equal to no data loss? }}
	$$
  Nop, this isn’t acceptable or reliable. However it is a problem that **can be fixed** once recieved the packages by **numbering the packages 

#### Duplicated packages:
The management of duplicated packages is **handled by the reciever**. 
+ Each package is given a **sequence number**
+ When the reciever gets a package, it compares the sequence number. If duplicated → drops the package.

Once dropped, the reciever must send a **positive acknowledgment**. (Even though it was duplicated). We can just think that the positive ACKs are allways send, unless corruption.

### Getting rid of the NAK:
Only have positive ack with the sequence number of the ack pck.
The receiver will generate an **ACK package with the sequence number of the last package it recieved ok**.
+ This way we get rid of the NaK
> f.e: 
> 1. Sender sends pck sequence number 0
> 2. Receiver says ack 0
> 3. Sender send pck sequence number 1
> 4. Receiver says ack 0 → This is a negative acknowledgment of pck 1


### Complete FSMs: 
+ Sender an receiver need to know how many packages there are and how are they numbered → Checking for duplicates. 
  Given the delteion of the NAK there can be only two numberings of the package.Alternating betwen those is enought.
+ There is only a need for two flags → **ACK and NAK** (positive/negative acknowledgment)
**Sender:**
	![[Screenshot 2024-09-24 at 1.54.39 PM.png]]
**Receiver:**
	![[Screenshot 2024-09-24 at 1.55.20 PM.png]]

***