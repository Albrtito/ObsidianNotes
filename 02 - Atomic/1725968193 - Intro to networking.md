---
aliases:
  - Intro to networking
tags:
  - review
  - Networks
References: "[[Net_Biblio_Kurose.pdf#page=28]]"
cssclasses:
sr-due: 2024-09-17
sr-interval: 2
sr-ease: 230
---
# Intro to networking
When we talk about the internet we are just describing a **net of connected devices**, nothing more. To have a connection we only need two **devices**, a data **transmission method** and a **medium** to do it in. 

>**The telephone net:** A basic example is the telephone network where there each phone(device) is connected through a copper wire (medium) and sends electric signals to other phones (transmission method)

## Two different points of view:
+ We can see the internet from a **nuts and bolts** view, focusing on the hardware, protocols, standarts,etc…
+ The internet can also be described from a service view. An **infrastructure that provides interfaces to apps**. These apps can be:
	+ **Distributed apps:** Those that need the internet to work 
	+ **Local apps:** Those that can run without the web
	 > f.e: The calculator
	 
## Fisionomía of the internet 

> [!NOTE] Host 
>We call **host or end system** to any device that is hooked to a net.  

+ Nowadays most of these end systems are portable devices while the initial host of the internet where traditional desktop workstations. 

In order to **connect all the host** to the network we use: 
+ [[1726049178 - Definition - Communication links|Communication links]] (the medium part of the net) 
+ [[1726049339 - Definition - Packet switches|Packet switches]] (More about this later)

Computers communicate between them using [[1726049888 - Net protocols|Net protocols]]. These protocols give an **standard way of establishing a communication between two nodes**. 
Anyone can create a protocol, though most protocols used are public.
### Packet switching:: 

> [!NOTE] Definition: 
> Information on the internet is sent by hoping from one host to another until the target host is reached. Messages are not sent whole but broken down into smaller pieces, this process is called **packet switching**.  

+ An explanatory header is added to each of this packets

This makes the network much quicker as **the links are being used constantly**. 



