---
aliases:
  - Intro to networking
tags:
  - review
  - Networks
References: "[[Net_Biblio_Kurose.pdf#page=28]]"
cssclasses:
---
# Intro to networking
## What is a net?
When we talk about the internet we are just describing a net of connected devices, nothing more. To have a connection we only need two **devices**, a data **transmission method** and a **medium** to do it in. 

**The telephone net:** A basic example is the telephone network where there each phone(device) is connected through a copper wire (medium) and sends electric signals to other phones (transmission method)

## Fisionomía of the internet 

> [!NOTE] Host 
>We call **host or end system** to any device that is hooked to a net.  

+ Nowadays most of these end systems are portable devices while the initial host of the internet where traditional desktop workstations. 

In order to **connect all the host** to the network we use: 
+ [[1726049178 - Definition - Communication links|Communication links]] (the medium part of the net) 
+ [[1726049339 - Definition - Packet switches|Packet switches]] (More about this later)

When a computer sends any data, it **splits it into smaller parts (packets) and adds an explanatory header to each of them**, then this packets are send to the nearest switcher.

### Protocols:

