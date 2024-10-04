---
aliases:
  - The network stack
  - Network layers
tags:
  - review
  - Networks
References: "[[Net_References_s1_2.pdf]]"
cssclasses: 
sr-due: 2024-10-07
sr-interval: 7
sr-ease: 250
---
# The network stack: 

> [!NOTE] Why layers? 
>  In order to organise the whole network. Split the network into smaller chunks of info. → **Modularization**
+ The layers are called an stack **because they are implemented as such:** Last in first out 

![[1726572508 - The network stack.png|center]]


From bottom to top, each layer offers a different services:
## Layers:
#Duda: Differences between link and network layers.
They are **numbered from bottom to top:**

1. **Physical:** The actual things we can touch 
   >Hardware

2. **Link:** Data transfer between **neighboring network elements**
   > Next connection that needs to be made.

3. **Network:** Joining all the linked devices in the link layer (the glue to actually create the network).
   > Where is the connection going? Whole image of the web.

4. [[1728038869 - Transport network layer|Transport layer]]: Processes talking to each other to transfer data. 
   >How is the info going to be encoded and transported

5. [[1726574469 - Application layer|Application layer]]: Supports network applications. 
   >Decodes the info given by transport.

### Implementations:
As previously defined, layers work as an stack. So if a message wants to be sent from the application layer of one host to another. 
+ **Numbering goes with repect to the layer**
>5. The message is created in the app layer. 
>4. The transport layer sees it, breaks it into chunks (Headers added)
>3. The network layer states the destination (Header added)
>2. The link layer adds a header
>1. Message goes through the physical layer.

> [!NOTE] Definitions
>+ Some definitions: 
>	+ **Segment:** Message + 1 header
>	+ **Datagram:** Message + 2 headers
>	+ **Frame:** Message + 3 headers

At the other end it goes in reverse: 

> 1. Through physical layer
> 2. Link sees that info is correct (check header)
> 3. Network checks that he is the correct recipient (check header)
> 4. Transpor layer decodes (check header)
> 5. App layer delivers to respective service 

#### Routers and switches:
The previous example only covers host to host **direct connection**, when going through routers or switches thing changes: 
+ Switches: **only have physical and link**
+ routers:**only have physical, link and network.**
